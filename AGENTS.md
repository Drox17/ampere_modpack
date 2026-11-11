# AGENTS.md — Estado del sistema de sets y balance (TheOptimizer)

> Lee este archivo **completo** antes de tocar balance. Es el registro canónico: qué está
> implementado, con qué números, dónde vive y cómo comprobarlo. Si algo no coincide con el
> código, el código manda y este archivo está mal: corrígelo en el mismo commit.

## 0. Protocolo en `/sync`

Al recibir `/sync` (o cualquier petición de "verifica el estado"), hacer **en este orden**:

1. Leer §3 (estado) y §4 (números de referencia).
2. Ejecutar **toda** la checklist de §6 y anotar resultado por línea.
3. Reportar en tres bloques, sin mezclar:
   - **✅ Verificado**: invariante comprobado con evidencia (comando + salida).
   - **⚠️ Deriva**: diferencia encontrada, con archivo/clave/valor real vs esperado.
   - **⏳ Pendiente**: puntos de §7 que siguen sin implementar.
4. No cambiar reglas de balance en un `/sync`: solo diagnóstico. Cualquier cambio de diseño
   se registra aquí (§8) con fecha, commit y criterio de aceptación.

## 1. Mapa de artefactos

| Pieza | Ruta |
|---|---|
| Fuente Java + generador | `%APPDATA%\PrismLauncher\instances\TheOptimizer\gestion\herramientas\reparaciones\balance_equipamiento\` |
| Pruebas del módulo | `...\balance_equipamiento\probar.py` (17 comprobaciones, `-Xverify:all`) |
| Compilación y despliegue | `...\balance_equipamiento\instalar.py` (javac 17 del `java-runtime-gamma`) |
| Repo publicado | `C:\Users\Metabodiru\Desktop\AmpereRepo` |
| Servidor | `C:\Users\Metabodiru\Desktop\servidor-theoptimizer` |
| Validador del pack | `AmpereRepo\validar.ps1` |
| Config de balance | `config/theoptimizer_equipment.json` (repo + servidor) |

Regla: `instalar.py` despliega jar+config a repo, servidor y `gestion/servidor-theoptimizer`.
**No copiar a mano**; la instancia de Prism se sincroniza con el updater (packwiz), nunca a mano.

## 2. Versiones

- Mod: `TheOptimizer-EquipmentBalance-1.2.0.jar` · modId `theoptimizer_equipment`
- Pack: `pack.toml version = 1.2.0` · Forge 47.4.28 · MC 1.20.1
- El hash vigente del jar está en `index.toml`; no se hardcodea aquí a propósito.

## 3. Estado implementado

### 3.1 Sets vanilla (armadura horizontal)

| Set | Armadura | Rol | Gana en | Coste |
|---|---|---|---|---|
| Cuero | 15 | Explorador | caída −5/12/20/35 %, piezas de movilidad | sin defensa extra |
| Cota de malla | 15 | Escaramuzador | proyectiles −5/10/18/30 %, velocidad +2/4/7/10 % | sin ayuda vs explosiones |
| Hierro | 15 | Infantería | empuje −5/10/18/30 %, explosiones −4/8/15/25 % | — |
| Oro | 15 | Arcano | magia/pociones −4/8/15/25 %, +1 Suerte, piglins | — |
| Diamante | 20 | Élite | golpes ≥8: −6/12/19/25 % | **+10 % daño de golpes <8**, agotamiento, rep. 25 % |
| Netherita | 20+ | Nether | fuego −5/12/20/35 %, wither −10/20/35/50 %, golpes ≥8 −4/8/13/18 % | **+5 % daño <8**, agotamiento, rep. 25 % |
| Tortuga | — | Escafandra | respiración + picar bajo el agua | — |

### 3.2 Linaje netherita (todo lo forjado sobre `minecraft:netherite_*`)

Debe heredar el tradeoff: fuego/wither, golpes ≥8, **+5 % daño de golpes <8** y rep. 25 %.

| Familia | Detección | Reparación |
|---|---|---|
| Netherita | `ArmorMaterials.NETHERITE` | `netherite_ingot` 25 % |
| `ignitium_*` (Cataclysm) | `EquipmentPolicy.cataclysmFamily` | `cataclysm:ignitium_ingot` 25 % |
| `cursium_*` (Cataclysm) | `cataclysmFamily` | `cataclysm:cursium_ingot` 25 % |
| `monstrous_helm` | `cataclysmFamily` | `netherite_ingot` 25 % |
| `netherite_mage_*` (Irons) | `isNetheriteMageArmor` | `netherite_ingot` 25 % |

**Fuera del linaje a propósito**: `bone_reptile_*` (ancient metal + huesos), `sturdy_boots`.

### 3.3 Rol mago (túnicas)

- Detecta namespace `irons_spellbooks` (52 piezas) y `alexs_caves_spellbooks` (7, dread/primordial mage), por sufijo `_helmet|_chestplate|_leggings|_boots`.
- Excluidos: `tarnished_helmet`, `speed_boots`.
- Coste: **−5 % daño cuerpo a cuerpo por pieza (máx −20 % a 4/4)** vía modificador de
  `ATTACK_DAMAGE` (no afecta al daño de hechizo, que Iron's calcula con `spell_power`).
- Tooltip: set + escuela inferida del nombre + coste. Battlemage añade su herencia netherita.
- `bard_*` (Alshanex Familiars) **fuera** hasta confirmar que dan `spell_power`.

### 3.4 Tooltips (formato)

- Encabezado: `⚡ Ampere · <material/set> — <rol> (n/4)`, un `•` por estadística.
- Sin números de encantamiento: los efectos se describen ("daño ×1.5 a artrópodos",
  "recoge bloques intactos", "más botín de minerales"), nunca "Pesadilla V" ni "Fortuna III".
- Los porcentajes salen de los arrays `PCT_*` de `EquipmentEvents`, nunca de prosa.

### 3.5 Economía de reparación

Cuero / malla / hierro / oro: **100 %** por unidad. Diamante y netherita (y su linaje): **25 %**.

## 4. Números de referencia (config)

| Clave | Valor |
|---|---|
| `netherite_impact_base_exhaustion` | 0.6 |
| `diamond_impact_base_exhaustion` | 0.5 |
| `heavy_exhaustion_hit_scale` | 0.03 |
| `diamond_weak_hit_penalty` | 0.10 |
| `netherite_weak_hit_penalty` | 0.05 |
| `mage_weapon_damage_penalty` | 0.05 |
| `*_repair_fraction` (cuero/malla/oro/hierro) | 1.0 |
| `diamond_repair_fraction` / `netherite_repair_fraction` | 0.25 |

## 5. Invariantes (violarlas = bug)

1. Ningún tooltip nombra encantamientos.
2. Todo set derivado de netherita hereda fuego/wither + debilidad <8 + rep. 25 %.
3. Toda armadura con `spell_power` paga coste de daño cuerpo a cuerpo.
4. Los sets horizontales (15 armadura) no ganan armadura extra.
5. Todo poder tiene coste explícito y visible en el tooltip.
6. Los números del tooltip son los mismos que aplica el código.
7. Las herramientas no dan armadura ni velocidad de movimiento; eso es de la armadura
   (pendiente de rediseño, ver §7.1).

## 6. Checklist de `/sync` (ejecutar y pegar resultados)

```powershell
$repo = "C:\Users\Metabodiru\Desktop\AmpereRepo"
$srv  = "C:\Users\Metabodiru\Desktop\servidor-theoptimizer"
$py   = "C:\Users\Metabodiru\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe"

