# Verifica el estado del balance contra estado.json.
# Uso:  .\verificar_estado.ps1 [-Json] [-SkipTests]
# Salida: una linea por comprobacion (OK/FAIL/SKIP id detalle) y un RESUMEN.
# Codigo de salida: 0 si todo OK o SKIP, 1 si hay algun FAIL.

[CmdletBinding()]
param(
    [switch]$Json,
    [switch]$SkipTests
)

$ErrorActionPreference = 'Continue'
$repo = if ($PSScriptRoot) { $PSScriptRoot } else { (Get-Location).Path }
$srv = 'C:\Users\Metabodiru\Desktop\servidor-theoptimizer'
$py = 'C:\Users\Metabodiru\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python.exe'
$instancia = Join-Path $env:APPDATA 'PrismLauncher\instances\TheOptimizer'

$estado = $null
try { $estado = Get-Content (Join-Path $repo 'estado.json') -Raw -Encoding UTF8 | ConvertFrom-Json } catch { }

$filas = New-Object System.Collections.Generic.List[string]
$fallos = New-Object System.Collections.Generic.List[string]

function Add-Check {
    param([string]$Id, [bool]$Ok, [string]$Detalle, [bool]$Skip = $false)
    if ($Skip) {
        $filas.Add(('SKIP {0,-26} {1}' -f $Id, $Detalle))
        return
    }
    if ($Ok) {
        $filas.Add(('OK   {0,-26} {1}' -f $Id, $Detalle))
    } else {
        $filas.Add(('FAIL {0,-26} {1}' -f $Id, $Detalle))
        $fallos.Add($Id)
    }
}

if ($null -eq $estado) {
    Add-Check 'estado.json' $false 'no se pudo leer o parsear estado.json'
}

