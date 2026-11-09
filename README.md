# ⚡ Ampere Modpack

Modpack privado para Minecraft **1.20.1 (Forge)** con sincronización automática de mods y configuraciones.

---

## 🎮 Guía de Instalación (Para Jugadores)

No necesitas descargar carpetas pesadas ni pegar archivos `.jar` a mano. El launcher se encarga de descargar y actualizar todo automáticamente cada vez que pulses **Jugar**.

### Requisitos previos
1. Descarga e instala **[Prism Launcher](https://prismlauncher.org/download/)**.
2. Abre Prism Launcher e inicia sesión con tu cuenta oficial de Minecraft (Microsoft).

---

### Pasos para instalar

1. En Prism Launcher, haz clic en **Añadir instancia** (*Add Instance*) en la esquina superior izquierda.
2. En el menú de la izquierda, selecciona la opción **Importar desde zip** (*Import from zip*).
3. En el campo de texto, copia y pega este enlace directo:
   ```text
   https://drox17.github.io/ampere_modpack/ampere_setup.zip
   ```
4. Haz clic en **OK**.
5. ¡Listo! Selecciona la instancia creada y haz clic en **Iniciar** (*Launch*). 

> ⏳ **Primera carga:** La primera vez que abras el juego aparecerá una pequeña ventana descargando todos los mods desde el servidor. Una vez termine la descarga, el juego arrancará con normalidad.

---

### ⚙️ Ajuste recomendado de RAM

Para evitar cierres inesperados o tirones:
1. Haz clic derecho en la instancia de Ampere -> **Editar** (*Edit*).
2. Ve a la pestaña **Ajustes** (*Settings*) -> marca la casilla de **Memoria**.
3. En **Memoria máxima** asigna entre **4096 MB (4 GB)** y **6144 MB (6 GB)**.

---

### 🔄 ¿Cómo se actualiza el modpack?
**No tienes que hacer nada.** Si el administrador añade, borra o cambia mods o configuraciones, tu launcher detectará los cambios y los descargará automáticamente en segundos antes de abrir el juego.

---

## 🛠️ Panel de Mantenimiento (Para Administradores)

Flujo de trabajo para aplicar cambios y mandar parches a los clientes:

### 1. Añadir o quitar mods
* Coloca o elimina los archivos `.jar` directamente dentro de la carpeta `mods/`.
* Si modificas configs, hazlo dentro de la carpeta `config/`.

### 2. Sincronizar y publicar cambios
Abre la terminal en la raíz del repositorio (`AmpereRepo`) y ejecuta:

```bash
# 1. Regenerar el catálogo de hashes
packwiz refresh

# 2. Guardar y subir a GitHub Pages
git add .
git commit -m "Update: descripción del cambio"
git push origin main
```

Los cambios tardarán ~30 segundos en propagarse en GitHub Pages y estarán disponibles para todos los jugadores en su siguiente inicio.