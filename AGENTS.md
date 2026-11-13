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
| P3 | **XP completamente erradicada** | No hay orbes de experiencia, mesa de encantamientos ni Mending. El yunque no cobra niveles y la barra de XP está oculta del HUD. | Que se usen los niveles para medir progresión, dar stats o desbloquear cosas |
| P4 | **Mesa de encantamientos decorativa** | Interacción cancelada; es un bloque de decoración | Que se pueda usar "con suerte" |
| P5 | **Encantamientos eliminados del juego** | Solo **Irrompibilidad I y Eficiencia I** aparecen en cofres de mina/mazmorra/templo y se combinan en yunque | Que existan libros de otros encantamientos |
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

**Reglas derivadas que ya han causado errores:**
- **No nombrar encantamientos en tooltips**: se describe el efecto ("daño ×1.5 a artrópodos").
- **Detalles avanzados con Shift**: Si se quiere ver información detallada o mecánicas complejas de un ítem, se usa la tecla **Shift** sobre el ítem con el cursor (mecánica por implementar).
- **Nada de prosa con números**: los valores salen del código y se muestran en el tooltip.
- **No proponer sistemas que usen XP** como moneda ni escalar mecánicas con niveles (P3).
- **No proponer "subir de tier" como recompensa** sin coste (P1/P2).
- **Cofre del End: estrella del Nether y solo materiales** (rechaza armas, herramientas, armaduras y contenedores; el tooltip lo avisa).
- **Pasivas de recolección en todo `DiggerItem`** (pico, pala, hacha, azada), no solo el pico. Madera=Hojas Gratis, Piedra=+15% en menas, Hierro=Minado 3x3, Oro=Auto-Fundición, Diamante=Toque de Seda oculto, Netherita=Fortuna III. *(Esta mecánica está abierta a ajustes coherentes que no violen otros puntos del balance)*.
- **Durabilidad 1.22.0**: armaduras de 15 puntos a 165/240/225/195 (825 el set); herramientas de tiers a 80→160→300→160→1561→2031.
- **Movimiento ÷5** (`movement_exhaustion_factor = 0.2`): correr 0.02/m, salto 0.01, salto corriendo 0.04. Combate intacto.
- **La piedra de afilar solo extrae Irrompibilidad y Eficiencia**; los innatos del material nunca son libros.
- **Equipo de spawn: no se dropea** (armadura/armas generadas e invocaciones); el que entrega el jugador sí.
- **Encantamientos innatos: solo para jugadores** (la Lealtad del tridente no vuelve a los mobs).
- **Drops cotidianos con mínimo 1, sin RNG de granja** (vara de blaze, pólvora, perla, caparazón, carbón del wither skeleton).
- **Jefes: respuestas reactivas, no prohibiciones**: se corrige el daño, el agro o el entorno; no se bloquean bloques ni se cancelan invocaciones.

## 2. Mods del pack (lo que existe y lo que no)

**Lista de mods instalados (Forge 1.20.1):**
`Alex's Caves (y Spellbooks), Alex's Mobs, All The Leaks, Almanac, Alshanex Familiars, Alternate Current, AmbientSounds, AppleSkin, Applied Energistics 2, Architectury, Balm, Better Advancements, BetterDays, Blueprint, Bountiful, Building Gadgets 2, Citadel, Chunk Loaders, Clean Swing Through Grass, Cloth Config v10, Comforts, Controlling, Create, Create Crafts & Additions, Create Repair, CreativeCore, Cubes Without Borders, Curios API, Default Options, Deimos, Dynamic Crosshair, Embeddium, Entity Model/Texture Features, Equipment Compare, ExtendedAE, FamiliarsLib, Fancy Tab Sections, FancyMenu, Fast Item Frames, Fast Leaf Decay, Fast Paintings, Ferrite Core, flib, FramedBlocks, Framework, Functional Storage, Gallery, GeckoLib 4, Glodium, Gnetum, Guard Ribbits, GuideME, Highlight, Iceberg, Icy's Better Horses, ImmersiveUI, Inventory Essentials, Iron's Spells 'n Spellbooks (y Lib), Jade, JEI, JER, JourneyMap, Kaleidoscope (Caves Cookery, ChineseFood, Cookery, Doll, End, Extension, Flora, ImmersiveEating, Nether), Kambrik, Kiwi Library, Konkrete, kotlinforforge, L_Enders_Cataclysm, LAN World Plug-n-Play, LaserIO, LetMeDespawn, LionfishAPI, Lootr, Melody, MezzConfig, ModernFix, Moonlight Library, Mouse Tweaks, No Trample, OctoLib, Oculus, Particular Reforged, Passable Foliage, Patchouli, Player Animator, Polymorph, Presence Footsteps, Punchy (y Moves), Puzzles Lib, Resourcefulconfig, Ribbits (y addons Croaks/Useful), Searchables, Simple Tombstone, Sound Physics Remastered, spark, Structure Layout Optimizer, SuperMartijn642's (Config/Core Lib), TheOptimizer (AdvancementLayout, EquipmentBalance, FamiliarsTagFix, MobBalance, SimpleTombParticlesFix, WildlifeRepopulation), Titanium, Wishful Recipes, YUNG's (API, Better Strongholds)`.