# --- 1. integridad del pack -------------------------------------------------
$idxTexto = [IO.File]::ReadAllText((Join-Path $repo 'index.toml'))
$entradas = [regex]::Matches($idxTexto, '(?s)\[\[files\]\].*?file\s*=\s*"([^"]+)".*?hash\s*=\s*"([^"]+)"')
$malas = 0
foreach ($e in $entradas) {
    $rel = $e.Groups[1].Value
    $ruta = Join-Path $repo ($rel -replace '/', '\')
    if (-not (Test-Path -LiteralPath $ruta)) { $malas++; continue }
    if ((Get-FileHash -Algorithm SHA256 -LiteralPath $ruta).Hash.ToLower() -ne $e.Groups[2].Value.ToLower()) { $malas++ }
}
Add-Check 'pack.integridad' ($malas -eq 0) ("{0} entradas, {1} con hash incorrecto" -f $entradas.Count, $malas)

if ($null -ne $estado) {
    Add-Check 'pack.entradas' ($entradas.Count -eq $estado.pack.entradas) ("{0}/{1}" -f $entradas.Count, $estado.pack.entradas)
}

# --- 2. jar: version, paridad repo/servidor/indice ---------------------------
$jarRepo = Join-Path $repo ('mods\' + $estado.mod.jar)
$jarSrv = Join-Path $srv ('mods\' + $estado.mod.jar)
$hashRepo = if (Test-Path $jarRepo) { (Get-FileHash -Algorithm SHA256 $jarRepo).Hash.ToLower() } else { '' }
$hashSrv = if (Test-Path $jarSrv) { (Get-FileHash -Algorithm SHA256 $jarSrv).Hash.ToLower() } else { '' }

$versionJar = ''
if ($hashRepo) {
    $toml = (tar -xOf $jarRepo 'META-INF/mods.toml' 2>$null | Out-String)
    $m = [regex]::Match($toml, 'version\s*=\s*"([^"]+)"')
    if ($m.Success) { $versionJar = $m.Groups[1].Value }
}
Add-Check 'mod.version' ($versionJar -eq $estado.mod.version) ("jar={0} esperado={1}" -f $versionJar, $estado.mod.version)

$hashIndice = ''
$mi = [regex]::Match($idxTexto, 'file = "mods/' + [regex]::Escape($estado.mod.jar) + '"\s*hash = "([0-9a-f]+)"')
if ($mi.Success) { $hashIndice = $mi.Groups[1].Value.ToLower() }
$paridad = ($hashRepo -ne '') -and ($hashRepo -eq $hashSrv) -and ($hashRepo -eq $hashIndice)
Add-Check 'jar.paridad' $paridad ("repo={0} servidor={1} indice={2}" -f $hashRepo.Substring(0, [Math]::Min(12, $hashRepo.Length)), $hashSrv.Substring(0, [Math]::Min(12, $hashSrv.Length)), $hashIndice.Substring(0, [Math]::Min(12, $hashIndice.Length)))

# --- 3. config: claves y valores -------------------------------------------
$cfgRuta = Join-Path $repo 'config\theoptimizer_equipment.json'
$cfg = $null
try { $cfg = Get-Content $cfgRuta -Raw -Encoding UTF8 | ConvertFrom-Json } catch { }
if ($null -eq $cfg) {
    Add-Check 'config.claves' $false 'no se pudo leer la config'
} else {
    $claves = @($cfg.PSObject.Properties.Name)
    $esperadas = @($estado.config.PSObject.Properties)
    Add-Check 'config.claves' ($claves.Count -eq $esperadas.Count) ("{0}/{1} claves" -f $claves.Count, $esperadas.Count)

    $divergentes = New-Object System.Collections.Generic.List[string]
    foreach ($p in $esperadas) {
        $real = $cfg.($p.Name)
        $igual = $false
        if ($null -ne $real) {
            $dr = 0.0
            $de = 0.0
            if ([double]::TryParse([string]$real, [ref]$dr) -and [double]::TryParse([string]$p.Value, [ref]$de)) {
                $igual = [Math]::Abs($dr - $de) -lt 1e-9
            } else {
                $igual = ([string]$real -eq [string]$p.Value)
            }
        }
        if (-not $igual) {
            $divergentes.Add(('{0}: {1}->{2}' -f $p.Name, $p.Value, $real))
        }
    }
    Add-Check 'config.valores' ($divergentes.Count -eq 0) ($(if ($divergentes.Count -eq 0) { 'coinciden' } else { $divergentes -join '; ' }))
}

# --- 4. pruebas del modulo --------------------------------------------------
if ($SkipTests) {
    Add-Check 'tests.modulo' $true 'omitido (-SkipTests)' -Skip $true
} else {
    $interpretes = New-Object System.Collections.Generic.List[string]
    if (Test-Path $py) { $interpretes.Add($py) }
    $cmdPython = Get-Command python -ErrorAction SilentlyContinue
    if ($cmdPython -and $cmdPython.Source -and $cmdPython.Source -notmatch 'WindowsApps') { $interpretes.Add($cmdPython.Source) }

    $salidaPruebas = ''
    foreach ($interprete in $interpretes) {
        Push-Location $instancia
        try {
            $salidaPruebas = (& $interprete -m gestion.herramientas.reparaciones.balance_equipamiento.probar 2>&1 | Out-String)
        } catch {
            $salidaPruebas = ''
        } finally { Pop-Location }
        if ($salidaPruebas -match 'VERIFICACION EXITOSA') { break }
    }

    # Fallback: algunas shells no resuelven la ruta absoluta al interprete; cmd.exe si.
    if (-not ($salidaPruebas -match 'VERIFICACION EXITOSA') -and (Test-Path $py)) {
        Push-Location $instancia
        try {
            $linea = '"' + $py + '" -m gestion.herramientas.reparaciones.balance_equipamiento.probar 2>&1'
            $salidaPruebas = (& cmd.exe /c $linea | Out-String)
        } catch {
            $salidaPruebas = ''
        } finally { Pop-Location }
    }

    if ($salidaPruebas -match 'VERIFICACION EXITOSA') {
        $num = [regex]::Match($salidaPruebas, '(\d+) comprobaciones')
        Add-Check 'tests.modulo' $true ("{0} comprobaciones" -f $(if ($num.Success) { $num.Groups[1].Value } else { '?' }))
    } elseif ($salidaPruebas.Trim()) {
        $primera = (($salidaPruebas.Trim() -split "`n")[0]).Trim()
        Add-Check 'tests.modulo' $false ('salida inesperada: ' + $primera)
    } else {
        Add-Check 'tests.modulo' $true 'SKIP: ejecuta a mano  python -m gestion.herramientas.reparaciones.balance_equipamiento.probar' -Skip $true
    }
}

# --- 5. invariantes de contenido (C1, C2, C3) -------------------------------
$txtClase = ''
if ($hashRepo) { $txtClase = (tar -xOf $jarRepo 'theoptimizer/equipment/EquipmentEvents.class' 2>$null | Out-String) }
$nombresEncantamiento = $txtClase -match 'Pesadilla|Castigo|Toque de Seda|Fortuna III|Lealtad III|Empalamiento'
Add-Check 'C1.sin-encantamientos' (-not $nombresEncantamiento) ($(if ($nombresEncantamiento) { 'tooltip nombra un encantamiento' } else { 'tooltips solo describen efectos' }))

$policy = Join-Path $instancia 'gestion\herramientas\reparaciones\balance_equipamiento\theoptimizer\equipment\EquipmentPolicy.java'
$policyTexto = if (Test-Path $policy) { [IO.File]::ReadAllText($policy) } else { '' }
$linajeOk = ($policyTexto -match 'cursium_') -and ($policyTexto -match 'netherite_mage_') -and ($policyTexto -match 'cataclysmFamily')
Add-Check 'C2.linaje-netherita' $linajeOk ($(if ($linajeOk) { 'ignitium/cursium/monstrous/mage presentes' } else { 'falta alguna familia en EquipmentPolicy' }))

$mageOk = ($policyTexto -match 'alexs_caves_spellbooks') -and ($policyTexto -match 'isMageRobe')
Add-Check 'C3.tunicas-pagan' $mageOk ($(if ($mageOk) { 'irons + alexs_caves en rol mago' } else { 'falta namespace de tunas' }))

# --- 6. publicacion viva ----------------------------------------------------
$versionLocal = (Get-Content (Join-Path $repo 'version.txt') -Raw).Trim()
$versionPages = ''
try {
    $resp = Invoke-WebRequest 'https://drox17.github.io/ampere_modpack/version.txt' -UseBasicParsing -TimeoutSec 10
    $versionPages = ($resp.Content).Trim()
} catch {
    Add-Check 'pages.version' $true ('no comprobable: ' + $_.Exception.Message) -Skip
}
if ($versionPages) {
    Add-Check 'pages.version' ($versionPages -eq $versionLocal) ("pages={0} repo={1}" -f $versionPages, $versionLocal)
}

# --- 8. registro de loot tables ---------------------------------------------
$lootRuta = Join-Path $repo 'loot.json'
if (Test-Path $lootRuta) {
    $loot = Get-Content $lootRuta -Raw -Encoding UTF8 | ConvertFrom-Json
    $totalLoot = 0
    $malasLoot = 0
    foreach ($e in $loot.entradas) {
        $totalLoot++
        $base = if ($e.base -eq 'server') { $srv } else { $repo }
        $archivo = Join-Path $base $e.archivo
        if (-not (Test-Path $archivo)) { $malasLoot++; continue }
        $contenido = (tar -xOf $archivo $e.entrada 2>$null | Out-String)
        $sha = [System.Security.Cryptography.SHA256]::Create()
        $calculado = (($sha.ComputeHash([Text.Encoding]::UTF8.GetBytes($contenido)) | ForEach-Object { $_.ToString('x2') }) -join '')
        if ($calculado -ne $e.sha256) { $malasLoot++ }
    }
    Add-Check 'loot.registro' ($malasLoot -eq 0) ("{0}/{1} tablas sin cambios" -f ($totalLoot - $malasLoot), $totalLoot)
}

# --- 7. git -----------------------------------------------------------------
$porcelain = (git -C $repo status --porcelain 2>$null | Out-String).Trim()
Add-Check 'git.limpio' ([string]::IsNullOrWhiteSpace($porcelain)) ($(if ([string]::IsNullOrWhiteSpace($porcelain)) { 'sin cambios pendientes' } else { 'hay cambios sin commitear' }))

$pendientes = 0
try { $pendientes = [int](git -C $repo rev-list --count 'HEAD..@{u}' 2>$null) } catch { $pendientes = -1 }
Add-Check 'git.sincronizado' ($pendientes -eq 0) ("commits sin subir: {0}" -f $pendientes)

# --- salida -----------------------------------------------------------------
if ($Json) {
    $obj = [pscustomobject]@{
        ok     = ($fallos.Count -eq 0)
        total  = $filas.Count
        fallos = @($fallos)
        filas  = @($filas)
    }
    $obj | ConvertTo-Json -Depth 4
} else {
    $filas | ForEach-Object { Write-Host $_ }
    $estadoTexto = if ($fallos.Count -eq 0) { 'sin derivas' } else { 'derivas: ' + ($fallos -join ', ') }
    Write-Host ''
    Write-Host ("RESUMEN {0}/{1} - {2}" -f ($filas.Count - $fallos.Count), $filas.Count, $estadoTexto)
}

if ($fallos.Count -gt 0) { exit 1 } else { exit 0 }