# 1. Integridad del pack (366/366 esperado)
powershell -NoProfile -ExecutionPolicy Bypass -File "$repo\validar.ps1"

# 2. Jar idéntico en repo y servidor, y coincide con index.toml
(Select-String -Path "$repo\index.toml" -Pattern "EquipmentBalance" -Context 0,1).Context.PostContext
Get-FileHash "$repo\mods\TheOptimizer-EquipmentBalance-*.jar", "$srv\mods\TheOptimizer-EquipmentBalance-*.jar" | Select-Object Hash, Path

# 3. Versión interna del jar
tar -xOf "$repo\mods\TheOptimizer-EquipmentBalance-*.jar" META-INF/mods.toml | Select-String 'version="'

# 4. Config: 26 claves y valores de §4
(Get-Content "$repo\config\theoptimizer_equipment.json" -Raw | ConvertFrom-Json).PSObject.Properties.Name

# 5. Pruebas del módulo (17 comprobaciones)
Push-Location "$env:APPDATA\PrismLauncher\instances\TheOptimizer"
& $py -m gestion.herramientas.reparaciones.balance_equipamiento.probar
Pop-Location

# 6. Invariante 1: sin nombres de encantamiento en tooltips
tar -xOf "$repo\mods\TheOptimizer-EquipmentBalance-*.jar" theoptimizer/equipment/EquipmentEvents.class |
  Select-String -Pattern "Pesadilla|Castigo|Toque de Seda|Fortuna III|Lealtad|Empalamiento"

# 7. Invariante 2: linaje completo
Select-String -Path "$env:APPDATA\PrismLauncher\instances\TheOptimizer\gestion\herramientas\reparaciones\balance_equipamiento\theoptimizer\equipment\EquipmentPolicy.java" `
  -Pattern "cursium|netherite_mage_|cataclysmFamily"

# 8. Publicación viva: Pages debe servir el mismo version.txt que el repo
Invoke-WebRequest "https://drox17.github.io/ampere_modpack/version.txt" -UseBasicParsing | Select-Object -ExpandProperty Content
Get-Content "$repo\version.txt"

# 9. Git limpio y sincronizado
git -C $repo status -sb
git -C $repo log --oneline -5
```

