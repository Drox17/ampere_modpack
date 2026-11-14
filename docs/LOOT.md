# Botín y contención mágica — actualización 1.24.6 (AdventureLoot 1.4.0)

Registro: **228 entradas SHA-256** en [loot.json](../loot.json) (`221` JSON dentro de `moonlight-global-datapacks/TheOptimizer_AdventureLoot.zip` —`222` archivos en el zip con `pack.mcmeta`— y `7` correcciones previas en `ampere/datapacks/TheOptimizer_LootFixes.zip`). Desglose total: `168` `loot_table`, `23` `glm`, `21` `receta` (`16` de `nuggets_for_all`, `4` caldero 3:1 y `1` anillo), `7` `correccion`, `6` `override_entity`, `2` `override_block`, `1` `tag`.

Los modifiers usan `irons_spellbooks:append_loot` con registro `replace=false`. Se conservan los overrides vanilla de cobre (`1` crudo fijo por mena con Fortuna) y los drops cotidianos deterministas. El datapack se instala en el repo del pack, el servidor (`ampere/datapacks` y `moonlight-global-datapacks`) y la instancia activa de PrismLauncher.

## 1. Caldero 3:1 y catalizador exclusivo de jefe

Recetas sobrescritas en `data/irons_spellbooks/recipes/alchemist_cauldron/`:

| Receta | Fluido base (`750 mB` = 3 botellas) | Catalizador | Salida (`250 mB` = 1 botella) |
|---|---|---|---|
| `brew_uncommon_ink` | `irons_spellbooks:common_ink` | `minecraft:copper_ingot` | `irons_spellbooks:uncommon_ink` |
| `brew_rare_ink` | `irons_spellbooks:uncommon_ink` | `minecraft:iron_ingot` | `irons_spellbooks:rare_ink` |
| `brew_epic_ink` | `irons_spellbooks:rare_ink` | `minecraft:gold_ingot` | `irons_spellbooks:epic_ink` |
| `brew_legendary_ink` | `irons_spellbooks:epic_ink` | `#theoptimizer:boss_legendary_catalysts` | `irons_spellbooks:legendary_ink` |

El tag cerrado `#theoptimizer:boss_legendary_catalysts` exige un trofeo no farmeable exclusivo de jefe (`minecraft:dragon_egg`, `minecraft:nether_star`, `cataclysm:ignitium_ingot`, `cataclysm:abyssal_egg`, `cataclysm:cursium_ingot`, `cataclysm:witherite_block`, `cataclysm:void_core`, `cataclysm:sandstorm_in_a_bottle`, `irons_spellbooks:blood_staff`). Ningún cofre ni mob común puede otorgar tinta ni catalizadores legendarios.

## 2. Cofres sin equipamiento vanilla, sin lingotes, 0% legendarios y máximo 1 libro

Reglas estrictas sobre todos los cofres del pack (`AdventureLoot 1.4.0` estático + `LootTableMixin` / `EquipmentPolicy.sanitizeChestLoot` en `EquipmentBalance 1.24.6`):

