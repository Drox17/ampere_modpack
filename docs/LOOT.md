# Botín en 3 capas — AdventureLoot 1.7.0 / EquipmentBalance 1.25.0

Revisión 2026-11-14, desplegada localmente; sin commit, push ni publicación. Sustituye el formato plano 1.6.0 en los `113` cofres activos (`R1–R4`, `F2–F4`) preservando el **núcleo mágico y único 100 % determinista**, mientras introduce variedad temática en suministros y un rol real para la **Suerte (`Luck >= 1`)**.

## Arquitectura de 3 capas (194 tablas)

1. **Capa 0 — Core determinista (inmune a semilla y Suerte):** `1` tirada, `0` `bonus_rolls`, cantidades exactas y NBT explícito en tintas (`common`/`uncommon`/`rare`), `scroll`, `blank_rune`, `ancient_knowledge_fragment`, `dead_king_phylactery_shard`, `mithril_scrap`, `diamondnugget`, coleccionables de Iron's/Cataclysm, discos, moldes y libro encantado nivel I permitido (`18` tablas). Tablas `r0_excluded`, `disabled_helper`, `lootr:chests/elytra` y `minecraft:chests/jungle_temple_dispenser` mantienen exclusivamente Capa 0 fija.
2. **Capa 1 — Suministros y temática por bioma (`9` biomas):** `iron_nugget` (`R1: 3–6`, `R2: 6–10`, `R3: 8–12`, `R4: 10–15`) y `create:andesite_alloy` (`R2: 3–5`, `R3: 4–7`, `R4: 6–10`) en `uniform(min, max)`, más `1` pool temático por bioma (`mine`, `combat`, `desert`, `crypt`, `nether`, `ice`, `marine`, `library`, `end`) con consumibles de `Create`, `Kaleidoscope` e `Iron's`, `"quality"` para favorecer comida/ingredientes de gama alta con Suerte y `bonus_rolls` (`0.0` en `R1`, `0.5` en `R2/R3`, `0.75` en `R4/F4`). Prohibido `minecraft:empty`.
3. **Capa 2 — Botín Íntegro de Fortuna (`Luck >= 1` en `EquipmentPolicy.sanitizeChestLoot`):** con `Luck <= 0` persiste la conversión estricta a pepitas (`P5`). Con `Luck = 1` se habilitan lingotes/gemas reducidos en `R2–R3` y puente de `1–2` lingotes (`iron`/`gold`) o `1` esmeralda en `R4/F3/F4` (`0` diamantes/chatarra). Con `Luck >= 2` se desbloquea el tope completo en `R2–R4` (`2–3` lingotes / `1–2` esmeraldas), probabilidad de `1` diamante en `F3` y `1` diamante o `1` `netherite_scrap` garantizado en `F4`. Contenedores menores/bolsas (`scroll_pouch` con `bonus_rolls: 1.0`, barriles, urnas y librerías) añaden `+1..2` pepitas de oro o esmeralda por punto (cap `3`).

## Segunda iteración (fragmentos de spawner y proporciones conservadas)

[Informe completo y archivos](LOOT_SEGUNDA_ITERACION.md): fragmentos al destruir generadores, 4 fragmentos → catalizador arcano, alternativa al catalizador de jefe en la misma receta de tinta. Libros en 18 tablas (antes 61); aleación en 79 tablas con cantidades fijas de 4/6/8 y límites para familias repetibles. 31.075 pruebas de botín y 2.062 de equipo; transportes reales y cliente pendientes.

## Contrato y cobertura

- [Matriz por tabla y cantidad](LOOT_DETERMINISTA_MATRIZ.md): 194 tablas, 147 con premios y 47 auxiliares desactivados.
- [Auditoría, diseño y límites](LOOT_DETERMINISTA_AUDITORIA.md).
- Contrato fuente: `TheOptimizerMods/botin_magia_aventura/matriz_determinista.json`.
- Snapshot anterior: `TheOptimizerMods/botin_magia_aventura/audit_determinismo_antes.json` (no regenerar como si fuera el estado anterior tras instalar).
- 434 archivos de AdventureLoot (433 JSON); 440 hashes en `loot.json`, incluidos los siete de LootFixes.

