# Matriz exacta del botín en 3 capas (Core + Suministros + Fortuna)

Contrato local de AdventureLoot 1.7.0 / EquipmentBalance 1.25.0. Cantidad exacta por apertura en **Capa 0 (Core)**; las tablas activas (`R1–R4`, `F2–F4`) añaden **Capa 1** de suministros acotados + temática de bioma (`bonus_rolls` por Suerte) y **Capa 2** de minerales/gemas enteros al abrir con `Luck >= 1`. Las tablas `r0_excluded`, `disabled_helper`, `lootr:chests/elytra` y `minecraft:chests/jungle_temple_dispenser` permanecen fijas en Capa 0.

| Tabla | Tier · Perfil / bioma | Capa 0 (Core determinista) |
|---|---|---|
| `betterdeserttemples:chests/food_storage` | R1 · r1_pantry / desert | 3 × nuggets_for_all:emeraldnugget |
| `betterdeserttemples:chests/lab` | R3 · r3_dungeon / desert | 3 × nuggets_for_all:emeraldnugget; 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo] |
| `betterdeserttemples:chests/library` | R3 · r3_other / library | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo] |
| `betterdeserttemples:chests/pharaoh_hidden` | R3 · f3_dungeon / desert | 3 × nuggets_for_all:emeraldnugget; 1 × irons_spellbooks:uncommon_ink; 2 × nuggets_for_all:diamondnugget; 1 × irons_spellbooks:rare_ink; 1 × irons_spellbooks:scroll [NBT fijo]; 1 × irons_spellbooks:emerald_stoneplate_ring |
| `betterdeserttemples:chests/pot` | R1 · r1_pantry / desert | 3 × nuggets_for_all:emeraldnugget |
| `betterdeserttemples:chests/statue` | R3 · r3_dungeon / desert | 3 × nuggets_for_all:emeraldnugget; 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo] |
| `betterdeserttemples:chests/storage` | R3 · r3_dungeon / desert | 3 × nuggets_for_all:emeraldnugget; 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo] |
| `betterdeserttemples:chests/tomb` | R3 · r3_dungeon / desert | 3 × nuggets_for_all:emeraldnugget; 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo] |
| `betterdeserttemples:chests/tomb_pharaoh` | R3 · f3_dungeon / desert | 3 × nuggets_for_all:emeraldnugget; 1 × irons_spellbooks:uncommon_ink; 2 × nuggets_for_all:diamondnugget; 1 × irons_spellbooks:rare_ink; 1 × minecraft:enchanted_book [NBT fijo]; 1 × irons_spellbooks:scroll [NBT fijo] |
| `betterdeserttemples:chests/wardrobe` | R1 · r1 / desert | 3 × nuggets_for_all:emeraldnugget |
| `betterdungeons:skeleton_dungeon/chests/common` | R2 · r2_dungeon / combat | 1 × irons_spellbooks:common_ink |
| `betterdungeons:skeleton_dungeon/chests/middle` | R2 · f2_dungeon / combat | 1 × irons_spellbooks:common_ink; 1 × nuggets_for_all:diamondnugget; 1 × minecraft:enchanted_book [NBT fijo] |
| `betterdungeons:small_dungeon/chests/loot_piles` | R2 · r2_dungeon / combat | 1 × irons_spellbooks:common_ink |
| `betterdungeons:small_nether_dungeon/chests/common` | R2 · r2_dungeon / nether | 1 × irons_spellbooks:common_ink; 1 × minecraft:music_disc_13; 1 × minecraft:music_disc_blocks; 1 × minecraft:music_disc_chirp; 1 × minecraft:music_disc_otherside; 1 × minecraft:music_disc_pigstep |
| `betterdungeons:spider_dungeon/chests/egg_room` | R2 · r2_dungeon / combat | 1 × irons_spellbooks:common_ink |
| `betterdungeons:zombie_dungeon/chests/common` | R2 · r2_dungeon / crypt | 1 × irons_spellbooks:common_ink |
| `betterdungeons:zombie_dungeon/chests/special` | R2 · f2_dungeon / crypt | 1 × irons_spellbooks:common_ink; 1 × nuggets_for_all:diamondnugget; 1 × minecraft:enchanted_book [NBT fijo] |
| `betterdungeons:zombie_dungeon/chests/tombstone` | R2 · f2_dungeon / crypt | 1 × irons_spellbooks:common_ink; 1 × nuggets_for_all:diamondnugget |
| `betterfortresses:chests/beacon` | R3 · r3_nether / nether | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo] |
| `betterfortresses:chests/extra` | R3 · r3_nether / nether | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo] |
| `betterfortresses:chests/hall` | R3 · r3_nether / nether | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo] |
| `betterfortresses:chests/keep` | R4 · f4_culm_nether_dungeon / nether | 1 × irons_spellbooks:uncommon_ink; 3 × nuggets_for_all:diamondnugget; 1 × irons_spellbooks:rare_ink; 1 × irons_spellbooks:blank_rune; 1 × minecraft:blaze_rod; 1 × minecraft:enchanted_book [NBT fijo]; 1 × irons_spellbooks:scroll [NBT fijo] |
| `betterfortresses:chests/obsidian` | R3 · r3_nether / nether | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo] |
| `betterfortresses:chests/puzzle` | R4 · f4_culm_nether_dungeon / nether | 1 × irons_spellbooks:uncommon_ink; 3 × nuggets_for_all:diamondnugget; 1 × irons_spellbooks:rare_ink; 1 × irons_spellbooks:blank_rune; 1 × minecraft:blaze_rod; 1 × minecraft:enchanted_book [NBT fijo]; 1 × irons_spellbooks:scroll [NBT fijo] |
| `betterfortresses:chests/quarters` | R3 · r3_nether / nether | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo] |
| `betterfortresses:chests/storage` | R3 · r3_nether / nether | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo] |
| `betterfortresses:chests/worship` | R3 · r3_nether / nether | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo] |
| `betteroceanmonuments:chests/upper_side_chamber` | R4 · f4_culm_overworld_dungeon / marine | 1 × irons_spellbooks:uncommon_ink; 3 × nuggets_for_all:diamondnugget; 1 × irons_spellbooks:rare_ink; 1 × irons_spellbooks:blank_rune; 1 × minecraft:enchanted_book [NBT fijo]; 1 × irons_spellbooks:scroll [NBT fijo] |
| `betterstrongholds:chests/armoury` | R3 · r3_dungeon / combat | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo] |
| `betterstrongholds:chests/cmd_yung` | R1 · r1 / combat | Sin Core fijo (solo Capa 1) |
| `betterstrongholds:chests/common` | R3 · r3_dungeon / combat | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo] |
| `betterstrongholds:chests/crypt` | R3 · r3_dungeon / crypt | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo] |
| `betterstrongholds:chests/grand_library` | R3 · r3_other / library | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo] |
| `betterstrongholds:chests/library_md` | R3 · r3_other / library | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo] |
| `betterstrongholds:chests/mess` | R1 · r1_pantry / combat | Sin Core fijo (solo Capa 1) |
| `betterstrongholds:chests/prison_lg` | R3 · r3_dungeon / combat | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo] |
| `betterstrongholds:chests/trap` | R3 · r3_dungeon / combat | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo] |
| `betterstrongholds:chests/treasure` | R3 · f3_dungeon / combat | 1 × irons_spellbooks:uncommon_ink; 2 × nuggets_for_all:diamondnugget; 1 × irons_spellbooks:rare_ink; 1 × minecraft:enchanted_book [NBT fijo]; 1 × irons_spellbooks:scroll [NBT fijo]; 1 × irons_spellbooks:silver_ring |
| `betterwitchhuts:chests/hut_0` | R2 · r2_other / combat | 1 × irons_spellbooks:common_ink |
| `cataclysm:chests/abandoned` | R2 · r2_dungeon / mine | 1 × irons_spellbooks:common_ink; 1 × cataclysm:sturdy_boots |
| `cataclysm:chests/abandoned_treasure` | R3 · f3_dungeon / mine | 1 × irons_spellbooks:uncommon_ink; 2 × nuggets_for_all:diamondnugget; 1 × irons_spellbooks:rare_ink; 1 × minecraft:enchanted_book [NBT fijo]; 1 × cataclysm:black_steel_sword; 1 × cataclysm:berserker_soul_amulet |
| `cataclysm:chests/acropolis_treasure` | R4 · f4_provisional_overworld / combat | 1 × irons_spellbooks:uncommon_ink; 3 × nuggets_for_all:diamondnugget; 1 × irons_spellbooks:rare_ink; 1 × irons_spellbooks:blank_rune; 1 × cataclysm:lacrima |
| `cataclysm:chests/amethyst_nest_chest` | R2 · r2_dungeon / combat | 1 × irons_spellbooks:common_ink; 1 × cataclysm:amethyst_crab_meat; 1 × cataclysm:amethyst_crab_shell; 1 × cataclysm:black_steel_shovel |
| `cataclysm:chests/desert_treasure` | R4 · f4_provisional_overworld / desert | 3 × nuggets_for_all:emeraldnugget; 1 × irons_spellbooks:uncommon_ink; 3 × nuggets_for_all:diamondnugget; 1 × irons_spellbooks:rare_ink; 1 × irons_spellbooks:blank_rune; 1 × cataclysm:unbreakable_skull; 1 × cataclysm:vitality_ankh; 1 × minecraft:dune_armor_trim_smithing_template |
| `cataclysm:chests/frosted_prison_treasure` | R4 · f4_provisional_overworld / ice | 1 × irons_spellbooks:uncommon_ink; 3 × nuggets_for_all:diamondnugget; 1 × irons_spellbooks:rare_ink; 1 × irons_spellbooks:blank_rune; 1 × cataclysm:black_steel_axe; 1 × cataclysm:ring_of_grudged |
| `irons_spellbooks:chests/additional_ancient_city_loot` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `irons_spellbooks:chests/additional_end_city_loot` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `irons_spellbooks:chests/additional_generic_loot` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `irons_spellbooks:chests/additional_good_loot` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `irons_spellbooks:chests/additional_library_loot` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `irons_spellbooks:chests/additional_nether_loot` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `irons_spellbooks:chests/additional_treasure_loot` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `irons_spellbooks:chests/battleground/burial_loot` | R4 · r4_dungeon / combat | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo]; 1 × irons_spellbooks:blank_rune |
| `irons_spellbooks:chests/battleground/piglin_camp` | R4 · r4_dungeon / combat | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo] |
| `irons_spellbooks:chests/bookshelf_loot` | R1 · r1 / library | Sin Core fijo (solo Capa 1) |
| `irons_spellbooks:chests/catacombs/armory_loot` | R4 · r4_dungeon / crypt | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo]; 1 × irons_spellbooks:heavy_chain_necklace |
| `irons_spellbooks:chests/catacombs/coffin_loot` | R4 · r4_dungeon / crypt | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo]; 1 × irons_spellbooks:rotten_spell_book; 1 × irons_spellbooks:teleportation_amulet |
| `irons_spellbooks:chests/catacombs/crypt_loot` | R4 · r4_dungeon / crypt | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo]; 1 × irons_spellbooks:ancient_knowledge_fragment; 1 × irons_spellbooks:blood_vial; 1 × irons_spellbooks:dead_king_phylactery_shard; 1 × irons_spellbooks:magic_cloth; 1 × irons_spellbooks:concentration_amulet |
| `irons_spellbooks:chests/catacombs/dead_king_vault` | R4 · f4_culm_overworld_dungeon / crypt | 1 × irons_spellbooks:uncommon_ink; 3 × nuggets_for_all:diamondnugget; 1 × irons_spellbooks:rare_ink; 1 × irons_spellbooks:blank_rune; 1 × minecraft:enchanted_book [NBT fijo]; 1 × irons_spellbooks:scroll [NBT fijo]; 1 × irons_spellbooks:ancient_knowledge_fragment; 1 × irons_spellbooks:blood_vial; 1 × irons_spellbooks:dead_king_phylactery_shard; 1 × irons_spellbooks:magic_cloth; 1 × irons_spellbooks:conjurers_talisman |
| `irons_spellbooks:chests/catacombs/hidden_trough_treasure` | R4 · r4_dungeon / crypt | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo]; 1 × irons_spellbooks:blank_rune; 1 × irons_spellbooks:rotten_spell_book; 1 × irons_spellbooks:invisibility_ring |
| `irons_spellbooks:chests/catacombs/pot` | R1 · r1_pantry / crypt | Sin Core fijo (solo Capa 1) |
| `irons_spellbooks:chests/catacombs/wall_loot` | R4 · r4_dungeon / crypt | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo]; 1 × irons_spellbooks:ancient_knowledge_fragment; 1 × irons_spellbooks:blank_rune; 1 × irons_spellbooks:rotten_spell_book |
| `irons_spellbooks:chests/citadel/citadel_bookshelf` | R3 · r3_other / nether | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo]; 1 × irons_spellbooks:ancient_knowledge_fragment; 1 × irons_spellbooks:chained_book; 1 × irons_spellbooks:disc_fragment_flame_still_burns; 1 × irons_spellbooks:furled_map; 1 × irons_spellbooks:ruined_book |
| `irons_spellbooks:chests/citadel/citadel_tomes` | R1 · r1 / nether | Sin Core fijo (solo Capa 1) |
| `irons_spellbooks:chests/citadel/citadel_vault` | R4 · f4_culm_nether_dungeon / nether | 1 × irons_spellbooks:uncommon_ink; 3 × nuggets_for_all:diamondnugget; 1 × irons_spellbooks:rare_ink; 1 × irons_spellbooks:blank_rune; 1 × minecraft:blaze_rod; 1 × minecraft:enchanted_book [NBT fijo]; 1 × irons_spellbooks:scroll [NBT fijo]; 1 × irons_spellbooks:ancient_knowledge_fragment; 1 × irons_spellbooks:disc_fragment_flame_still_burns; 1 × irons_spellbooks:mithril_scrap; 1 × irons_spellbooks:cooldown_ring |
| `irons_spellbooks:chests/citadel/rampart_chest` | R4 · r4_dungeon / nether | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo]; 1 × irons_spellbooks:blank_rune; 1 × irons_spellbooks:keeper_flamberge; 1 × irons_spellbooks:ominous_bottle |
| `irons_spellbooks:chests/citadel/rampart_supplies` | R1 · r1_pantry / nether | Sin Core fijo (solo Capa 1) |
| `irons_spellbooks:chests/citadel/spawner_reward` | R3 · f3_dungeon / nether | 1 × irons_spellbooks:uncommon_ink; 2 × nuggets_for_all:diamondnugget; 1 × irons_spellbooks:rare_ink; 1 × minecraft:blaze_rod; 1 × minecraft:enchanted_book [NBT fijo]; 1 × irons_spellbooks:scroll [NBT fijo]; 1 × irons_spellbooks:cast_time_ring |
| `irons_spellbooks:chests/component_storage` | FIXED · r0_excluded / settlement | 3 × minecraft:bread; 2 × minecraft:paper |
| `irons_spellbooks:chests/evoker_fort` | R3 · r3_dungeon / combat | 1 × irons_spellbooks:uncommon_ink; 1 × minecraft:enchanted_book [NBT fijo]; 1 × irons_spellbooks:scroll [NBT fijo]; 1 × irons_spellbooks:poisonward_ring |
| `irons_spellbooks:chests/evoker_fort/guard_tower` | R1 · r1 / combat | Sin Core fijo (solo Capa 1) |
| `irons_spellbooks:chests/filler_storage_loot` | FIXED · r0_excluded / settlement | 3 × minecraft:bread; 2 × minecraft:paper |
| `irons_spellbooks:chests/generic_magic_treasure` | R3 · r3_dungeon / combat | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo]; 1 × irons_spellbooks:blank_rune |
| `irons_spellbooks:chests/ice_spider_den/basement` | R1 · r1 / ice | Sin Core fijo (solo Capa 1) |
| `irons_spellbooks:chests/ice_spider_den/cask` | R1 · r1_pantry / ice | Sin Core fijo (solo Capa 1) |
| `irons_spellbooks:chests/ice_spider_den/dungeon` | R3 · r3_dungeon / ice | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo]; 1 × irons_spellbooks:blank_rune; 1 × irons_spellbooks:frozen_bone; 1 × irons_spellbooks:invisibility_elixir; 1 × irons_spellbooks:frostward_ring |
| `irons_spellbooks:chests/ice_spider_den/pot` | R1 · r1_pantry / ice | Sin Core fijo (solo Capa 1) |
| `irons_spellbooks:chests/ice_spider_den/spawner_reward` | R3 · f3_dungeon / ice | 1 × irons_spellbooks:uncommon_ink; 2 × nuggets_for_all:diamondnugget; 1 × irons_spellbooks:rare_ink; 1 × minecraft:enchanted_book [NBT fijo]; 1 × irons_spellbooks:scroll [NBT fijo] |
| `irons_spellbooks:chests/ice_spider_den/tower` | R2 · r2_other / ice | 1 × irons_spellbooks:common_ink |
| `irons_spellbooks:chests/impaled_icebreaker/captain_quarters` | R2 · r2_other / marine | 1 × irons_spellbooks:common_ink; 1 × irons_spellbooks:permafrost_shard |
| `irons_spellbooks:chests/impaled_icebreaker/food_barrel` | R1 · r1_pantry / marine | Sin Core fijo (solo Capa 1) |
| `irons_spellbooks:chests/magic_bookshelf_loot` | R3 · r3_other / library | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo]; 1 × irons_spellbooks:ancient_knowledge_fragment |
| `irons_spellbooks:chests/mangrove_hut` | R1 · r1 / combat | Sin Core fijo (solo Capa 1) |
| `irons_spellbooks:chests/mangrove_hut/hidden_potion_storage` | R1 · r1 / combat | Sin Core fijo (solo Capa 1) |
| `irons_spellbooks:chests/mangrove_hut/potion_ingredient_storage` | R1 · r1_pantry / combat | Sin Core fijo (solo Capa 1) |
| `irons_spellbooks:chests/mountain_tower/ice_barrel` | R1 · r1 / ice | Sin Core fijo (solo Capa 1) |
| `irons_spellbooks:chests/mountain_tower/mountain_tower` | R3 · r3_dungeon / ice | 1 × irons_spellbooks:uncommon_ink; 1 × minecraft:enchanted_book [NBT fijo]; 1 × irons_spellbooks:scroll [NBT fijo]; 1 × irons_spellbooks:frozen_bone; 1 × irons_spellbooks:furled_map; 1 × irons_spellbooks:affinity_ring |
| `irons_spellbooks:chests/priest_house` | FIXED · r0_excluded / settlement | 3 × minecraft:bread; 2 × minecraft:paper |
| `irons_spellbooks:chests/pyromancer_tower/burnt_chest` | R3 · r3_dungeon / nether | 1 × irons_spellbooks:uncommon_ink; 1 × minecraft:enchanted_book [NBT fijo]; 1 × irons_spellbooks:scroll [NBT fijo]; 1 × irons_spellbooks:fireward_ring |
| `irons_spellbooks:chests/pyromancer_tower/fire_ale_cask` | R1 · r1_pantry / nether | Sin Core fijo (solo Capa 1) |
| `irons_spellbooks:chests/pyromancer_tower/fire_ale_trove` | R1 · r1_pantry / nether | Sin Core fijo (solo Capa 1) |
| `irons_spellbooks:chests/pyromancer_tower/old_cask` | R1 · r1_pantry / nether | Sin Core fijo (solo Capa 1) |
| `irons_spellbooks:chests/pyromancer_tower/pot` | R1 · r1_pantry / nether | Sin Core fijo (solo Capa 1) |
| `irons_spellbooks:chests/pyromancer_tower/pyromancer_basic_storage` | R1 · r1_pantry / nether | Sin Core fijo (solo Capa 1) |
| `irons_spellbooks:chests/pyromancer_tower/pyromancer_supplies` | R3 · r3_dungeon / nether | 1 × irons_spellbooks:uncommon_ink; 1 × irons_spellbooks:scroll [NBT fijo] |
| `irons_spellbooks:chests/sewer_loot` | FIXED · r0_excluded / settlement | 3 × minecraft:bread; 2 × minecraft:paper |
| `irons_spellbooks:chests/trial_chambers/additional_ominous_spawner_consumable_loot` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `irons_spellbooks:chests/trial_chambers/additional_ominous_vault_loot` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `irons_spellbooks:chests/trial_chambers/additional_regular_spawner_consumable_loot` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `irons_spellbooks:chests/trial_chambers/additional_regular_vault_loot` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `irons_spellbooks:chests/trial_chambers/additional_trial_chest_loot` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `irons_spellbooks:chests/trial_chambers/pot_replacement` | R1 · r1_pantry / combat | Sin Core fijo (solo Capa 1) |
| `irons_spellbooks:chests/wheat` | FIXED · r0_excluded / settlement | 3 × minecraft:bread; 2 × minecraft:paper |
| `kaleidoscope_cookery:chest/village_chest` | FIXED · r0_excluded / settlement | 3 × minecraft:bread; 2 × minecraft:paper; 1 × kaleidoscope_cookery:chili_seed; 1 × kaleidoscope_cookery:lettuce_seed; 1 × kaleidoscope_cookery:oil; 1 × kaleidoscope_cookery:red_chili; 1 × kaleidoscope_cookery:rice_panicle; 1 × kaleidoscope_cookery:straw_block; 1 × kaleidoscope_cookery:tomato; 1 × kaleidoscope_cookery:tomato_seed; 1 × kaleidoscope_cookery:wild_rice |
| `kaleidoscope_cookery:chest/village_hide_chest` | FIXED · r0_excluded / settlement | 3 × minecraft:bread; 2 × minecraft:paper; 1 × kaleidoscope_cookery:beef_meatball_soup; 1 × kaleidoscope_cookery:braised_beef_with_potatoes; 1 × kaleidoscope_cookery:chicken_and_mushroom_stew; 1 × kaleidoscope_cookery:egg_fried_rice; 1 × kaleidoscope_cookery:pork_bone_soup; 1 × kaleidoscope_cookery:seafood_miso_soup; 1 × kaleidoscope_cookery:slime_ball_meal |
| `kaleidoscope_nether:chests/bastion_hoglin_stable` | R1 · r1 / nether | 1 × kaleidoscope_nether:ham; 1 × kaleidoscope_nether:nether_caterpillar; 1 × kaleidoscope_nether:roasted_ham; 1 × kaleidoscope_nether:soul_pepper |
| `kaleidoscope_nether:chests/bastion_treasure` | R1 · r1 / nether | 1 × kaleidoscope_nether:ghast_pendant; 1 × kaleidoscope_nether:gilded_fragment; 1 × kaleidoscope_nether:star_dust |
| `lootr:chests/elytra` | FIXED · r1 / combat | 1 × minecraft:elytra |
| `minecraft:chests/abandoned_mineshaft` | R2 · r2_dungeon / mine | 1 × irons_spellbooks:common_ink |
| `minecraft:chests/ancient_city` | R4 · r4_dungeon / mine | 1 × irons_spellbooks:uncommon_ink; 1 × minecraft:disc_fragment_5; 1 × minecraft:music_disc_13; 1 × minecraft:music_disc_cat; 1 × minecraft:music_disc_otherside; 1 × minecraft:silence_armor_trim_smithing_template; 1 × minecraft:ward_armor_trim_smithing_template |
| `minecraft:chests/ancient_city_ice_box` | R1 · r1_pantry / ice | Sin Core fijo (solo Capa 1) |
| `minecraft:chests/bastion_bridge` | R3 · r3_other / nether | 1 × irons_spellbooks:uncommon_ink; 1 × minecraft:netherite_upgrade_smithing_template; 1 × minecraft:snout_armor_trim_smithing_template |
| `minecraft:chests/bastion_hoglin_stable` | R3 · r3_other / nether | 1 × irons_spellbooks:uncommon_ink; 1 × minecraft:netherite_upgrade_smithing_template; 1 × minecraft:snout_armor_trim_smithing_template |
| `minecraft:chests/bastion_other` | R3 · r3_other / nether | 1 × irons_spellbooks:uncommon_ink; 1 × minecraft:music_disc_pigstep; 1 × minecraft:netherite_upgrade_smithing_template; 1 × minecraft:piglin_banner_pattern; 1 × minecraft:snout_armor_trim_smithing_template |
| `minecraft:chests/bastion_treasure` | R4 · f4_culm_nether_end_nobook / nether | 1 × irons_spellbooks:uncommon_ink; 3 × nuggets_for_all:diamondnugget; 1 × irons_spellbooks:rare_ink; 1 × irons_spellbooks:blank_rune; 1 × minecraft:blaze_rod; 1 × minecraft:enchanted_book [NBT fijo]; 1 × minecraft:netherite_upgrade_smithing_template; 1 × minecraft:snout_armor_trim_smithing_template |
| `minecraft:chests/buried_treasure` | R1 · r1_marine / marine | 1 × minecraft:heart_of_the_sea |
| `minecraft:chests/desert_pyramid` | R2 · f2_dungeon / desert | 3 × nuggets_for_all:emeraldnugget; 1 × irons_spellbooks:common_ink; 1 × nuggets_for_all:diamondnugget; 1 × minecraft:dune_armor_trim_smithing_template |
| `minecraft:chests/end_city_treasure` | R4 · f4_culm_nether_end_nobook / end | 4 × minecraft:popped_chorus_fruit; 1 × minecraft:ender_pearl; 1 × irons_spellbooks:uncommon_ink; 3 × nuggets_for_all:diamondnugget; 1 × irons_spellbooks:rare_ink; 1 × irons_spellbooks:blank_rune; 1 × minecraft:spire_armor_trim_smithing_template |
| `minecraft:chests/igloo_chest` | FIXED · r0_excluded / mine | 3 × minecraft:bread; 8 × minecraft:rail; 4 × minecraft:coal |
| `minecraft:chests/jungle_temple` | R2 · f2_dungeon / mine | 1 × irons_spellbooks:common_ink; 1 × nuggets_for_all:diamondnugget; 1 × minecraft:enchanted_book [NBT fijo]; 1 × minecraft:wild_armor_trim_smithing_template |
| `minecraft:chests/jungle_temple_dispenser` | FIXED · r1 / mine | 8 × minecraft:arrow |
| `minecraft:chests/nether_bridge` | R3 · r3_nether / nether | 1 × irons_spellbooks:uncommon_ink; 1 × minecraft:rib_armor_trim_smithing_template |
| `minecraft:chests/pillager_outpost` | R2 · r2_other / mine | 1 × irons_spellbooks:common_ink; 1 × minecraft:sentry_armor_trim_smithing_template |
| `minecraft:chests/ruined_portal` | R1 · r1 / mine | Sin Core fijo (solo Capa 1) |
| `minecraft:chests/shipwreck_map` | R1 · r1 / marine | 1 × minecraft:coast_armor_trim_smithing_template |
| `minecraft:chests/shipwreck_supply` | R1 · r1 / marine | 1 × minecraft:coast_armor_trim_smithing_template |
| `minecraft:chests/shipwreck_treasure` | R1 · r1_marine / marine | 1 × minecraft:coast_armor_trim_smithing_template |
| `minecraft:chests/simple_dungeon` | R2 · r2_dungeon / mine | 1 × irons_spellbooks:common_ink; 1 × minecraft:enchanted_book [NBT fijo]; 1 × minecraft:music_disc_13; 1 × minecraft:music_disc_cat; 1 × minecraft:music_disc_otherside |
| `minecraft:chests/spawn_bonus_chest` | FIXED · r0_excluded / mine | 3 × minecraft:bread; 8 × minecraft:rail; 4 × minecraft:coal |
| `minecraft:chests/stronghold_corridor` | R3 · r3_dungeon / mine | 1 × irons_spellbooks:uncommon_ink; 1 × minecraft:eye_armor_trim_smithing_template; 1 × minecraft:music_disc_otherside |
| `minecraft:chests/stronghold_crossing` | R3 · r3_dungeon / mine | 1 × irons_spellbooks:uncommon_ink |
| `minecraft:chests/stronghold_library` | R3 · r3_other / library | 1 × irons_spellbooks:uncommon_ink; 1 × minecraft:eye_armor_trim_smithing_template |
| `minecraft:chests/underwater_ruin_big` | R2 · r2_other / mine | 1 × irons_spellbooks:common_ink |
| `minecraft:chests/underwater_ruin_small` | R1 · r1 / mine | Sin Core fijo (solo Capa 1) |
| `minecraft:chests/village/village_armorer` | FIXED · r0_excluded / mine | 3 × minecraft:bread; 3 × minecraft:iron_nugget; 8 × minecraft:rail; 4 × minecraft:coal |
| `minecraft:chests/village/village_butcher` | FIXED · r0_excluded / mine | 3 × minecraft:bread; 8 × minecraft:rail; 4 × minecraft:coal |
| `minecraft:chests/village/village_cartographer` | FIXED · r0_excluded / mine | 3 × minecraft:bread; 8 × minecraft:rail; 4 × minecraft:coal |
| `minecraft:chests/village/village_desert_house` | FIXED · r0_excluded / desert | 3 × minecraft:bread; 6 × minecraft:terracotta; 3 × nuggets_for_all:emeraldnugget |
| `minecraft:chests/village/village_fisher` | FIXED · r0_excluded / mine | 3 × minecraft:bread; 8 × minecraft:rail; 4 × minecraft:coal |
| `minecraft:chests/village/village_fletcher` | FIXED · r0_excluded / mine | 3 × minecraft:bread; 8 × minecraft:rail; 4 × minecraft:coal |
| `minecraft:chests/village/village_mason` | FIXED · r0_excluded / mine | 3 × minecraft:bread; 8 × minecraft:rail; 4 × minecraft:coal |
| `minecraft:chests/village/village_plains_house` | FIXED · r0_excluded / mine | 3 × minecraft:bread; 8 × minecraft:rail; 4 × minecraft:coal |
| `minecraft:chests/village/village_savanna_house` | FIXED · r0_excluded / mine | 3 × minecraft:bread; 8 × minecraft:rail; 4 × minecraft:coal |
| `minecraft:chests/village/village_shepherd` | FIXED · r0_excluded / mine | 3 × minecraft:bread; 8 × minecraft:rail; 4 × minecraft:coal |
| `minecraft:chests/village/village_snowy_house` | FIXED · r0_excluded / mine | 3 × minecraft:bread; 8 × minecraft:rail; 4 × minecraft:coal |
| `minecraft:chests/village/village_taiga_house` | FIXED · r0_excluded / mine | 3 × minecraft:bread; 8 × minecraft:rail; 4 × minecraft:coal |
| `minecraft:chests/village/village_tannery` | FIXED · r0_excluded / mine | 3 × minecraft:bread; 8 × minecraft:rail; 4 × minecraft:coal |
| `minecraft:chests/village/village_temple` | FIXED · r0_excluded / mine | 3 × minecraft:bread; 8 × minecraft:rail; 4 × minecraft:coal |
| `minecraft:chests/village/village_toolsmith` | FIXED · r0_excluded / mine | 3 × minecraft:bread; 3 × minecraft:iron_nugget; 8 × minecraft:rail; 4 × minecraft:coal |
| `minecraft:chests/village/village_weaponsmith` | FIXED · r0_excluded / mine | 3 × minecraft:bread; 3 × minecraft:iron_nugget; 8 × minecraft:rail; 4 × minecraft:coal |
| `minecraft:chests/woodland_mansion` | R3 · r3_other / mine | 1 × irons_spellbooks:uncommon_ink; 1 × minecraft:music_disc_13; 1 × minecraft:music_disc_cat; 1 × minecraft:vex_armor_trim_smithing_template |
| `ribbits:chests/fisherman_main` | FIXED · r0_excluded / marine | 3 × minecraft:cooked_cod; 3 × minecraft:prismarine_shard; 4 × minecraft:kelp; 1 × ribbits:giant_lilypad |
| `ribbits:chests/fisherman_storage` | FIXED · r0_excluded / marine | 3 × minecraft:cooked_cod; 3 × minecraft:prismarine_shard; 4 × minecraft:kelp; 1 × ribbits:giant_lilypad |
| `ribbits:chests/gardener` | FIXED · r0_excluded / settlement | 3 × minecraft:bread; 2 × minecraft:paper; 1 × ribbits:giant_lilypad |
| `ribbits:chests/merchant` | FIXED · r0_excluded / settlement | 3 × minecraft:bread; 2 × minecraft:paper |
| `ribbits:chests/nitwit` | FIXED · r0_excluded / settlement | 3 × minecraft:bread; 2 × minecraft:paper; 1 × ribbits:giant_lilypad |
| `ribbits:chests/sorcerer` | FIXED · r0_excluded / settlement | 3 × minecraft:bread; 2 × minecraft:paper |
| `theoptimizer:chests/book_f2` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/book_f3` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/book_f4` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/book_r2` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/book_r3` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/book_r4` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/magic_otros` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/magic_otros_nether` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/mat_f2` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/mat_f3` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/mat_f4_nether_end` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/mat_f4_overworld` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/pkg_marine_bonus` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/pkg_mat_r1` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/pkg_mat_r23` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/pkg_mat_r4` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/pkg_supply` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/pkg_thematic` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/profile_f2_dungeon` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/profile_f3_dungeon` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/profile_f4_culm_nether_dungeon` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/profile_f4_culm_nether_end_nobook` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/profile_f4_culm_overworld_dungeon` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/profile_f4_provisional_overworld` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/profile_r1` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/profile_r1_marine` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/profile_r2_dungeon` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/profile_r2_other` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/profile_r3_dungeon` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/profile_r3_nether` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/profile_r3_other` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/profile_r4_dungeon` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/scrolls_high` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/scrolls_r1` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `theoptimizer:chests/scrolls_r23` | FIXED · disabled_helper / auxiliar inactivo | Sin añadidos |
| `yungsextras:desert/chillzone` | FIXED · r0_excluded / desert | 3 × minecraft:bread; 6 × minecraft:terracotta; 3 × nuggets_for_all:emeraldnugget |
| `yungsextras:desert/ruins` | R1 · r1 / desert | 3 × nuggets_for_all:emeraldnugget |