**No están** (no los asumas): Apotheosis, Tinkers, Spore, Botania, Mekanism, Sophisticated Backpacks, Ars Nouveau. Tampoco asumas mecánicas de XP (`MiningXP` y `DeathXP` fueron retirados).

## 3. Estado implementado (IDs estables)

**Sets vanilla (S), EquipmentBalance 1.23.0** — físicos: 16 armadura (2/5/6/3), túnicas: 10 (1/3/4/2), Cursium: 12 (2/4/4/2). Dureza 0 en toda armadura:
| ID | Set | Rol | Coste |
|---|---|---|---|
| S1 | Cuero | Explorador: caída −7/15/25/40 % | sin defensa extra |
| S2 | Cota de malla | Escaramuzador: proyectiles −5/10/18/30 %, velocidad +4/8/12/16 % | sin ayuda vs explosiones |
| S3 | Hierro | Infantería: empuje −5/10/18/30 %, explosiones −4/8/15/25 % | — |
| S4 | Oro | Arcano: magia −4/8/15/25 %, +1 Suerte, piglins | — |
| S5 | Diamante | Coloso: absorbe 50 % del excedente sobre 10 de daño a 4 piezas | ataque −15 %, brecha de enjambre, agotamiento, rep. 25 % |
| S6 | Netherita | Coloso como diamante; fuego/wither −25 % por pieza (inmunidad completa), repulsión −25 % con linaje completo | ataque −20 %, brecha, daño +10 % con luz ambiental <8 (proporcional a piezas), agotamiento, rep. 25 % |
| S7 | Tortuga | Escafandra: respiración + minar bajo el agua | — |

**Linaje netherita (L)** — todo lo forjado sobre `minecraft:netherite_*` hereda S6:
`L1` ignitium · `L2` cursium · `L3` monstrous_helm · `L4` netherite_mage. Fuera del linaje: `bone_reptile`, `sturdy_boots` (sus atributos físicos de Cataclysm sí se normalizan).

**Variantes 1.23.0**: Monstrous (casco) duplica la amortiguación combinada, hasta 100 % del excedente, y añade movimiento −10 % y ataque −30 % por casco (se compone con las demás piezas pesadas). Ignitium aporta la mitad de amortiguación y prende al atacante cuerpo a cuerpo durante 3 s, con recarga de 40 ticks por jugador. Cursium no aporta Coloso, brecha ni coste de ataque.

**Brecha**: 2 impactos de combate aceptados dentro de 30 ticks reducen la armadura efectiva a la mitad en el segundo impacto. Ventana móvil; las fuentes ambientales y la inanición no cuentan. Cursium conserva la exención por pieza; mezclarlo con una pieza pesada vuelve a permitir brecha.

**Feedback de hambre (EquipmentBalance 1.23.1)**: a ≤6 puntos de comida se muestran los sprites vanilla de Hambre y un temblor de −1 a +1 píxel, cada 4 ticks; a ≤2, cada 2 ticks. Gruñido local de Sniffer cada 160 ticks con 1–6 puntos, cada 80 ticks con 1–2 (volumen 0.20, tono 0.55). Comer por encima del umbral reinicia el temporizador; creativo/espectador/muerto quedan excluidos. Solo cambia el feedback, sin aplicar efectos ni alterar saturación. STARVE a cero conserva el latido y la supresión de animación de daño de 1.23.0. Se sustituye el aviso anterior de cruce 8→7.

**Roles (R)**: `R1` mago (túnicas `irons_spellbooks` + `alexs_caves_spellbooks`, −5 % daño cuerpo a cuerpo por pieza, máx −20 %) · `R2` anti-mago (oro, S4).

**Herramientas/armas (T)**: rediseño unificando extracción a 6.0.
*   **Madera:** Daño x1.5 a artrópodos. Hojas no gastan durabilidad. +25% vel en madera/cultivos y sueltan polvo de hueso.
*   **Piedra:** Empuje I, Lentitud I al golpear, interrumpe casters/creepers. +15% vel en menas y piedra.
*   **Hierro:** Barrido III y alcance +0.5 (armas). Minado 3x3 y doble durabilidad (DiggerItem). 100% rep por lingote.
*   **Oro:** Castigo III, pacifica piglins, +1 Suerte. Auto-fundición en DiggerItem. 100% rep por lingote. Daño/durabilidad = Hierro.
*   **Diamante:** 15% chance de crítico, alcance +1.0. Toque de seda oculto en herramientas. 25% rep por diamante.
*   **Netherita:** Lentitud II al golpear, +15% daño vs armadura. Fortuna III oculta. 25% rep por lingote.

