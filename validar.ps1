# Valida la integridad del pack antes de publicar.
# Uso:  ./validar.ps1
# Codigos de salida: 0 = todo correcto, 1 = hay errores (no publicar).

$ErrorActionPreference = 'Stop'
$root = if ($PSScriptRoot) { $PSScriptRoot } else { (Get-Location).Path }
$errores = New-Object System.Collections.Generic.List[string]

function Leer($ruta) { [IO.File]::ReadAllText((Join-Path $root $ruta)) }
function Sha256($ruta) { (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $root $ruta)).Hash.ToLower() }

# 1) pack.toml -> index.toml
$pack = Leer 'pack.toml'
$mPack = [regex]::Match($pack, 'hash-format\s*=\s*"sha256"\s*hash\s*=\s*"([0-9a-fA-F]+)"')
if (-not $mPack.Success) {
    $errores.Add('pack.toml: no se encontro el bloque [index] con hash sha256')
} else {
    $real = Sha256 'index.toml'
    if ($real -ne $mPack.Groups[1].Value.ToLower()) {
        $errores.Add("pack.toml declara index hash $($mPack.Groups[1].Value) pero el archivo real es $real -> ejecuta 'packwiz refresh'")
    }
}

# 2) cada entrada de index.toml debe existir y coincidir
$idx = Leer 'index.toml'
$entradas = [regex]::Matches($idx, '(?s)\[\[files\]\].*?file\s*=\s*"([^"]+)".*?hash\s*=\s*"([^"]+)"')
if ($entradas.Count -eq 0) { $errores.Add('index.toml no contiene entradas [[files]]') }
foreach ($e in $entradas) {
    $rel = $e.Groups[1].Value
    $esp = $e.Groups[2].Value.ToLower()
    if (-not (Test-Path -LiteralPath (Join-Path $root $rel))) {
        $errores.Add("index.toml lista '$rel' pero el archivo no existe")
    } elseif ((Sha256 $rel) -ne $esp) {
        $errores.Add("hash incorrecto en index.toml para '$rel'")
    }
}

# 3) metadatos de cada mod
$metas = @(Get-ChildItem (Join-Path $root 'mods') -Filter *.pw.toml -File)
foreach ($pw in $metas) {
    $c = [IO.File]::ReadAllText($pw.FullName)
    if ($c -notmatch '\[download\]')               { $errores.Add("mods/$($pw.Name): falta el bloque [download]") }
    if ($c -notmatch '(?m)^hash\s*=\s*"')          { $errores.Add("mods/$($pw.Name): falta el hash de descarga") }
    if ($c -notmatch '(?m)^filename\s*=\s*"')      { $errores.Add("mods/$($pw.Name): falta filename") }
    if ($c -notmatch 'https://')                   { $errores.Add("mods/$($pw.Name): la descarga no usa una URL https") }
}

# 4) cada jar local de mods/ debe estar indexado
$indexados = @($entradas | ForEach-Object { $_.Groups[1].Value })
foreach ($jar in @(Get-ChildItem (Join-Path $root 'mods') -Filter *.jar -File)) {
    $rel = "mods/$($jar.Name)"
    if ($indexados -notcontains $rel) { $errores.Add("'$rel' existe pero no esta indexado -> ejecuta 'packwiz refresh'") }
}

Write-Host ("Validacion: {0} entradas de indice, {1} metafiles, {2} jars locales" -f $entradas.Count, $metas.Count, (@(Get-ChildItem (Join-Path $root 'mods') -Filter *.jar -File)).Count)
if ($errores.Count -eq 0) {
    Write-Host 'OK: el pack es coherente.' -ForegroundColor Green
    exit 0
}
Write-Host ("ERRORES ({0}):" -f $errores.Count) -ForegroundColor Red
$errores | ForEach-Object { Write-Host " - $_" -ForegroundColor Red }
exit 1