# AGENTS.md — Ampere Better Survival (modpack)

> **Punto de entrada.** Lee §1 (filosofía) y §2 (mods) antes de proponer cualquier cosa.
> En `/sync` ejecuta **un solo comando**: `.\verificar_estado.ps1`. Detalle largo en `docs/BALANCE.md`.

## 1. Filosofía del pack (no negociable)

Modpack privado Forge 1.20.1 pensado como **RPG de equipo y exploración**, no como sandbox
vanilla con mods. Si una propuesta contradice estos trece puntos, está mal.

| # | Principio | Qué implica | Qué **no** implica |
|---|---|---|---|
| P1 | **Progresión horizontal + vertical** | Cada set/tier tiene un rol; el vertical (diamante→netherita) añade aguante pero arrastra un coste | Que el tier alto sea mejor en todo |
| P2 | **Todo poder tiene coste explícito** | Agotamiento, daño recibido, daño de arma, reparación cara | Que exista un set "gratis" |
| P3 | **XP sin función económica** | No hay mesa de encantamientos, el yunque no cobra niveles, Mending no existe: los niveles solo marcan progreso | Que la XP se elimine del HUD o de las estadísticas |
| P4 | **Mesa de encantamientos decorativa** | Interacción cancelada; es un bloque de decoración | Que se pueda usar "con suerte" |
| P5 | **Encantamientos eliminados del juego** | Solo **Irrompibilidad I, Botín I y Eficiencia I** aparecen en cofres de mina/mazmorra/templo y se combinan en yunque | Que existan libros de otros encantamientos |
| P6 | **Velocidad de minado unificada a hierro (6.0)** | Ninguna herramienta es más rápida por tier; la diferencia es el rol | Que el diamante mine más rápido |
| P7 | **Ninguna pieza opaca a otra** | Cada material debe ser la mejor opción en al menos una actividad | Que todas sirvan para todo |
| P8 | **Spawns adulterados a propósito** | Reparto 55/45 vanilla-mods, cap de criaturas 16 (config `creature_spawn_cap`), nigromante 18→2, fauna vanilla con respawn cíclico | Que sea "spawn vanilla" |
| P9 | **Yunque reworkeado** | 0 niveles de XP, sin "demasiado caro", reparación por familia (100 % baratos / 25 % caros), forja de tridentes | Que sea el yunque vanilla |
| P10 | **Iron's Spellbooks looteable** | Las tintas y materiales mágicos entran por cofres (datapack `TheOptimizer_AdventureLoot`), porque en vanilla una granja de mobs es más eficiente | Que se hayan añadido recetas nuevas para tintas |
| P11 | **Se buscan sugerencias** | Cualquier mecánica propuesta se evalúa contra P1-P10 y, si encaja, se implementa | Que la filosofía esté cerrada: el diseño está abierto a ideas |
| P12 | **Juego tradicional primero** | Las recompensas salen de explorar, combatir, construir y coleccionar | Que la automatización o el AFK sean la vía óptima |
| P13 | **Desincentivar al jugador técnico** | Granjas AFK, duplicación, min-max y automatización deben **dejar de ser la mejor opción** (no se prohíben: se vuelven peores) | Que se bloqueen mecánicas legítimas de construcción o redstone |

**Prueba de diseño (aplicar antes de proponer nada):**

1. ¿La forma más eficiente de conseguir X es **jugar** (explorar, pelear, construir) o **dejar una máquina**?
2. ¿Un jugador técnico que optimiza 200 horas obtiene una ventaja que rompe la progresión?
3. ¿La mecánica se puede resolver **AFK**?

Si la respuesta lleva a máquina, optimización extrema o AFK, **la propuesta se rediseña** antes de implementarse.

