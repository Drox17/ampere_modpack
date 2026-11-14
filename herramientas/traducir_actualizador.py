"""Traducción reproducible de constantes visibles del instalador Ampere personalizado.

Conserva bytecode, metadatos ZIP y recursos. No cambia URLs, argumentos ni hashes.
Sin --instalar solo produce un JAR de revisión dentro de datos/actualizador.
"""
import argparse
import io
import json
import struct
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLIENT = Path(r'C:\Users\Metabodiru\AppData\Roaming\PrismLauncher\instances\Ampere Better Survival\minecraft')
TEXTS = {
    'Ampere Updater': 'Actualizador de Ampere',
    'Loading...': 'Cargando...', 'Optional mods...': 'Mods opcionales...',
    'No optional mods': 'Sin mods opcionales', 'Continue (': 'Continuar (',
    'Cancel': 'Cancelar', 'Continue': 'Continuar', 'Quit': 'Salir', 'Ignore': 'Omitir',
    'Enabled': 'Activado', 'Mod name': 'Nombre del mod', 'OK': 'Aceptar',
    'Select optional mods...': 'Seleccionar mods opcionales...',
    'Select an option...': 'Selecciona una opción...',
    'This modpack has no optional mods!': 'Este pack no tiene mods opcionales.',
    'Optional mods': 'Mods opcionales',
    'The installation was cancelled. Would you like to quit the game, or ignore the update and start the game?': 'Se canceló la instalación. ¿Quieres salir u omitir la actualización e iniciar el juego?',
    'Cancelled installation': 'Instalación cancelada',
    '<html>This modpack uses newer versions of the following:<br><ul>': '<html>Este pack necesita versiones más recientes de estos componentes:<br><ul>',
    'Not found': 'No encontrado', 'New versions:<ul>': 'Versiones nuevas:<ul>',
    '</ul><br>Would you like to update the versions, launch without updating, or cancel the launch?': '</ul><br>¿Quieres actualizar, iniciar sin actualizar o cancelar el inicio?',
    'Continue anyways': 'Continuar de todos modos', 'Update': 'Actualizar',
    'Updating MultiMC versions': 'Actualización de componentes de la instancia',
    'Continue without installing': 'Continuar sin instalar',
    'Continue without updating': 'Continuar sin actualizar',
    'Failed file downloads': 'Descargas fallidas',
    'One or more errors were encountered while installing the modpack!': 'Se produjeron errores al instalar el pack.',
    'Select a file': 'Selecciona un archivo',
    'Attempt to continue installing, excluding the failed downloads': 'Continuar la instalación omitiendo las descargas fallidas',
    'Cancel launch': 'Cancelar inicio', 'Stop launching the game': 'Detener el inicio del juego',
    'Ignore update': 'Omitir actualización', 'Start the game without attempting to update': 'Iniciar el juego sin actualizar',
    'Open missing mods': 'Abrir mods pendientes', 'Open missing mods in your browser': 'Abrir los mods pendientes en el navegador',
    ' errored': ' con errores', 'Report issue': 'Informar de un problema',
    'Loading manifest file...': 'Cargando el registro local...',
    'Loading pack file...': 'Cargando la información del pack...',
    'Loading MultiMC pack file...': 'Cargando la información de la instancia...',
    'Checking local files...': 'Comprobando los archivos locales...',
    'Modpack is already up to date!': '¡El pack ya está actualizado!',
    'Modpack files are already up to date!': '¡Los archivos del pack ya están actualizados!',
    'Comparing new files...': 'Comparando archivos nuevos...',
    'Validating existing files...': 'Verificando los archivos existentes...',
    'Resolving CurseForge metadata...': 'Consultando la información de CurseForge...',
    'Reconfigure optional mods?': '¿Configurar los mods opcionales?',
    'Failed to download ': 'No se pudo descargar ', 'Downloaded ': 'Descargado: ',
    'Skipped ': 'Omitido: ', 'Deleted ': 'Eliminado: ',
    ' (removed from pack)': ' (retirado del pack)', ' (wrong side)': ' (no corresponde a este entorno)',
    ' (disabled)': ' (desactivado)', ' already exists (validated)': ' ya existe (verificado)',
    ' already exists (cached)': ' ya existe (en caché)',
    'Failed to save local manifest file': 'No se pudo guardar el registro local',
    'Failed to process index file': 'No se pudo procesar el índice',
    'Failed to parse pack.toml': 'No se pudo interpretar pack.toml',
    'Failed to download pack.toml': 'No se pudo descargar pack.toml',
    'Failed to parse index file': 'No se pudo interpretar el índice',
    'Failed to download index file': 'No se pudo descargar el índice',
    'Index is empty!': 'El índice está vacío.',
    'Update cancelled by user! Continuing to start game...': 'Actualización cancelada. Iniciando el juego...',
    'Update cancelled by user!': 'Actualización cancelada por el usuario.',
    'A fatal error occurred: \n': 'Se produjo un error que impide continuar: \n',
    'Update process failed': 'No se pudo completar la actualización',
    'Finished successfully!': '¡Proceso completado!',
    'Failed to delete file': 'No se pudo eliminar el archivo',
    'Failed to delete file removed from index': 'No se pudo eliminar un archivo retirado del pack',
    'Invalid hash for ': 'La verificación del archivo falló: ',
    'Calculated: ': 'Calculado: ', 'Expected:   ': 'Esperado:  ', 'Hash invalid!': 'La verificación no coincide.',
    'Failed to execute download task': 'No se pudo completar una descarga',
    'Your index file hash is invalid! The pack developer should packwiz refresh on the pack again': 'El índice no supera la verificación. El administrador debe regenerarlo con packwiz refresh.',
    'Failed to read local manifest file, try deleting ': 'No se pudo leer el registro local. Prueba a eliminar ',
    'Invalid local manifest file, try deleting ': 'El registro local no es válido. Prueba a eliminar ',
    'Failed to download modpack, the following errors were encountered:': 'No se pudo descargar el pack. Se encontraron estos errores:',
}