- **Cero equipamiento vanilla en cofres:** se eliminan armas, herramientas, armaduras, escudos, arcos, ballestas, tridentes, cañas de pescar, tijeras, mecheros y armaduras de caballo de `minecraft:*`. Única excepción explícita preservada: `minecraft:elytra` en `lootr:chests/elytra`.
- **Máximo 1 encantamiento vanilla por cofre (y máximo 1 libro encantado nivel I):** ninguna tabla base ni función `enchant_randomly` / `enchant_with_levels` genera libros o encantamientos arbitrarios; solo los pools `theoptimizer:chests/book_*` pueden soltar como máximo `1` libro de `minecraft:unbreaking`, `minecraft:looting` o `minecraft:efficiency` a nivel I. En ejecución, `LootTableMixin` elimina encantamientos ilegales/duplicados (incluidos los aplicados sobre ítems no-libro).
- **Cero lingotes, bloques ni minerales enteros (pepitas salvo carbón):** todo lingote, bloque mineral, mena en bruto o gema completa en tablas base y subtablas `theoptimizer` pasa a pepitas:
  - Mod **`Nuggets For All`** (`nuggets_for_all-1.0.0-forge-1.20.1.jar`, añadido al repo/servidor/instancia) aporta `coppernugget`, `diamondnugget`, `emeraldnugget`, `lapisnugget`, `quartznugget`, `amethystnugget`, `netheritenugget` y `chickennugget`. `AdventureLoot 1.4.0` genera las `16` recetas bidireccionales `1 ↔ 9` en `data/nuggets_for_all/recipes/*.json` formato MC `1.20.1` (`result.item`, normalizando también `lapisnuggetr` a `1 → 9`).
  - Hierro y oro usan `minecraft:iron_nugget` y `minecraft:gold_nugget`; `ancient_metal_ingot` y `black_steel_ingot` usan `cataclysm:ancient_metal_nugget` y `cataclysm:black_steel_nugget`; `irons_spellbooks:arcane_ingot` y `pyrium_ingot` usan `arcane_essence` y `cinder_essence`.
  - `minecraft:coal` y `minecraft:charcoal` se conservan intactos.
  - Cualquier tabla no vacía cuyos ítems fueran únicamente equipo vanilla eliminado (como `betterstrongholds:chests/cmd_yung`) conserva un pool alternativo de `2–5` `nuggets_for_all:diamondnugget`.
- **`0%` `irons_spellbooks:legendary_ink` y `0%` pergaminos `LEGENDARY`:**
  - Los 8 modifiers nativos de `irons_spellbooks` quedan redirigidos a `theoptimizer:disabled`; `dead_king_vault`, `citadel_vault`, `crypt_loot`, `citadel_bookshelf`, `buried_treasure`, `shipwreck_treasure`, `zombie_dungeon`, `evoker_fort` y `impaled_icebreaker/captain_quarters` usan sus overrides limpios.
  - `data/irons_spellbooks/loot_tables/magic_items/scroll_pouch.json` y `data/irons_spellbooks/loot_tables/chests/filler_storage_loot.json` quedan limitados a `quality.max = 0.65`; `RandomizeSpellFunctionMixin` degrada a `EPIC` cualquier pergamino `LEGENDARY` generado fuera de muertes válidas de jefes cerrados.

## 3. Perfiles de riesgo `R0–R4` y cámaras finales `F2–F4`

**Exclusiones R0 (`100%` sin magia, accesorios ni libros):** todas las aldeas vanilla (`village_*`), estructuras de Ribbits (`ribbits:chests/*`), `irons_spellbooks:chests/priest_house`, `wheat`, `sewer_loot`, `component_storage`, `filler_storage_loot`, `minecraft:chests/igloo_chest` y `minecraft:chests/spawn_bonus_chest`.

**Perfiles `R1–R4` y `F2–F4`** (paquetes útiles con comida preparada/antorchas, materiales de reparación en pepitas/cuero/carbón y temáticos, más **una única selección mágica por cofre sumando `1000` = `100%`**; en `R3` de Nether se incluye `cinder_essence` dentro de otros):

