# Segunda iteración del botín — informe local

2026-11-14. EquipmentBalance **1.24.8**, AdventureLoot **1.6.0**, pack **1.24.8**. Implementado y verificado automáticamente; integración completa de transportes y cliente pendiente. Sin commit, push ni publicación.

## A. Fragmentos de generadores

Objeto real `theoptimizer_equipment:spawner_fragment`. La minería normal de un `minecraft:spawner` por un jugador real en supervivencia entrega exactamente uno después de la retirada efectiva. El interceptor usa el resultado de `ServerPlayerGameMode.removeBlock`, no el resultado general de `m_9280_` ni el evento previo cancelable. También exige que el bloque haya quedado en aire. Estado y resultado son locales a cada llamada: la minería de hierro reentrante conserva sus recompensas individuales.

No entrega objeto generador, no concede XP y no depende de Fortuna, Botín ni herramienta. El jugador sigue pagando el desgaste normal de su herramienta. Creativo, jugadores simulados, cancelación, transporte, máquinas y explosiones quedan fuera de la ruta premiada. Se admite un generador trasladado cuando se destruye después mediante minería legítima. Sin registro de origen, historial o persistencia por coordenadas; los generadores de mundos anteriores no necesitan migración.

La destrucción es el consumo irreversible del recurso. No se ha demostrado una duplicación reproducible en la ruta probada, pero no se afirma inmunidad universal a duplicaciones de mods: falta integración real de sus mecanismos de transporte.

## B. Catalizador arcano

Objeto real `theoptimizer_equipment:arcane_catalyst`. Receta sin forma: **4 fragmentos individuales → 1 catalizador arcano**. No son cuatro unidades implícitas en un ingrediente: hay cuatro entradas consumibles.

Una sola receta del caldero: **750 mB de tinta épica + 1 catalizador → 250 mB de tinta legendaria**. El tag histórico `theoptimizer:boss_legendary_catalysts` acepta `boss_catalyst` y `arcane_catalyst`. Se conserva la vía de los once jefes; no se modifican sus recompensas ni se añade tinta legendaria a cofres.

Se mantiene el coste inicial de cuatro: consume cuatro generadores y conserva el coste completo de tinta épica. No equivale a cuatro dungeons ni demuestra equivalencia con matar un jefe. La concentración de generadores y el saqueo evitando combate son riesgos plausibles; matar criaturas infinitamente no produce fragmentos. No se bloquea el transporte ni la construcción.

Ambos objetos incluyen modelo, textura propia, traducciones inglés/es_es/es_mx y tooltips cuyos valores salen de constantes. La configuración de equipo conserva sus 131 claves.

## C. Libros

De **61 a 18 tablas** con un libro permitido de nivel I; retirado de 43. Lista explícita en `segunda_iteracion.py`, sin sorteo ni sustitución de NBT. Cofre común de esqueletos: cero libros. Central: uno por cofre. Algunas plantillas centrales de YUNG contienen dos referencias `middle`, por lo que no se promete un libro por dungeon. El resto del suministro de esos cofres permanece.

## D. Aleación de andesita

Mismas **79 ubicaciones**. Antes: 19 tablas con 1, 41 con 2 y 19 con 3. Ahora: **59 con 4, 11 con 6 y 9 con 8**. Base moderado/alto/máximo: 4/6/8; varias tablas modulares o repetibles quedan topadas a cuatro, incluido tesoro repetible del End. Esqueletos: común cuatro, central seis.

Una apertura de cada ID sumaría 158 antes y 374 ahora. Esta suma no es un rendimiento por estructura. Cada plantilla central confirmada con dos cofres aporta 12 aleaciones y dos libros; una dungeon completa depende de su ensamblaje. No se midió la distribución real de todas las variantes ni se afirma que el 54% de tablas sea el 54% de cofres encontrados. El ahorro de fabricación de Create es real; se limita el premio por cofre para reducir concentración y se preservan las ubicaciones.