def patch_class(data):
    end = 10
    count = struct.unpack_from('>H', data, 8)[0]
    entries, references = {}, set()
    i = 1
    while i < count:
        start = end
        tag = data[end]; end += 1
        if tag == 1:
            length = struct.unpack_from('>H', data, end)[0]; end += 2 + length
        elif tag in (3, 4): end += 4
        elif tag in (5, 6): end += 8
        elif tag in (7, 8, 16, 19, 20):
            if tag == 8: references.add(struct.unpack_from('>H', data, end)[0])
            end += 2
        elif tag in (9, 10, 11, 12, 17, 18): end += 4
        elif tag == 15: end += 3
        else: raise ValueError(f'Constant pool desconocido: {tag}')
        entries[i] = (tag, data[start:end])
        i += 2 if tag in (5, 6) else 1
    pieces, changed = [], []
    for index, (tag, raw) in entries.items():
        if tag == 1 and index in references:
            value = raw[3:].decode('utf-8', errors='replace')
            if value in TEXTS:
                value_es = TEXTS[value].encode('utf-8')
                raw = b'\x01' + struct.pack('>H', len(value_es)) + value_es
                changed.append(value)
        pieces.append(raw)
    return data[:10] + b''.join(pieces) + data[end:], changed


def localize(raw):
    output = io.BytesIO(); changes = {}
    with zipfile.ZipFile(io.BytesIO(raw)) as source, zipfile.ZipFile(output, 'w') as target:
        assert not any(n.upper().endswith(('.SF', '.RSA', '.DSA')) for n in source.namelist()), 'JAR firmado: no parchear'
        for info in source.infolist():
            data = source.read(info)
            if info.filename.startswith('link/infra/packwiz/installer/') and '/deps/' not in info.filename and info.filename.endswith('.class'):
                data, edited = patch_class(data)
                if edited: changes[info.filename] = edited
            target.writestr(info, data)
    return output.getvalue(), changes


def main():
    parser = argparse.ArgumentParser(); parser.add_argument('--instalar', action='store_true'); args = parser.parse_args()
    source = CLIENT / 'packwiz-installer.jar'
    raw, changes = localize(source.read_bytes())
    dest = ROOT / 'datos/actualizador'; dest.mkdir(parents=True, exist_ok=True)
    (dest / 'packwiz-installer-es.jar').write_bytes(raw)
    (dest / 'traducciones.json').write_bytes((json.dumps(changes, ensure_ascii=False, indent=2)+'\n').encode('utf-8'))
    if args.instalar:
        backup = dest / 'packwiz-installer-original.jar'
        if not backup.exists(): backup.write_bytes(source.read_bytes())
        source.write_bytes(raw)
        distribution = ROOT / 'Ampere Better Survival.zip'
        with zipfile.ZipFile(distribution) as z: contents = [(i, z.read(i)) for i in z.infolist()]
        found = 0
        with zipfile.ZipFile(distribution, 'w') as z:
            for info, content in contents:
                if info.filename.endswith('packwiz-installer.jar'):
                    content, _ = localize(content); found += 1
                z.writestr(info, content)
        assert found == 1, f'JARs en paquete de instalación: {found}'
    print(sum(map(len, changes.values())), 'textos traducidos en', len(changes), 'clases')


if __name__ == '__main__': main()
