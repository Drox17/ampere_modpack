# LOOT.md — Registro de loot tables del pack

> Regla de oro: **si una tabla no aparece aquí, el pack NO la modifica.** El registro contiene
> solo lo tocado y guarda el hash de cada entrada en `loot.json`. Si un hash cambia, alguien
> modificó esa tabla: hay que revisarla y actualizar `loot.json` en el mismo commit.

## Resumen

| Fuente | Tablas tocadas | Tipo | Para qué |
|---|---|---|---|
| `TheOptimizer_AdventureLoot.zip` | 4 cofres vanilla (dungeon, pirámide, templo, minas) | override | Inyectar **Irrompibilidad I, Botín I y Eficiencia I** (P5: solo esos tres encantamientos existen y solo en botín) |
| `TheOptimizer_AdventureLoot.zip` | `entities/wither_skeleton` | override | Tabla reescrita (incluye cráneo) — **intención exacta pendiente de documentar** |
| `TheOptimizer_AdventureLoot.zip` | 3 cofres de Iron's (pyromancer_supplies, mountain_tower, ice_spider_den) | override | Tintas y materiales mágicos por exploración (P10) |
| `TheOptimizer_AdventureLoot.zip` | `additional_generic/good/treasure_loot` + 3 loot modifiers | loot_modifier | Inyección en cofres de Iron's sin reemplazar sus tablas base |
| `TheOptimizer_LootFixes.zip` | `expatternprovider:ex_emc_interface` | corrección | La tabla del mod apunta a un item que no existe; el datapack la sustituye por el item real (`ex_emc_interface_part`) |
| `TheOptimizer_LootFixes.zip` | `kaleidoscope_chinesefood:doll_0..5` | corrección | Las muñecas ya no existen como item: tabla vacía para cortar el error de parseo |

Total registrado: **21 entradas** (5 overrides vanilla, 6 overrides de mods, 3 loot modifiers, 7 correcciones en datapack).

## Detalle

### Vanilla (5 overrides)

| Tabla | Qué se inyecta |
|---|---|
| `minecraft:chests/simple_dungeon` | Eficiencia, Botín, Irrompibilidad (nivel 1) |
| `minecraft:chests/desert_pyramid` | ídem |
| `minecraft:chests/jungle_temple` | ídem |
| `minecraft:chests/abandoned_mineshaft` | ídem |
| `minecraft:entities/wither_skeleton` | tabla reescrita (hueso, carbón, cráneo) |

Estas cuatro tablas de cofre son las **únicas vías** de conseguir los tres encantamientos
looteables, y por eso su hash es crítico: si se rompen, desaparece el bucle de botín del pack.

### Iron's Spellbooks (9 entradas)

- **3 loot modifiers** (`chest_loot/vanilla_generic`, `compat_good`, `compat_treasure`): añaden
  contenido a cofres existentes sin pisar la tabla del mod.
- **3 tablas nuevas** (`additional_generic_loot`, `additional_good_loot`,
  `additional_treasure_loot`): el contenido que inyectan esos modifiers.
- **3 cofres de estructura** (`pyromancer_supplies`, `mountain_tower`, `ice_spider_den/dungeon`):
  overrides con tintas (`good_ink`, `blank_rune`, `scroll`) y esencias.

### Drops de bloque (7)

`expatternprovider:ex_emc_interface` y `kaleidoscope_chinesefood:doll_0..5`. Son tablas de
bloque, no de botín: garantizan que el bloque suelte lo que debe.

## Mods con loot **sin tocar**

Todo lo demás. Ejemplos de mods con tablas propias que el pack deja intactas: `alexsmobs`,
`alexscaves`, `cataclysm`, `create`, `kaleidoscope_*`, `lootr`, `bountiful`, `simpletomb`,
`irons_spellbooks` (fuera de las 9 entradas de arriba), `alshanex_familiars`. Si el pack quisiera
tocarlas, tendrían que aparecer en `loot.json`.

## Cómo se revisa

1. `.\verificar_estado.ps1` incluye el check **`loot.registro`**: recalcula el SHA-256 de cada
   entrada registrada y avisa si alguna cambió.
2. Si sale `FAIL loot.registro`, alguien editó una tabla. Abre el archivo indicado, revisa el
   cambio y, si es intención, actualiza `loot.json` (regenerar hashes) en el mismo commit.
3. Para añadir una tabla nueva al registro: incluirla en `loot.json` con `base` (`repo` o
   `server`), `archivo`, `entrada`, `tipo`, `objetivo` y `sha256`.

## Limitaciones conocidas

- No se guarda una copia de la tabla vanilla original: el hash protege la versión del pack, no
  permite ver el diff contra vanilla. Para eso haría falta una copia de referencia.
- `entities/wither_skeleton` está registrada pero su intención no está escrita; conviene
  documentarla cuando se revise.
- El registro cubre datapacks y jars propios; si un mod del pack cambia sus tablas al
  actualizarse, el hash no lo detecta (no lo controlamos nosotros).


### Correcciones de tablas de mods (`TheOptimizer_LootFixes.zip`)

Estas siete tablas se envían en un **datapack**, no en el jar: un datapack tiene prioridad sobre los
recursos de los mods, y desde el jar perdían la prioridad y no servían de nada (verificado en log).
El zip se despliega al mundo del servidor y además viaja en el pack (`moonlight-global-datapacks/`),
así que también aplica en partidas individuales del cliente.

| Tabla del mod | Problema (bug del mod) | Corrección del pack |
|---|---|---|
| `expatternprovider:blocks/ex_emc_interface` | Referencia `expatternprovider:ex_emc_interface` como item, pero el item real es `…_emc_interface_part` | Dropea `…_emc_interface_part` |
| `kaleidoscope_chinesefood:blocks/doll_0..5` | Las muñecas no existen como item en 1.1.16 | Tabla vacía (sin drop) para cortar el error |

### Bugs upstream que NO se corrigen (documentados)

| Tabla de Iron's | Error | Efecto |
|---|---|---|
| `chests/citadel/citadel_tomes` | `Unknown type 'minecraft:set_written_book_pages'` (función que no existe en 1.20.1) | La tabla no carga: el cofre `citadel_tomes` y el pool 8 de `citadel_bookshelf` quedan sin botín |
| `chests/catacombs/crypt_loot` | `Missing name, expected to find a string` en `LootTableReference` | La tabla no carga: los cofres de catacumbas quedan sin botín |

No se tocan porque son del mod y decidir qué botín deberían dar es una decisión de diseño, no una
corrección mecánica. Si se quiere arreglar, la vía es reescribir ambas tablas en este mismo datapack
con contenido coherente (tintas, runas, pergaminos).