## E. Fases y revisiones secuenciales

1. Terra 6.1: auditoría de matriz, receta, eventos y plantillas. Confirmó multiplicidad de cofres; transporte real no resuelto.
2. Astra: diseñó cuatro fragmentos, tag compartido, lista de 18 libros y presupuestos conservadores de aleación.
3. Sol 6: revisión adversarial. Confirmó que el retorno general de rotura no garantiza retirada; conservó la vía de jefes.
4. Coordinador Sol 6.1: única persona agente que modificó código, recursos, pruebas y documentación.
5. Luna 6: inspección estructural; confirmó objetos, recetas, 194 tablas y cantidades. Su objeción sobre tablas ausentes en recursos_base no era un defecto: el generador aplica el contrato al construir el ZIP; se verificó el resultado efectivo en Forge.
6. Luna 6: ejecutó pruebas y reportó una aserción incorrecta en la primera prueba del caldero. El coordinador la sustituyó por ejecución del caldero real y repitió las suites.
7. Sol 6.1: revisión independiente del código nuevo; sin hallazgos de gravedad demostrados, con límites de integración explícitos.
8. Terra 6.1: propuso documentación y cierre; integrada y corregida por el coordinador.

Los modelos 5.6 solicitados no estaban disponibles; se usaron los equivalentes disponibles. Ningún subagente editó fuentes y no trabajaron simultáneamente.

## F. Pruebas y límites

- Compilación Java 17, advertencias como errores: aprobada.
- Botín: **31.075 comprobaciones** (2.081 estáticas/regresión y 28.994 Forge real), 194 tablas, 32 semillas, suerte variable, NBT, sanitización e invariantes. Cero variación de composición. 208 recursos no-cofre del generador permanecen idénticos al desactivar el contrato; el cambio de tag es intencional y se valida por separado.
- Equipo: **2.062 JVM**, incluidas 409 de compatibilidad externa real y 97 firmas/descriptores de la suite existente. El nuevo interceptor se verifica además al transformar y ejecutar GameMode dentro de Forge.
- Generadores: uno en supervivencia; segunda rotura no duplica; sin objeto generador; Fortuna/Botín/Seda no alteran cantidad; cero orbes; cancelación/creativo/FakePlayer cero; dos roturas reentrantes producen dos; retirada externa cero y recolocación seguida de minería produce uno. La retirada/recolocación es una simulación de transporte, no una prueba de AE2/Create/Gadgets.
- Caldero real de Iron's: 749 mB no consumen; 750 consumen un catalizador y producen 250 legendaria con cualquiera de los dos; fragmento directo rechazado; intento con entrada vacía no duplica.
- Receta de fabricación cargada: cuatro ingredientes y una salida. Interacción completa con la mesa de un cliente pendiente.

La primera aserción suponía erróneamente que `Brew.matches` rechaza cantidades insuficientes; ese método compara tipos. Se corrigió el test para ejecutar `AlchemistCauldronTile.tryMeltInput`, que sí verifica el volumen. No se alteró Iron's para acomodar el test.

Pendientes: transportes reales AE2/Create/Gadgets, dos clientes disputando el mismo bloque, reinicio del servidor, descarga/recarga del chunk, otras dimensiones, destrucción por explosión como interacción real, matar criaturas como escenario específico, generación completa de variantes y presentación visual de los objetos/tooltips. No se abrieron mundos existentes para probar. Los cofres ya materializados no se regeneran.

Evidencia: `TheOptimizerMods/datos/reparaciones/botin_determinista/determinism-result.json`, `determinism-runtime.log` (incluye `SPAWNER_ITERATION_OK`), y registro `validacion_1.24.8.json`. Los logs de arranque incluyen advertencias/recetas nativas preexistentes; las suites llegan a sus aserciones y terminan con éxito.

## G. Archivos de esta iteración