Cada recompensa usa una pool con una entrada, una tirada, bonus_rolls=0, cantidad entera fija y como única función opcional `set_nbt` explícito. No quedan condiciones aleatorias, referencias anidadas ni funciones de generación aleatoria dentro del contrato. Los 13 accesorios antes anidados se distribuyen entre cofres hostiles específicos; no se borra la tabla compartida que también usa Iron's en muertes de entidades.

Los cofres de aldeas no dan magia; despensas y barriles quedan en R0/R1. Agua y botellas vacías salen. Minas dan raíles/carbón; mar prismarina/algas; bibliotecas papel/libros; desierto terracota y pepitas; criptas huesos/pólvora; Nether oro/verruga y polvo de blaze; End chorus/perla. La matriz enumera cada coleccionable, equipo modded permitido y pergamino fijo. El pergamino almacena hechizo y nivel 1 en NBT nativo de Iron's; no llama a randomize_spell. En cofres altos se elimina la épica anteriormente garantizada en cada apertura: tintas poco comunes y raras de tesoro sostienen el caldero 3:1.

## Invariantes

Cero equipo vanilla salvo élitros en `lootr:chests/elytra`. Cero lingotes/gemas/bloques minerales salvo carbón/carbón vegetal; recompensas en pepitas válidas. Máximo un libro vanilla nivel I permitido por cofre. Cero XP, tinta legendaria, catalizadores de jefe o pergaminos legendarios. La proporción del caldero no cambia; su tag acepta también el catalizador arcano. Se añade su receta de fabricación; se conservan Nuggets For All, Create/AE2 y drops de mobs/jefes. La minería legítima de generadores añade el fragmento tras la retirada efectiva. `LootTableMixin` sigue activo; `EquipmentPolicy.sanitizeChestLoot` usa 3 pepitas fijas para un bloque de respaldo.

## Compatibilidad

Las tablas base contienen el presupuesto completo. El registro Forge propio mantiene replace=false con entries vacío. Los modificadores de cofres nativos/de perfiles se desactivan individualmente con `forge:loot_table_id=theoptimizer:disabled`, incluidos Kaleidoscope Cookery y Nether. No se desactivan modificadores de pesca, mobs ni bloques. Se mantiene Lootr individual sin refresco; no se inspecciona ni se abre el mundo existente para probar. La matriz no acredita victoria por abrir una cámara final: siguen siendo posibles rutas de saqueo evitando enemigos.

Exclusiones comprobadas: `ae2:blocks/chests/meteorite` es drop de bloque; `magic_items/great_ink` y `reward_ink` están compartidas con entidades. Se preservan estas tres raíces y se eliminan sus referencias desde cofres. Arqueología y pesca fuera de alcance. Tablas auxiliares trial_chambers presentes en el JAR no prueban generación de estructuras 1.21 en 1.20.1.

## Pruebas reproducibles

Desde TheOptimizerMods: `python -B scripts/compile_quiet.py`, `python -B -m botin_magia_aventura.probar`, `python -B -m balance_equipamiento.probar`.

Resultado histórico de 1.5.0: 1.833 checks estructurales/regresión, 208 recursos no-cofre idénticos y 29.006 comprobaciones de ejecución Forge (194 tablas × 32 semillas, suerte -5/0/+5, NBT, gestor efectivo y segunda sanitización). Total 30.839; variación de contenido final cero. Equipo: 2.062 JVM con 409 verificaciones de compatibilidad externa y 97 firmas/descriptores Mixin.

El runner crea una copia temporal del servidor, mundo plano nuevo, puerto local efímero y mods reales. Nunca usa el mundo ampere. El log y la prueba JSON quedan en `TheOptimizerMods/datos/reparaciones/botin_determinista/`. La creación de chunks del mundo temporal no valida interacción de un cliente ni todas las variantes de estructuras. Comprobar manualmente un cofre nuevo por familia y Lootr multijugador; los cofres ya materializados no se regeneran.

## Auditoría estructural multi-contenedor, discos y libros I — AdventureLoot 1.8.0 / EquipmentBalance 1.25.1 (2026-11-14)

Ajuste derivado de la auditoría `.nbt` sobre todas las estructuras activas del pack (`198` tablas en `docs/LOOT_DETERMINISTA_MATRIZ.md`, `447` entradas registradas en `loot.json`):