Reglas derivadas que ya han causado errores:
- **No nombrar encantamientos en tooltips**: se describe el efecto ("daño ×1.5 a artrópodos").
- **Nada de prosa con números**: los valores salen del código y se muestran en el tooltip.
- **No proponer sistemas que usen XP** como moneda (P3).
- **No proponer "subir de tier" como recompensa** sin coste (P1/P2).
- **Cofre del End: estrella del Nether y solo materiales** (rechaza armas, herramientas, armaduras y contenedores; el tooltip lo avisa).
- **Drops cotidianos con mínimo 1, sin RNG de granja** (vara de blaze, pólvora, perla, caparazón, carbón del wither skeleton).
- **Jefes: respuestas reactivas, no prohibiciones**: se corrige el daño, el agro o el entorno; no se bloquean bloques ni se cancelan invocaciones (ver `docs/BALANCE.md` §1.6).

## 2. Mods del pack (lo que existe y lo que no)

363 entradas (103 metafiles Modrinth + 20 jars locales) · servidor con 90 jars · Forge 47.4.28.
**Si un mod no aparece aquí, no está en el pack: no lo propongas.**

| Dominio | Mods |
|---|---|
| Equipo y balance | `TheOptimizer-EquipmentBalance`, `TheOptimizer-MobBalance`, `TheOptimizer-WildlifeRepopulation` |
| Magia | `irons_spellbooks`, `irons_lib`, `alexs_caves_spellbooks`, `alshanex_familiars`, `familiarslib` |
| Combate/jefes | `L_Enders_Cataclysm`, `alexsmobs`, `alexscaves`, `citadel`, `lionfishapi` |
| Spawns y fauna | (TheOptimizer) + `alexsmobs` config, `letmedespawn` |
| Loot y cofres | `lootr`, `Bountiful`, `BountifulBounties` (datapack), datapacks `TheOptimizer_*` |
| Cocina/hogar | `kaleidoscope_cookery`, `kaleidoscope_flora`, `kaleidoscope_nether`, `kaleidoscope_end`, `kaleidoscope_doll`, `kaleidoscope_chinesefood`, `KaleidoscopeCavescookery`, `comforts` |
| Tecnología | `create`, `createaddition`, `create_repair`, `appliedenergistics2`, `ExtendedAE`, `expatternprovider`, `laserio`, `functionalstorage`, `framedblocks`, `buildinggadgets2`, `blueprint` |
| Progresión/estructuras | `yungs-better-strongholds`, `yungsapi`, `structure_layout_optimizer` |
| Rendimiento | `modernfix`, `ferritecore`, `alternate-current`, `spark`, `alltheleaks` |
| Cliente/QoL | `jei`, `jade`, `journeymap`, `journeymap-shared-maps`, `embeddium`, `oculus`, `fancymenu`, `patchouli`, `simpletomb` |