Rutas relativas a `C:/Users/Metabodiru/Desktop/TheOptimizerMods`; contraste con snapshot previo, sin atribuir los cambios preexistentes de Cataclysm a esta misión:

- `balance_equipamiento/instalar.py`
- `balance_equipamiento/probar.py`
- `balance_equipamiento/recursos/assets/theoptimizer_equipment/lang/en_us.json`
- `balance_equipamiento/recursos/assets/theoptimizer_equipment/lang/es_es.json`
- `balance_equipamiento/recursos/assets/theoptimizer_equipment/lang/es_mx.json`
- `balance_equipamiento/recursos/assets/theoptimizer_equipment/models/item/arcane_catalyst.json`
- `balance_equipamiento/recursos/assets/theoptimizer_equipment/models/item/spawner_fragment.json`
- `balance_equipamiento/recursos/assets/theoptimizer_equipment/textures/item/arcane_catalyst.png`
- `balance_equipamiento/recursos/assets/theoptimizer_equipment/textures/item/spawner_fragment.png`
- `balance_equipamiento/recursos/data/theoptimizer_equipment/recipes/arcane_catalyst.json`
- `balance_equipamiento/theoptimizer/equipment/EquipmentMod.java`
- `balance_equipamiento/theoptimizer/equipment/mixin/SpawnerRemovalMixin.java`
- `balance_equipamiento/theoptimizer/equipment/SpawnerRewards.java`
- `botin_magia_aventura/disenar_determinismo.py`
- `botin_magia_aventura/instalar.py`
- `botin_magia_aventura/matriz_determinista.json`
- `botin_magia_aventura/probar.py`
- `botin_magia_aventura/recursos_base/data/theoptimizer/tags/items/boss_legendary_catalysts.json`
- `botin_magia_aventura/segunda_iteracion.py`
- `botin_magia_aventura/segunda_iteracion_base.json`
- `botin_magia_aventura/verificar_determinismo.py`
- `botin_magia_aventura/VerifyDeterministicLoot.java`
- `botin_magia_aventura/VerifySpawnerIteration.java`

Propósitos: registro y lógica en EquipmentMod/SpawnerRewards/SpawnerRemovalMixin; recursos de ambos objetos y receta en recursos; versiones/empaquetado en instalar/probar; política y contrato en segunda_iteracion/disenar/matriz; fixture y pruebas de regresión/Forge en archivos de verificación. El tag añade el catalizador arcano sin eliminar el de jefe.

En AmpereRepo: AGENTS.md, docs/BALANCE.md, docs/LOOT.md, docs/LOOT_DETERMINISTA_MATRIZ.md, referencias históricas de auditoría/informe, este informe, estado.json, version.txt, changelog.md, pack.toml/index.toml, loot.json, JAR de equipo renovado y ZIP AdventureLoot. El instalador actualiza copias locales de servidor/Prism y rota el registro generado de validación. No se modificó el trabajo previo del actualizador.

## H. Estado final

Implementado, compilado y verificado automáticamente; parcialmente verificado en integración de juego. Cambios locales preparados, sin commit, push ni publicación. Consulta el resultado del verificador al cierre; git.limpio y pages.version pueden diferir porque no se publicó esta versión.

## Tablas con cambios (anterior → actual)

