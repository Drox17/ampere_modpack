@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo ========================================================
echo   Ampere Modpack - Actualizador y Sincronizador
echo ========================================================
echo.

cd /d "%~dp0"

echo [1/4] Generando version de changelog y normalizando a Unix (LF)...
if exist changelog.md (
    powershell -NoProfile -Command "$h = (Get-FileHash -Algorithm MD5 changelog.md).Hash.Substring(0,8); [IO.File]::WriteAllText('version.txt', \"$h`n\", (New-Object Text.UTF8Encoding($false)))"
)
git add --renormalize . >nul 2>&1

echo [2/4] Actualizando catálogo y hashes de Packwiz...
packwiz refresh
if %ERRORLEVEL% neq 0 (
    echo.
    echo [ERROR] Falló 'packwiz refresh'. Revisa si algún archivo está bloqueado.
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo [3/4] Preparando cambios para Git...
git add .

git status --short
echo.

set /p commit_msg="Ingresa la descripción del cambio (o presiona Enter para 'Actualizar modpack'): "
if "!commit_msg!"=="" set commit_msg=Actualizar modpack

echo.
echo [4/4] Creando commit y subiendo a GitHub Pages...
git commit -m "!commit_msg!"
if %ERRORLEVEL% neq 0 (
    echo No había cambios nuevos que subir.
    pause
    exit /b 0
)

git push origin main
if %ERRORLEVEL% neq 0 (
    echo.
    echo [ERROR] No se pudo hacer 'git push'. Comprueba tu conexión o permisos de GitHub.
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo ========================================================
echo   ¡Listo! Cambios subidos correctamente.
echo   GitHub Pages estará actualizado en ~30-60 segundos.
echo ========================================================
echo.
pause