- **Rebajas a `R1` (sin tinta fija ni Pool 2 de minerales enteros):** `betterdungeons:small_dungeon/chests/loot_piles`, `irons_spellbooks:chests/citadel/citadel_bookshelf` (~19 barriles por ciudadela; coleccionables movidos a `choice_pools` `20 %`), `betterdeserttemples:chests/storage` (conserva `3 × emeraldnugget`) y `cataclysm:chests/abandoned` (19 cofres; `sturdy_boots` al `15 %`).
- **Subida a `R2` (`r2_other`) e inclusión faltante:** `irons_spellbooks:chests/evoker_fort/guard_tower` recibe `1 × common_ink`; `minecraft:chests/village_desert_house` (`desert_occupied_village.nbt`) queda sellado en `r0_excluded`.
- **Perfiles multi-contenedor (`r2_multi`, `r3_multi`, `f3_multi`):** suministros base reducidos (`2` tiradas, `bonus_rolls: 0.25`), núcleo en `chance_rewards` (`25 %` en `r2_multi`, `15 %` en `r3_multi` para `betterfortresses:chests/keep`, `20 %` en `f3_multi` para `betterstrongholds:chests/treasure`) y cuota/chance acotada en Capa 2 (`EquipmentCombatRules.fortuneRollChance` `0.25`/`0.20`). `betterfortresses:chests/puzzle` se mantiene `F4` puro.
- **Discos musicales y libros encantados nivel I (`P5`):** las `6` tablas repetibles con discos unifican sus discos en `disc_pool` único (`20 %`, máx. `1` disco); las `18` tablas con libros reemplazan el libro fijo por `book_pool` equilibrado `1:1:1` (`unbreaking`, `looting`, `efficiency` nivel I) con probabilidad escalada (`10 %` `simple_dungeon`, `15 %` `evoker_fort`/`mountain_tower`/`burnt_chest`/`keep`/`abandoned_treasure`, `20 %` `strongholds/treasure`, `100 %` en las `11` cámaras `F2–F4`).
- **Verificación (`botin_magia_aventura.probar`):** `77.629` comprobaciones pasadas (`1.319` estáticas + `76.310` en Forge real sobre `198` tablas × `32` semillas y `Luck -5/0/1/2/5`).

## Economía de Explorador, Bartering y Tableros — AdventureLoot 1.9.0 / EquipmentBalance 1.25.2 (2026-11-14)

Extiende `TheOptimizer_AdventureLoot.zip` a `462` archivos (`468` entradas en `loot.json`) e integra la verificación en vivo en `VerifyTradingEconomy.java`:

- **`irons_spellbooks:magic_items/scroll_pouch`:** techo de calidad acotado de `0.65` a `0.38` (`<= UNCOMMON`).
- **`minecraft:gameplay/piglin_bartering`:** retirados `iron_boots`, `book` (`soul_speed`) y `ender_pearl`; `iron_nugget` reducido a `4–8 (weight 5)` y reequilibrado con `gold_nugget`, `netherward_tincture`, `glowstone_dust` y `magma_cream`.
- **`minecraft:gameplay/hero_of_the_village/{armorer,toolsmith,weaponsmith,cleric,fletcher}_gift`:** purgados equipo vanilla, `lapis_lazuli`, botellas de XP y perlas; sustituidos por `create:andesite_alloy`, pepitas de `nuggets_for_all`, `common_ink`, `blank_rune`, elixires, `builders_tea`, `spectral_arrow` y `cataclysm:void_scatter_arrow`.
- **`Bountiful` (`15` `bounty_pools/bountiful/*.json` con `"replace": true`):** retirados por completo armaduras, herramientas, arcos, `shield`, `trident`, `totem_of_undying`, `heart_of_the_sea`, `lapis_*`, `experience_bottle`, `ender_pearl` y `enchanted_book`; sustituidos por objetivos de caza y botín de mazmorras (`frozen_bone`, `blank_rune`, `andesite_alloy`) y recompensas legales (`diamondnugget`, `emeraldnugget`, `common_ink`/`uncommon_ink`, elixires de Iron's, tés/comidas de `Kaleidoscope` y `Create`).
- **Verificación (`botin_magia_aventura.probar`):** `80.072` comprobaciones pasadas (`1.344` estáticas + `78.728` en Forge real, incluyendo `2.113` comprobaciones en `VerifyTradingEconomy` sobre las `15` profesiones `L1–L5`, Errante, `Ribbit`, `4` magos, curación, restock, Suerte, bartering, regalos Hero, `scroll_pouch` y `bounty_pools/bountiful`).