Interpretación rápida: si (1) no da `OK: el pack es coherente`, para y reporta. Si (2) da
hashes distintos repo/servidor, **no publiques**: ejecuta `instalar.py` del módulo. Si (4)
devuelve menos de 26 claves, alguien pisó la config: revisa §9.8.

## 7. Backlog priorizado

### 7.1 Rediseño de herramientas y armas (siguiente, aprobado en conversación)
Quitar de herramientas la velocidad de movimiento y de armas la guardia de armadura; dar
identidad de recolección (madera +25 % madera/hojas/cultivos, piedra +15 % piedra/menas) y de
combate (piedra aturdimiento 0.4 s, diamante +10 % crítico). Criterio de aceptación: ninguna
herramienta modifica movimiento ni armadura; cada tier tiene una línea propia en el tooltip.

### 7.2 Familias de armaduras huérfanas (~32 piezas)
Inventario completo: `irons_spellbooks` 52, `alexscaves` 13, `cataclysm` 12, `create` 8,
`alexsmobs` 8, `alexs_caves_spellbooks` 7, `alshanex_familiars` 5, `kaleidoscope_cookery` 2
(`geckolib` 8 son de mascota, ignorar). Familias propuestas: **Profundidad** (diving, aire +
velocidad acuática, −velocidad en tierra), **Supervivencia** (hazmat), **Ligero** (rainbounce,
roadrunner, emú, farmer, cardboard), **Ancestral** (bone reptile, sturdy boots).

### 7.3 Núcleos de Rol
Crafteo que transfiere el bonus de un set a otra armadura al 50 % y consume el set. Requiere
ítems nuevos (registro + texturas + recetas) y prueba en juego.

### 7.4 Jefes multifase
Rotación de daño (físico → mágico → fuego) por umbral de vida para que ningún set sea la
respuesta universal. No implementar sin una sesión de prueba: rompe el endgame si falla.

### 7.5 Sueltas
`bone_reptile_*` y `sturdy_boots` sin rol; `bard_*` pendiente de decidir si entran al rol mago.

## 8. Registro de cambios

| Fecha | Commit | Cambio | Verificación |
|---|---|---|---|
| 2026-11-10 | `e5c2a71` | Coste visible, debilidad de sets pesados, economía de reparación | probar 17/17 |
| 2026-11-10 | `4eb900f` | Cursium hereda tradeoff de netherita | revisión de recetas + build |
| 2026-11-10 | `5863fae` | Rol mago Iron's (−20 % melee a 4/4) | build + tooltips |
| 2026-11-10 | `0a0a2b6` | Battlemage hereda netherita | receta verificada |
| 2026-11-10 | `be46a44` | Tooltips sin nombres de encantamiento | grep sin coincidencias |
| 2026-11-10 | `0ea8e99` | Túnicas de Alex's Caves entran al rol mago | build |
| 2026-11-10 | — | `instalar.py` deja de pisar la config (merge) y añade 9 claves | 26 claves verificadas |

## 9. Trampas conocidas (ya nos costaron un fallo cada una)

1. **`MixinConfigs` solo en `mods.toml` no registra el mixin** en Forge 47.4.28: debe estar en
   `META-INF/MANIFEST.MF`. Pasó con MobBalance.
2. **`refmap` declarado sin archivo** en `*.mixins.json`: quitar la clave o generar el refmap.
3. **Herencia por `ArmorMaterial`** se rompe con materiales custom (Cataclysm, Irons): usar
   `ItemStack` + namespace/path.
4. **Sustituir rangos de líneas** en `EquipmentEvents.java` se comió
   `cleanInjectedAttributeTooltips` una vez: compilar siempre después.
5. **Nombres SRG**: `ItemStack.getDamageValue()` es `m_41773_` (no `m_41775_`).
6. **`probar.py` puede pasar con el jar viejo** si el build falló antes: mirar el `Empaquetando`.
7. **El generador de equipamiento no normaliza timestamps** del zip → el hash del jar cambia
   en cada build aunque el código no (el de MobBalance sí lo hace).
8. **`instalar.py` reescribía la config** con una plantilla de 17 claves y borraba los ajustes:
   corregido con merge que respeta valores existentes. Si vuelve a pasar, revisar §4.

## 10. Cómo publicar sin romper el pack

1. Editar fuente en `gestion/.../balance_equipamiento`.
2. `python -m gestion.herramientas.reparaciones.balance_equipamiento.instalar` (desde la instancia).
3. `python -m ... .probar` → debe decir `VERIFICACION EXITOSA`.
4. En el repo: `packwiz refresh` (o commit; el hook lo hace) y `validar.ps1`.
5. Si cambió comportamiento visible: ampliar `changelog.md` y **regenerar `version.txt`**
   (`MD5(changelog.md)` primeros 8 en minúsculas).
6. `git commit` + `git push`; comprobar Pages (§6.8).
7. Nunca copiar jars a la instancia de Prism: el updater los baja.