| Perfil | Paquetes (sup / mat / tem) | Vacío | `common_ink` | `uncommon_ink` | `rare_ink` | `epic_ink` | Otros mágicos | Libros lv. I | Extra material (en pepitas) |
|---|---|---|---|---|---|---|---|---|---|
| `r1` / `r1_marine` | 2 × (55 / 35 / 10) | 90.0% | 8.0% | 0% | 0% | 0% | 2.0% | — | `mat_r1` (pep. hierro/oro 3–6, cuero 2–4, pep. cobre 4–8) + bonus marino (`r1_marine`) |
| `r2_dungeon` / `r2_other` | 3 × (40 / 50 / 10) | 75.0% | 12.0% | 5.0% | 0% | 0% | 8.0% | 10% (`_dungeon`) / — | `mat_r23` (pep. hierro/oro 4–8, cuero 2–4, carbón 3–5) |
| `f2_dungeon` | 3 × (40 / 50 / 10) | 55.0% | 20.0% | 10.0% | 2.0% | 0% | 13.0% | 15% | `mat_f2` (pep. hierro 6–12, pep. oro 4–8, cuero 4–6) |
| `r3_dungeon` / `r3_nether` / `r3_other` | 3 × (30 / 60 / 10) | 60.0% | 15.0% | 10.0% | 2.0% | 0% | 13.0% | 15% (dungeon/nether) / — | `mat_r23` |
| `f3_dungeon` | 3 × (30 / 60 / 10) | 35.0% | 15.0% | 20.0% | 8.0% | 1.0% | 21.0% | 20% | `mat_f3` (pep. hierro 8–14, pep. oro 6–10, pep. diamante 2–4) |
| `r4_dungeon` | 4 × (25 / 65 / 10) | 45.0% | 15.0% | 15.0% | 4.0% | 0.5% | 20.5% | 20% | `mat_r4` (pep. hierro/oro 5–10, cuero 2–5, carbón 3–6) |
| `f4_culm_*` (cámaras finales) | 4 × (25 / 65 / 10) | 0% | 0% | 0% | **97.0%** | **3.0%** | 0% | 25% (`_dungeon`) / — (`bastion`/`end_city`) | `mat_f4` (50% pep. oro 8–14, 35% pep. diamante 3–6, 15% pep. netherita 2–3 o pep. diamante 2–4) |
| `f4_provisional_overworld` | 4 × (25 / 65 / 10) | 20.0% | 10.0% | 20.0% | 15.0% | 3.0% | 32.0% | 25% | `mat_f4_overworld` (en pepitas) |

- Cámaras `F4` de culminación reales (`97%` `rare_ink` / `3%` `epic_ink`): `dead_king_vault`, `citadel_vault`, `betterfortresses:chests/keep`, `betterfortresses:chests/puzzle`, `betteroceanmonuments:chests/upper_side_chamber`, `bastion_treasure`, `end_city_treasure`.
- Los libros permitidos salen con igual peso y siempre a nivel I (`<= 1` por cofre): `minecraft:unbreaking`, `minecraft:looting`, `minecraft:efficiency`.

## 4. Lista cerrada de jefes (`EquipmentBalance 1.24.6`)

`EquipmentEvents` entrega un único drop garantizado en inventario/muerte válida (exige atacante jugador real, sin multiplicador de Botín):

- **`1 × irons_spellbooks:legendary_ink`:** `cataclysm:ignis`, `cataclysm:the_leviathan`, `cataclysm:ender_guardian`, `cataclysm:maledictus`, `cataclysm:scylla`, `minecraft:ender_dragon`, `minecraft:wither`, `irons_spellbooks:dead_king`.
- **`2 × irons_spellbooks:epic_ink`:** `cataclysm:netherite_monstrosity`, `cataclysm:the_harbinger`, `cataclysm:ancient_remnant`.

## 5. Verificación

- `python -B -m botin_magia_aventura.probar`: `457 comprobaciones pasadas` (tablas base de vanilla/mods y datapack con `0` equipo vanilla salvo `elytra`, `0` minerales completos salvo carbón, `<= 1` libro/encantamiento vanilla por cofre, `16` recetas MC 1.20.1 de `nuggets_for_all`, caldero 3:1, `0%` legendarios en cofres/GLMs y `scroll_pouch`/`filler_storage_loot` `<= 0.65`, suma `1000` por fila mágica, exclusiones `R0`, y `F4` 97%/3%).
- `LootTableMixin` + `EquipmentPolicy.sanitizeChestLoot`: validados en la instancia real Forge headless en `VerifyExternalEquipment.java`.
- `.\verificar_estado.ps1`: contrasta los `228` hashes SHA-256 de [loot.json](../loot.json). Ver inventario base de JARs en [LOOT_SOURCE_AUDIT.md](LOOT_SOURCE_AUDIT.md).
