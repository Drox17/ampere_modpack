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
| P5 | **Encantamientos eliminados y cofres sanitizados** | Solo **Irrompibilidad I, Botín I y Eficiencia I** (máximo **1 encantamiento vanilla por cofre**, nivel I); **ningún cofre otorga equipamiento vanilla** (armas, herramientas, armaduras, escudos, arcos, ballestas, tridentes, cañas, tijeras, mechero o armadura de caballo; `elytra` preservada en `lootr:chests/elytra`) y **ningún cofre otorga lingotes, bloques ni minerales completos** salvo carbón/carbón vegetal (conversión a **pepitas** con `Nuggets For All`) | Que existan otros encantamientos, equipo vanilla en cofres, >1 libro por cofre o lingotes/gemas enteras |
| P6 | **Velocidad de minado unificada a hierro (6.0)** | Ninguna herramienta es más rápida por tier; la diferencia es el rol | Que el diamante mine más rápido |
| P7 | **Ninguna pieza opaca a otra** | Cada material debe ser la mejor opción en al menos una actividad | Que todas sirvan para todo |
| P8 | **Spawns adulterados a propósito** | Reparto 55/45 vanilla-mods, cap de criaturas 16 (config `creature_spawn_cap`), nigromante 18→2, fauna vanilla con respawn cíclico | Que sea "spawn vanilla" |
| P9 | **Yunque reworkeado** | 0 niveles de XP, sin "demasiado caro", reparación por familia (100 % básicos / 25 % diamante / 50 % netherita y linaje), forja de tridentes | Que sea el yunque vanilla |
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
- **No nombrar encantamientos en tooltips**: se describe el efecto ("daño ×2 a artrópodos").
- **Detalles avanzados con Shift** (1.24.2): resumen de rol y costes al pasar el cursor; mantener **Shift** muestra cifras y condiciones del equipo vestido actualmente, nunca un conjunto completo hipotético. Usar segundos, corazones y muslitos en vez de ticks o fórmulas técnicas.
- **Nada de prosa con números**: los valores salen del código y se muestran en el tooltip.
- **No proponer sistemas que usen XP** como moneda ni escalar mecánicas con niveles (P3).
- **No proponer "subir de tier" como recompensa** sin coste (P1/P2).
- **Cofre del End: estrella del Nether y solo materiales** (rechaza armas, herramientas, armaduras y contenedores; el tooltip lo avisa).
- **Sanitización integral de cofres (AdventureLoot 1.4.0 + EquipmentBalance 1.24.6):** ningún cofre genera equipamiento vanilla (salvo `minecraft:elytra` en `lootr:chests/elytra`), nunca caen lingotes, bloques minerales ni minerales enteros salvo carbón/carbón vegetal (conversión a pepitas vanilla, `Nuggets For All`, pepitas de Cataclysm o esencias de Iron's) y cada cofre contiene como máximo `1` encantamiento vanilla permitido de nivel I (`unbreaking`, `looting`, `efficiency`), reforzado en ejecución vía `LootTableMixin` (`sanitize_chest_loot = true`).
- **Pasivas de recolección en todo `DiggerItem`** (pico, pala, hacha, azada), no solo el pico. Madera=Hojas Gratis, Piedra=+20% en piedra/menas y cantera sin desgaste, Hierro=Minado 3x3 (agachado=1x1), Oro=Auto-Fundición, Diamante=Toque de Seda oculto, Netherita=Fortuna III. *(Esta mecánica está abierta a ajustes coherentes que no violen otros puntos del balance)*.
- **Durabilidad 1.22.0**: armaduras de 15 puntos a 165/240/225/195 (825 el set); herramientas de tiers a 80→160→300→160→1561→2031.
- **Movimiento ÷5** (`movement_exhaustion_factor = 0.2`): correr 0.02/m, salto 0.01, salto corriendo 0.04. Combate intacto.
- **La piedra de afilar solo extrae Irrompibilidad, Botín y Eficiencia**; los innatos del material nunca son libros.
- **Equipo de spawn: no se dropea** (armadura/armas generadas e invocaciones); el que entrega el jugador sí.
- **Encantamientos innatos: solo para jugadores** (la Lealtad del tridente no vuelve a los mobs).
- **Drops cotidianos con mínimo 1, sin RNG de granja** (vara de blaze, pólvora, perla, caparazón, carbón del wither skeleton).
- **Jefes: respuestas reactivas, no prohibiciones**: se corrige el daño, el agro o el entorno; no se bloquean bloques ni se cancelan invocaciones.
- **Create + AE2 acotados a construcción y logística (`AdventureLoot 1.4.0`):** `Create Repair` queda retirado (`P2`/`P9`); el lavado (`gravel`, `red_sand`, `soul_sand`) y triturado de rocas (`crimsite`, `ochrum`, `tuff`) no producen hierro, oro ni `electrum`; todas las recetas de `create:experience_nugget` y reciclado de armaduras de caballo quedan suprimidas (`P3`); menas de equipo (`iron`, `gold`, `diamond`, `emerald`) topadas `1:1`; añadidas recetas de puente Create ↔ AE2 (`certus`, `fluix`, `sky_dust`, prensas `deploying`) y piedra decorativa renovable (`tuff`, `calcite`, `crimsite`, `ochrum`, `veridium`, `asurine`).

## 2. Mods del pack (lo que existe y lo que no)

**Lista de mods declarados (Forge 1.20.1):**
`Almanac, Alternate Current, AmbientSounds, AppleSkin, Applied Energistics 2, Architectury API, Balm, Better Advancements, Better Days, Blueprint, Bountiful, Cataclysm x YUNG's Better Nether Fortress, Chunk Loaders, Cloth Config API, Comforts, Controlling, Create, Create Crafts & Additions, CreativeCore, Cubes Without Borders, Curios API, Default Options, Deimos, Dynamic Crosshair, Embeddium, Equipment Compare, Extended AE, FLIB, Fancy Tab Sections, FancyMenu, Fast Item Frames, Fast Paintings, FastLeafDecay-32, FerriteCore, FramedBlocks, Functional Storage, Gallery, Geckolib, Glodium, Gnetum, Guard Ribbits, GuideME, Highlight, Iceberg, Icy's Better Horses, Immersive UI, Inventory Essentials, Iron's Lib, Iron's Spells 'n Spellbooks, Jade 🔍, JourneyMap, JourneyMap Shared Maps, Just Enough Items (JEI), Just Enough Resources (JER), Kaleidoscope  Jei Extension, Kaleidoscope Cookery, Kaleidoscope End, Kaleidoscope Nether, Kaleidoscope: Immersive Eating, KaleidoscopeChineseFood, Kambrik, Kiwi 🥝, Konkrete, Kotlin for Forge, LAN World Plug-n-Play (mcwifipnp), L_Ender's Cataclysm, Let Me Despawn, Lionfish-API, Lootr, Melody, MezzConfig, ModernFix, Moonlight Lib, Mouse Tweaks, Nuggets For All, Oculus, Particular ✨ Reforged, Passable Foliage 🌳, Patchouli, Polymorph, PresenceFootsteps-1.20.1-1.9.1-beta.1, Puzzles Lib, Resourceful Config, Ribbits, Ribbits: Croaks, Searchables, ShatterLib | OctoLib, Sound Physics Remastered, Structure Layout Optimizer, SuperMartijn642's Config Lib, SuperMartijn642's Core Lib, TerraBlender, TheOptimizer-AdvancementLayout-1.0.0, TheOptimizer-EquipmentBalance-1.24.7, TheOptimizer-MobBalance-1.5.1, TheOptimizer-SimpleTombParticlesFix-1.0.0, TheOptimizer-WildlifeRepopulation-1.6.1, Titanium, Traveler's Titles, Useful Ribbits, Wishful Recipes, YUNG's API, YUNG's Better Desert Temples, YUNG's Better Dungeons, YUNG's Better Mineshafts, YUNG's Better Nether Fortresses, YUNG's Better Ocean Monuments, YUNG's Better Strongholds, YUNG's Better Witch Huts, YUNG's Cave Biomes, YUNG's Extras, [EMF] Entity Model Features, [ETF] Entity Texture Features, alltheleaks-1.1.4+1.20.1-forge, buildinggadgets2-1.0.8, cleanswing-1.20-1.8, framework-forge-1.20.1-0.8.0, kaleidoscope_flora-0.3.5.1-all, laserio-1.6.8, notrample-1.20.1-1.0.1, playerAnimator, simpletomb-1.20.1-1.3.0, spark`.

**No están** (no los asumas): Apotheosis, Tinkers, Spore, Botania, Mekanism, Sophisticated Backpacks, Ars Nouveau. Tampoco asumas mecánicas de XP (`MiningXP` y `DeathXP` fueron retirados).

## 3. Estado implementado (IDs estables)

**Sets vanilla (S), EquipmentBalance 1.24.7** — físicos: 16 armadura (2/5/6/3), túnicas: 10 (1/3/4/2), Cursium: 12 (2/4/4/2). Dureza 0 en toda armadura:
| ID | Set | Rol | Coste |
|---|---|---|---|
| S1 | Cuero | Explorador: caída −5/12/20/35 %; cuero completo: proyectil +30 %, carga de ballesta ×2 y perforación | no aporta Coloso |
| S2 | Cota de malla | Espeleólogo: proyectiles −5/10/18/30 %, velocidad +4/8/12/16 % | sin ayuda vs explosiones |
| S3 | Hierro | Constructor/infantería: empuje −5/10/18/30 %, explosiones −4/8/15/25 %; ≥2 piezas: alcance de bloques +0.5 | no aporta Coloso |
| S4 | Oro | Arcano: magia −4/8/15/25 %, +1 Suerte, piglins | — |
| S5 | Diamante | Coloso: absorbe 50 % del excedente sobre 10 de daño a 4 piezas | ataque −15 %, brecha de enjambre, agotamiento, rep. 25 % |
| S6 | Netherita | Coloso como diamante; fuego/wither −25 % por pieza (inmunidad completa), repulsión −25 % con linaje completo | ataque −20 %, brecha, daño +10 % con luz ambiental <8 (proporcional a piezas), agotamiento solo de combate, rep. 50 % |
| S7 | Tortuga | Escafandra: respiración + minar bajo el agua | — |

**Linaje netherita (L)** — todo lo forjado sobre `minecraft:netherite_*` hereda S6:
`L1` ignitium · `L2` cursium · `L3` monstrous_helm · `L4` netherite_mage. Fuera del linaje: `bone_reptile`, `sturdy_boots` (sus atributos físicos de Cataclysm sí se normalizan).

**Variantes 1.23.0**: Monstrous (casco) duplica la amortiguación combinada, hasta 100 % del excedente, y añade movimiento −10 % y ataque −30 % por casco (se compone con las demás piezas pesadas). Ignitium aporta la mitad de amortiguación y prende al atacante cuerpo a cuerpo durante 3 s, con recarga de 40 ticks por jugador. Cursium no aporta Coloso, brecha ni coste de ataque.

**Brecha**: 2 impactos de combate aceptados dentro de 30 ticks reducen la armadura efectiva a la mitad en el segundo impacto. Ventana móvil; las fuentes ambientales y la inanición no cuentan. Cursium conserva la exención por pieza; mezclarlo con una pieza pesada vuelve a permitir brecha.

**Feedback de hambre (EquipmentBalance 1.23.2)**: a ≤6 puntos de comida se muestran los sprites vanilla de Hambre y un temblor de −1 a +1 píxel, cada 4 ticks; a ≤2, cada 2 ticks. Gruñido local de Sniffer cada 160 ticks con 1–6 puntos, cada 80 ticks con 1–2 (volumen 0.20, tono 0.55). Comer por encima del umbral reinicia el temporizador; creativo/espectador/muerto quedan excluidos. Solo cambia el feedback, sin aplicar efectos ni alterar saturación. STARVE a cero conserva el latido y la supresión de animación de daño de 1.23.0. Se sustituye el aviso anterior de cruce 8→7.

**Roles (R)**: `R1` mago (túnicas `irons_spellbooks`, −5 % daño cuerpo a cuerpo por pieza, máx −20 %) · `R2` anti-mago (oro, S4).

**Herramientas/armas (T)**: rediseño unificando extracción a 6.0.
*   **Madera:** Daño x2 configurable a artrópodos; reparación 100% por tablón. Hojas no gastan durabilidad. +25% vel en madera/cultivos y sueltan polvo de hueso.
*   **Piedra:** Empuje I y lentitud al golpear; cancela preparación de conjuros, bebida y mechas. +20% en menas/piedra; roca común de cantera sin desgaste. Espada sin penalización de ataque. Reparación 100% por material de piedra vanilla.
*   **Hierro:** Barrido III y alcance +0.5 (armas). Minado 3x3, agachado 1x1 y mitad del desgaste medio (DiggerItem). Hacha rompe escudo durante 5 s: +15% daño si esprinta, cuesta 1 agotamiento y 1 durabilidad extra por activación. 100% rep por lingote.
*   **Oro:** Bono directo a no-muertos equivalente al nivel configurado (sin depender de NBT), única tregua de piglins, +1 Suerte. Auto-fundición en DiggerItem. 100% rep por lingote. Daño base de hierro, durabilidad 160; azada de daño 1.
*   **Diamante:** 15% de crítico, alcance +1.0; daño −15% contra objetivos con armadura ≥8. Toque de seda oculto en herramientas. 25% rep por diamante.
*   **Netherita:** +15% daño vs armadura; sin lentitud ni tregua de piglins. Fortuna III oculta. 50% rep por lingote; equipo de material netherita admite fragmentos al 15%. Ignitium/Cursium conservan sus minerales propios, al 50%.

**Matriz familia ↔ counter (1.19.0):**
| Familia | Mecánica | Counter |
|---|---|---|
| Arañas | Esquiva 25 % (mitad de daño) | **Madera** (precisión + ×2) |
| No-muertos | Horda: +25 % empuje y 1.5 de agotamiento con 3+ zombis | **Hierro** (área) · **Oro** (Castigo III) |
| Esqueletos/ saqueadores | Lentitud I 1 s a más de 8 bloques | **Cota de malla ≥2 piezas** |
| Enderman/Shulker | Teletransporte | **Diamante** (anclaje 3 s) |
| Creeper/Bruja/Evocador | Mecha, poción o conjuro | **Piedra** (interrupción) |

## 4. Invariantes (si falla una, es bug)

1. **C1** Ningún tooltip nombra encantamientos.
2. **C2** Todo set del linaje L hereda fuego/wither, repulsión, debilidad con luz ambiental <8 y reparación 50 % desde 1.24.2. Los efectos defensivos escalan por pieza; la inmunidad requiere el linaje completo.
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
- El estado esperado vive en `estado.json` (versiones, conteos, 131 claves de config, IDs).

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
| 2026-11-13 | corrección 1.23.2 | 15/16 antes del commit; 781 comprobaciones JVM, 90 claves, 27 tablas de loot | eliminado Args$1 del HUD; git.limpio temporal hasta commit; Pages SKIP por DNS |
| 2026-11-13 | tooltips 1.23.3 | 15/16 antes del commit; 781 comprobaciones JVM previas y orden de encabezados verificado en bytecode | corregidas estadísticas antes del encabezado y piezas externas sin título; git.limpio temporal; inspección visual en cliente pendiente |
| 2026-11-13 | publicación 1.24.0 | 15/16 antes del commit; 1268 comprobaciones JVM, 90 claves y 27 tablas sin cambios | solo git.limpio temporal; Pages SKIP por DNS; resumen/Shift y unidades familiares; publicación autorizada en ambos repositorios |
| 2026-11-13 | corrección local 1.24.1 | 15/16 antes del commit; 1294 comprobaciones JVM, 90 claves y 27 tablas sin cambios | solo git.limpio temporal; Pages SKIP por DNS; Shift calcula el equipo vestido en lugar del máximo hipotético |
| 2026-11-13 | armonización 1.24.2 | 15/16 antes del commit; 1506 comprobaciones JVM, 104 claves y 27 tablas sin cambios | solo git.limpio temporal; Pages SKIP por DNS; corregidas rutas Forge y seis arquetipos; verificación visual en juego pendiente |
| 2026-11-13 | compatibilidad externa 1.24.3 | 1606 comprobaciones JVM, incluidas 100 con Forge/Cataclysm/Curios reales; 108 claves, 27 tablas | valores vanilla conservados; retirados Alshanex, su parche y FamiliarsLib; publicación del pack autorizada |
| 2026-11-13 | botín y contención mágica 1.24.5 | 1699 comprobaciones JVM (182 Forge/Cataclysm/Curios) y 141 de botín; 117 claves, 111 entradas en `loot.json` | AdventureLoot 1.3.0 (`R0–R4`/`F2–F4`, caldero 3:1, `0%` legendario en cofres) y EquipmentBalance 1.24.5 (11 armas Iron's, contención física, anillos −25%/−5%, 11 jefes); sin commit ni push |
| 2026-11-13 | sanitización de cofres y pepitas 1.24.6 | 1780 comprobaciones JVM (263 Forge/Cataclysm/Curios/Nuggets) y 457 de botín; 118 claves, 228 entradas en `loot.json` | Cero equipo vanilla en cofres (`elytra` preservada), ≤1 encantamiento vanilla nivel I por cofre, minerales/lingotes en pepitas (excepto carbón) con `Nuggets For All` (16 recetas MC 1.20.1), `LootTableMixin` + `AdventureLoot 1.4.0`; sin commit ni push |

**Tooltips 1.23.3**: en armaduras, el encabezado Ampere y el rol se añaden antes de las reglas numéricas. Las piezas físicas externas sin rol conocido reciben un encabezado genérico con el nombre traducido del ítem. Todas las líneas de detalle usan la misma sangría de viñeta; los detalles largos de Monstrous y linaje Nether se separan en líneas temáticas. No se modifican valores ni atributos nativos.

**Tooltips 1.24.0**: sustituye el bloque siempre expandido por resumen y detalles con Shift. Las botas de netherita tienen cinco líneas de resumen, con sus costes visibles. Los números proceden de config o constantes compartidas con la lógica; segundos, corazones y comida sustituyen ticks y fórmulas. Los atributos se reconocen por claves, conservando estilos y atributos ajenos; alcance traducido para es_mx/es_es. Suite: 1268 comprobaciones JVM, 90 claves. La escala de caída del cuero se documenta como 5/12/20/35 %, coincidiendo con la lógica ya existente; no cambia el balance.

**Corrección 1.24.1**: Shift usa solo las piezas vestidas y la armadura real del jugador. Cuero 3/4 muestra caída −20 % y 4/4 −35 %. Coloso, fuego/marchitamiento, firmeza, penalización de ataque, coste de comida y daño por oscuridad usan el conjunto mixto actual y la luz presente. Pasar el cursor por una pieza no simula equiparla; sin jugador no se inventan valores. 1294 comprobaciones JVM, incluidas 513 de tooltips; sin cambios de balance ni claves nuevas.

**Corrección de arranque 1.23.2**: los adaptadores de comida usan `@Redirect` con tipos nativos. No introducir `@ModifyArgs` ni `Args` en este HUD: en el cliente Forge/ModLauncher provocó `NoClassDefFoundError: org.spongepowered.asm.synthetic.args.Args$1` durante la carga. La suite comprueba esta regresión y ejecuta el adaptador real con dobles del renderer, sin Mixin en el classpath de prueba.

**Armonización 1.24.2**: conserva tarjetas y estado vestido, HUD sin Args y armaduras 16/10/12. Corrige reparación por familia/sentinela, oro directo sin duplicar NBT, desgaste por tag de hojas y cantera exacta, agachado 1x1, cancelación de warmup y señal de conjuro, costes cinéticos solo por entidad/proyectil no ambiental, hacha de hierro rompeguardias, alcance de obra, oro exclusivo para piglins, penalización ofensiva de diamante y mantenimiento netherita. Compatibilidad: solo notas de mecánicas propias; no borra texto de terceros. Contenedores: equipo, caña, tijeras, bundles, capacidades de inventario y bloques de almacenamiento. Configuración de pack/servidor/instancia: 104 claves. Suite: 1506 comprobaciones JVM; prueba visual en juego pendiente.

## 7. Memoria profunda (léela solo si vas a diseñar, no en `/sync`)

`docs/BALANCE.md`: números de referencia, backlog con criterios de aceptación, trampas conocidas, procedimiento de publicación y razón de cada regla.
`docs/LOOT.md` + `loot.json`: qué loot tables toca el pack (y cuáles no), con hashes verificados en cada `/sync`.
`docs/HAMBRE_VANILLA.md`: fuentes vanilla de agotamiento (correr 0.1/m, salto 0.05, ataque 0.1, minería 0.005, regen 6.0) y su conversión a saturación/hambre.
`docs/MOBS_HOSTILES_VANILLA.md` + `datos/mobs_hostiles_vanilla.json`: atributos de los 37 hostiles vanilla (bytecode 1.20.1) y qué cambia MobBalance. Reejecutable con `herramientas/extraer_atributos_vanilla.py`.
`docs/PROGRESION_EQUIPAMIENTO.md`: auditoría horizontal vs vertical del equipo, hallazgos H1-H8 y márgenes de mejora priorizados.

**Retirada local 2026-11-13 (pack 1.24.3):** retirados Alshanex Familiars 4.1.0 y TheOptimizer-FamiliarsTagFix 1.0.0 (dependencia obligatoria de Alshanex) del pack, servidor e instancia activa. FamiliarsLib se conserva; sin consumidores obligatorios restantes y con dos tags nativos que referencian objetos de Alshanex ausentes. EquipmentBalance sigue en 1.24.2. Auditoría de equipables en `reporte.md`, sin ajustes de balance ni publicación.

**Compatibilidad externa 1.24.3 (2026-11-13):** normalización de atributos en prioridad LOWEST; Ignitium 16/0, Cursium 12/0 y repulsión de linaje 25%. Excepciones físicas externas por decisión explícita: Bone Reptile casco 3/peto 6; Bloom Stone peto 6. Skull y efecto Monstrous sin dureza añadida. Emerald Stoneplate da suerte configurable en anillo con coste visible de ranura; Fluix DiggerItem extrae a 6.0. Grave Key queda excluida de combate pese a heredar SwordItem. Rocky conserva únicamente mecánicas nativas; retirados daño y niveles virtuales adicionales. Alshanex, FamiliarsTagFix y FamiliarsLib retirados; 108 claves. El reporte original es una fotografía anterior a esta corrección, no una afirmación del estado posterior. Otras familias físicas y poderes nativos de H3/H6 siguen siendo backlog; no se consideran rediseñados por esta compatibilidad acotada.

**Migración YUNG’s 1.24.4:** AdventureLoot 1.2.0, 29 tablas propias por niveles y 36 entradas en loot.json. EquipmentBalance 1.24.4, MobBalance 1.5.1 y WildlifeRepopulation 1.6.1 sin referencias activas a los mods retirados. Se conservan los números de balance vanilla y el reparto de fauna 55/45. Los faltantes no integrados y las delegaciones vanilla se detallan en docs/LOOT.md.

**Actualización botín y contención mágica 1.24.5:** AdventureLoot 1.3.0 reemplaza la inyección mágica por perfiles de riesgo `R0–R4` y cámaras finales `F2–F4` (`105` archivos en datapack, `111` entradas registradas en `loot.json`), receta 3:1 en caldero (`750 mB → 250 mB`) con `#theoptimizer:boss_legendary_catalysts` para tinta legendaria, `0%` tinta/pergaminos legendarios en cofres (con failsafe en `RandomizeSpellFunctionMixin`) y expulsión de botín mágico en aldeas (`R0`). En `EquipmentBalance 1.24.5` se normalizan 11 armas cuerpo a cuerpo de `irons_spellbooks` en `LOWEST` (purgando armadura de los dos flamberges) con reparación del `25%` a `0 XP`, se aplica contención de conjuros en armadura física pesada (`1–2` piezas doblan maná; `3+` bloquean), se sustituye la inmunidad total de los tres anillos protectores por `-25%` de daño elemental y `-5%` de velocidad de ataque, y se unifica la recompensa cerrada de tintas en `11` jefes (sin Botín ni doble premio en bóvedas). `117` claves sincronizadas; `1699` comprobaciones JVM + `141` comprobaciones de botín.

**Actualización de cofres sin equipo vanilla y pepitas 1.24.6 (2026-11-13):** Se añade `Nuggets For All` (`nuggets_for_all-1.0.0-forge-1.20.1.jar`, proyecto Modrinth `wMBsm3EI`) en repo, servidor e instancia; `AdventureLoot 1.4.0` (`222` archivos en el datapack, `228` entradas en `loot.json`) genera las `16` recetas MC `1.20.1` en `data/nuggets_for_all/recipes/*.json` (normalizando `lapisnuggetr` a `1 ↔ 9`), convierte todas las recompensas minerales de sus subtablas a pepitas (conservando `coal`/`charcoal`), limita `scroll_pouch.json` y `filler_storage_loot.json` a `quality.max = 0.65`, y sanitiza `116+` tablas base `/chests/` de vanilla/mods (incluyendo respaldo `diamondnugget` `2–5` en `cmd_yung`) para garantizar **0 equipo vanilla** (salvo `elytra` en `lootr:chests/elytra`), **0 lingotes/bloques/minerales completos** y **≤1 encantamiento vanilla nivel I** permitido por cofre. `EquipmentBalance 1.24.6` (`118` claves con `sanitize_chest_loot = true`) incorpora `LootTableMixin` sobre `LootTable.m_230922_` + `EquipmentPolicy.sanitizeChestLoot` como salvaguarda en tiempo de ejecución. `1780` comprobaciones JVM (`263` Forge/Cataclysm/Curios/Nuggets reales, `70` descriptores Mixin) + `457` comprobaciones de botín.

**Revisión local determinista 2026-11-14 (sin publicar):** AdventureLoot 1.5.0 cubre 194 tablas (147 con premios y 47 auxiliares inactivos); contrato por ID en `docs/LOOT_DETERMINISTA_MATRIZ.md`. Cada premio es fijo en identidad, cantidad y NBT; sin `randomize_spell`, selecciones ponderadas, rangos, bonus de suerte ni GLMs adicionales de cofres. No modificar tablas compartidas de jefes para arreglar cofres. EquipmentBalance 1.24.7 fija a 3 la conversión de respaldo de bloques a pepitas. 131 claves, sin claves nuevas de esta revisión; 434 archivos en AdventureLoot y 440 hashes totales. 30.839 comprobaciones de botín (29.006 Forge real) y 2.062 JVM de equipo. Auditoría y límites: `docs/LOOT_DETERMINISTA_AUDITORIA.md`. El registro histórico anterior permanece intacto.