**No están** (no los asumas): Apotheosis, Tinkers, Spore, Botania, Mekanism, Sophisticated
Backpacks, Ars Nouveau, Tetra (solo el addon de barras de Iron's), Create: Crafts & Additions
sí está, Create: Diesel Generators no.
También fuera: `TheOptimizer-MiningXP` y `TheOptimizer-DeathXP` (retirados: la XP no tiene función, P3).

## 3. Estado implementado (IDs estables)

**Sets vanilla (S)** — 15 armadura los cuatro primeros, 20 los dos últimos:

| ID | Set | Rol | Coste |
|---|---|---|---|
| S1 | Cuero | Explorador: caída −7/15/25/40 % | sin defensa extra |
| S2 | Cota de malla | Escaramuzador: proyectiles −5/10/18/30 %, velocidad +4/8/12/16 % | sin ayuda vs explosiones |
| S3 | Hierro | Infantería: empuje −5/10/18/30 %, explosiones −4/8/15/25 %, dureza +0.5/pieza | — |
| S4 | Oro | Arcano: magia −4/8/15/25 %, +1 Suerte, piglins | — |
| S5 | Diamante | Élite: golpes ≥8 −6/12/19/25 % | **+5 % daño <8**, agotamiento, rep. 25 % |
| S6 | Netherita | Nether: fuego −5/12/20/35 %, wither −10/20/35/50 %, golpes ≥8 −4/8/13/18 % | **+10 % daño <8**, agotamiento, rep. 25 % |
| S7 | Tortuga | Escafandra: respiración + minar bajo el agua | — |

**Linaje netherita (L)** — todo lo forjado sobre `minecraft:netherite_*` hereda S6:
`L1` ignitium · `L2` cursium · `L3` monstrous_helm · `L4` netherite_mage. Fuera: `bone_reptile`, `sturdy_boots`.

**Roles (R)**: `R1` mago (túnicas `irons_spellbooks` + `alexs_caves_spellbooks`, −5 % daño cuerpo a cuerpo por pieza, máx −20 %; `bard_*` fuera) · `R2` anti-mago (oro, S4).

**Herramientas/armas (T)**: rediseño hecho en 1.10.0/1.11.0. Madera: +25 % en madera/hojas/cultivos y hojas sin desgaste · Piedra: +15 % en cantera/menas y aturdimiento 0.4 s (solo armas) · Hierro: alcance +0.5 y barrido 75 % (Filo Arrasador III real) · Diamante: alcance +1.0 y 15 % crítico ×1.5 · Oro: Castigo III (+7.5 vs no-muertos), suerte y piglins · Madera: ×1.5 real contra artrópodos, recolección +25 %. Detalle y números en `docs/BALANCE.md`.

## 4. Invariantes (si falla una, es bug)

1. **C1** Ningún tooltip nombra encantamientos.
2. **C2** Todo set del linaje L hereda fuego/wither + debilidad <8 + reparación 25 %.
3. **C3** Toda armadura con `spell_power` paga coste de daño cuerpo a cuerpo.
4. **C4** Los sets S1–S4 no ganan armadura extra (15).
5. **C5** Todo poder tiene coste visible en el tooltip (P2).
6. **C6** Los números del tooltip son los del código.

## 5. Verificación

```powershell
cd C:\Users\Metabodiru\Desktop\AmpereRepo
.\verificar_estado.ps1          # imprime OK/FAIL/SKIP por check y un RESUMEN
```

- **1 sola llamada.** No abras fuentes, jars ni configs si el resumen dice `9/9` o más.
- Si hay `FAIL`, el script imprime `id · esperado · real`: con eso basta para reportar.
- `.\verificar_estado.ps1 -Json` para salida máquina; `-SkipTests` si no quieres esperar `probar.py`.
- El estado esperado vive en `estado.json` (versiones, conteos, 26 claves de config, IDs).

## 6. Registro de `/sync` (append-only: añade una línea por pasada)

| Fecha | Commit | Resultado | Deriva detectada |
|---|---|---|---|
| 2026-11-10 | `97ab9e0` | base del registro | config reescrita por `instalar.py` → corregido con merge |
| 2026-11-10 | `1dd27aa` | 13/13 sin derivas (1 SKIP en `tests.modulo`) | ninguna; config y jar alineados |
| 2026-11-10 | `6b2f902` | 13/13 tras 1.3.0 (reparación simple) | `pages.version` desfasado ~50 s; convergió |
| 2026-11-10 | `1addb4e` | 13/13 tras 1.5.0 (elytra, hambre-escudo, beacon) | ninguna |
| 2026-11-11 | `ccc36b6` | 13/13 tras 1.7.0 (yunque en EquipmentBalance, MiningXP retirado) | orbes de XP vuelven a vanilla hasta la siguiente pasada |
| 2026-11-11 | `0211a6a` | 1.8.0: orbes de XP apagados; estados D1.1-D1.5 corregidos | ninguna |
| 2026-11-11 | `7068456` | 1.11.0: hojas sin desgaste (cierra T1) | ninguna |

## 7. Memoria profunda (léela solo si vas a diseñar, no en `/sync`)

`docs/BALANCE.md`: números de referencia, backlog con criterios de aceptación, trampas
conocidas, procedimiento de publicación y razón de cada regla.
`docs/LOOT.md` + `loot.json`: qué loot tables toca el pack (y cuáles no), con hashes verificados en cada `/sync`.
`docs/MOBS_HOSTILES_VANILLA.md` + `datos/mobs_hostiles_vanilla.json`: atributos de los 37 hostiles vanilla (bytecode 1.20.1) y qué cambia MobBalance. Reejecutable con `herramientas/extraer_atributos_vanilla.py`.
`docs/PROGRESION_EQUIPAMIENTO.md`: auditoría horizontal vs vertical del equipo, hallazgos H1-H8 y márgenes de mejora priorizados.