**Matriz familia ↔ counter (1.19.0):**
| Familia | Mecánica | Counter |
|---|---|---|
| Arañas | Esquiva 25 % (mitad de daño) | **Madera** (precisión + ×1.5) |
| No-muertos | Horda: +25 % empuje y 1.5 de agotamiento con 3+ zombis | **Hierro** (área) · **Oro** (Castigo III) |
| Esqueletos/ saqueadores | Lentitud I 1 s a más de 8 bloques | **Cota de malla ≥2 piezas** |
| Enderman/Shulker | Teletransporte | **Diamante** (anclaje 3 s) |
| Creeper/Bruja/Evocador | Mecha, poción o conjuro | **Piedra** (interrupción) |

## 4. Invariantes (si falla una, es bug)

1. **C1** Ningún tooltip nombra encantamientos.
2. **C2** Todo set del linaje L hereda fuego/wither, repulsión, debilidad con luz ambiental <8 y reparación 25 %. Los efectos defensivos escalan por pieza; la inmunidad requiere el linaje completo.
3. **C3** Toda armadura con `spell_power` paga coste de daño cuerpo a cuerpo.
4. **C4** Paridad horizontal: sets físicos 16 (2/5/6/3), túnicas 10 y Cursium 12; dureza 0, también en atributos externos. Sustituye el techo anterior de 15/20 por decisión explícita de la 1.23.0.
5. **C5** Todo poder tiene coste visible en el tooltip (P2).
6. **C6** Los números del tooltip son los del código.

## 5. Verificación y Rutas de Desarrollo (Antigravity Workspace)

**A. Ejecución de Diagnóstico (`/sync`)**
    cd C:\Users\Metabodiru\Desktop\AmpereRepo
    .\verificar_estado.ps1          # imprime OK/FAIL/SKIP por check y un RESUMEN

- **1 sola llamada.** No abras fuentes, jars ni configs si el resumen dice `9/9` o más.
- Si hay `FAIL`, el script imprime `id · esperado · real`: con eso basta para reportar.
- Opciones útiles: `.\verificar_estado.ps1 -Json` para salida máquina; `-SkipTests` si no quieres esperar `probar.py`.
- El estado esperado vive en `estado.json` (versiones, conteos, 90 claves de config, IDs).

**B. Mapa de Rutas (Dónde programar sin explorar)**
| Tarea / Componente | Directorio / Comando exacto |
|---|---|
| **Lógica Java, Mixins y Eventos** | `C:\Users\Metabodiru\Desktop\TheOptimizerMods\balance_equipamiento\theoptimizer\equipment\` (MobBalance: módulo vecino `balance_mobs`) |
| **Loot Tables y Recetas** | `datapacks/TheOptimizer_AdventureLoot/data/` |
| **Búsqueda de Tags (Scripts)** | Usa `python scripts/find_tags.py` |
| **Compilación silenciosa** | Desde `TheOptimizerMods`, usa `python scripts/compile_quiet.py` antes de testear |
| **Gestión de Mods** | Vía `packwiz` (modifica `packwiz.json` o usa comandos CLI, no subas `.jar` al repo) |

**C. Post-Operación (Regla de Limpieza)**
Al terminar una operación de desarrollo o añadir/quitar mods, **debes actualizar obligatoriamente los datos de mods y versiones** en la documentación si es necesario para mantener sincronizado este archivo y `estado.json`.

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
| 2026-11-13 | pendiente de commit | EquipmentBalance 1.23.0: 15/16; 75 pruebas JVM, 86 claves, 27 tablas de loot | solo git.limpio (cambios locales para prueba); Pages SKIP por DNS; sin push |
| 2026-11-13 | publicación 1.23.1 | 15/16 antes del commit; 737 comprobaciones JVM, 90 claves, 27 tablas de loot | git.limpio temporal hasta commit; Pages SKIP por DNS; push autorizado en ambos repositorios |

## 7. Memoria profunda (léela solo si vas a diseñar, no en `/sync`)

`docs/BALANCE.md`: números de referencia, backlog con criterios de aceptación, trampas conocidas, procedimiento de publicación y razón de cada regla.
`docs/LOOT.md` + `loot.json`: qué loot tables toca el pack (y cuáles no), con hashes verificados en cada `/sync`.
`docs/HAMBRE_VANILLA.md`: fuentes vanilla de agotamiento (correr 0.1/m, salto 0.05, ataque 0.1, minería 0.005, regen 6.0) y su conversión a saturación/hambre.
`docs/MOBS_HOSTILES_VANILLA.md` + `datos/mobs_hostiles_vanilla.json`: atributos de los 37 hostiles vanilla (bytecode 1.20.1) y qué cambia MobBalance. Reejecutable con `herramientas/extraer_atributos_vanilla.py`.
`docs/PROGRESION_EQUIPAMIENTO.md`: auditoría horizontal vs vertical del equipo, hallazgos H1-H8 y márgenes de mejora priorizados.