| Tabla | Libro | Aleación |
|---|---:|---:|
| `betterdeserttemples:chests/lab` | 1 → 0 | 2 → 4 |
| `betterdeserttemples:chests/library` | 0 → 0 | 2 → 4 |
| `betterdeserttemples:chests/pharaoh_hidden` | 1 → 0 | 2 → 6 |
| `betterdeserttemples:chests/statue` | 1 → 0 | 2 → 4 |
| `betterdeserttemples:chests/storage` | 1 → 0 | 2 → 4 |
| `betterdeserttemples:chests/tomb` | 1 → 0 | 2 → 4 |
| `betterdeserttemples:chests/tomb_pharaoh` | 1 → 1 | 2 → 6 |
| `betterdungeons:skeleton_dungeon/chests/common` | 1 → 0 | 1 → 4 |
| `betterdungeons:skeleton_dungeon/chests/middle` | 1 → 1 | 1 → 6 |
| `betterdungeons:small_dungeon/chests/loot_piles` | 1 → 0 | 1 → 4 |
| `betterdungeons:small_nether_dungeon/chests/common` | 1 → 0 | 1 → 4 |
| `betterdungeons:spider_dungeon/chests/egg_room` | 1 → 0 | 1 → 4 |
| `betterdungeons:zombie_dungeon/chests/common` | 1 → 0 | 1 → 4 |
| `betterdungeons:zombie_dungeon/chests/special` | 1 → 1 | 1 → 4 |
| `betterdungeons:zombie_dungeon/chests/tombstone` | 1 → 0 | 1 → 4 |
| `betterfortresses:chests/beacon` | 1 → 0 | 2 → 4 |
| `betterfortresses:chests/extra` | 1 → 0 | 2 → 4 |
| `betterfortresses:chests/hall` | 1 → 0 | 2 → 4 |
| `betterfortresses:chests/keep` | 1 → 1 | 3 → 8 |
| `betterfortresses:chests/obsidian` | 1 → 0 | 2 → 4 |
| `betterfortresses:chests/puzzle` | 1 → 1 | 3 → 8 |
| `betterfortresses:chests/quarters` | 1 → 0 | 2 → 4 |
| `betterfortresses:chests/storage` | 1 → 0 | 2 → 4 |
| `betterfortresses:chests/worship` | 1 → 0 | 2 → 4 |
| `betteroceanmonuments:chests/upper_side_chamber` | 1 → 1 | 3 → 8 |
| `betterstrongholds:chests/armoury` | 1 → 0 | 2 → 4 |
| `betterstrongholds:chests/common` | 1 → 0 | 2 → 4 |
| `betterstrongholds:chests/crypt` | 1 → 0 | 2 → 4 |
| `betterstrongholds:chests/grand_library` | 0 → 0 | 2 → 4 |
| `betterstrongholds:chests/library_md` | 0 → 0 | 2 → 4 |
| `betterstrongholds:chests/prison_lg` | 1 → 0 | 2 → 4 |
| `betterstrongholds:chests/trap` | 1 → 0 | 2 → 4 |
| `betterstrongholds:chests/treasure` | 1 → 1 | 2 → 6 |
| `betterwitchhuts:chests/hut_0` | 0 → 0 | 1 → 4 |
| `cataclysm:chests/abandoned` | 1 → 0 | 1 → 4 |
| `cataclysm:chests/abandoned_treasure` | 1 → 1 | 2 → 6 |
| `cataclysm:chests/acropolis_treasure` | 0 → 0 | 3 → 8 |
| `cataclysm:chests/amethyst_nest_chest` | 1 → 0 | 1 → 4 |
| `cataclysm:chests/desert_treasure` | 0 → 0 | 3 → 8 |
| `cataclysm:chests/frosted_prison_treasure` | 0 → 0 | 3 → 8 |
| `irons_spellbooks:chests/battleground/burial_loot` | 1 → 0 | 3 → 4 |
| `irons_spellbooks:chests/battleground/piglin_camp` | 1 → 0 | 3 → 4 |
| `irons_spellbooks:chests/catacombs/armory_loot` | 1 → 0 | 3 → 4 |
| `irons_spellbooks:chests/catacombs/coffin_loot` | 1 → 0 | 3 → 4 |
| `irons_spellbooks:chests/catacombs/crypt_loot` | 1 → 0 | 3 → 4 |
| `irons_spellbooks:chests/catacombs/dead_king_vault` | 1 → 1 | 3 → 8 |
| `irons_spellbooks:chests/catacombs/hidden_trough_treasure` | 1 → 0 | 3 → 4 |
| `irons_spellbooks:chests/catacombs/wall_loot` | 1 → 0 | 3 → 4 |
| `irons_spellbooks:chests/citadel/citadel_bookshelf` | 0 → 0 | 2 → 4 |
| `irons_spellbooks:chests/citadel/citadel_vault` | 1 → 1 | 3 → 8 |
| `irons_spellbooks:chests/citadel/rampart_chest` | 1 → 0 | 3 → 4 |
| `irons_spellbooks:chests/citadel/spawner_reward` | 1 → 1 | 2 → 6 |
| `irons_spellbooks:chests/evoker_fort` | 1 → 1 | 2 → 6 |
| `irons_spellbooks:chests/generic_magic_treasure` | 1 → 0 | 2 → 4 |
| `irons_spellbooks:chests/ice_spider_den/dungeon` | 1 → 0 | 2 → 6 |
| `irons_spellbooks:chests/ice_spider_den/spawner_reward` | 1 → 1 | 2 → 6 |
| `irons_spellbooks:chests/ice_spider_den/tower` | 0 → 0 | 1 → 4 |
| `irons_spellbooks:chests/impaled_icebreaker/captain_quarters` | 0 → 0 | 1 → 4 |
| `irons_spellbooks:chests/magic_bookshelf_loot` | 0 → 0 | 2 → 4 |
| `irons_spellbooks:chests/mountain_tower/mountain_tower` | 1 → 1 | 2 → 6 |
| `irons_spellbooks:chests/pyromancer_tower/burnt_chest` | 1 → 1 | 2 → 6 |
| `irons_spellbooks:chests/pyromancer_tower/pyromancer_supplies` | 1 → 0 | 2 → 4 |
| `minecraft:chests/abandoned_mineshaft` | 1 → 0 | 1 → 4 |
| `minecraft:chests/ancient_city` | 1 → 0 | 3 → 4 |
| `minecraft:chests/bastion_bridge` | 0 → 0 | 2 → 4 |
| `minecraft:chests/bastion_hoglin_stable` | 0 → 0 | 2 → 4 |
| `minecraft:chests/bastion_other` | 0 → 0 | 2 → 4 |
| `minecraft:chests/bastion_treasure` | 1 → 1 | 3 → 8 |
| `minecraft:chests/desert_pyramid` | 1 → 0 | 1 → 4 |
| `minecraft:chests/end_city_treasure` | 1 → 0 | 3 → 4 |
| `minecraft:chests/jungle_temple` | 1 → 1 | 1 → 4 |
| `minecraft:chests/nether_bridge` | 1 → 0 | 2 → 4 |
| `minecraft:chests/pillager_outpost` | 0 → 0 | 1 → 4 |
| `minecraft:chests/simple_dungeon` | 1 → 1 | 1 → 4 |
| `minecraft:chests/stronghold_corridor` | 1 → 0 | 2 → 4 |
| `minecraft:chests/stronghold_crossing` | 1 → 0 | 2 → 4 |
| `minecraft:chests/stronghold_library` | 0 → 0 | 2 → 4 |
| `minecraft:chests/underwater_ruin_big` | 0 → 0 | 1 → 4 |
| `minecraft:chests/woodland_mansion` | 0 → 0 | 2 → 4 |

## Verificación final

`verificar_estado.ps1 -SkipTests`: **15/16**, única deriva `git.limpio` por cambios locales autorizados. `tests.modulo` omitido en este comando porque la suite completa ya pasó por separado; `pages.version` no comprobable por DNS. Integridad 362/362, paridad del JAR, 131 claves y 440/440 hashes de loot correctos. `git diff --check` sin errores en ambos repositorios. Snapshot anterior archivado fuera de los repositorios en el directorio de artefactos de esta sesión (`output/auditoria_loot/iteracion2_antes.zip`).
