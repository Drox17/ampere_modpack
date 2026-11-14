# Guía de botín por estructura

Esta guía cubre las tablas de cofres identificadas en la extracción anterior. El porcentaje indicado es **por tirada**, no por cofre completo. Si hay varias tiradas, puede salir el mismo objeto más de una vez. Las condiciones, suerte, funciones, tablas anidadas y modificadores pueden cambiar el resultado. No se presentan porcentajes globales cuando faltan datos.

Los nombres son aproximados cuando no hay traducción instalada; se conserva el identificador para evitar ambigüedades. Los cofres identificados por mods no cubren necesariamente todas las estructuras posibles.

## ae2:blocks — meteorite

Tabla: `ae2:blocks/chests/meteorite` · fuente: `appliedenergistics2-forge-15.4.12.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 3.0, "min": 1.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Piedra del Cielo (`ae2:sky_stone_block`) | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

## betterdeserttemples — food storage

Tabla: `betterdeserttemples:chests/food_storage` · fuente: `YungsBetterDesertTemples-1.20-Forge-3.0.3.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 5.0, "max": 7.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| potato (`minecraft:potato`) | 5 | 12.82 % | Cantidad: {"type": "minecraft:uniform", "min": 6.0, "max": 12.0} |
| poisonous potato (`minecraft:poisonous_potato`) | 2 | 5.13 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 3.0} |
| wheat (`minecraft:wheat`) | 5 | 12.82 % | Cantidad: {"type": "minecraft:uniform", "min": 6.0, "max": 12.0} |
| bread (`minecraft:bread`) | 5 | 12.82 % | Cantidad: {"type": "minecraft:uniform", "min": 4.0, "max": 6.0} |
| golden apple (`minecraft:golden_apple`) | 1 | 2.56 % | 1 por resultado; puede variar por funciones de la tabla |
| enchanted golden apple (`minecraft:enchanted_golden_apple`) | 1 | 2.56 % | 1 por resultado; puede variar por funciones de la tabla |
| dried kelp (`minecraft:dried_kelp`) | 5 | 12.82 % | Cantidad: {"type": "minecraft:uniform", "min": 3.0, "max": 6.0} |
| honey bottle (`minecraft:honey_bottle`) | 5 | 12.82 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 3.0} |
| beetroot soup (`minecraft:beetroot_soup`) | 5 | 12.82 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 5.0} |
| melon seeds (`minecraft:melon_seeds`) | 5 | 12.82 % | Cantidad: {"type": "minecraft:uniform", "min": 6.0, "max": 12.0} |

## betterdeserttemples — lab

Tabla: `betterdeserttemples:chests/lab` · fuente: `YungsBetterDesertTemples-1.20-Forge-3.0.3.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 3.0, "max": 5.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| potion (`minecraft:potion`) | 10 | 18.18 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 3.0}; Función: minecraft:set_nbt |
| fermented spider eye (`minecraft:fermented_spider_eye`) | 10 | 18.18 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 3.0} |
| melon slice (`minecraft:melon_slice`) | 10 | 18.18 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 5.0} |
| glistering melon slice (`minecraft:glistering_melon_slice`) | 4 | 7.27 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 3.0} |
| rabbit foot (`minecraft:rabbit_foot`) | 1 | 1.82 % | 1 por resultado; puede variar por funciones de la tabla |
| carrot (`minecraft:carrot`) | 10 | 18.18 % | Cantidad: {"type": "minecraft:uniform", "min": 3.0, "max": 8.0} |
| golden carrot (`minecraft:golden_carrot`) | 4 | 7.27 % | Cantidad: {"type": "minecraft:uniform", "min": 3.0, "max": 8.0} |
| gunpowder (`minecraft:gunpowder`) | 6 | 10.91 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 3.0} |

**Grupo 2** · tiradas: `4`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| coal (`minecraft:coal`) | 10 | 33.33 % | Cantidad: {"min": 3.0, "max": 6.0, "type": "minecraft:uniform"} |
| stick (`minecraft:stick`) | 10 | 33.33 % | Cantidad: {"min": 2.0, "max": 4.0, "type": "minecraft:uniform"} |
| cobweb (`minecraft:cobweb`) | 10 | 33.33 % | Cantidad: {"min": 3.0, "max": 6.0, "type": "minecraft:uniform"} |

## betterdeserttemples — library

Tabla: `betterdeserttemples:chests/library` · fuente: `YungsBetterDesertTemples-1.20-Forge-3.0.3.jar`.

**Grupo 1** · tiradas: `{"min": 2.0, "max": 10.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| book (`minecraft:book`) | 20 | 41.67 % | Cantidad: {"min": 1.0, "max": 3.0, "type": "minecraft:uniform"} |
| paper (`minecraft:paper`) | 20 | 41.67 % | Cantidad: {"min": 2.0, "max": 7.0, "type": "minecraft:uniform"} |
| map (`minecraft:map`) | 1 | 2.08 % | 1 por resultado; puede variar por funciones de la tabla |
| compass (`minecraft:compass`) | 1 | 2.08 % | 1 por resultado; puede variar por funciones de la tabla |
| book (`minecraft:book`) | 3 | 6.25 % | Función: minecraft:enchant_with_levels |
| book (`minecraft:book`) | 3 | 6.25 % | Función: minecraft:enchant_with_levels |

## betterdeserttemples — pharaoh hidden

Tabla: `betterdeserttemples:chests/pharaoh_hidden` · fuente: `YungsBetterDesertTemples-1.20-Forge-3.0.3.jar`.

**Grupo 1** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| golden sword (`minecraft:golden_sword`) | 1 | 100.00 % | Función: minecraft:enchant_with_levels; Función: minecraft:enchant_randomly |

**Grupo 2** · tiradas: `4`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| sand (`minecraft:sand`) | 5 | 100.00 % | Cantidad: {"type": "minecraft:uniform", "min": 4.0, "max": 8.0} |

## betterdeserttemples — pot

Tabla: `betterdeserttemples:chests/pot` · fuente: `YungsBetterDesertTemples-1.20-Forge-3.0.3.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 4.0, "max": 6.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| terracotta (`minecraft:terracotta`) | 5 | 14.29 % | Cantidad: {"type": "minecraft:uniform", "min": 6.0, "max": 12.0} |
| dirt (`minecraft:dirt`) | 5 | 14.29 % | Cantidad: {"type": "minecraft:uniform", "min": 6.0, "max": 12.0} |
| emerald (`minecraft:emerald`) | 5 | 14.29 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 3.0} |
| potato (`minecraft:potato`) | 5 | 14.29 % | Cantidad: {"type": "minecraft:uniform", "min": 6.0, "max": 12.0} |
| wheat (`minecraft:wheat`) | 5 | 14.29 % | Cantidad: {"type": "minecraft:uniform", "min": 6.0, "max": 12.0} |
| gunpowder (`minecraft:gunpowder`) | 5 | 14.29 % | Cantidad: {"type": "minecraft:uniform", "min": 4.0, "max": 6.0} |
| melon seeds (`minecraft:melon_seeds`) | 5 | 14.29 % | Cantidad: {"type": "minecraft:uniform", "min": 6.0, "max": 12.0} |

## betterdeserttemples — statue

Tabla: `betterdeserttemples:chests/statue` · fuente: `YungsBetterDesertTemples-1.20-Forge-3.0.3.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 1.0, "max": 2.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| emerald (`minecraft:emerald`) | 10 | 50.00 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 3.0} |
| gold ingot (`minecraft:gold_ingot`) | 10 | 50.00 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 3.0} |

## betterdeserttemples — storage

Tabla: `betterdeserttemples:chests/storage` · fuente: `YungsBetterDesertTemples-1.20-Forge-3.0.3.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 2.0, "max": 4.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| sand (`minecraft:sand`) | 50 | 14.08 % | Cantidad: {"type": "minecraft:uniform", "min": 4.0, "max": 8.0} |
| emerald (`minecraft:emerald`) | 10 | 2.82 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 2.0} |
| lapis lazuli (`minecraft:lapis_lazuli`) | 10 | 2.82 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 4.0} |
| weathered copper (`minecraft:weathered_copper`) | 10 | 2.82 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 3.0} |
| oxidized copper (`minecraft:oxidized_copper`) | 10 | 2.82 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 3.0} |
| gunpowder (`minecraft:gunpowder`) | 50 | 14.08 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 6.0} |
| bone (`minecraft:bone`) | 50 | 14.08 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 5.0} |
| string (`minecraft:string`) | 50 | 14.08 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 4.0} |
| rotten flesh (`minecraft:rotten_flesh`) | 50 | 14.08 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 4.0} |
| book (`minecraft:book`) | 10 | 2.82 % | Función: minecraft:enchant_randomly |
| golden apple (`minecraft:golden_apple`) | 10 | 2.82 % | 1 por resultado; puede variar por funciones de la tabla |
| saddle (`minecraft:saddle`) | 10 | 2.82 % | 1 por resultado; puede variar por funciones de la tabla |
| iron horse armor (`minecraft:iron_horse_armor`) | 15 | 4.23 % | 1 por resultado; puede variar por funciones de la tabla |
| golden horse armor (`minecraft:golden_horse_armor`) | 10 | 2.82 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond horse armor (`minecraft:diamond_horse_armor`) | 10 | 2.82 % | 1 por resultado; puede variar por funciones de la tabla |

## betterdeserttemples — tomb

Tabla: `betterdeserttemples:chests/tomb` · fuente: `YungsBetterDesertTemples-1.20-Forge-3.0.3.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 1.0, "max": 3.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| gold ingot (`minecraft:gold_ingot`) | 5 | 11.11 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 7.0} |
| emerald (`minecraft:emerald`) | 5 | 11.11 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 3.0} |
| saddle (`minecraft:saddle`) | 5 | 11.11 % | 1 por resultado; puede variar por funciones de la tabla |
| cobweb (`minecraft:cobweb`) | 15 | 33.33 % | 1 por resultado; puede variar por funciones de la tabla |
| book (`minecraft:book`) | 5 | 11.11 % | Función: minecraft:enchant_randomly |
| Nada | 10 | 22.22 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 2** · tiradas: `4`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| bone (`minecraft:bone`) | 15 | 30.00 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 4.0} |
| bone meal (`minecraft:bone_meal`) | 15 | 30.00 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 4.0} |
| gunpowder (`minecraft:gunpowder`) | 5 | 10.00 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 4.0} |
| rotten flesh (`minecraft:rotten_flesh`) | 5 | 10.00 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 4.0} |
| string (`minecraft:string`) | 5 | 10.00 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 4.0} |
| sand (`minecraft:sand`) | 5 | 10.00 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 8.0} |

## betterdeserttemples — tomb pharaoh

Tabla: `betterdeserttemples:chests/tomb_pharaoh` · fuente: `YungsBetterDesertTemples-1.20-Forge-3.0.3.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 3.0, "max": 4.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| gold ingot (`minecraft:gold_ingot`) | 5 | 14.29 % | Cantidad: {"type": "minecraft:uniform", "min": 3.0, "max": 8.0} |
| emerald (`minecraft:emerald`) | 5 | 14.29 % | Cantidad: {"type": "minecraft:uniform", "min": 3.0, "max": 6.0} |
| book (`minecraft:book`) | 5 | 14.29 % | Función: minecraft:enchant_randomly |
| diamond (`minecraft:diamond`) | 5 | 14.29 % | Cantidad: {"type": "minecraft:uniform", "min": 3.0, "max": 6.0} |
| golden sword (`minecraft:golden_sword`) | 5 | 14.29 % | Función: minecraft:enchant_randomly; Función: minecraft:enchant_randomly |
| enchanted golden apple (`minecraft:enchanted_golden_apple`) | 5 | 14.29 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond horse armor (`minecraft:diamond_horse_armor`) | 5 | 14.29 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 2** · tiradas: `4`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| bone (`minecraft:bone`) | 15 | 30.00 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 4.0} |
| bone meal (`minecraft:bone_meal`) | 15 | 30.00 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 4.0} |
| gunpowder (`minecraft:gunpowder`) | 5 | 10.00 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 4.0} |
| rotten flesh (`minecraft:rotten_flesh`) | 5 | 10.00 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 4.0} |
| string (`minecraft:string`) | 5 | 10.00 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 4.0} |
| sand (`minecraft:sand`) | 5 | 10.00 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 8.0} |

## betterdeserttemples — wardrobe

Tabla: `betterdeserttemples:chests/wardrobe` · fuente: `YungsBetterDesertTemples-1.20-Forge-3.0.3.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 3.0, "max": 6.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| yellow wool (`minecraft:yellow_wool`) | 5 | 11.36 % | Cantidad: {"type": "minecraft:uniform", "min": 3.0, "max": 6.0} |
| blue wool (`minecraft:blue_wool`) | 5 | 11.36 % | Cantidad: {"type": "minecraft:uniform", "min": 3.0, "max": 6.0} |
| leather (`minecraft:leather`) | 5 | 11.36 % | Cantidad: {"type": "minecraft:uniform", "min": 3.0, "max": 6.0} |
| leather helmet (`minecraft:leather_helmet`) | 2 | 4.55 % | 1 por resultado; puede variar por funciones de la tabla |
| leather chestplate (`minecraft:leather_chestplate`) | 2 | 4.55 % | 1 por resultado; puede variar por funciones de la tabla |
| leather leggings (`minecraft:leather_leggings`) | 2 | 4.55 % | 1 por resultado; puede variar por funciones de la tabla |
| leather boots (`minecraft:leather_boots`) | 2 | 4.55 % | 1 por resultado; puede variar por funciones de la tabla |
| leather helmet (`minecraft:leather_helmet`) | 1 | 2.27 % | Función: minecraft:enchant_randomly; Función: minecraft:enchant_randomly |
| leather chestplate (`minecraft:leather_chestplate`) | 1 | 2.27 % | Función: minecraft:enchant_randomly; Función: minecraft:enchant_randomly |
| leather leggings (`minecraft:leather_leggings`) | 1 | 2.27 % | Función: minecraft:enchant_randomly; Función: minecraft:enchant_randomly |
| leather boots (`minecraft:leather_boots`) | 1 | 2.27 % | Función: minecraft:enchant_randomly; Función: minecraft:enchant_randomly |
| leather helmet (`minecraft:leather_helmet`) | 1 | 2.27 % | Función: minecraft:enchant_randomly |
| leather chestplate (`minecraft:leather_chestplate`) | 1 | 2.27 % | Función: minecraft:enchant_randomly |
| leather leggings (`minecraft:leather_leggings`) | 1 | 2.27 % | Función: minecraft:enchant_randomly |
| leather boots (`minecraft:leather_boots`) | 1 | 2.27 % | Función: minecraft:enchant_randomly |
| orange dye (`minecraft:orange_dye`) | 2 | 4.55 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 6.0} |
| yellow dye (`minecraft:yellow_dye`) | 2 | 4.55 % | Cantidad: {"type": "minecraft:uniform", "min": 3.0, "max": 6.0} |
| blue dye (`minecraft:blue_dye`) | 2 | 4.55 % | Cantidad: {"type": "minecraft:uniform", "min": 3.0, "max": 6.0} |
| green dye (`minecraft:green_dye`) | 2 | 4.55 % | Cantidad: {"type": "minecraft:uniform", "min": 3.0, "max": 6.0} |
| feather (`minecraft:feather`) | 5 | 11.36 % | Cantidad: {"type": "minecraft:uniform", "min": 4.0, "max": 6.0} |

## betterdungeons:skeleton dungeon — common

Tabla: `betterdungeons:skeleton_dungeon/chests/common` · fuente: `YungsBetterDungeons-1.20-Forge-4.0.4.jar`.

**Grupo 1** · tiradas: `{"min": 2.0, "max": 4.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| golden apple (`minecraft:golden_apple`) | 5 | 17.24 % | 1 por resultado; puede variar por funciones de la tabla |
| enchanted golden apple (`minecraft:enchanted_golden_apple`) | 1 | 3.45 % | 1 por resultado; puede variar por funciones de la tabla |
| book (`minecraft:book`) | 2 | 6.90 % | Función: minecraft:enchant_randomly |
| book (`minecraft:book`) | 10 | 34.48 % | Función: minecraft:enchant_randomly |
| bow (`minecraft:bow`) | 3 | 10.34 % | Función: minecraft:enchant_randomly |
| tipped arrow (`minecraft:tipped_arrow`) | 1 | 3.45 % | Cantidad: {"min": 2.0, "max": 6.0, "type": "minecraft:uniform"}; Función: minecraft:set_nbt |
| tipped arrow (`minecraft:tipped_arrow`) | 1 | 3.45 % | Cantidad: {"min": 2.0, "max": 6.0, "type": "minecraft:uniform"}; Función: minecraft:set_nbt |
| tipped arrow (`minecraft:tipped_arrow`) | 1 | 3.45 % | Cantidad: {"min": 2.0, "max": 6.0, "type": "minecraft:uniform"}; Función: minecraft:set_nbt |
| tipped arrow (`minecraft:tipped_arrow`) | 1 | 3.45 % | Cantidad: {"min": 2.0, "max": 6.0, "type": "minecraft:uniform"}; Función: minecraft:set_nbt |
| tipped arrow (`minecraft:tipped_arrow`) | 1 | 3.45 % | Cantidad: {"min": 2.0, "max": 6.0, "type": "minecraft:uniform"}; Función: minecraft:set_nbt |
| tipped arrow (`minecraft:tipped_arrow`) | 1 | 3.45 % | Cantidad: {"min": 2.0, "max": 6.0, "type": "minecraft:uniform"}; Función: minecraft:set_nbt |
| tipped arrow (`minecraft:tipped_arrow`) | 1 | 3.45 % | Cantidad: {"min": 2.0, "max": 6.0, "type": "minecraft:uniform"}; Función: minecraft:set_nbt |
| tipped arrow (`minecraft:tipped_arrow`) | 1 | 3.45 % | Cantidad: {"min": 2.0, "max": 6.0, "type": "minecraft:uniform"}; Función: minecraft:set_nbt |

**Grupo 2** · tiradas: `{"min": 1.0, "max": 3.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| iron ingot (`minecraft:iron_ingot`) | 10 | 37.04 % | Cantidad: {"min": 2.0, "max": 6.0, "type": "minecraft:uniform"} |
| gold ingot (`minecraft:gold_ingot`) | 5 | 18.52 % | Cantidad: {"min": 2.0, "max": 4.0, "type": "minecraft:uniform"} |
| redstone (`minecraft:redstone`) | 10 | 37.04 % | Cantidad: {"min": 2.0, "max": 4.0, "type": "minecraft:uniform"} |
| name tag (`minecraft:name_tag`) | 1 | 3.70 % | 1 por resultado; puede variar por funciones de la tabla |
| lead (`minecraft:lead`) | 1 | 3.70 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 3** · tiradas: `2`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| bone (`minecraft:bone`) | 10 | 50.00 % | Cantidad: {"min": 2.0, "max": 8.0, "type": "minecraft:uniform"} |
| bone meal (`minecraft:bone_meal`) | 10 | 50.00 % | Cantidad: {"min": 2.0, "max": 8.0, "type": "minecraft:uniform"} |

## betterdungeons:skeleton dungeon — middle

Tabla: `betterdungeons:skeleton_dungeon/chests/middle` · fuente: `YungsBetterDungeons-1.20-Forge-4.0.4.jar`.

**Grupo 1** · tiradas: `{"min": 3.0, "max": 5.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| charcoal (`minecraft:charcoal`) | 10 | 20.00 % | Cantidad: {"min": 2.0, "max": 4.0, "type": "minecraft:uniform"} |
| coal (`minecraft:coal`) | 10 | 20.00 % | Cantidad: {"min": 2.0, "max": 4.0, "type": "minecraft:uniform"} |
| torch (`minecraft:torch`) | 10 | 20.00 % | Cantidad: {"min": 2.0, "max": 4.0, "type": "minecraft:uniform"} |
| stick (`minecraft:stick`) | 10 | 20.00 % | Cantidad: {"min": 3.0, "max": 5.0, "type": "minecraft:uniform"} |
| diamond (`minecraft:diamond`) | 10 | 20.00 % | 1 por resultado; puede variar por funciones de la tabla |

## betterdungeons:small dungeon — loot piles

Tabla: `betterdungeons:small_dungeon/chests/loot_piles` · fuente: `YungsBetterDungeons-1.20-Forge-4.0.4.jar`.

**Grupo 1** · tiradas: `{"min": 2.0, "max": 3.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| cobweb (`minecraft:cobweb`) | 1 | 33.33 % | Cantidad: {"min": 1.0, "max": 5.0, "type": "minecraft:uniform"} |
| dirt (`minecraft:dirt`) | 1 | 33.33 % | Cantidad: {"min": 1.0, "max": 5.0, "type": "minecraft:uniform"} |
| cobblestone (`minecraft:cobblestone`) | 1 | 33.33 % | Cantidad: {"min": 1.0, "max": 5.0, "type": "minecraft:uniform"} |

## betterdungeons:small nether dungeon — common

Tabla: `betterdungeons:small_nether_dungeon/chests/common` · fuente: `YungsBetterDungeons-1.20-Forge-4.0.4.jar`.

**Grupo 1** · tiradas: `{"min": 2.0, "max": 6.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| coal (`minecraft:coal`) | 15 | 15.31 % | Cantidad: {"min": 1.0, "max": 4.0, "type": "minecraft:uniform"} |
| rotten flesh (`minecraft:rotten_flesh`) | 10 | 10.20 % | Cantidad: {"min": 1.0, "max": 8.0, "type": "minecraft:uniform"} |
| quartz (`minecraft:quartz`) | 5 | 5.10 % | Cantidad: {"min": 2.0, "max": 7.0, "type": "minecraft:uniform"} |
| iron ingot (`minecraft:iron_ingot`) | 10 | 10.20 % | Cantidad: {"min": 4.0, "max": 8.0, "type": "minecraft:uniform"} |
| gold ingot (`minecraft:gold_ingot`) | 15 | 15.31 % | Cantidad: {"min": 2.0, "max": 7.0, "type": "minecraft:uniform"} |
| redstone (`minecraft:redstone`) | 2 | 2.04 % | Cantidad: {"min": 2.0, "max": 6.0, "type": "minecraft:uniform"} |
| nether wart (`minecraft:nether_wart`) | 5 | 5.10 % | Cantidad: {"min": 1.0, "max": 10.0, "type": "minecraft:uniform"} |
| saddle (`minecraft:saddle`) | 3 | 3.06 % | 1 por resultado; puede variar por funciones de la tabla |
| golden horse armor (`minecraft:golden_horse_armor`) | 1 | 1.02 % | 1 por resultado; puede variar por funciones de la tabla |
| golden sword (`minecraft:golden_sword`) | 3 | 3.06 % | Función: minecraft:enchant_with_levels |
| golden boots (`minecraft:golden_boots`) | 3 | 3.06 % | Función: minecraft:enchant_with_levels |
| golden chestplate (`minecraft:golden_chestplate`) | 3 | 3.06 % | Función: minecraft:enchant_with_levels |
| golden leggings (`minecraft:golden_leggings`) | 3 | 3.06 % | Función: minecraft:enchant_with_levels |
| golden helmet (`minecraft:golden_helmet`) | 3 | 3.06 % | Función: minecraft:enchant_with_levels |
| iron sword (`minecraft:iron_sword`) | 3 | 3.06 % | Función: minecraft:enchant_with_levels |
| chainmail boots (`minecraft:chainmail_boots`) | 3 | 3.06 % | Función: minecraft:enchant_with_levels |
| chainmail chestplate (`minecraft:chainmail_chestplate`) | 3 | 3.06 % | Función: minecraft:enchant_with_levels |
| chainmail leggings (`minecraft:chainmail_leggings`) | 3 | 3.06 % | Función: minecraft:enchant_with_levels |
| chainmail helmet (`minecraft:chainmail_helmet`) | 3 | 3.06 % | Función: minecraft:enchant_with_levels |
| music disc otherside (`minecraft:music_disc_otherside`) | 2 | 2.04 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 2** · tiradas: `{"min": 1.0, "max": 3.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| saddle (`minecraft:saddle`) | 20 | 19.80 % | 1 por resultado; puede variar por funciones de la tabla |
| music disc 13 (`minecraft:music_disc_13`) | 15 | 14.85 % | 1 por resultado; puede variar por funciones de la tabla |
| music disc blocks (`minecraft:music_disc_blocks`) | 15 | 14.85 % | 1 por resultado; puede variar por funciones de la tabla |
| music disc chirp (`minecraft:music_disc_chirp`) | 15 | 14.85 % | 1 por resultado; puede variar por funciones de la tabla |
| music disc pigstep (`minecraft:music_disc_pigstep`) | 4 | 3.96 % | 1 por resultado; puede variar por funciones de la tabla |
| name tag (`minecraft:name_tag`) | 20 | 19.80 % | 1 por resultado; puede variar por funciones de la tabla |
| enchanted golden apple (`minecraft:enchanted_golden_apple`) | 2 | 1.98 % | 1 por resultado; puede variar por funciones de la tabla |
| book (`minecraft:book`) | 10 | 9.90 % | Función: minecraft:enchant_randomly |

**Grupo 3** · tiradas: `{"min": 1.0, "max": 3.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| coal (`minecraft:coal`) | 15 | 22.39 % | Cantidad: {"min": 1.0, "max": 9.0, "type": "minecraft:uniform"} |
| rotten flesh (`minecraft:rotten_flesh`) | 10 | 14.93 % | Cantidad: {"min": 1.0, "max": 5.0, "type": "minecraft:uniform"} |
| quartz (`minecraft:quartz`) | 5 | 7.46 % | Cantidad: {"min": 2.0, "max": 9.0, "type": "minecraft:uniform"} |
| gold nugget (`minecraft:gold_nugget`) | 15 | 22.39 % | Cantidad: {"min": 4.0, "max": 8.0, "type": "minecraft:uniform"} |
| gold ingot (`minecraft:gold_ingot`) | 15 | 22.39 % | Cantidad: {"min": 3.0, "max": 9.0, "type": "minecraft:uniform"} |
| redstone (`minecraft:redstone`) | 2 | 2.99 % | Cantidad: {"min": 2.0, "max": 9.0, "type": "minecraft:uniform"} |
| nether wart (`minecraft:nether_wart`) | 5 | 7.46 % | Cantidad: {"min": 6.0, "max": 10.0, "type": "minecraft:uniform"} |

## betterdungeons:spider dungeon — egg room

Tabla: `betterdungeons:spider_dungeon/chests/egg_room` · fuente: `YungsBetterDungeons-1.20-Forge-4.0.4.jar`.

**Grupo 1** · tiradas: `{"min": 1.0, "max": 2.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| golden apple (`minecraft:golden_apple`) | 5 | 14.29 % | 1 por resultado; puede variar por funciones de la tabla |
| saddle (`minecraft:saddle`) | 5 | 14.29 % | 1 por resultado; puede variar por funciones de la tabla |
| enchanted golden apple (`minecraft:enchanted_golden_apple`) | 1 | 2.86 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond (`minecraft:diamond`) | 1 | 2.86 % | 1 por resultado; puede variar por funciones de la tabla |
| book (`minecraft:book`) | 3 | 8.57 % | Función: minecraft:enchant_randomly |
| book (`minecraft:book`) | 20 | 57.14 % | Función: minecraft:enchant_randomly |

**Grupo 2** · tiradas: `{"min": 3.0, "max": 6.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| potion (`minecraft:potion`) | 2 | 12.50 % | Función: minecraft:set_nbt |
| potion (`minecraft:potion`) | 2 | 12.50 % | Función: minecraft:set_nbt |
| potion (`minecraft:potion`) | 1 | 6.25 % | Función: minecraft:set_nbt |
| potion (`minecraft:potion`) | 1 | 6.25 % | Función: minecraft:set_nbt |
| potion (`minecraft:potion`) | 2 | 12.50 % | Función: minecraft:set_nbt |
| splash potion (`minecraft:splash_potion`) | 2 | 12.50 % | Función: minecraft:set_nbt |
| splash potion (`minecraft:splash_potion`) | 2 | 12.50 % | Función: minecraft:set_nbt |
| splash potion (`minecraft:splash_potion`) | 1 | 6.25 % | Función: minecraft:set_nbt |
| splash potion (`minecraft:splash_potion`) | 1 | 6.25 % | Función: minecraft:set_nbt |
| splash potion (`minecraft:splash_potion`) | 2 | 12.50 % | Función: minecraft:set_nbt |

**Grupo 3** · tiradas: `{"min": 3.0, "max": 4.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| spider eye (`minecraft:spider_eye`) | 3 | 17.65 % | Cantidad: {"min": 2.0, "max": 5.0, "type": "minecraft:uniform"} |
| coal (`minecraft:coal`) | 3 | 17.65 % | Cantidad: {"min": 2.0, "max": 5.0, "type": "minecraft:uniform"} |
| beetroot seeds (`minecraft:beetroot_seeds`) | 3 | 17.65 % | Cantidad: {"min": 2.0, "max": 5.0, "type": "minecraft:uniform"} |
| pumpkin seeds (`minecraft:pumpkin_seeds`) | 3 | 17.65 % | Cantidad: {"min": 2.0, "max": 5.0, "type": "minecraft:uniform"} |
| melon seeds (`minecraft:melon_seeds`) | 3 | 17.65 % | Cantidad: {"min": 2.0, "max": 5.0, "type": "minecraft:uniform"} |
| lead (`minecraft:lead`) | 1 | 5.88 % | 1 por resultado; puede variar por funciones de la tabla |
| name tag (`minecraft:name_tag`) | 1 | 5.88 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 4** · tiradas: `3`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| cobweb (`minecraft:cobweb`) | 10 | 50.00 % | Cantidad: {"min": 3.0, "max": 6.0, "type": "minecraft:uniform"} |
| string (`minecraft:string`) | 10 | 50.00 % | Cantidad: {"min": 3.0, "max": 6.0, "type": "minecraft:uniform"} |

## betterdungeons:zombie dungeon — common

Tabla: `betterdungeons:zombie_dungeon/chests/common` · fuente: `YungsBetterDungeons-1.20-Forge-4.0.4.jar`.

**Grupo 1** · tiradas: `{"min": 0.0, "max": 2.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| golden apple (`minecraft:golden_apple`) | 5 | 9.80 % | 1 por resultado; puede variar por funciones de la tabla |
| saddle (`minecraft:saddle`) | 5 | 9.80 % | 1 por resultado; puede variar por funciones de la tabla |
| name tag (`minecraft:name_tag`) | 5 | 9.80 % | 1 por resultado; puede variar por funciones de la tabla |
| experience bottle (`minecraft:experience_bottle`) | 10 | 19.61 % | 1 por resultado; puede variar por funciones de la tabla |
| enchanted golden apple (`minecraft:enchanted_golden_apple`) | 1 | 1.96 % | 1 por resultado; puede variar por funciones de la tabla |
| book (`minecraft:book`) | 5 | 9.80 % | Función: minecraft:enchant_randomly |
| book (`minecraft:book`) | 20 | 39.22 % | Función: minecraft:enchant_randomly |

**Grupo 2** · tiradas: `{"min": 1.0, "max": 2.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| stone sword (`minecraft:stone_sword`) | 3 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |
| stone axe (`minecraft:stone_axe`) | 3 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |
| stone shovel (`minecraft:stone_shovel`) | 3 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |
| iron sword (`minecraft:iron_sword`) | 2 | 6.67 % | 1 por resultado; puede variar por funciones de la tabla |
| iron axe (`minecraft:iron_axe`) | 2 | 6.67 % | 1 por resultado; puede variar por funciones de la tabla |
| iron shovel (`minecraft:iron_shovel`) | 2 | 6.67 % | 1 por resultado; puede variar por funciones de la tabla |
| iron helmet (`minecraft:iron_helmet`) | 2 | 6.67 % | 1 por resultado; puede variar por funciones de la tabla |
| iron chestplate (`minecraft:iron_chestplate`) | 2 | 6.67 % | 1 por resultado; puede variar por funciones de la tabla |
| iron leggings (`minecraft:iron_leggings`) | 2 | 6.67 % | 1 por resultado; puede variar por funciones de la tabla |
| iron boots (`minecraft:iron_boots`) | 2 | 6.67 % | 1 por resultado; puede variar por funciones de la tabla |
| iron ingot (`minecraft:iron_ingot`) | 2 | 6.67 % | Cantidad: {"min": 3.0, "max": 6.0, "type": "minecraft:uniform"} |
| gold ingot (`minecraft:gold_ingot`) | 2 | 6.67 % | Cantidad: {"min": 3.0, "max": 6.0, "type": "minecraft:uniform"} |
| diamond sword (`minecraft:diamond_sword`) | 1 | 3.33 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond axe (`minecraft:diamond_axe`) | 1 | 3.33 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond shovel (`minecraft:diamond_shovel`) | 1 | 3.33 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 3** · tiradas: `{"min": 3.0, "max": 4.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| apple (`minecraft:apple`) | 3 | 10.00 % | Cantidad: {"min": 1.0, "max": 3.0, "type": "minecraft:uniform"} |
| coal (`minecraft:coal`) | 3 | 10.00 % | Cantidad: {"min": 3.0, "max": 6.0, "type": "minecraft:uniform"} |
| torch (`minecraft:torch`) | 3 | 10.00 % | Cantidad: {"min": 4.0, "max": 6.0, "type": "minecraft:uniform"} |
| beetroot seeds (`minecraft:beetroot_seeds`) | 3 | 10.00 % | Cantidad: {"min": 2.0, "max": 4.0, "type": "minecraft:uniform"} |
| wheat seeds (`minecraft:wheat_seeds`) | 3 | 10.00 % | Cantidad: {"min": 2.0, "max": 4.0, "type": "minecraft:uniform"} |
| cornflower (`minecraft:cornflower`) | 3 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |
| brown mushroom (`minecraft:brown_mushroom`) | 3 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |
| red mushroom (`minecraft:red_mushroom`) | 3 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |
| dead bush (`minecraft:dead_bush`) | 3 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |
| poppy (`minecraft:poppy`) | 3 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 4** · tiradas: `{"min": 1.0, "max": 3.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| rotten flesh (`minecraft:rotten_flesh`) | 10 | 50.00 % | Cantidad: {"min": 1.0, "max": 3.0, "type": "minecraft:uniform"} |
| carrot (`minecraft:carrot`) | 5 | 25.00 % | Cantidad: {"min": 1.0, "max": 2.0, "type": "minecraft:uniform"} |
| potato (`minecraft:potato`) | 5 | 25.00 % | Cantidad: {"min": 1.0, "max": 2.0, "type": "minecraft:uniform"} |

## betterdungeons:zombie dungeon — special

Tabla: `betterdungeons:zombie_dungeon/chests/special` · fuente: `YungsBetterDungeons-1.20-Forge-4.0.4.jar`.

**Grupo 1** · tiradas: `{"min": 0.0, "max": 2.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| golden apple (`minecraft:golden_apple`) | 5 | 9.80 % | 1 por resultado; puede variar por funciones de la tabla |
| saddle (`minecraft:saddle`) | 5 | 9.80 % | 1 por resultado; puede variar por funciones de la tabla |
| name tag (`minecraft:name_tag`) | 5 | 9.80 % | 1 por resultado; puede variar por funciones de la tabla |
| experience bottle (`minecraft:experience_bottle`) | 10 | 19.61 % | 1 por resultado; puede variar por funciones de la tabla |
| enchanted golden apple (`minecraft:enchanted_golden_apple`) | 1 | 1.96 % | 1 por resultado; puede variar por funciones de la tabla |
| book (`minecraft:book`) | 5 | 9.80 % | Función: minecraft:enchant_randomly |
| book (`minecraft:book`) | 20 | 39.22 % | Función: minecraft:enchant_randomly |

**Grupo 2** · tiradas: `{"min": 1.0, "max": 2.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| stone sword (`minecraft:stone_sword`) | 3 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |
| stone axe (`minecraft:stone_axe`) | 3 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |
| stone shovel (`minecraft:stone_shovel`) | 3 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |
| iron sword (`minecraft:iron_sword`) | 2 | 6.67 % | 1 por resultado; puede variar por funciones de la tabla |
| iron axe (`minecraft:iron_axe`) | 2 | 6.67 % | 1 por resultado; puede variar por funciones de la tabla |
| iron shovel (`minecraft:iron_shovel`) | 2 | 6.67 % | 1 por resultado; puede variar por funciones de la tabla |
| iron helmet (`minecraft:iron_helmet`) | 2 | 6.67 % | 1 por resultado; puede variar por funciones de la tabla |
| iron chestplate (`minecraft:iron_chestplate`) | 2 | 6.67 % | 1 por resultado; puede variar por funciones de la tabla |
| iron leggings (`minecraft:iron_leggings`) | 2 | 6.67 % | 1 por resultado; puede variar por funciones de la tabla |
| iron boots (`minecraft:iron_boots`) | 2 | 6.67 % | 1 por resultado; puede variar por funciones de la tabla |
| iron ingot (`minecraft:iron_ingot`) | 2 | 6.67 % | Cantidad: {"min": 3.0, "max": 6.0, "type": "minecraft:uniform"} |
| gold ingot (`minecraft:gold_ingot`) | 2 | 6.67 % | Cantidad: {"min": 3.0, "max": 6.0, "type": "minecraft:uniform"} |
| diamond sword (`minecraft:diamond_sword`) | 1 | 3.33 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond axe (`minecraft:diamond_axe`) | 1 | 3.33 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond shovel (`minecraft:diamond_shovel`) | 1 | 3.33 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 3** · tiradas: `{"min": 3.0, "max": 4.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| apple (`minecraft:apple`) | 3 | 10.00 % | Cantidad: {"min": 1.0, "max": 3.0, "type": "minecraft:uniform"} |
| coal (`minecraft:coal`) | 3 | 10.00 % | Cantidad: {"min": 3.0, "max": 6.0, "type": "minecraft:uniform"} |
| torch (`minecraft:torch`) | 3 | 10.00 % | Cantidad: {"min": 4.0, "max": 6.0, "type": "minecraft:uniform"} |
| beetroot seeds (`minecraft:beetroot_seeds`) | 3 | 10.00 % | Cantidad: {"min": 2.0, "max": 4.0, "type": "minecraft:uniform"} |
| wheat seeds (`minecraft:wheat_seeds`) | 3 | 10.00 % | Cantidad: {"min": 2.0, "max": 4.0, "type": "minecraft:uniform"} |
| cornflower (`minecraft:cornflower`) | 3 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |
| brown mushroom (`minecraft:brown_mushroom`) | 3 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |
| red mushroom (`minecraft:red_mushroom`) | 3 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |
| dead bush (`minecraft:dead_bush`) | 3 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |
| poppy (`minecraft:poppy`) | 3 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 4** · tiradas: `{"min": 1.0, "max": 3.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| rotten flesh (`minecraft:rotten_flesh`) | 10 | 50.00 % | Cantidad: {"min": 1.0, "max": 3.0, "type": "minecraft:uniform"} |
| carrot (`minecraft:carrot`) | 5 | 25.00 % | Cantidad: {"min": 1.0, "max": 2.0, "type": "minecraft:uniform"} |
| potato (`minecraft:potato`) | 5 | 25.00 % | Cantidad: {"min": 1.0, "max": 2.0, "type": "minecraft:uniform"} |

## betterdungeons:zombie dungeon — tombstone

Tabla: `betterdungeons:zombie_dungeon/chests/tombstone` · fuente: `YungsBetterDungeons-1.20-Forge-4.0.4.jar`.

**Grupo 1** · tiradas: `{"min": 4.0, "max": 6.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| bone (`minecraft:bone`) | 10 | 50.00 % | Cantidad: {"min": 3.0, "max": 6.0, "type": "minecraft:uniform"} |
| bone meal (`minecraft:bone_meal`) | 5 | 25.00 % | Cantidad: {"min": 3.0, "max": 6.0, "type": "minecraft:uniform"} |
| emerald (`minecraft:emerald`) | 2 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond (`minecraft:diamond`) | 2 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond sword (`minecraft:diamond_sword`) | 1 | 5.00 % | Función: minecraft:enchant_randomly |

## betterfortresses — beacon

Tabla: `betterfortresses:chests/beacon` · fuente: `YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 2.0, "max": 4.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| arrow (`minecraft:arrow`) | 5 | 50.00 % | Cantidad: {"type": "minecraft:uniform", "min": 4.0, "max": 8.0} |
| fire charge (`minecraft:fire_charge`) | 5 | 50.00 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 3.0} |

**Grupo 2** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| bow (`minecraft:bow`) | 20 | 57.14 % | Función: minecraft:set_damage |
| bow (`minecraft:bow`) | 10 | 28.57 % | Función: minecraft:enchant_with_levels; Función: minecraft:set_damage |
| bow (`minecraft:bow`) | 5 | 14.29 % | Función: minecraft:enchant_with_levels; Función: minecraft:set_damage |

## betterfortresses — extra

Tabla: `betterfortresses:chests/extra` · fuente: `YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 2.0, "max": 5.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| iron nugget (`minecraft:iron_nugget`) | 25 | 7.14 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 4.0} |
| gold nugget (`minecraft:gold_nugget`) | 50 | 14.29 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 4.0} |
| iron ingot (`minecraft:iron_ingot`) | 25 | 7.14 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 4.0} |
| gold ingot (`minecraft:gold_ingot`) | 50 | 14.29 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 4.0} |
| leather (`minecraft:leather`) | 50 | 14.29 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 3.0} |
| string (`minecraft:string`) | 50 | 14.29 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 3.0} |
| glowstone dust (`minecraft:glowstone_dust`) | 50 | 14.29 % | Cantidad: {"type": "minecraft:uniform", "min": 3.0, "max": 6.0} |
| quartz (`minecraft:quartz`) | 50 | 14.29 % | Cantidad: {"type": "minecraft:uniform", "min": 3.0, "max": 6.0} |

## betterfortresses — hall

Tabla: `betterfortresses:chests/hall` · fuente: `YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 2.0, "max": 5.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| iron nugget (`minecraft:iron_nugget`) | 50 | 15.38 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 4.0} |
| gold nugget (`minecraft:gold_nugget`) | 50 | 15.38 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 4.0} |
| iron ingot (`minecraft:iron_ingot`) | 25 | 7.69 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 2.0} |
| gold ingot (`minecraft:gold_ingot`) | 50 | 15.38 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 3.0} |
| leather (`minecraft:leather`) | 50 | 15.38 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 3.0} |
| string (`minecraft:string`) | 50 | 15.38 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 3.0} |
| glowstone dust (`minecraft:glowstone_dust`) | 50 | 15.38 % | Cantidad: {"type": "minecraft:uniform", "min": 3.0, "max": 6.0} |

## betterfortresses — keep

Tabla: `betterfortresses:chests/keep` · fuente: `YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 2.0, "max": 4.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| flint (`minecraft:flint`) | 100 | 12.80 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 3.0} |
| coal (`minecraft:coal`) | 100 | 12.80 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 3.0} |
| string (`minecraft:string`) | 100 | 12.80 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 3.0} |
| gunpowder (`minecraft:gunpowder`) | 100 | 12.80 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 3.0} |
| saddle (`minecraft:saddle`) | 10 | 1.28 % | 1 por resultado; puede variar por funciones de la tabla |
| iron horse armor (`minecraft:iron_horse_armor`) | 10 | 1.28 % | Función: minecraft:set_damage |
| golden horse armor (`minecraft:golden_horse_armor`) | 7 | 0.90 % | Función: minecraft:set_damage |
| diamond horse armor (`minecraft:diamond_horse_armor`) | 4 | 0.51 % | Función: minecraft:set_damage |
| stone sword (`minecraft:stone_sword`) | 20 | 2.56 % | Función: minecraft:set_damage |
| stone sword (`minecraft:stone_sword`) | 20 | 2.56 % | Función: minecraft:enchant_with_levels; Función: minecraft:set_damage |
| iron sword (`minecraft:iron_sword`) | 10 | 1.28 % | Función: minecraft:set_damage |
| iron sword (`minecraft:iron_sword`) | 10 | 1.28 % | Función: minecraft:enchant_with_levels; Función: minecraft:set_damage |
| golden sword (`minecraft:golden_sword`) | 5 | 0.64 % | Función: minecraft:set_damage |
| golden sword (`minecraft:golden_sword`) | 5 | 0.64 % | Función: minecraft:enchant_with_levels; Función: minecraft:set_damage |
| leather helmet (`minecraft:leather_helmet`) | 20 | 2.56 % | Función: minecraft:set_damage |
| leather helmet (`minecraft:leather_helmet`) | 20 | 2.56 % | Función: minecraft:enchant_with_levels; Función: minecraft:set_damage |
| chainmail helmet (`minecraft:chainmail_helmet`) | 10 | 1.28 % | Función: minecraft:set_damage |
| chainmail helmet (`minecraft:chainmail_helmet`) | 10 | 1.28 % | Función: minecraft:enchant_with_levels; Función: minecraft:set_damage |
| golden helmet (`minecraft:golden_helmet`) | 5 | 0.64 % | Función: minecraft:set_damage |
| golden helmet (`minecraft:golden_helmet`) | 5 | 0.64 % | Función: minecraft:enchant_with_levels; Función: minecraft:set_damage |
| leather chestplate (`minecraft:leather_chestplate`) | 20 | 2.56 % | Función: minecraft:set_damage |
| leather chestplate (`minecraft:leather_chestplate`) | 20 | 2.56 % | Función: minecraft:enchant_with_levels; Función: minecraft:set_damage |
| chainmail chestplate (`minecraft:chainmail_chestplate`) | 10 | 1.28 % | Función: minecraft:set_damage |
| chainmail chestplate (`minecraft:chainmail_chestplate`) | 10 | 1.28 % | Función: minecraft:enchant_with_levels; Función: minecraft:set_damage |
| golden chestplate (`minecraft:golden_chestplate`) | 5 | 0.64 % | Función: minecraft:set_damage |
| golden chestplate (`minecraft:golden_chestplate`) | 5 | 0.64 % | Función: minecraft:enchant_with_levels; Función: minecraft:set_damage |
| leather leggings (`minecraft:leather_leggings`) | 20 | 2.56 % | Función: minecraft:set_damage |
| leather leggings (`minecraft:leather_leggings`) | 20 | 2.56 % | Función: minecraft:enchant_with_levels; Función: minecraft:set_damage |
| chainmail leggings (`minecraft:chainmail_leggings`) | 10 | 1.28 % | Función: minecraft:set_damage |
| chainmail leggings (`minecraft:chainmail_leggings`) | 10 | 1.28 % | Función: minecraft:enchant_with_levels; Función: minecraft:set_damage |
| golden leggings (`minecraft:golden_leggings`) | 5 | 0.64 % | Función: minecraft:set_damage |
| golden leggings (`minecraft:golden_leggings`) | 5 | 0.64 % | Función: minecraft:enchant_with_levels; Función: minecraft:set_damage |
| leather boots (`minecraft:leather_boots`) | 20 | 2.56 % | Función: minecraft:set_damage |
| leather boots (`minecraft:leather_boots`) | 20 | 2.56 % | Función: minecraft:enchant_with_levels; Función: minecraft:set_damage |
| chainmail boots (`minecraft:chainmail_boots`) | 10 | 1.28 % | Función: minecraft:set_damage |
| chainmail boots (`minecraft:chainmail_boots`) | 10 | 1.28 % | Función: minecraft:enchant_with_levels; Función: minecraft:set_damage |
| golden boots (`minecraft:golden_boots`) | 5 | 0.64 % | Función: minecraft:set_damage |
| golden boots (`minecraft:golden_boots`) | 5 | 0.64 % | Función: minecraft:enchant_with_levels; Función: minecraft:set_damage |

## betterfortresses — obsidian

Tabla: `betterfortresses:chests/obsidian` · fuente: `YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 1.0, "max": 2.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| obsidian (`minecraft:obsidian`) | 50 | 50.00 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 5.0} |
| crying obsidian (`minecraft:crying_obsidian`) | 50 | 50.00 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 3.0} |

**Grupo 2** · tiradas: `{"type": "minecraft:uniform", "min": 0.0, "max": 1.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| flint and steel (`minecraft:flint_and_steel`) | 10 | 66.67 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond (`minecraft:diamond`) | 5 | 33.33 % | 1 por resultado; puede variar por funciones de la tabla |

## betterfortresses — puzzle

Tabla: `betterfortresses:chests/puzzle` · fuente: `YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 3.0, "max": 6.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| iron nugget (`minecraft:iron_nugget`) | 50 | 16.67 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 5.0} |
| gold nugget (`minecraft:gold_nugget`) | 50 | 16.67 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 5.0} |
| iron ingot (`minecraft:iron_ingot`) | 50 | 16.67 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 5.0} |
| gold ingot (`minecraft:gold_ingot`) | 50 | 16.67 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 5.0} |
| nether wart (`minecraft:nether_wart`) | 50 | 16.67 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 4.0} |
| diamond (`minecraft:diamond`) | 50 | 16.67 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 2.0} |

**Grupo 2** · tiradas: `{"type": "minecraft:constant", "value": 1}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| blaze rod (`minecraft:blaze_rod`) | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

## betterfortresses — quarters

Tabla: `betterfortresses:chests/quarters` · fuente: `YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 3.0, "max": 6.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| iron nugget (`minecraft:iron_nugget`) | 50 | 18.18 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 5.0} |
| gold nugget (`minecraft:gold_nugget`) | 50 | 18.18 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 5.0} |
| iron ingot (`minecraft:iron_ingot`) | 50 | 18.18 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 5.0} |
| gold ingot (`minecraft:gold_ingot`) | 50 | 18.18 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 5.0} |
| nether wart (`minecraft:nether_wart`) | 50 | 18.18 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 4.0} |
| diamond (`minecraft:diamond`) | 25 | 9.09 % | 1 por resultado; puede variar por funciones de la tabla |

## betterfortresses — storage

Tabla: `betterfortresses:chests/storage` · fuente: `YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 1.0, "max": 3.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| iron nugget (`minecraft:iron_nugget`) | 50 | 20.00 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 3.0} |
| gold nugget (`minecraft:gold_nugget`) | 50 | 20.00 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 4.0} |
| gold ingot (`minecraft:gold_ingot`) | 50 | 20.00 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 4.0} |
| raw gold (`minecraft:raw_gold`) | 50 | 20.00 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 3.0} |
| quartz (`minecraft:quartz`) | 50 | 20.00 % | Cantidad: {"type": "minecraft:uniform", "min": 3.0, "max": 8.0} |

**Grupo 2** · tiradas: `{"type": "minecraft:uniform", "min": 1.0, "max": 2.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| magma cream (`minecraft:magma_cream`) | 50 | 33.33 % | 1 por resultado; puede variar por funciones de la tabla |
| fire charge (`minecraft:fire_charge`) | 50 | 33.33 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond (`minecraft:diamond`) | 50 | 33.33 % | 1 por resultado; puede variar por funciones de la tabla |

## betterfortresses — worship

Tabla: `betterfortresses:chests/worship` · fuente: `YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 3.0, "max": 6.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| iron nugget (`minecraft:iron_nugget`) | 50 | 20.00 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 5.0} |
| gold nugget (`minecraft:gold_nugget`) | 50 | 20.00 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 5.0} |
| iron ingot (`minecraft:iron_ingot`) | 50 | 20.00 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 5.0} |
| gold ingot (`minecraft:gold_ingot`) | 50 | 20.00 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 5.0} |
| nether wart (`minecraft:nether_wart`) | 50 | 20.00 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 4.0} |

**Grupo 2** · tiradas: `{"type": "minecraft:uniform", "min": 1.0, "max": 2.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| diamond (`minecraft:diamond`) | 50 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

## betteroceanmonuments — upper side chamber

Tabla: `betteroceanmonuments:chests/upper_side_chamber` · fuente: `YungsBetterOceanMonuments-1.20-Forge-3.0.4.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 8.0, "max": 10.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| nautilus shell (`minecraft:nautilus_shell`) | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 2** · tiradas: `{"type": "minecraft:uniform", "min": 3.0, "max": 6.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| prismarine shard (`minecraft:prismarine_shard`) | 1 | 50.00 % | Cantidad: {"type": "minecraft:uniform", "min": 10.0, "max": 16.0} |
| prismarine crystals (`minecraft:prismarine_crystals`) | 1 | 50.00 % | Cantidad: {"type": "minecraft:uniform", "min": 10.0, "max": 16.0} |

## betterstrongholds — armoury

Tabla: `betterstrongholds:chests/armoury` · fuente: `YungsBetterStrongholds-1.20-Forge-4.0.3.jar`.

**Grupo 1** · tiradas: `{"min": 1.0, "max": 3.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| wooden sword (`minecraft:wooden_sword`) | 5 | 4.76 % | 1 por resultado; puede variar por funciones de la tabla |
| wooden sword (`minecraft:wooden_sword`) | 2 | 1.90 % | Función: minecraft:enchant_with_levels |
| iron sword (`minecraft:iron_sword`) | 5 | 4.76 % | 1 por resultado; puede variar por funciones de la tabla |
| iron sword (`minecraft:iron_sword`) | 1 | 0.95 % | Función: minecraft:enchant_with_levels |
| diamond sword (`minecraft:diamond_sword`) | 1 | 0.95 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond sword (`minecraft:diamond_sword`) | 1 | 0.95 % | Función: minecraft:enchant_with_levels |
| leather helmet (`minecraft:leather_helmet`) | 5 | 4.76 % | 1 por resultado; puede variar por funciones de la tabla |
| leather chestplate (`minecraft:leather_chestplate`) | 5 | 4.76 % | 1 por resultado; puede variar por funciones de la tabla |
| leather leggings (`minecraft:leather_leggings`) | 5 | 4.76 % | 1 por resultado; puede variar por funciones de la tabla |
| leather boots (`minecraft:leather_boots`) | 5 | 4.76 % | 1 por resultado; puede variar por funciones de la tabla |
| chainmail helmet (`minecraft:chainmail_helmet`) | 3 | 2.86 % | 1 por resultado; puede variar por funciones de la tabla |
| chainmail chestplate (`minecraft:chainmail_chestplate`) | 3 | 2.86 % | 1 por resultado; puede variar por funciones de la tabla |
| chainmail leggings (`minecraft:chainmail_leggings`) | 3 | 2.86 % | 1 por resultado; puede variar por funciones de la tabla |
| chainmail boots (`minecraft:chainmail_boots`) | 3 | 2.86 % | 1 por resultado; puede variar por funciones de la tabla |
| iron helmet (`minecraft:iron_helmet`) | 5 | 4.76 % | 1 por resultado; puede variar por funciones de la tabla |
| iron helmet (`minecraft:iron_helmet`) | 1 | 0.95 % | Función: minecraft:enchant_with_levels |
| iron chestplate (`minecraft:iron_chestplate`) | 5 | 4.76 % | 1 por resultado; puede variar por funciones de la tabla |
| iron chestplate (`minecraft:iron_chestplate`) | 1 | 0.95 % | Función: minecraft:enchant_with_levels |
| iron leggings (`minecraft:iron_leggings`) | 5 | 4.76 % | 1 por resultado; puede variar por funciones de la tabla |
| iron leggings (`minecraft:iron_leggings`) | 1 | 0.95 % | Función: minecraft:enchant_with_levels |
| iron boots (`minecraft:iron_boots`) | 5 | 4.76 % | 1 por resultado; puede variar por funciones de la tabla |
| iron boots (`minecraft:iron_boots`) | 1 | 0.95 % | Función: minecraft:enchant_with_levels |
| diamond helmet (`minecraft:diamond_helmet`) | 1 | 0.95 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond helmet (`minecraft:diamond_helmet`) | 1 | 0.95 % | Función: minecraft:enchant_with_levels |
| diamond chestplate (`minecraft:diamond_chestplate`) | 1 | 0.95 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond chestplate (`minecraft:diamond_chestplate`) | 1 | 0.95 % | Función: minecraft:enchant_with_levels |
| diamond leggings (`minecraft:diamond_leggings`) | 1 | 0.95 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond leggings (`minecraft:diamond_leggings`) | 1 | 0.95 % | Función: minecraft:enchant_with_levels |
| diamond boots (`minecraft:diamond_boots`) | 1 | 0.95 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond boots (`minecraft:diamond_boots`) | 1 | 0.95 % | Función: minecraft:enchant_with_levels |
| shield (`minecraft:shield`) | 6 | 5.71 % | 1 por resultado; puede variar por funciones de la tabla |
| bow (`minecraft:bow`) | 5 | 4.76 % | 1 por resultado; puede variar por funciones de la tabla |
| bow (`minecraft:bow`) | 1 | 0.95 % | Función: minecraft:enchant_with_levels |
| coal (`minecraft:coal`) | 7 | 6.67 % | Cantidad: {"min": 2.0, "max": 7.0, "type": "minecraft:uniform"} |
| charcoal (`minecraft:charcoal`) | 7 | 6.67 % | Cantidad: {"min": 2.0, "max": 7.0, "type": "minecraft:uniform"} |

## betterstrongholds — cmd yung

Tabla: `betterstrongholds:chests/cmd_yung` · fuente: `YungsBetterStrongholds-1.20-Forge-4.0.3.jar`.

**Grupo 1** · tiradas: `{"min": 1.0, "max": 1.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| diamond sword (`minecraft:diamond_sword`) | 1 | 100.00 % | Función: minecraft:enchant_with_levels; Función: minecraft:set_name |

## betterstrongholds — common

Tabla: `betterstrongholds:chests/common` · fuente: `YungsBetterStrongholds-1.20-Forge-4.0.3.jar`.

**Grupo 1** · tiradas: `{"min": 2.0, "max": 3.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| iron ingot (`minecraft:iron_ingot`) | 10 | 10.64 % | Cantidad: {"min": 1.0, "max": 5.0, "type": "minecraft:uniform"} |
| gold ingot (`minecraft:gold_ingot`) | 1 | 1.06 % | Cantidad: {"min": 1.0, "max": 3.0, "type": "minecraft:uniform"} |
| redstone (`minecraft:redstone`) | 5 | 5.32 % | Cantidad: {"min": 4.0, "max": 9.0, "type": "minecraft:uniform"} |
| coal (`minecraft:coal`) | 10 | 10.64 % | Cantidad: {"min": 3.0, "max": 8.0, "type": "minecraft:uniform"} |
| bread (`minecraft:bread`) | 15 | 15.96 % | Cantidad: {"min": 1.0, "max": 3.0, "type": "minecraft:uniform"} |
| potato (`minecraft:potato`) | 15 | 15.96 % | Cantidad: {"min": 1.0, "max": 3.0, "type": "minecraft:uniform"} |
| apple (`minecraft:apple`) | 15 | 15.96 % | Cantidad: {"min": 1.0, "max": 3.0, "type": "minecraft:uniform"} |
| stick (`minecraft:stick`) | 5 | 5.32 % | Cantidad: {"min": 2.0, "max": 4.0, "type": "minecraft:uniform"} |
| iron pickaxe (`minecraft:iron_pickaxe`) | 1 | 1.06 % | 1 por resultado; puede variar por funciones de la tabla |
| wooden pickaxe (`minecraft:wooden_pickaxe`) | 1 | 1.06 % | 1 por resultado; puede variar por funciones de la tabla |
| ender pearl (`minecraft:ender_pearl`) | 1 | 1.06 % | 1 por resultado; puede variar por funciones de la tabla |
| iron horse armor (`minecraft:iron_horse_armor`) | 1 | 1.06 % | 1 por resultado; puede variar por funciones de la tabla |
| golden horse armor (`minecraft:golden_horse_armor`) | 1 | 1.06 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond horse armor (`minecraft:diamond_horse_armor`) | 1 | 1.06 % | 1 por resultado; puede variar por funciones de la tabla |
| saddle (`minecraft:saddle`) | 1 | 1.06 % | 1 por resultado; puede variar por funciones de la tabla |
| cobweb (`minecraft:cobweb`) | 5 | 5.32 % | Cantidad: {"min": 3.0, "max": 6.0, "type": "minecraft:uniform"} |
| torch (`minecraft:torch`) | 5 | 5.32 % | Cantidad: {"min": 2.0, "max": 4.0, "type": "minecraft:uniform"} |
| book (`minecraft:book`) | 1 | 1.06 % | Función: minecraft:enchant_with_levels |

## betterstrongholds — crypt

Tabla: `betterstrongholds:chests/crypt` · fuente: `YungsBetterStrongholds-1.20-Forge-4.0.3.jar`.

**Grupo 1** · tiradas: `{"min": 4.0, "max": 6.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| bone (`minecraft:bone`) | 10 | 52.63 % | Cantidad: {"min": 3.0, "max": 6.0, "type": "minecraft:uniform"} |
| bone meal (`minecraft:bone_meal`) | 5 | 26.32 % | Cantidad: {"min": 3.0, "max": 6.0, "type": "minecraft:uniform"} |
| ender pearl (`minecraft:ender_pearl`) | 1 | 5.26 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond (`minecraft:diamond`) | 2 | 10.53 % | 1 por resultado; puede variar por funciones de la tabla |
| iron sword (`minecraft:iron_sword`) | 1 | 5.26 % | 1 por resultado; puede variar por funciones de la tabla |

## betterstrongholds — grand library

Tabla: `betterstrongholds:chests/grand_library` · fuente: `YungsBetterStrongholds-1.20-Forge-4.0.3.jar`.

**Grupo 1** · tiradas: `{"min": 2.0, "max": 10.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| book (`minecraft:book`) | 20 | 39.22 % | Cantidad: {"min": 1.0, "max": 3.0, "type": "minecraft:uniform"} |
| paper (`minecraft:paper`) | 20 | 39.22 % | Cantidad: {"min": 2.0, "max": 7.0, "type": "minecraft:uniform"} |
| map (`minecraft:map`) | 1 | 1.96 % | 1 por resultado; puede variar por funciones de la tabla |
| compass (`minecraft:compass`) | 1 | 1.96 % | 1 por resultado; puede variar por funciones de la tabla |
| book (`minecraft:book`) | 3 | 5.88 % | Función: minecraft:enchant_with_levels |
| book (`minecraft:book`) | 3 | 5.88 % | Función: minecraft:enchant_with_levels |
| book (`minecraft:book`) | 3 | 5.88 % | Función: minecraft:enchant_with_levels |

## betterstrongholds — library md

Tabla: `betterstrongholds:chests/library_md` · fuente: `YungsBetterStrongholds-1.20-Forge-4.0.3.jar`.

**Grupo 1** · tiradas: `{"min": 2.0, "max": 10.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| book (`minecraft:book`) | 10 | 32.26 % | Cantidad: {"min": 1.0, "max": 3.0, "type": "minecraft:uniform"} |
| paper (`minecraft:paper`) | 10 | 32.26 % | Cantidad: {"min": 2.0, "max": 7.0, "type": "minecraft:uniform"} |
| map (`minecraft:map`) | 1 | 3.23 % | 1 por resultado; puede variar por funciones de la tabla |
| compass (`minecraft:compass`) | 1 | 3.23 % | 1 por resultado; puede variar por funciones de la tabla |
| book (`minecraft:book`) | 3 | 9.68 % | Función: minecraft:enchant_with_levels |
| book (`minecraft:book`) | 3 | 9.68 % | Función: minecraft:enchant_with_levels |
| book (`minecraft:book`) | 3 | 9.68 % | Función: minecraft:enchant_with_levels |

## betterstrongholds — mess

Tabla: `betterstrongholds:chests/mess` · fuente: `YungsBetterStrongholds-1.20-Forge-4.0.3.jar`.

**Grupo 1** · tiradas: `{"min": 2.0, "max": 10.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| bread (`minecraft:bread`) | 5 | 17.24 % | Cantidad: {"min": 1.0, "max": 3.0, "type": "minecraft:uniform"} |
| apple (`minecraft:apple`) | 5 | 17.24 % | Cantidad: {"min": 1.0, "max": 3.0, "type": "minecraft:uniform"} |
| potato (`minecraft:potato`) | 5 | 17.24 % | Cantidad: {"min": 1.0, "max": 3.0, "type": "minecraft:uniform"} |
| mushroom stew (`minecraft:mushroom_stew`) | 3 | 10.34 % | Cantidad: {"min": 1.0, "max": 2.0, "type": "minecraft:uniform"} |
| cookie (`minecraft:cookie`) | 3 | 10.34 % | Cantidad: {"min": 3.0, "max": 7.0, "type": "minecraft:uniform"} |
| beetroot (`minecraft:beetroot`) | 3 | 10.34 % | Cantidad: {"min": 3.0, "max": 7.0, "type": "minecraft:uniform"} |
| melon slice (`minecraft:melon_slice`) | 3 | 10.34 % | Cantidad: {"min": 5.0, "max": 7.0, "type": "minecraft:uniform"} |
| golden apple (`minecraft:golden_apple`) | 2 | 6.90 % | 1 por resultado; puede variar por funciones de la tabla |

## betterstrongholds — prison lg

Tabla: `betterstrongholds:chests/prison_lg` · fuente: `YungsBetterStrongholds-1.20-Forge-4.0.3.jar`.

**Grupo 1** · tiradas: `{"min": 2.0, "max": 6.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| iron bars (`minecraft:iron_bars`) | 5 | 22.73 % | Cantidad: {"min": 2.0, "max": 3.0, "type": "minecraft:uniform"} |
| coal (`minecraft:coal`) | 5 | 22.73 % | Cantidad: {"min": 2.0, "max": 7.0, "type": "minecraft:uniform"} |
| rotten flesh (`minecraft:rotten_flesh`) | 5 | 22.73 % | Cantidad: {"min": 2.0, "max": 7.0, "type": "minecraft:uniform"} |
| chain (`minecraft:chain`) | 5 | 22.73 % | Cantidad: {"min": 2.0, "max": 4.0, "type": "minecraft:uniform"} |
| diamond (`minecraft:diamond`) | 1 | 4.55 % | 1 por resultado; puede variar por funciones de la tabla |
| emerald (`minecraft:emerald`) | 1 | 4.55 % | 1 por resultado; puede variar por funciones de la tabla |

## betterstrongholds — trap

Tabla: `betterstrongholds:chests/trap` · fuente: `YungsBetterStrongholds-1.20-Forge-4.0.3.jar`.

**Grupo 1** · tiradas: `{"min": 4.0, "max": 5.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| iron ingot (`minecraft:iron_ingot`) | 1 | 14.29 % | Cantidad: {"min": 4.0, "max": 6.0, "type": "minecraft:uniform"} |
| gold ingot (`minecraft:gold_ingot`) | 1 | 14.29 % | Cantidad: {"min": 4.0, "max": 6.0, "type": "minecraft:uniform"} |
| diamond (`minecraft:diamond`) | 1 | 14.29 % | Cantidad: {"min": 1.0, "max": 2.0, "type": "minecraft:uniform"} |
| emerald (`minecraft:emerald`) | 1 | 14.29 % | Cantidad: {"min": 1.0, "max": 2.0, "type": "minecraft:uniform"} |
| bone (`minecraft:bone`) | 1 | 14.29 % | Cantidad: {"min": 5.0, "max": 7.0, "type": "minecraft:uniform"} |
| golden apple (`minecraft:golden_apple`) | 1 | 14.29 % | 1 por resultado; puede variar por funciones de la tabla |
| ender pearl (`minecraft:ender_pearl`) | 1 | 14.29 % | 1 por resultado; puede variar por funciones de la tabla |

## betterstrongholds — treasure

Tabla: `betterstrongholds:chests/treasure` · fuente: `YungsBetterStrongholds-1.20-Forge-4.0.3.jar`.

**Grupo 1** · tiradas: `{"min": 1.0, "max": 2.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| iron ingot (`minecraft:iron_ingot`) | 3 | 15.00 % | Cantidad: {"min": 2.0, "max": 3.0, "type": "minecraft:uniform"} |
| iron nugget (`minecraft:iron_nugget`) | 3 | 15.00 % | Cantidad: {"min": 2.0, "max": 7.0, "type": "minecraft:uniform"} |
| gold ingot (`minecraft:gold_ingot`) | 3 | 15.00 % | Cantidad: {"min": 2.0, "max": 3.0, "type": "minecraft:uniform"} |
| gold nugget (`minecraft:gold_nugget`) | 3 | 15.00 % | Cantidad: {"min": 2.0, "max": 7.0, "type": "minecraft:uniform"} |
| diamond (`minecraft:diamond`) | 1 | 5.00 % | Cantidad: {"min": 1.0, "max": 3.0, "type": "minecraft:uniform"} |
| emerald (`minecraft:emerald`) | 1 | 5.00 % | Cantidad: {"min": 1.0, "max": 2.0, "type": "minecraft:uniform"} |
| redstone (`minecraft:redstone`) | 3 | 15.00 % | Cantidad: {"min": 3.0, "max": 6.0, "type": "minecraft:uniform"} |
| lapis lazuli (`minecraft:lapis_lazuli`) | 3 | 15.00 % | Cantidad: {"min": 3.0, "max": 6.0, "type": "minecraft:uniform"} |

## betterwitchhuts — hut 0

Tabla: `betterwitchhuts:chests/hut_0` · fuente: `YungsBetterWitchHuts-1.20-Forge-3.0.3.jar`.

**Grupo 1** · tiradas: `{"min": 3.0, "max": 5.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| sugar (`minecraft:sugar`) | 10 | 14.08 % | Cantidad: {"min": 1.0, "max": 3.0, "type": "minecraft:uniform"} |
| gunpowder (`minecraft:gunpowder`) | 10 | 14.08 % | Cantidad: {"min": 2.0, "max": 5.0, "type": "minecraft:uniform"} |
| carrot (`minecraft:carrot`) | 10 | 14.08 % | Cantidad: {"min": 3.0, "max": 6.0, "type": "minecraft:uniform"} |
| rabbit foot (`minecraft:rabbit_foot`) | 1 | 1.41 % | 1 por resultado; puede variar por funciones de la tabla |
| pufferfish (`minecraft:pufferfish`) | 5 | 7.04 % | 1 por resultado; puede variar por funciones de la tabla |
| phantom membrane (`minecraft:phantom_membrane`) | 5 | 7.04 % | 1 por resultado; puede variar por funciones de la tabla |
| redstone (`minecraft:redstone`) | 10 | 14.08 % | Cantidad: {"min": 4.0, "max": 7.0, "type": "minecraft:uniform"} |
| spider eye (`minecraft:spider_eye`) | 10 | 14.08 % | Cantidad: {"min": 1.0, "max": 3.0, "type": "minecraft:uniform"} |
| slime ball (`minecraft:slime_ball`) | 10 | 14.08 % | Cantidad: {"min": 4.0, "max": 8.0, "type": "minecraft:uniform"} |

**Grupo 2** · tiradas: `{"min": 2.0, "max": 4.0, "type": "minecraft:uniform"}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| potion (`minecraft:potion`) | 10 | 14.29 % | Función: minecraft:set_nbt |
| potion (`minecraft:potion`) | 10 | 14.29 % | Función: minecraft:set_nbt |
| potion (`minecraft:potion`) | 10 | 14.29 % | Función: minecraft:set_nbt |
| potion (`minecraft:potion`) | 10 | 14.29 % | Función: minecraft:set_nbt |
| splash potion (`minecraft:splash_potion`) | 10 | 14.29 % | Función: minecraft:set_nbt |
| splash potion (`minecraft:splash_potion`) | 10 | 14.29 % | Función: minecraft:set_nbt |
| splash potion (`minecraft:splash_potion`) | 10 | 14.29 % | Función: minecraft:set_nbt |

## cataclysm — abandoned

Tabla: `cataclysm:chests/abandoned` · fuente: `L_Enders_Cataclysm-3.31.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 6.0, "min": 2.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Botas robustas (`cataclysm:sturdy_boots`) | 2 | 2.94 % | 1 por resultado; puede variar por funciones de la tabla |
| leather (`minecraft:leather`) | 12 | 17.65 % | Cantidad: {"type": "minecraft:uniform", "max": 7.0, "min": 4.0} |
| iron ingot (`minecraft:iron_ingot`) | 10 | 14.71 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 2.0} |
| Lingote de acero negro (`cataclysm:black_steel_ingot`) | 7 | 10.29 % | Cantidad: {"type": "minecraft:uniform", "max": 2.0, "min": 1.0} |
| gold ingot (`minecraft:gold_ingot`) | 7 | 10.29 % | Cantidad: {"type": "minecraft:uniform", "max": 2.0, "min": 1.0} |
| emerald (`minecraft:emerald`) | 3 | 4.41 % | 1 por resultado; puede variar por funciones de la tabla |
| saddle (`minecraft:saddle`) | 3 | 4.41 % | 1 por resultado; puede variar por funciones de la tabla |
| iron horse armor (`minecraft:iron_horse_armor`) | 1 | 1.47 % | 1 por resultado; puede variar por funciones de la tabla |
| golden horse armor (`minecraft:golden_horse_armor`) | 1 | 1.47 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond horse armor (`minecraft:diamond_horse_armor`) | 1 | 1.47 % | 1 por resultado; puede variar por funciones de la tabla |
| iron sword (`minecraft:iron_sword`) | 3 | 4.41 % | Función: minecraft:enchant_with_levels |
| iron boots (`minecraft:iron_boots`) | 3 | 4.41 % | Función: minecraft:enchant_with_levels |
| iron chestplate (`minecraft:iron_chestplate`) | 3 | 4.41 % | Función: minecraft:enchant_with_levels |
| iron leggings (`minecraft:iron_leggings`) | 3 | 4.41 % | Función: minecraft:enchant_with_levels |
| iron helmet (`minecraft:iron_helmet`) | 3 | 4.41 % | Función: minecraft:enchant_with_levels |
| iron pickaxe (`minecraft:iron_pickaxe`) | 3 | 4.41 % | Función: minecraft:enchant_with_levels |
| iron shovel (`minecraft:iron_shovel`) | 3 | 4.41 % | Función: minecraft:enchant_with_levels |

## cataclysm — abandoned treasure

Tabla: `cataclysm:chests/abandoned_treasure` · fuente: `L_Enders_Cataclysm-3.31.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 6.0, "min": 2.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Botas robustas (`cataclysm:sturdy_boots`) | 4 | 5.06 % | 1 por resultado; puede variar por funciones de la tabla |
| leather (`minecraft:leather`) | 12 | 15.19 % | Cantidad: {"type": "minecraft:uniform", "max": 7.0, "min": 4.0} |
| iron ingot (`minecraft:iron_ingot`) | 10 | 12.66 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 2.0} |
| Lingote de acero negro (`cataclysm:black_steel_ingot`) | 7 | 8.86 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 2.0} |
| gold ingot (`minecraft:gold_ingot`) | 7 | 8.86 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 2.0} |
| emerald (`minecraft:emerald`) | 4 | 5.06 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| diamond (`minecraft:diamond`) | 2 | 2.53 % | 1 por resultado; puede variar por funciones de la tabla |
| saddle (`minecraft:saddle`) | 3 | 3.80 % | 1 por resultado; puede variar por funciones de la tabla |
| iron horse armor (`minecraft:iron_horse_armor`) | 1 | 1.27 % | 1 por resultado; puede variar por funciones de la tabla |
| golden horse armor (`minecraft:golden_horse_armor`) | 1 | 1.27 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond horse armor (`minecraft:diamond_horse_armor`) | 1 | 1.27 % | 1 por resultado; puede variar por funciones de la tabla |
| iron sword (`minecraft:iron_sword`) | 3 | 3.80 % | Función: minecraft:enchant_with_levels |
| iron boots (`minecraft:iron_boots`) | 3 | 3.80 % | Función: minecraft:enchant_with_levels |
| iron chestplate (`minecraft:iron_chestplate`) | 3 | 3.80 % | Función: minecraft:enchant_with_levels |
| iron leggings (`minecraft:iron_leggings`) | 3 | 3.80 % | Función: minecraft:enchant_with_levels |
| iron helmet (`minecraft:iron_helmet`) | 3 | 3.80 % | Función: minecraft:enchant_with_levels |
| iron pickaxe (`minecraft:iron_pickaxe`) | 3 | 3.80 % | Función: minecraft:enchant_with_levels |
| Espada de acero negro (`cataclysm:black_steel_sword`) | 3 | 3.80 % | Función: minecraft:enchant_with_levels |
| Hacha de acero negro (`cataclysm:black_steel_axe`) | 3 | 3.80 % | Función: minecraft:enchant_with_levels |
| Pala de acero negro (`cataclysm:black_steel_shovel`) | 3 | 3.80 % | Función: minecraft:enchant_with_levels |

**Grupo 2** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Anillo de los rencorosos (`cataclysm:ring_of_grudged`) | 1 | 25.00 % | 1 por resultado; puede variar por funciones de la tabla |
| Amuleto del alma berserker (`cataclysm:berserker_soul_amulet`) | 1 | 25.00 % | 1 por resultado; puede variar por funciones de la tabla |
| Nada | 2 | 50.00 % | 1 por resultado; puede variar por funciones de la tabla |

## cataclysm — acropolis treasure

Tabla: `cataclysm:chests/acropolis_treasure` · fuente: `L_Enders_Cataclysm-3.31.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 6.0, "min": 2.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| diamond (`minecraft:diamond`) | 5 | 4.03 % | Cantidad: {"type": "minecraft:uniform", "max": 9.0, "min": 4.0} |
| copper ingot (`minecraft:copper_ingot`) | 10 | 8.06 % | Cantidad: {"type": "minecraft:uniform", "max": 8.0, "min": 4.0} |
| Lácrima (`cataclysm:lacrima`) | 6 | 4.84 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 3.0} |
| book (`minecraft:book`) | 20 | 16.13 % | Función: minecraft:enchant_with_levels |
| golden apple (`minecraft:golden_apple`) | 20 | 16.13 % | 1 por resultado; puede variar por funciones de la tabla |
| enchanted golden apple (`minecraft:enchanted_golden_apple`) | 1 | 0.81 % | 1 por resultado; puede variar por funciones de la tabla |
| gold ingot (`minecraft:gold_ingot`) | 15 | 12.10 % | Cantidad: {"type": "minecraft:uniform", "max": 7.0, "min": 2.0} |
| emerald (`minecraft:emerald`) | 5 | 4.03 % | Cantidad: {"type": "minecraft:uniform", "max": 9.0, "min": 4.0} |
| nautilus shell (`minecraft:nautilus_shell`) | 7 | 5.65 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 2.0} |
| scute (`minecraft:scute`) | 12 | 9.68 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 2.0} |
| diamond sword (`minecraft:diamond_sword`) | 2 | 1.61 % | Función: minecraft:enchant_with_levels |
| diamond boots (`minecraft:diamond_boots`) | 2 | 1.61 % | Función: minecraft:enchant_with_levels |
| diamond chestplate (`minecraft:diamond_chestplate`) | 2 | 1.61 % | Función: minecraft:enchant_with_levels |
| diamond leggings (`minecraft:diamond_leggings`) | 2 | 1.61 % | Función: minecraft:enchant_with_levels |
| diamond helmet (`minecraft:diamond_helmet`) | 2 | 1.61 % | Función: minecraft:enchant_with_levels |
| diamond pickaxe (`minecraft:diamond_pickaxe`) | 2 | 1.61 % | Función: minecraft:enchant_with_levels |
| diamond shovel (`minecraft:diamond_shovel`) | 2 | 1.61 % | Función: minecraft:enchant_with_levels |
| golden sword (`minecraft:golden_sword`) | 3 | 2.42 % | Función: minecraft:enchant_with_levels |
| trident (`minecraft:trident`) | 3 | 2.42 % | Función: minecraft:enchant_with_levels |
| golden shovel (`minecraft:golden_shovel`) | 3 | 2.42 % | Función: minecraft:enchant_with_levels |

## cataclysm — amethyst nest chest

Tabla: `cataclysm:chests/amethyst_nest_chest` · fuente: `L_Enders_Cataclysm-3.31.jar`.

**Grupo 1** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| golden apple (`minecraft:golden_apple`) | 20 | 35.71 % | 1 por resultado; puede variar por funciones de la tabla |
| enchanted golden apple (`minecraft:enchanted_golden_apple`) | 1 | 1.79 % | 1 por resultado; puede variar por funciones de la tabla |
| name tag (`minecraft:name_tag`) | 30 | 53.57 % | 1 por resultado; puede variar por funciones de la tabla |
| Nada | 5 | 8.93 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 2** · tiradas: `{"type": "minecraft:uniform", "max": 4.0, "min": 2.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Amethyst Crab Meat (`cataclysm:amethyst_crab_meat`) | 10 | 10.20 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 1.0} |
| Amethyst Crab Shell (`cataclysm:amethyst_crab_shell`) | 5 | 5.10 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| redstone (`minecraft:redstone`) | 5 | 5.10 % | Cantidad: {"type": "minecraft:uniform", "max": 9.0, "min": 4.0} |
| lapis lazuli (`minecraft:lapis_lazuli`) | 5 | 5.10 % | Cantidad: {"type": "minecraft:uniform", "max": 9.0, "min": 4.0} |
| diamond (`minecraft:diamond`) | 3 | 3.06 % | Cantidad: {"type": "minecraft:uniform", "max": 2.0, "min": 1.0} |
| coal (`minecraft:coal`) | 10 | 10.20 % | Cantidad: {"type": "minecraft:uniform", "max": 8.0, "min": 3.0} |
| bread (`minecraft:bread`) | 15 | 15.31 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| glow berries (`minecraft:glow_berries`) | 15 | 15.31 % | Cantidad: {"type": "minecraft:uniform", "max": 6.0, "min": 3.0} |
| melon seeds (`minecraft:melon_seeds`) | 10 | 10.20 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 2.0} |
| pumpkin seeds (`minecraft:pumpkin_seeds`) | 10 | 10.20 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 2.0} |
| beetroot seeds (`minecraft:beetroot_seeds`) | 10 | 10.20 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 2.0} |

**Grupo 3** · tiradas: `3.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| amethyst shard (`minecraft:amethyst_shard`) | 15 | 100.00 % | Cantidad: {"type": "minecraft:uniform", "max": 16.0, "min": 1.0} |

## cataclysm — desert treasure

Tabla: `cataclysm:chests/desert_treasure` · fuente: `L_Enders_Cataclysm-3.31.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 4.0, "min": 2.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| diamond (`minecraft:diamond`) | 4 | 2.92 % | 1 por resultado; puede variar por funciones de la tabla |
| iron ingot (`minecraft:iron_ingot`) | 15 | 10.95 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 1.0} |
| Lingote de metal antiguo (`cataclysm:ancient_metal_ingot`) | 15 | 10.95 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 2.0} |
| emerald (`minecraft:emerald`) | 15 | 10.95 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| iron horse armor (`minecraft:iron_horse_armor`) | 15 | 10.95 % | 1 por resultado; puede variar por funciones de la tabla |
| golden horse armor (`minecraft:golden_horse_armor`) | 10 | 7.30 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond horse armor (`minecraft:diamond_horse_armor`) | 5 | 3.65 % | 1 por resultado; puede variar por funciones de la tabla |
| book (`minecraft:book`) | 20 | 14.60 % | Función: minecraft:enchant_randomly |
| golden apple (`minecraft:golden_apple`) | 20 | 14.60 % | 1 por resultado; puede variar por funciones de la tabla |
| enchanted golden apple (`minecraft:enchanted_golden_apple`) | 3 | 2.19 % | 1 por resultado; puede variar por funciones de la tabla |
| Nada | 15 | 10.95 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 2** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 6 | 85.71 % | 1 por resultado; puede variar por funciones de la tabla |
| dune armor trim smithing template (`minecraft:dune_armor_trim_smithing_template`) | 1 | 14.29 % | Cantidad: 2.0 |

**Grupo 3** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Cráneo irrompible (`cataclysm:unbreakable_skull`) | 1 | 25.00 % | 1 por resultado; puede variar por funciones de la tabla |
| Ankh de la vitalidad (`cataclysm:vitality_ankh`) | 1 | 25.00 % | 1 por resultado; puede variar por funciones de la tabla |
| Nada | 2 | 50.00 % | 1 por resultado; puede variar por funciones de la tabla |

## cataclysm — frosted prison treasure

Tabla: `cataclysm:chests/frosted_prison_treasure` · fuente: `L_Enders_Cataclysm-3.31.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 6.0, "min": 2.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| diamond (`minecraft:diamond`) | 5 | 6.41 % | Cantidad: {"type": "minecraft:uniform", "max": 9.0, "min": 4.0} |
| iron ingot (`minecraft:iron_ingot`) | 10 | 12.82 % | Cantidad: {"type": "minecraft:uniform", "max": 8.0, "min": 4.0} |
| Lingote de acero negro (`cataclysm:black_steel_ingot`) | 10 | 12.82 % | Cantidad: {"type": "minecraft:uniform", "max": 9.0, "min": 5.0} |
| gold ingot (`minecraft:gold_ingot`) | 15 | 19.23 % | Cantidad: {"type": "minecraft:uniform", "max": 7.0, "min": 2.0} |
| emerald (`minecraft:emerald`) | 2 | 2.56 % | Cantidad: {"type": "minecraft:uniform", "max": 9.0, "min": 4.0} |
| saddle (`minecraft:saddle`) | 3 | 3.85 % | 1 por resultado; puede variar por funciones de la tabla |
| iron horse armor (`minecraft:iron_horse_armor`) | 1 | 1.28 % | 1 por resultado; puede variar por funciones de la tabla |
| golden horse armor (`minecraft:golden_horse_armor`) | 1 | 1.28 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond horse armor (`minecraft:diamond_horse_armor`) | 1 | 1.28 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond sword (`minecraft:diamond_sword`) | 3 | 3.85 % | Función: minecraft:enchant_with_levels |
| diamond boots (`minecraft:diamond_boots`) | 3 | 3.85 % | Función: minecraft:enchant_with_levels |
| diamond chestplate (`minecraft:diamond_chestplate`) | 3 | 3.85 % | Función: minecraft:enchant_with_levels |
| diamond leggings (`minecraft:diamond_leggings`) | 3 | 3.85 % | Función: minecraft:enchant_with_levels |
| diamond helmet (`minecraft:diamond_helmet`) | 3 | 3.85 % | Función: minecraft:enchant_with_levels |
| diamond pickaxe (`minecraft:diamond_pickaxe`) | 3 | 3.85 % | Función: minecraft:enchant_with_levels |
| diamond shovel (`minecraft:diamond_shovel`) | 3 | 3.85 % | Función: minecraft:enchant_with_levels |
| Espada de acero negro (`cataclysm:black_steel_sword`) | 3 | 3.85 % | Función: minecraft:enchant_with_levels |
| Hacha de acero negro (`cataclysm:black_steel_axe`) | 3 | 3.85 % | Función: minecraft:enchant_with_levels |
| iron shovel (`minecraft:iron_shovel`) | 3 | 3.85 % | Función: minecraft:enchant_with_levels |

## irons spellbooks — additional ancient city loot

Tabla: `irons_spellbooks:chests/additional_ancient_city_loot` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 1 | 100.00 % | Cantidad: {"min": 1, "max": 7} |

**Grupo 2** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/basic_curios` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.15}]`.

**Grupo 3** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | Condicionada; sin cifra única | Función: irons_spellbooks:randomize_spell |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.7}]`.

**Grupo 4** · tiradas: `{"min": 1, "max": 3}` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/good_ink` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.35}]`.

**Grupo 5** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Libro Arruinado (`irons_spellbooks:ruined_book`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.1}]`.

**Grupo 6** · tiradas: `3`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Fragmento de Conocimiento Antiguo (`irons_spellbooks:ancient_knowledge_fragment`) | 1 | Condicionada; sin cifra única | Condiciones: [{"condition": "minecraft:random_chance", "chance": 0.25}] |

**Grupo 7** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Piedra Rúnica en blanco (`irons_spellbooks:blank_rune`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.25}]`.

## irons spellbooks — additional end city loot

Tabla: `irons_spellbooks:chests/additional_end_city_loot` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 1 | 100.00 % | Cantidad: {"min": 0, "max": 15} |

**Grupo 2** · tiradas: `{"min": 0, "max": 2}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | 50.00 % | Función: irons_spellbooks:randomize_spell |
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | 50.00 % | Función: irons_spellbooks:randomize_spell |

**Grupo 3** · tiradas: `{"min": 0, "max": 2}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/random_elixir` | 8 | 66.67 % | 1 por resultado; puede variar por funciones de la tabla |
| potion (`minecraft:potion`) | 1 | 8.33 % | Función: minecraft:set_potion |
| potion (`minecraft:potion`) | 1 | 8.33 % | Función: minecraft:set_potion |
| potion (`minecraft:potion`) | 1 | 8.33 % | Función: minecraft:set_potion |
| potion (`minecraft:potion`) | 1 | 8.33 % | Función: minecraft:set_potion |

**Grupo 4** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Piedra Rúnica en blanco (`irons_spellbooks:blank_rune`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.3}]`.

**Grupo 5** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/basic_curios` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.5}]`.

**Grupo 6** · tiradas: `3`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/good_ink` | 1 | 50.00 % | 1 por resultado; puede variar por funciones de la tabla |
| Nada | 1 | 50.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 7** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Fragmento de Conocimiento Antiguo (`irons_spellbooks:ancient_knowledge_fragment`) | 1 | Condicionada; sin cifra única | Cantidad: {"min": 0, "max": 3} |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.2}]`.

## irons spellbooks — additional generic loot

Tabla: `irons_spellbooks:chests/additional_generic_loot` · fuente: `TheOptimizer_AdventureLoot.zip`.

Hay varias versiones de esta tabla; se ha priorizado el datapack del mundo y después el datapack global. Confirma el orden de carga si el mundo usa otros datapacks.

**Grupo 1** · tiradas: `{"min": 1, "max": 3}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 1 | 100.00 % | Cantidad: {"min": 1, "max": 3} |

**Grupo 2** · tiradas: `2`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 2 | 66.67 % | Función: irons_spellbooks:randomize_spell |
| Nada | 1 | 33.33 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 3** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Piedra Rúnica en blanco (`irons_spellbooks:blank_rune`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.45}]`.

**Grupo 4** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/basic_curios` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.25}]`.

**Grupo 5** · tiradas: `{"min": 1, "max": 3}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/decent_ink` | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

## irons spellbooks — additional good loot

Tabla: `irons_spellbooks:chests/additional_good_loot` · fuente: `TheOptimizer_AdventureLoot.zip`.

Hay varias versiones de esta tabla; se ha priorizado el datapack del mundo y después el datapack global. Confirma el orden de carga si el mundo usa otros datapacks.

**Grupo 1** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 1 | 100.00 % | Cantidad: {"min": 2, "max": 5} |

**Grupo 2** · tiradas: `2`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 3 | 75.00 % | Función: irons_spellbooks:randomize_spell |
| Nada | 1 | 25.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 3** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Libro de Hechizos Putrefacto (`irons_spellbooks:rotten_spell_book`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.35}]`.

**Grupo 4** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Piedra Rúnica en blanco (`irons_spellbooks:blank_rune`) | 1 | Condicionada; sin cifra única | Cantidad: {"min": 1, "max": 2} |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.75}]`.

**Grupo 5** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/basic_curios` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.4}]`.

**Grupo 6** · tiradas: `{"min": 2, "max": 4}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/good_ink` | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

## irons spellbooks — additional library loot

Tabla: `irons_spellbooks:chests/additional_library_loot` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 1 | Condicionada; sin cifra única | Cantidad: {"min": 2, "max": 15} |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.3}]`.

**Grupo 2** · tiradas: `{"min": 3, "max": 5}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | 50.00 % | Función: irons_spellbooks:randomize_spell |
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | 50.00 % | Función: irons_spellbooks:randomize_spell |

**Grupo 3** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Piedra Rúnica en blanco (`irons_spellbooks:blank_rune`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.3}]`.

**Grupo 4** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/basic_curios` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.5}]`.

**Grupo 5** · tiradas: `5`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/good_ink` | 1 | 50.00 % | 1 por resultado; puede variar por funciones de la tabla |
| Nada | 1 | 50.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 6** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Fragmento de Conocimiento Antiguo (`irons_spellbooks:ancient_knowledge_fragment`) | 1 | Condicionada; sin cifra única | Cantidad: {"min": 1, "max": 3} |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.8}]`.

## irons spellbooks — additional nether loot

Tabla: `irons_spellbooks:chests/additional_nether_loot` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 1 | Condicionada; sin cifra única | Cantidad: {"min": 1, "max": 7} |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.75}]`.

**Grupo 2** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/basic_curios` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.075}]`.

**Grupo 3** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | Condicionada; sin cifra única | Función: irons_spellbooks:randomize_spell |
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | Condicionada; sin cifra única | Función: irons_spellbooks:randomize_spell |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.6}]`.

**Grupo 4** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Piedra Rúnica en blanco (`irons_spellbooks:blank_rune`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.15}]`.

## irons spellbooks — additional treasure loot

Tabla: `irons_spellbooks:chests/additional_treasure_loot` · fuente: `TheOptimizer_AdventureLoot.zip`.

Hay varias versiones de esta tabla; se ha priorizado el datapack del mundo y después el datapack global. Confirma el orden de carga si el mundo usa otros datapacks.

**Grupo 1** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 1 | 100.00 % | Cantidad: {"min": 4, "max": 8} |

**Grupo 2** · tiradas: `{"min": 2, "max": 3}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 4 | 80.00 % | Función: irons_spellbooks:randomize_spell |
| Nada | 1 | 20.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 3** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Piedra Rúnica en blanco (`irons_spellbooks:blank_rune`) | 1 | 100.00 % | Cantidad: {"min": 2, "max": 3} |

**Grupo 4** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/basic_curios` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.6}]`.

**Grupo 5** · tiradas: `{"min": 2, "max": 4}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/great_ink` | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 6** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Fragmento de Conocimiento Antiguo (`irons_spellbooks:ancient_knowledge_fragment`) | 1 | Condicionada; sin cifra única | Cantidad: {"min": 1, "max": 2} |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.75}]`.

## irons spellbooks — battleground/burial loot

Tabla: `irons_spellbooks:chests/battleground/burial_loot` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `2`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| bone (`minecraft:bone`) | 5 | 17.86 % | 1 por resultado; puede variar por funciones de la tabla |
| cobweb (`minecraft:cobweb`) | 5 | 17.86 % | 1 por resultado; puede variar por funciones de la tabla |
| flint (`minecraft:flint`) | 5 | 17.86 % | Cantidad: {"min": 1, "max": 3} |
| nether brick (`minecraft:nether_brick`) | 4 | 14.29 % | Cantidad: {"min": 4, "max": 9} |
| gunpowder (`minecraft:gunpowder`) | 6 | 21.43 % | Cantidad: {"min": 3, "max": 5} |
| wither rose (`minecraft:wither_rose`) | 3 | 10.71 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 2** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia de Ceniza (`irons_spellbooks:cinder_essence`) | 1 | 100.00 % | Cantidad: {"min": 0, "max": 1} |

**Grupo 3** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| wither skeleton skull (`minecraft:wither_skeleton_skull`) | 1 | 5.56 % | 1 por resultado; puede variar por funciones de la tabla |
| potion (`minecraft:potion`) | 2 | 11.11 % | Función: minecraft:set_potion |
| potion (`minecraft:potion`) | 1 | 5.56 % | Función: minecraft:set_potion |
| netherite scrap (`minecraft:netherite_scrap`) | 1 | 5.56 % | 1 por resultado; puede variar por funciones de la tabla |
| Piedra Rúnica en blanco (`irons_spellbooks:blank_rune`) | 3 | 16.67 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond (`minecraft:diamond`) | 5 | 27.78 % | Cantidad: {"min": 1, "max": 2} |
| copper ingot (`minecraft:copper_ingot`) | 5 | 27.78 % | Cantidad: {"min": 3, "max": 12} |

**Grupo 4** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| diamond sword (`minecraft:diamond_sword`) | 1 | 4.76 % | Función: irons_spellbooks:randomize_spell; Función: minecraft:enchant_with_levels |
| iron sword (`minecraft:iron_sword`) | 1 | 4.76 % | Función: irons_spellbooks:randomize_spell; Función: minecraft:enchant_with_levels |
| netherite sword (`minecraft:netherite_sword`) | 1 | 4.76 % | Función: irons_spellbooks:randomize_spell; Función: minecraft:enchant_with_levels |
| diamond helmet (`minecraft:diamond_helmet`) | 1 | 4.76 % | Función: minecraft:enchant_with_levels |
| diamond chestplate (`minecraft:diamond_chestplate`) | 1 | 4.76 % | Función: minecraft:enchant_with_levels |
| diamond leggings (`minecraft:diamond_leggings`) | 1 | 4.76 % | Función: minecraft:enchant_with_levels |
| diamond boots (`minecraft:diamond_boots`) | 1 | 4.76 % | Función: minecraft:enchant_with_levels |
| Nada | 14 | 66.67 % | 1 por resultado; puede variar por funciones de la tabla |

## irons spellbooks — battleground/piglin camp

Tabla: `irons_spellbooks:chests/battleground/piglin_camp` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `3`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| porkchop (`minecraft:porkchop`) | 5 | 17.86 % | Cantidad: {"min": 4, "max": 12} |
| crimson fungus (`minecraft:crimson_fungus`) | 5 | 17.86 % | Cantidad: {"min": 1, "max": 2} |
| flint (`minecraft:flint`) | 5 | 17.86 % | Cantidad: {"min": 1, "max": 3} |
| nether brick (`minecraft:nether_brick`) | 4 | 14.29 % | Cantidad: {"min": 4, "max": 9} |
| gunpowder (`minecraft:gunpowder`) | 6 | 21.43 % | Cantidad: {"min": 3, "max": 5} |
| soul soil (`minecraft:soul_soil`) | 3 | 10.71 % | Cantidad: {"min": 8, "max": 22} |

**Grupo 2** · tiradas: `2`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| gold nugget (`minecraft:gold_nugget`) | 1 | 50.00 % | Cantidad: {"min": 4, "max": 12} |
| iron nugget (`minecraft:iron_nugget`) | 1 | 50.00 % | Cantidad: {"min": 4, "max": 12} |

**Grupo 3** · tiradas: `{"min": 1, "max": 3}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| golden shovel (`minecraft:golden_shovel`) | 1 | 50.00 % | 1 por resultado; puede variar por funciones de la tabla |
| golden pickaxe (`minecraft:golden_pickaxe`) | 1 | 50.00 % | 1 por resultado; puede variar por funciones de la tabla |

## irons spellbooks — bookshelf loot

Tabla: `irons_spellbooks:chests/bookshelf_loot` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `{"min": 2, "max": 3}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| paper (`minecraft:paper`) | 8 | 66.67 % | Cantidad: {"min": 2, "max": 6} |
| book (`minecraft:book`) | 3 | 25.00 % | Cantidad: {"min": 1, "max": 2} |
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 1 | 8.33 % | Cantidad: {"min": 1, "max": 3} |

**Grupo 2** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| writable book (`minecraft:writable_book`) | 2 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |
| book (`minecraft:book`) | 5 | Condicionada; sin cifra única | Función: minecraft:enchant_with_levels |
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | Condicionada; sin cifra única | Función: irons_spellbooks:randomize_spell |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.7}]`.

**Grupo 3** · tiradas: `{"min": 0, "max": 5}` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/poor_ink` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.7}]`.

## irons spellbooks — catacombs/armory loot

Tabla: `irons_spellbooks:chests/catacombs/armory_loot` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `{"min": 3, "max": 4}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| stone sword (`minecraft:stone_sword`) | 3 | 50.00 % | 1 por resultado; puede variar por funciones de la tabla |
| iron sword (`minecraft:iron_sword`) | 1 | 16.67 % | 1 por resultado; puede variar por funciones de la tabla |
| bow (`minecraft:bow`) | 1 | 16.67 % | 1 por resultado; puede variar por funciones de la tabla |
| crossbow (`minecraft:crossbow`) | 1 | 16.67 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 2** · tiradas: `{"min": 1, "max": 2}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| chainmail chestplate (`minecraft:chainmail_chestplate`) | 1 | 20.00 % | 1 por resultado; puede variar por funciones de la tabla |
| leather helmet (`minecraft:leather_helmet`) | 1 | 20.00 % | 1 por resultado; puede variar por funciones de la tabla |
| leather boots (`minecraft:leather_boots`) | 1 | 20.00 % | 1 por resultado; puede variar por funciones de la tabla |
| iron helmet (`minecraft:iron_helmet`) | 1 | 20.00 % | 1 por resultado; puede variar por funciones de la tabla |
| leather chestplate (`minecraft:leather_chestplate`) | 1 | 20.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 3** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| arrow (`minecraft:arrow`) | 1 | 100.00 % | Cantidad: {"min": 0, "max": 32} |

## irons spellbooks — catacombs/coffin loot

Tabla: `irons_spellbooks:chests/catacombs/coffin_loot` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Libro de Hechizos Putrefacto (`irons_spellbooks:rotten_spell_book`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.15}]`.

**Grupo 2** · tiradas: `5`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| bone (`minecraft:bone`) | 5 | 33.33 % | Cantidad: {"min": 3, "max": 5} |
| cobweb (`minecraft:cobweb`) | 5 | 33.33 % | 1 por resultado; puede variar por funciones de la tabla |
| gold ingot (`minecraft:gold_ingot`) | 3 | 20.00 % | Cantidad: {"min": 2, "max": 5} |
| diamond (`minecraft:diamond`) | 1 | 6.67 % | 1 por resultado; puede variar por funciones de la tabla |
| emerald (`minecraft:emerald`) | 1 | 6.67 % | Cantidad: {"min": 1, "max": 3} |

**Grupo 3** · tiradas: `{"min": 1, "max": 2}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | 100.00 % | Función: irons_spellbooks:randomize_spell |

**Grupo 4** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 1 | 100.00 % | Cantidad: {"min": 5, "max": 16} |

**Grupo 5** · tiradas: `2`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| diamond sword (`minecraft:diamond_sword`) | 1 | 5.26 % | Función: irons_spellbooks:randomize_spell; Función: minecraft:enchant_with_levels |
| iron sword (`minecraft:iron_sword`) | 2 | 10.53 % | Función: irons_spellbooks:randomize_spell; Función: minecraft:enchant_with_levels |
| iron sword (`minecraft:iron_sword`) | 1 | 5.26 % | Función: irons_spellbooks:randomize_spell |
| iron helmet (`minecraft:iron_helmet`) | 1 | 5.26 % | Función: minecraft:enchant_with_levels |
| iron chestplate (`minecraft:iron_chestplate`) | 1 | 5.26 % | Función: minecraft:enchant_with_levels |
| iron leggings (`minecraft:iron_leggings`) | 1 | 5.26 % | Función: minecraft:enchant_with_levels |
| iron boots (`minecraft:iron_boots`) | 1 | 5.26 % | Función: minecraft:enchant_with_levels |
| diamond helmet (`minecraft:diamond_helmet`) | 1 | 5.26 % | Función: minecraft:enchant_with_levels |
| diamond chestplate (`minecraft:diamond_chestplate`) | 1 | 5.26 % | Función: minecraft:enchant_with_levels |
| diamond leggings (`minecraft:diamond_leggings`) | 1 | 5.26 % | Función: minecraft:enchant_with_levels |
| diamond boots (`minecraft:diamond_boots`) | 1 | 5.26 % | Función: minecraft:enchant_with_levels |
| Nada | 7 | 36.84 % | 1 por resultado; puede variar por funciones de la tabla |

## irons spellbooks — catacombs/crypt loot

Tabla: `irons_spellbooks:chests/catacombs/crypt_loot` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/basic_curios` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.25}]`.

**Grupo 2** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Fragmento de Conocimiento Antiguo (`irons_spellbooks:ancient_knowledge_fragment`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.5}]`.

**Grupo 3** · tiradas: `3`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| gold ingot (`minecraft:gold_ingot`) | 1 | 20.00 % | Cantidad: {"min": 2, "max": 5} |
| diamond (`minecraft:diamond`) | 1 | 20.00 % | 1 por resultado; puede variar por funciones de la tabla |
| Tela Arcana (`irons_spellbooks:magic_cloth`) | 1 | 20.00 % | Cantidad: {"min": 1, "max": 2} |
| Lingote Arcano (`irons_spellbooks:arcane_ingot`) | 1 | 20.00 % | Cantidad: {"min": 1, "max": 2} |
| emerald (`minecraft:emerald`) | 1 | 20.00 % | Cantidad: {"min": 1, "max": 6} |

**Grupo 4** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| golden apple (`minecraft:golden_apple`) | 3 | 75.00 % | 1 por resultado; puede variar por funciones de la tabla |
| enchanted golden apple (`minecraft:enchanted_golden_apple`) | 1 | 25.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 5** · tiradas: `2`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | 50.00 % | Función: irons_spellbooks:randomize_spell |
| Piedra Rúnica en blanco (`irons_spellbooks:blank_rune`) | 1 | 50.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 6** · tiradas: `3`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/reward_ink` | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 7** · tiradas: `2`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Vial de Sangre (`irons_spellbooks:blood_vial`) | 1 | 100.00 % | Cantidad: {"min": 1, "max": 4} |

**Grupo 8** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| dead king phylactery shard (`irons_spellbooks:dead_king_phylactery_shard`) | 1 | 100.00 % | Cantidad: {"min": 1, "max": 3} |

## irons spellbooks — catacombs/dead king vault

Tabla: `irons_spellbooks:chests/catacombs/dead_king_vault` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/basic_curios` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.25}]`.

**Grupo 2** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Fragmento de Conocimiento Antiguo (`irons_spellbooks:ancient_knowledge_fragment`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.5}]`.

**Grupo 3** · tiradas: `3`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| gold ingot (`minecraft:gold_ingot`) | 1 | 20.00 % | Cantidad: {"min": 2, "max": 5} |
| diamond (`minecraft:diamond`) | 1 | 20.00 % | 1 por resultado; puede variar por funciones de la tabla |
| Tela Arcana (`irons_spellbooks:magic_cloth`) | 1 | 20.00 % | Cantidad: {"min": 1, "max": 2} |
| Lingote Arcano (`irons_spellbooks:arcane_ingot`) | 1 | 20.00 % | Cantidad: {"min": 1, "max": 2} |
| emerald (`minecraft:emerald`) | 1 | 20.00 % | Cantidad: {"min": 1, "max": 6} |

**Grupo 4** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| golden apple (`minecraft:golden_apple`) | 3 | 75.00 % | 1 por resultado; puede variar por funciones de la tabla |
| enchanted golden apple (`minecraft:enchanted_golden_apple`) | 1 | 25.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 5** · tiradas: `2`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | 50.00 % | Función: irons_spellbooks:randomize_spell |
| Piedra Rúnica en blanco (`irons_spellbooks:blank_rune`) | 1 | 50.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 6** · tiradas: `3`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/reward_ink` | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 7** · tiradas: `2`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Vial de Sangre (`irons_spellbooks:blood_vial`) | 1 | 100.00 % | Cantidad: {"min": 1, "max": 4} |

**Grupo 8** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| dead king phylactery shard (`irons_spellbooks:dead_king_phylactery_shard`) | 1 | 100.00 % | Cantidad: {"min": 1, "max": 3} |

## irons spellbooks — catacombs/hidden trough treasure

Tabla: `irons_spellbooks:chests/catacombs/hidden_trough_treasure` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Libro de Hechizos Putrefacto (`irons_spellbooks:rotten_spell_book`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.05}]`.

**Grupo 2** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 2 | 66.67 % | Función: irons_spellbooks:randomize_spell |
| Piedra Rúnica en blanco (`irons_spellbooks:blank_rune`) | 1 | 33.33 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 3** · tiradas: `12`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| wheat (`minecraft:wheat`) | 5 | 83.33 % | Cantidad: {"min": 1, "max": 4} |
| hay block (`minecraft:hay_block`) | 1 | 16.67 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 4** · tiradas: `3`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| emerald (`minecraft:emerald`) | 5 | 83.33 % | Cantidad: {"min": 1, "max": 4} |
| diamond (`minecraft:diamond`) | 1 | 16.67 % | 1 por resultado; puede variar por funciones de la tabla |

## irons spellbooks — catacombs/pot

Tabla: `irons_spellbooks:chests/catacombs/pot` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 9 | 33.33 % | 1 por resultado; puede variar por funciones de la tabla |
| emerald (`minecraft:emerald`) | 4 | 14.81 % | Cantidad: {"min": 1, "max": 5} |
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 3 | 11.11 % | Cantidad: {"min": 2, "max": 7} |
| bone (`minecraft:bone`) | 4 | 14.81 % | Cantidad: {"min": 1, "max": 3} |
| cobweb (`minecraft:cobweb`) | 4 | 14.81 % | Cantidad: {"min": 1, "max": 2} |
| music disc dead king lullaby (`irons_spellbooks:music_disc_dead_king_lullaby`) | 1 | 3.70 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond (`minecraft:diamond`) | 1 | 3.70 % | 1 por resultado; puede variar por funciones de la tabla |
| skeleton skull (`minecraft:skeleton_skull`) | 1 | 3.70 % | 1 por resultado; puede variar por funciones de la tabla |

## irons spellbooks — catacombs/wall loot

Tabla: `irons_spellbooks:chests/catacombs/wall_loot` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 1 | Condicionada; sin cifra única | Cantidad: {"min": 0, "max": 4} |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.25}]`.

**Grupo 2** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Fragmento de Conocimiento Antiguo (`irons_spellbooks:ancient_knowledge_fragment`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.05}]`.

**Grupo 3** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | Condicionada; sin cifra única | Función: irons_spellbooks:randomize_spell |
| Piedra Rúnica en blanco (`irons_spellbooks:blank_rune`) | 2 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |
| Tabla adicional `irons_spellbooks:magic_items/basic_curios` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.35}]`.

**Grupo 4** · tiradas: `2`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| emerald (`minecraft:emerald`) | 1 | 10.00 % | Cantidad: {"min": 1, "max": 3} |
| diamond (`minecraft:diamond`) | 1 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |
| iron ingot (`minecraft:iron_ingot`) | 1 | 10.00 % | Cantidad: {"min": 1, "max": 4} |
| rotten flesh (`minecraft:rotten_flesh`) | 2 | 20.00 % | Cantidad: {"min": 1, "max": 8} |
| cobweb (`minecraft:cobweb`) | 2 | 20.00 % | Cantidad: {"min": 1, "max": 4} |
| bone (`minecraft:bone`) | 2 | 20.00 % | Cantidad: {"min": 2, "max": 5} |
| chain (`minecraft:chain`) | 1 | 10.00 % | Cantidad: {"min": 1, "max": 5} |

**Grupo 5** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| skeleton skull (`minecraft:skeleton_skull`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.35}]`.

**Grupo 6** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Libro de Hechizos Putrefacto (`irons_spellbooks:rotten_spell_book`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |
| diamond sword (`minecraft:diamond_sword`) | 1 | Condicionada; sin cifra única | Función: irons_spellbooks:randomize_spell; Función: minecraft:enchant_with_levels |
| iron sword (`minecraft:iron_sword`) | 2 | Condicionada; sin cifra única | Función: irons_spellbooks:randomize_spell; Función: minecraft:enchant_with_levels |
| iron sword (`minecraft:iron_sword`) | 2 | Condicionada; sin cifra única | Función: irons_spellbooks:randomize_spell |
| chainmail helmet (`minecraft:chainmail_helmet`) | 1 | Condicionada; sin cifra única | Función: minecraft:enchant_with_levels |
| chainmail chestplate (`minecraft:chainmail_chestplate`) | 1 | Condicionada; sin cifra única | Función: minecraft:enchant_with_levels |
| iron leggings (`minecraft:iron_leggings`) | 1 | Condicionada; sin cifra única | Función: minecraft:enchant_with_levels |
| iron boots (`minecraft:iron_boots`) | 1 | Condicionada; sin cifra única | Función: minecraft:enchant_with_levels |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.35}]`.

## irons spellbooks — citadel/citadel bookshelf

Tabla: `irons_spellbooks:chests/citadel/citadel_bookshelf` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| paper (`minecraft:paper`) | 1 | 100.00 % | Cantidad: {"type": "minecraft:uniform", "min": 8, "max": 16} |

**Grupo 2** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Fragmento de Conocimiento Antiguo (`irons_spellbooks:ancient_knowledge_fragment`) | 1 | 100.00 % | Cantidad: {"type": "minecraft:binomial", "n": 5, "p": 0.05} |

**Grupo 3** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| chained book (`irons_spellbooks:chained_book`) | 1 | 100.00 % | Cantidad: {"type": "minecraft:binomial", "n": 2, "p": 0.15} |

**Grupo 4** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Libro Arruinado (`irons_spellbooks:ruined_book`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.01}]`.

**Grupo 5** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| disc fragment flame still burns (`irons_spellbooks:disc_fragment_flame_still_burns`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.2}]`.

**Grupo 6** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Mapa Enrollado (`irons_spellbooks:furled_map`) | 1 | Condicionada; sin cifra única | Función: irons_spellbooks:set_furled_map |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.05}]`.

**Grupo 7** · tiradas: `{"type": "minecraft:binomial", "n": 3, "p": 0.25}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | 50.00 % | Función: irons_spellbooks:randomize_spell |
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | 50.00 % | Función: irons_spellbooks:randomize_spell |

**Grupo 8** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| book (`minecraft:book`) | 1 | 100.00 % | Cantidad: {"type": "minecraft:binomial", "n": 8, "p": 0.25} |

**Grupo 9** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:chests/citadel/citadel_tomes` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.5}]`.

## irons spellbooks — citadel/citadel tomes

Tabla: `irons_spellbooks:chests/citadel/citadel_tomes` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| written book (`minecraft:written_book`) | 1 | 8.33 % | Función: minecraft:set_name; Función: minecraft:set_nbt |
| written book (`minecraft:written_book`) | 1 | 8.33 % | Función: minecraft:set_name; Función: minecraft:set_nbt |
| written book (`minecraft:written_book`) | 1 | 8.33 % | Función: minecraft:set_name; Función: minecraft:set_nbt |
| written book (`minecraft:written_book`) | 1 | 8.33 % | Función: minecraft:set_name; Función: minecraft:set_nbt |
| written book (`minecraft:written_book`) | 1 | 8.33 % | Función: minecraft:set_name; Función: minecraft:set_nbt |
| written book (`minecraft:written_book`) | 1 | 8.33 % | Función: minecraft:set_name; Función: minecraft:set_nbt |
| written book (`minecraft:written_book`) | 1 | 8.33 % | Función: minecraft:set_name; Función: minecraft:set_nbt |
| written book (`minecraft:written_book`) | 1 | 8.33 % | Función: minecraft:set_name; Función: minecraft:set_nbt |
| written book (`minecraft:written_book`) | 1 | 8.33 % | Función: minecraft:set_name; Función: minecraft:set_nbt |
| written book (`minecraft:written_book`) | 1 | 8.33 % | Función: minecraft:set_name; Función: minecraft:set_nbt |
| written book (`minecraft:written_book`) | 1 | 8.33 % | Función: minecraft:set_name; Función: minecraft:set_nbt |
| written book (`minecraft:written_book`) | 1 | 8.33 % | Función: minecraft:set_name; Función: minecraft:set_nbt |

## irons spellbooks — citadel/citadel vault

Tabla: `irons_spellbooks:chests/citadel/citadel_vault` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Fragmento de Conocimiento Antiguo (`irons_spellbooks:ancient_knowledge_fragment`) | 1 | 100.00 % | Cantidad: {"type": "minecraft:binomial", "n": 4, "p": 0.25} |

**Grupo 2** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| disc fragment flame still burns (`irons_spellbooks:disc_fragment_flame_still_burns`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.4}]`.

**Grupo 3** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| pyrium ingot (`irons_spellbooks:pyrium_ingot`) | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 4** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 1 | 100.00 % | Cantidad: {"min": 5, "max": 16} |

**Grupo 5** · tiradas: `{"min": 2, "max": 4}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 3 | 25.00 % | Función: irons_spellbooks:randomize_spell |
| (Pergamino) (`irons_spellbooks:scroll`) | 3 | 25.00 % | Función: irons_spellbooks:randomize_spell |
| (Pergamino) (`irons_spellbooks:scroll`) | 2 | 16.67 % | Función: irons_spellbooks:randomize_spell |
| Piedra Rúnica en blanco (`irons_spellbooks:blank_rune`) | 4 | 33.33 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 6** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/basic_curios` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.5}]`.

**Grupo 7** · tiradas: `4`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/reward_ink` | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 8** · tiradas: `4`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| diamond (`minecraft:diamond`) | 6 | 16.22 % | Cantidad: {"min": 1, "max": 2} |
| mithril scrap (`irons_spellbooks:mithril_scrap`) | 5 | 13.51 % | Cantidad: {"min": 1, "max": 2} |
| netherite scrap (`minecraft:netherite_scrap`) | 3 | 8.11 % | Cantidad: {"min": 1, "max": 2} |
| ancient debris (`minecraft:ancient_debris`) | 3 | 8.11 % | Cantidad: {"min": 1, "max": 3} |
| netherite ingot (`minecraft:netherite_ingot`) | 2 | 5.41 % | 1 por resultado; puede variar por funciones de la tabla |
| emerald (`minecraft:emerald`) | 8 | 21.62 % | Cantidad: {"min": 2, "max": 4} |
| gold ingot (`minecraft:gold_ingot`) | 10 | 27.03 % | Cantidad: {"min": 4, "max": 8} |

## irons spellbooks — citadel/rampart chest

Tabla: `irons_spellbooks:chests/citadel/rampart_chest` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1.0` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| ominous bottle (`irons_spellbooks:ominous_bottle`) | 1 | Condicionada; sin cifra única | Cantidad: 1.0 |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.25}]`.

**Grupo 2** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Espadón Decrépito (`irons_spellbooks:keeper_flamberge`) | 2 | Condicionada; sin cifra única | Función: minecraft:set_damage; Condiciones: [{"condition": "minecraft:random_chance", "chance": 0.25}] |

**Grupo 3** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| flint and steel (`minecraft:flint_and_steel`) | 2 | Condicionada; sin cifra única | Función: minecraft:set_damage; Condiciones: [{"condition": "minecraft:random_chance", "chance": 0.55}] |

**Grupo 4** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| lantern (`minecraft:lantern`) | 1 | 100.00 % | Cantidad: {"min": 0, "max": 8} |

**Grupo 5** · tiradas: `3`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| soul sand (`minecraft:soul_sand`) | 1 | 25.00 % | Cantidad: {"type": "minecraft:uniform", "min": 4, "max": 8} |
| bone (`minecraft:bone`) | 1 | 25.00 % | Cantidad: {"type": "minecraft:uniform", "min": 4, "max": 8} |
| flint (`minecraft:flint`) | 1 | 25.00 % | Cantidad: {"type": "minecraft:uniform", "min": 4, "max": 8} |
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 1 | 25.00 % | Cantidad: {"type": "minecraft:uniform", "min": 2, "max": 5} |

**Grupo 6** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| emerald (`minecraft:emerald`) | 1 | 25.00 % | Cantidad: {"type": "minecraft:uniform", "min": 4, "max": 8} |
| diamond (`minecraft:diamond`) | 1 | 25.00 % | Cantidad: {"type": "minecraft:uniform", "min": 1, "max": 2} |
| ancient debris (`minecraft:ancient_debris`) | 1 | 25.00 % | 1 por resultado; puede variar por funciones de la tabla |
| Nada | 1 | 25.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 7** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| emerald (`minecraft:emerald`) | 1 | 3.70 % | Cantidad: {"type": "minecraft:uniform", "min": 4, "max": 8} |
| diamond (`minecraft:diamond`) | 1 | 3.70 % | Cantidad: {"type": "minecraft:uniform", "min": 1, "max": 2} |
| Nada | 7 | 25.93 % | 1 por resultado; puede variar por funciones de la tabla |
| Piedra Rúnica en blanco (`irons_spellbooks:blank_rune`) | 5 | 18.52 % | 1 por resultado; puede variar por funciones de la tabla |
| (Pergamino) (`irons_spellbooks:scroll`) | 13 | 48.15 % | Función: irons_spellbooks:randomize_spell |

## irons spellbooks — citadel/rampart supplies

Tabla: `irons_spellbooks:chests/citadel/rampart_supplies` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1.0` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| ominous bottle (`irons_spellbooks:ominous_bottle`) | 1 | Condicionada; sin cifra única | Cantidad: 1.0 |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.1}]`.

**Grupo 2** · tiradas: `{"min": 1, "max": 2}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| crossbow (`minecraft:crossbow`) | 2 | 100.00 % | Función: minecraft:set_damage |

**Grupo 3** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| arrow (`minecraft:arrow`) | 1 | 100.00 % | Cantidad: {"min": 0, "max": 32} |

**Grupo 4** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| lantern (`minecraft:lantern`) | 1 | 100.00 % | Cantidad: {"min": 0, "max": 8} |

**Grupo 5** · tiradas: `3`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| soul sand (`minecraft:soul_sand`) | 1 | 25.00 % | Cantidad: {"type": "minecraft:uniform", "min": 4, "max": 8} |
| bone (`minecraft:bone`) | 1 | 25.00 % | Cantidad: {"type": "minecraft:uniform", "min": 4, "max": 8} |
| flint (`minecraft:flint`) | 1 | 25.00 % | Cantidad: {"type": "minecraft:uniform", "min": 4, "max": 8} |
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 1 | 25.00 % | Cantidad: {"type": "minecraft:uniform", "min": 2, "max": 5} |

## irons spellbooks — citadel/spawner reward

Tabla: `irons_spellbooks:chests/citadel/spawner_reward` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia de Ceniza (`irons_spellbooks:cinder_essence`) | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

## irons spellbooks — component storage

Tabla: `irons_spellbooks:chests/component_storage` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `{"min": 2, "max": 3}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 1 | 16.67 % | Cantidad: {"min": 1, "max": 2} |
| Piedra de Absolución (`irons_spellbooks:shriving_stone`) | 1 | 16.67 % | 1 por resultado; puede variar por funciones de la tabla |
| Tabla adicional `irons_spellbooks:magic_items/all_focuses` | 4 | 66.67 % | Cantidad: {"min": 1, "max": 5} |

## irons spellbooks — evoker fort

Tabla: `irons_spellbooks:chests/evoker_fort` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `15`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 5 | 16.13 % | Cantidad: {"min": 1, "max": 3} |
| raw iron (`minecraft:raw_iron`) | 5 | 16.13 % | Cantidad: {"min": 0, "max": 4} |
| experience bottle (`minecraft:experience_bottle`) | 5 | 16.13 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond (`minecraft:diamond`) | 2 | 6.45 % | 1 por resultado; puede variar por funciones de la tabla |
| arrow (`minecraft:arrow`) | 6 | 19.35 % | Cantidad: {"min": 0, "max": 4} |
| emerald (`minecraft:emerald`) | 8 | 25.81 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 2** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| goat horn (`minecraft:goat_horn`) | 1 | Condicionada; sin cifra única | Función: minecraft:set_instrument |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.45}]`.

**Grupo 3** · tiradas: `{"min": 1, "max": 2}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | 100.00 % | Función: irons_spellbooks:randomize_spell |

**Grupo 4** · tiradas: `{"min": 0, "max": 5}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/poor_ink` | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 5** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/basic_curios` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.2}]`.

## irons spellbooks — evoker fort/guard tower

Tabla: `irons_spellbooks:chests/evoker_fort/guard_tower` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `{"min": 1, "max": 3}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| iron axe (`minecraft:iron_axe`) | 1 | 33.33 % | 1 por resultado; puede variar por funciones de la tabla |
| crossbow (`minecraft:crossbow`) | 2 | 66.67 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 2** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| arrow (`minecraft:arrow`) | 1 | 100.00 % | Cantidad: {"min": 0, "max": 32} |

**Grupo 3** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| torch (`minecraft:torch`) | 1 | 100.00 % | Cantidad: {"min": 0, "max": 8} |

**Grupo 4** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| goat horn (`minecraft:goat_horn`) | 1 | 100.00 % | Función: minecraft:set_instrument |

## irons spellbooks — filler storage loot

Tabla: `irons_spellbooks:chests/filler_storage_loot` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 1 | Condicionada; sin cifra única | Cantidad: {"min": 0, "max": 4} |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.35}]`.

**Grupo 2** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | Condicionada; sin cifra única | Función: irons_spellbooks:randomize_spell |
| Piedra Rúnica en blanco (`irons_spellbooks:blank_rune`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.02}]`.

**Grupo 3** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/poor_ink` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.25}]`.

**Grupo 4** · tiradas: `4`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| emerald (`minecraft:emerald`) | 1 | 3.70 % | 1 por resultado; puede variar por funciones de la tabla |
| book (`minecraft:book`) | 2 | 7.41 % | 1 por resultado; puede variar por funciones de la tabla |
| apple (`minecraft:apple`) | 2 | 7.41 % | 1 por resultado; puede variar por funciones de la tabla |
| rotten flesh (`minecraft:rotten_flesh`) | 5 | 18.52 % | 1 por resultado; puede variar por funciones de la tabla |
| cobweb (`minecraft:cobweb`) | 8 | 29.63 % | 1 por resultado; puede variar por funciones de la tabla |
| charcoal (`minecraft:charcoal`) | 3 | 11.11 % | 1 por resultado; puede variar por funciones de la tabla |
| Nada | 6 | 22.22 % | 1 por resultado; puede variar por funciones de la tabla |

## irons spellbooks — generic magic treasure

Tabla: `irons_spellbooks:chests/generic_magic_treasure` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 1 | 100.00 % | Cantidad: {"min": 3, "max": 13} |

**Grupo 2** · tiradas: `{"min": 1, "max": 2}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | 100.00 % | Función: irons_spellbooks:randomize_spell |

**Grupo 3** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Piedra Rúnica en blanco (`irons_spellbooks:blank_rune`) | 1 | Condicionada; sin cifra única | Condiciones: [{"condition": "minecraft:random_chance", "chance": 0.3}] |

**Grupo 4** · tiradas: `{"min": 1, "max": 2}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/all_focuses` | 1 | 100.00 % | Cantidad: {"min": 1, "max": 2} |

**Grupo 5** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/basic_curios` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.2}]`.

**Grupo 6** · tiradas: `{"min": 1, "max": 4}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/decent_ink` | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 7** · tiradas: `6`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| diamond (`minecraft:diamond`) | 1 | 3.45 % | 1 por resultado; puede variar por funciones de la tabla |
| copper ingot (`minecraft:copper_ingot`) | 8 | 27.59 % | 1 por resultado; puede variar por funciones de la tabla |
| gold ingot (`minecraft:gold_ingot`) | 5 | 17.24 % | Cantidad: {"min": 1, "max": 3} |
| emerald (`minecraft:emerald`) | 3 | 10.34 % | Cantidad: {"min": 1, "max": 3} |
| iron ingot (`minecraft:iron_ingot`) | 12 | 41.38 % | Cantidad: {"min": 1, "max": 4} |

**Grupo 8** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| diamond sword (`minecraft:diamond_sword`) | 1 | Condicionada; sin cifra única | Función: irons_spellbooks:randomize_spell; Función: minecraft:enchant_with_levels |
| iron sword (`minecraft:iron_sword`) | 2 | Condicionada; sin cifra única | Función: irons_spellbooks:randomize_spell; Función: minecraft:enchant_with_levels |
| iron sword (`minecraft:iron_sword`) | 1 | Condicionada; sin cifra única | Función: irons_spellbooks:randomize_spell |
| iron helmet (`minecraft:iron_helmet`) | 2 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |
| iron chestplate (`minecraft:iron_chestplate`) | 2 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |
| iron leggings (`minecraft:iron_leggings`) | 2 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |
| iron boots (`minecraft:iron_boots`) | 2 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |
| diamond helmet (`minecraft:diamond_helmet`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |
| diamond chestplate (`minecraft:diamond_chestplate`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |
| diamond leggings (`minecraft:diamond_leggings`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |
| diamond boots (`minecraft:diamond_boots`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.4}]`.

## irons spellbooks — ice spider den/basement

Tabla: `irons_spellbooks:chests/ice_spider_den/basement` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/basic_curios` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.25}]`.

**Grupo 2** · tiradas: `{"min": 0, "max": 2}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| ice venom vial (`irons_spellbooks:ice_venom_vial`) | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 3** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Piedra Rúnica en blanco (`irons_spellbooks:blank_rune`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.6}]`.

**Grupo 4** · tiradas: `{"min": 6, "max": 12}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| snowball (`minecraft:snowball`) | 1 | 25.00 % | Cantidad: {"min": 1, "max": 2} |
| ice (`minecraft:ice`) | 1 | 25.00 % | Cantidad: {"min": 2, "max": 4} |
| cobweb (`minecraft:cobweb`) | 1 | 25.00 % | Cantidad: {"min": 2, "max": 4} |
| Hueso Congelado (`irons_spellbooks:frozen_bone`) | 1 | 25.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 5** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 1 | 100.00 % | Cantidad: {"min": 10, "max": 30} |

**Grupo 6** · tiradas: `5`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 8 | 61.54 % | 1 por resultado; puede variar por funciones de la tabla |
| emerald (`minecraft:emerald`) | 4 | 30.77 % | Cantidad: {"min": 2, "max": 3} |
| diamond (`minecraft:diamond`) | 1 | 7.69 % | 1 por resultado; puede variar por funciones de la tabla |

## irons spellbooks — ice spider den/cask

Tabla: `irons_spellbooks:chests/ice_spider_den/cask` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| honey bottle (`minecraft:honey_bottle`) | 1 | 100.00 % | Cantidad: {"min": 1, "max": 4} |

**Grupo 2** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| glass bottle (`minecraft:glass_bottle`) | 1 | 100.00 % | Cantidad: {"min": 4, "max": 10} |

**Grupo 3** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| sweet berries (`minecraft:sweet_berries`) | 1 | 100.00 % | Cantidad: {"min": 5, "max": 16} |

**Grupo 4** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| ice (`minecraft:ice`) | 1 | 100.00 % | Cantidad: {"min": 15, "max": 25} |

## irons spellbooks — ice spider den/dungeon

Tabla: `irons_spellbooks:chests/ice_spider_den/dungeon` · fuente: `TheOptimizer_AdventureLoot.zip`.

Hay varias versiones de esta tabla; se ha priorizado el datapack del mundo y después el datapack global. Confirma el orden de carga si el mundo usa otros datapacks.

**Grupo 1** · tiradas: `{"min": 2, "max": 3}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/good_ink` | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 2** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Piedra Rúnica en blanco (`irons_spellbooks:blank_rune`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.7}]`.

**Grupo 3** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | 100.00 % | Función: irons_spellbooks:randomize_spell |

## irons spellbooks — ice spider den/pot

Tabla: `irons_spellbooks:chests/ice_spider_den/pot` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 6 | 24.00 % | 1 por resultado; puede variar por funciones de la tabla |
| emerald (`minecraft:emerald`) | 4 | 16.00 % | Cantidad: {"min": 1, "max": 5} |
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 3 | 12.00 % | Cantidad: {"min": 2, "max": 7} |
| cobweb (`minecraft:cobweb`) | 4 | 16.00 % | Cantidad: {"min": 1, "max": 3} |
| Hueso Congelado (`irons_spellbooks:frozen_bone`) | 7 | 28.00 % | 1 por resultado; puede variar por funciones de la tabla |
| iron ingot (`minecraft:iron_ingot`) | 1 | 4.00 % | 1 por resultado; puede variar por funciones de la tabla |

## irons spellbooks — ice spider den/spawner reward

Tabla: `irons_spellbooks:chests/ice_spider_den/spawner_reward` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| book (`minecraft:book`) | 1 | 33.33 % | Función: minecraft:enchant_with_levels |
| Tabla adicional `irons_spellbooks:magic_items/decent_ink` | 1 | 33.33 % | 1 por resultado; puede variar por funciones de la tabla |
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | 33.33 % | Función: irons_spellbooks:randomize_spell |

## irons spellbooks — ice spider den/tower

Tabla: `irons_spellbooks:chests/ice_spider_den/tower` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/basic_curios` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.25}]`.

**Grupo 2** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| spyglass (`minecraft:spyglass`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.25}]`.

**Grupo 3** · tiradas: `2`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | 50.00 % | Función: irons_spellbooks:randomize_spell |
| Nada | 1 | 50.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 4** · tiradas: `{"min": 6, "max": 12}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| snowball (`minecraft:snowball`) | 1 | 33.33 % | Cantidad: {"min": 1, "max": 2} |
| ice (`minecraft:ice`) | 1 | 33.33 % | Cantidad: {"min": 2, "max": 4} |
| cobweb (`minecraft:cobweb`) | 1 | 33.33 % | Cantidad: {"min": 2, "max": 4} |

**Grupo 5** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 1 | 100.00 % | Cantidad: {"min": 5, "max": 20} |

## irons spellbooks — impaled icebreaker/captain quarters

Tabla: `irons_spellbooks:chests/impaled_icebreaker/captain_quarters` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/basic_curios` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.25}]`.

**Grupo 2** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| bundle (`minecraft:bundle`) | 1 | 100.00 % | Función: minecraft:set_nbt |

**Grupo 3** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| permafrost shard (`irons_spellbooks:permafrost_shard`) | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 4** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| spyglass (`minecraft:spyglass`) | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 5** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tinta Épica (`irons_spellbooks:epic_ink`) | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 6** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| goat horn (`minecraft:goat_horn`) | 1 | 100.00 % | Función: minecraft:set_instrument |

**Grupo 7** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| paper (`minecraft:paper`) | 1 | 100.00 % | Cantidad: {"min": 27, "max": 35} |

## irons spellbooks — impaled icebreaker/food barrel

Tabla: `irons_spellbooks:chests/impaled_icebreaker/food_barrel` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `{"min": 2, "max": 4}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| mushroom stew (`minecraft:mushroom_stew`) | 1 | 25.00 % | 1 por resultado; puede variar por funciones de la tabla |
| beetroot soup (`minecraft:beetroot_soup`) | 1 | 25.00 % | 1 por resultado; puede variar por funciones de la tabla |
| rabbit stew (`minecraft:rabbit_stew`) | 1 | 25.00 % | 1 por resultado; puede variar por funciones de la tabla |
| suspicious stew (`minecraft:suspicious_stew`) | 1 | 25.00 % | Función: minecraft:set_stew_effect |

**Grupo 2** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| fishing rod (`minecraft:fishing_rod`) | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 3** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| bucket (`minecraft:bucket`) | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 4** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| pufferfish (`minecraft:pufferfish`) | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 5** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| bread (`minecraft:bread`) | 1 | 100.00 % | Cantidad: {"min": 5, "max": 9} |

**Grupo 6** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| cod (`minecraft:cod`) | 1 | 100.00 % | Cantidad: {"min": 3, "max": 6} |

## irons spellbooks — magic bookshelf loot

Tabla: `irons_spellbooks:chests/magic_bookshelf_loot` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 1 | 100.00 % | Cantidad: {"min": 2, "max": 9} |

**Grupo 2** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/basic_curios` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.05}]`.

**Grupo 3** · tiradas: `{"min": 2, "max": 3}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| paper (`minecraft:paper`) | 8 | 72.73 % | Cantidad: {"min": 2, "max": 6} |
| book (`minecraft:book`) | 3 | 27.27 % | Cantidad: {"min": 1, "max": 2} |

**Grupo 4** · tiradas: `{"min": 1, "max": 3}` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| book (`minecraft:book`) | 5 | Condicionada; sin cifra única | Función: minecraft:enchant_with_levels |
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | Condicionada; sin cifra única | Función: irons_spellbooks:randomize_spell |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.8}]`.

**Grupo 5** · tiradas: `{"min": 1, "max": 5}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/decent_ink` | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 6** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Fragmento de Conocimiento Antiguo (`irons_spellbooks:ancient_knowledge_fragment`) | 1 | Condicionada; sin cifra única | Cantidad: {"min": 1, "max": 2} |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.05}]`.

## irons spellbooks — mangrove hut

Tabla: `irons_spellbooks:chests/mangrove_hut` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `10`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 5 | 17.86 % | Cantidad: {"min": 1, "max": 3} |
| nether wart (`minecraft:nether_wart`) | 5 | 17.86 % | 1 por resultado; puede variar por funciones de la tabla |
| brown mushroom (`minecraft:brown_mushroom`) | 5 | 17.86 % | 1 por resultado; puede variar por funciones de la tabla |
| copper ingot (`minecraft:copper_ingot`) | 2 | 7.14 % | 1 por resultado; puede variar por funciones de la tabla |
| red mushroom (`minecraft:red_mushroom`) | 3 | 10.71 % | 1 por resultado; puede variar por funciones de la tabla |
| fern (`minecraft:fern`) | 8 | 28.57 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 2** · tiradas: `{"min": 1, "max": 3}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/random_potion_or_elixir` | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 3** · tiradas: `{"min": 0, "max": 5}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/poor_ink` | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 4** · tiradas: `{"min": 0, "max": 2}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | 100.00 % | Función: irons_spellbooks:randomize_spell |

**Grupo 5** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/basic_curios` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.4}]`.

## irons spellbooks — mangrove hut/hidden potion storage

Tabla: `irons_spellbooks:chests/mangrove_hut/hidden_potion_storage` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `15`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| emerald (`minecraft:emerald`) | 1 | 50.00 % | Cantidad: 2 |
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 1 | 50.00 % | Cantidad: 2 |

**Grupo 2** · tiradas: `{"min": 3, "max": 5}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/random_potion_or_elixir` | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 3** · tiradas: `{"min": 2, "max": 5}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| netherward tincture (`irons_spellbooks:netherward_tincture`) | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

## irons spellbooks — mangrove hut/potion ingredient storage

Tabla: `irons_spellbooks:chests/mangrove_hut/potion_ingredient_storage` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `10`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| glass bottle (`minecraft:glass_bottle`) | 20 | 76.92 % | 1 por resultado; puede variar por funciones de la tabla |
| potion (`minecraft:potion`) | 5 | 19.23 % | Función: minecraft:set_potion |
| emerald (`minecraft:emerald`) | 1 | 3.85 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 2** · tiradas: `{"min": 0, "max": 2}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/random_potion_or_elixir` | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

## irons spellbooks — mountain tower/ice barrel

Tabla: `irons_spellbooks:chests/mountain_tower/ice_barrel` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `2`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | 100.00 % | Función: irons_spellbooks:randomize_spell |

**Grupo 2** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Anillo de %s Afinidad (`irons_spellbooks:affinity_ring`) | 4 | 57.14 % | Función: irons_spellbooks:randomize_ring_enhancement |
| Anillo de Escarcha Helada (`irons_spellbooks:frostward_ring`) | 1 | 14.29 % | 1 por resultado; puede variar por funciones de la tabla |
| Nada | 2 | 28.57 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 3** · tiradas: `{"min": 6, "max": 12}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| snowball (`minecraft:snowball`) | 1 | 50.00 % | Cantidad: {"min": 1, "max": 2} |
| ice (`minecraft:ice`) | 1 | 50.00 % | Cantidad: {"min": 2, "max": 4} |

## irons spellbooks — mountain tower/mountain tower

Tabla: `irons_spellbooks:chests/mountain_tower/mountain_tower` · fuente: `TheOptimizer_AdventureLoot.zip`.

Hay varias versiones de esta tabla; se ha priorizado el datapack del mundo y después el datapack global. Confirma el orden de carga si el mundo usa otros datapacks.

**Grupo 1** · tiradas: `8`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 4 | 40.00 % | Cantidad: {"min": 2, "max": 5} |
| lapis lazuli (`minecraft:lapis_lazuli`) | 3 | 30.00 % | Cantidad: {"min": 4, "max": 10} |
| amethyst shard (`minecraft:amethyst_shard`) | 3 | 30.00 % | Cantidad: {"min": 2, "max": 6} |

**Grupo 2** · tiradas: `{"min": 2, "max": 4}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/good_ink` | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 3** · tiradas: `{"min": 1, "max": 2}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | 100.00 % | Función: irons_spellbooks:randomize_spell |

**Grupo 4** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Runa de Hielo (`irons_spellbooks:ice_rune`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.65}]`.

**Grupo 5** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/basic_curios` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.5}]`.

## irons spellbooks — priest house

Tabla: `irons_spellbooks:chests/priest_house` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `{"min": 1, "max": 3}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| potion (`minecraft:potion`) | 1 | 50.00 % | Función: minecraft:set_potion |
| potion (`minecraft:potion`) | 1 | 50.00 % | Función: minecraft:set_potion |

**Grupo 2** · tiradas: `{"min": 0, "max": 4}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/poor_ink` | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 3** · tiradas: `{"min": 0, "max": 2}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | 100.00 % | Función: irons_spellbooks:randomize_spell |

**Grupo 4** · tiradas: `12`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| emerald (`minecraft:emerald`) | 1 | 25.00 % | 1 por resultado; puede variar por funciones de la tabla |
| Perla Divina (`irons_spellbooks:divine_pearl`) | 1 | 25.00 % | 1 por resultado; puede variar por funciones de la tabla |
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 1 | 25.00 % | 1 por resultado; puede variar por funciones de la tabla |
| paper (`minecraft:paper`) | 1 | 25.00 % | 1 por resultado; puede variar por funciones de la tabla |

## irons spellbooks — pyromancer tower/burnt chest

Tabla: `irons_spellbooks:chests/pyromancer_tower/burnt_chest` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| gunpowder (`minecraft:gunpowder`) | 1 | 100.00 % | Cantidad: {"min": 7, "max": 16} |

**Grupo 2** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| charcoal (`minecraft:charcoal`) | 1 | 100.00 % | Cantidad: {"min": 7, "max": 16} |

**Grupo 3** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| ghast tear (`minecraft:ghast_tear`) | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 4** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Anillo de %s Afinidad (`irons_spellbooks:affinity_ring`) | 1 | 50.00 % | Función: irons_spellbooks:randomize_ring_enhancement |
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | 50.00 % | Función: irons_spellbooks:randomize_spell |

## irons spellbooks — pyromancer tower/fire ale cask

Tabla: `irons_spellbooks:chests/pyromancer_tower/fire_ale_cask` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `{"min": 0, "max": 2}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| fire ale (`irons_spellbooks:fire_ale`) | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 2** · tiradas: `{"min": 3, "max": 9}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| glass bottle (`minecraft:glass_bottle`) | 1 | 12.50 % | 1 por resultado; puede variar por funciones de la tabla |
| potion (`minecraft:potion`) | 1 | 12.50 % | Función: minecraft:set_potion |
| pumpkin (`minecraft:pumpkin`) | 1 | 12.50 % | 1 por resultado; puede variar por funciones de la tabla |
| sugar (`minecraft:sugar`) | 1 | 12.50 % | 1 por resultado; puede variar por funciones de la tabla |
| honeycomb (`minecraft:honeycomb`) | 1 | 12.50 % | 1 por resultado; puede variar por funciones de la tabla |
| fermented spider eye (`minecraft:fermented_spider_eye`) | 1 | 12.50 % | 1 por resultado; puede variar por funciones de la tabla |
| wheat (`minecraft:wheat`) | 1 | 12.50 % | 1 por resultado; puede variar por funciones de la tabla |
| water bucket (`minecraft:water_bucket`) | 1 | 12.50 % | 1 por resultado; puede variar por funciones de la tabla |

## irons spellbooks — pyromancer tower/fire ale trove

Tabla: `irons_spellbooks:chests/pyromancer_tower/fire_ale_trove` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `{"min": 5, "max": 9}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| fire ale (`irons_spellbooks:fire_ale`) | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 2** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| glass bottle (`minecraft:glass_bottle`) | 1 | 100.00 % | Cantidad: {"min": 5, "max": 9} |

**Grupo 3** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| emerald (`minecraft:emerald`) | 1 | 100.00 % | Cantidad: {"min": 8, "max": 17} |

## irons spellbooks — pyromancer tower/old cask

Tabla: `irons_spellbooks:chests/pyromancer_tower/old_cask` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `{"min": 1, "max": 3}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| honeycomb (`minecraft:honeycomb`) | 1 | 20.00 % | Cantidad: {"min": 1, "max": 2} |
| fermented spider eye (`minecraft:fermented_spider_eye`) | 1 | 20.00 % | 1 por resultado; puede variar por funciones de la tabla |
| wheat (`minecraft:wheat`) | 1 | 20.00 % | Cantidad: {"min": 3, "max": 8} |
| sugar (`minecraft:sugar`) | 1 | 20.00 % | Cantidad: {"min": 2, "max": 4} |
| beetroot seeds (`minecraft:beetroot_seeds`) | 1 | 20.00 % | Cantidad: {"min": 2, "max": 4} |

**Grupo 2** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| glass bottle (`minecraft:glass_bottle`) | 1 | 100.00 % | Cantidad: {"min": 8, "max": 24} |

**Grupo 3** · tiradas: `3`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| potion (`minecraft:potion`) | 1 | Condicionada; sin cifra única | Función: minecraft:set_potion; Condiciones: [{"condition": "minecraft:random_chance", "chance": 0.2}] |

## irons spellbooks — pyromancer tower/pot

Tabla: `irons_spellbooks:chests/pyromancer_tower/pot` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 6 | 21.43 % | 1 por resultado; puede variar por funciones de la tabla |
| emerald (`minecraft:emerald`) | 4 | 14.29 % | Cantidad: {"min": 1, "max": 5} |
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 3 | 10.71 % | Cantidad: {"min": 2, "max": 7} |
| charcoal (`minecraft:charcoal`) | 4 | 14.29 % | Cantidad: {"min": 1, "max": 3} |
| cobweb (`minecraft:cobweb`) | 2 | 7.14 % | Cantidad: {"min": 1, "max": 2} |
| fire ale (`irons_spellbooks:fire_ale`) | 7 | 25.00 % | 1 por resultado; puede variar por funciones de la tabla |
| gold ingot (`minecraft:gold_ingot`) | 1 | 3.57 % | 1 por resultado; puede variar por funciones de la tabla |
| copper ingot (`minecraft:copper_ingot`) | 1 | 3.57 % | 1 por resultado; puede variar por funciones de la tabla |

## irons spellbooks — pyromancer tower/pyromancer basic storage

Tabla: `irons_spellbooks:chests/pyromancer_tower/pyromancer_basic_storage` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | Condicionada; sin cifra única | Función: irons_spellbooks:randomize_spell |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.4}]`.

**Grupo 2** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tela Arcana (`irons_spellbooks:magic_cloth`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |
| Piedra Rúnica en blanco (`irons_spellbooks:blank_rune`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.1}]`.

**Grupo 3** · tiradas: `{"min": 0, "max": 3}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/poor_ink` | 1 | 3.45 % | 1 por resultado; puede variar por funciones de la tabla |
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 1 | 3.45 % | Cantidad: {"min": 0, "max": 4} |
| book (`minecraft:book`) | 2 | 6.90 % | Cantidad: {"min": 1, "max": 2} |
| paper (`minecraft:paper`) | 5 | 17.24 % | Cantidad: {"min": 1, "max": 3} |
| cobweb (`minecraft:cobweb`) | 8 | 27.59 % | Cantidad: {"min": 1, "max": 4} |
| Nada | 6 | 20.69 % | 1 por resultado; puede variar por funciones de la tabla |
| candle (`minecraft:candle`) | 6 | 20.69 % | Cantidad: {"min": 2, "max": 4} |

**Grupo 4** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/basic_curios` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.075}]`.

## irons spellbooks — pyromancer tower/pyromancer supplies

Tabla: `irons_spellbooks:chests/pyromancer_tower/pyromancer_supplies` · fuente: `TheOptimizer_AdventureLoot.zip`.

Hay varias versiones de esta tabla; se ha priorizado el datapack del mundo y después el datapack global. Confirma el orden de carga si el mundo usa otros datapacks.

**Grupo 1** · tiradas: `10`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 5 | 31.25 % | Cantidad: {"min": 2, "max": 4} |
| blaze rod (`minecraft:blaze_rod`) | 4 | 25.00 % | Cantidad: {"min": 1, "max": 3} |
| obsidian (`minecraft:obsidian`) | 3 | 18.75 % | Cantidad: {"min": 2, "max": 4} |
| paper (`minecraft:paper`) | 4 | 25.00 % | Cantidad: {"min": 3, "max": 8} |

**Grupo 2** · tiradas: `{"min": 2, "max": 4}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/good_ink` | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 3** · tiradas: `{"min": 1, "max": 2}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | 100.00 % | Función: irons_spellbooks:randomize_spell |

**Grupo 4** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Runa de Fuego (`irons_spellbooks:fire_rune`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.65}]`.

**Grupo 5** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/basic_curios` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.5}]`.

## irons spellbooks — sewer loot

Tabla: `irons_spellbooks:chests/sewer_loot` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| emerald (`minecraft:emerald`) | 1 | 12.50 % | Cantidad: {"min": 1, "max": 3} |
| diamond (`minecraft:diamond`) | 1 | 12.50 % | 1 por resultado; puede variar por funciones de la tabla |
| turtle egg (`minecraft:turtle_egg`) | 1 | 12.50 % | 1 por resultado; puede variar por funciones de la tabla |
| Nada | 5 | 62.50 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 2** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 1 | 100.00 % | Cantidad: {"min": 1, "max": 12} |

**Grupo 3** · tiradas: `3`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| rotten flesh (`minecraft:rotten_flesh`) | 1 | 33.33 % | Cantidad: {"min": 2, "max": 3} |
| slime ball (`minecraft:slime_ball`) | 1 | 33.33 % | Cantidad: {"min": 2, "max": 6} |
| bone (`minecraft:bone`) | 1 | 33.33 % | Cantidad: {"min": 1, "max": 4} |

## irons spellbooks — trial chambers/additional ominous spawner consumable loot

Tabla: `irons_spellbooks:chests/trial_chambers/additional_ominous_spawner_consumable_loot` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 25 | 53.19 % | 1 por resultado; puede variar por funciones de la tabla |
| potion (`minecraft:potion`) | 6 | 12.77 % | Función: minecraft:set_potion |
| potion (`minecraft:potion`) | 8 | 17.02 % | Función: minecraft:set_potion |
| potion (`minecraft:potion`) | 4 | 8.51 % | Función: minecraft:set_potion |
| Tabla adicional `irons_spellbooks:magic_items/random_elixir` | 4 | 8.51 % | 1 por resultado; puede variar por funciones de la tabla |

## irons spellbooks — trial chambers/additional ominous vault loot

Tabla: `irons_spellbooks:chests/trial_chambers/additional_ominous_vault_loot` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 25 | 46.30 % | 1 por resultado; puede variar por funciones de la tabla |
| Ballesta de cargador automático (`irons_spellbooks:autoloader_crossbow`) | 8 | 14.81 % | 1 por resultado; puede variar por funciones de la tabla |
| weapon parts (`irons_spellbooks:weapon_parts`) | 2 | 3.70 % | 1 por resultado; puede variar por funciones de la tabla |
| Orbe de mejora vacío (`irons_spellbooks:upgrade_orb`) | 7 | 12.96 % | 1 por resultado; puede variar por funciones de la tabla |
| (Pergamino) (`irons_spellbooks:scroll`) | 12 | 22.22 % | Función: irons_spellbooks:randomize_spell |

**Grupo 2** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 8 | 33.33 % | 1 por resultado; puede variar por funciones de la tabla |
| (Pergamino) (`irons_spellbooks:scroll`) | 8 | 33.33 % | Función: irons_spellbooks:randomize_spell |
| Tabla adicional `irons_spellbooks:magic_items/great_ink` | 5 | 20.83 % | 1 por resultado; puede variar por funciones de la tabla |
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 3 | 12.50 % | Cantidad: {"min": 10, "max": 20} |

**Grupo 3** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| visibility ring (`irons_spellbooks:visibility_ring`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.075}]`.

## irons spellbooks — trial chambers/additional regular spawner consumable loot

Tabla: `irons_spellbooks:chests/trial_chambers/additional_regular_spawner_consumable_loot` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 25 | 60.98 % | 1 por resultado; puede variar por funciones de la tabla |
| potion (`minecraft:potion`) | 8 | 19.51 % | Función: minecraft:set_potion |
| potion (`minecraft:potion`) | 8 | 19.51 % | Función: minecraft:set_potion |

## irons spellbooks — trial chambers/additional regular vault loot

Tabla: `irons_spellbooks:chests/trial_chambers/additional_regular_vault_loot` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 10 | 34.48 % | 1 por resultado; puede variar por funciones de la tabla |
| (Pergamino) (`irons_spellbooks:scroll`) | 8 | 27.59 % | Función: irons_spellbooks:randomize_spell |
| Tabla adicional `irons_spellbooks:magic_items/good_ink` | 5 | 17.24 % | Cantidad: {"min": 1, "max": 2} |
| Tabla adicional `irons_spellbooks:magic_items/basic_curios` | 3 | 10.34 % | 1 por resultado; puede variar por funciones de la tabla |
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 3 | 10.34 % | Cantidad: {"min": 10, "max": 20} |

**Grupo 2** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 8 | 80.00 % | 1 por resultado; puede variar por funciones de la tabla |
| Piedra Rúnica en blanco (`irons_spellbooks:blank_rune`) | 2 | 20.00 % | 1 por resultado; puede variar por funciones de la tabla |

## irons spellbooks — trial chambers/additional trial chest loot

Tabla: `irons_spellbooks:chests/trial_chambers/additional_trial_chest_loot` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `2` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 4 | Condicionada; sin cifra única | Cantidad: {"min": 1, "max": 4} |
| Tela Arcana (`irons_spellbooks:magic_cloth`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.35}]`.

**Grupo 2** · tiradas: `2` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| (Pergamino) (`irons_spellbooks:scroll`) | 1 | Condicionada; sin cifra única | Función: irons_spellbooks:randomize_spell |
| Nada | 3 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.75}]`.

**Grupo 3** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Piedra Rúnica en blanco (`irons_spellbooks:blank_rune`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.08}]`.

**Grupo 4** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/basic_curios` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.075}]`.

**Grupo 5** · tiradas: `2` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/random_elixir` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |
| Nada | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.2}]`.

**Grupo 6** · tiradas: `{"min": 1, "max": 4}` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tabla adicional `irons_spellbooks:magic_items/good_ink` | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.25}]`.

## irons spellbooks — trial chambers/pot replacement

Tabla: `irons_spellbooks:chests/trial_chambers/pot_replacement` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 15 | 78.95 % | Cantidad: {"min": 1, "max": 7} |
| (Pergamino) (`irons_spellbooks:scroll`) | 4 | 21.05 % | Función: irons_spellbooks:randomize_spell |

## irons spellbooks — wheat

Tabla: `irons_spellbooks:chests/wheat` · fuente: `irons_spellbooks-1.20.1-3.16.3.jar`.

**Grupo 1** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| pumpkin (`minecraft:pumpkin`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.25}]`.

**Grupo 2** · tiradas: `12`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| wheat (`minecraft:wheat`) | 5 | 83.33 % | Cantidad: {"min": 1, "max": 4} |
| hay block (`minecraft:hay_block`) | 1 | 16.67 % | 1 por resultado; puede variar por funciones de la tabla |

## kaleidoscope nether — bastion hoglin stable

Tabla: `kaleidoscope_nether:chests/bastion_hoglin_stable` · fuente: `kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`.

**Grupo 1** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Cuchillo de cocina de diamante (`kaleidoscope_cookery:diamond_kitchen_knife`) | 1 | 16.67 % | Función: minecraft:set_damage; Función: minecraft:enchant_randomly |
| Cuchillo de cocina de oro (`kaleidoscope_cookery:gold_kitchen_knife`) | 2 | 33.33 % | Función: minecraft:enchant_randomly |
| Nada | 3 | 50.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 2** · tiradas: `{"type": "minecraft:uniform", "max": 2.0, "min": 1.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| soul pepper (`kaleidoscope_nether:soul_pepper`) | 5 | 33.33 % | Cantidad: {"type": "minecraft:uniform", "max": 6.0, "min": 3.0} |
| ham (`kaleidoscope_nether:ham`) | 4 | 26.67 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 2.0} |
| roasted ham (`kaleidoscope_nether:roasted_ham`) | 2 | 13.33 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| nether caterpillar (`kaleidoscope_nether:nether_caterpillar`) | 1 | 6.67 % | Cantidad: {"type": "minecraft:uniform", "max": 2.0, "min": 1.0} |
| Nada | 3 | 20.00 % | 1 por resultado; puede variar por funciones de la tabla |

## kaleidoscope nether — bastion treasure

Tabla: `kaleidoscope_nether:chests/bastion_treasure` · fuente: `kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`.

**Grupo 1** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Cuchillo de cocina de diamante (`kaleidoscope_cookery:diamond_kitchen_knife`) | 1 | 12.50 % | Función: minecraft:set_damage; Función: minecraft:enchant_randomly |
| Cuchillo de cocina de diamante (`kaleidoscope_cookery:diamond_kitchen_knife`) | 1 | 12.50 % | 1 por resultado; puede variar por funciones de la tabla |
| Nada | 6 | 75.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 2** · tiradas: `1`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| star dust (`kaleidoscope_nether:star_dust`) | 1 | 8.33 % | 1 por resultado; puede variar por funciones de la tabla |
| ghast pendant (`kaleidoscope_nether:ghast_pendant`) | 1 | 8.33 % | 1 por resultado; puede variar por funciones de la tabla |
| gilded fragment (`kaleidoscope_nether:gilded_fragment`) | 4 | 33.33 % | Cantidad: {"type": "minecraft:uniform", "max": 8.0, "min": 4.0} |
| Nada | 6 | 50.00 % | 1 por resultado; puede variar por funciones de la tabla |

## lootr — elytra

Tabla: `lootr:chests/elytra` · fuente: `lootr-forge-1.20-0.7.35.94.jar`.

**Grupo 1** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| elytra (`minecraft:elytra`) | 1 | 100.00 % | Cantidad: 1.0 |

## minecraft — abandoned mineshaft

Tabla: `minecraft:chests/abandoned_mineshaft` · fuente: `TheOptimizer_AdventureLoot.zip`.

Hay varias versiones de esta tabla; se ha priorizado el datapack del mundo y después el datapack global. Confirma el orden de carga si el mundo usa otros datapacks.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 2.0, "max": 4.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| tnt (`minecraft:tnt`) | 20 | 10.00 % | Cantidad: {"min": 2, "max": 5} |
| powered rail (`minecraft:powered_rail`) | 20 | 10.00 % | Cantidad: {"min": 4, "max": 12} |
| rail (`minecraft:rail`) | 25 | 12.50 % | Cantidad: {"min": 8, "max": 24} |
| gold ingot (`minecraft:gold_ingot`) | 15 | 7.50 % | Cantidad: {"min": 2, "max": 6} |
| iron ingot (`minecraft:iron_ingot`) | 20 | 10.00 % | Cantidad: {"min": 2, "max": 6} |
| diamond (`minecraft:diamond`) | 8 | 4.00 % | Cantidad: {"min": 1, "max": 2} |
| torch (`minecraft:torch`) | 20 | 10.00 % | Cantidad: {"min": 8, "max": 16} |
| golden apple (`minecraft:golden_apple`) | 12 | 6.00 % | 1 por resultado; puede variar por funciones de la tabla |
| book (`minecraft:book`) | 15 | 7.50 % | Función: minecraft:enchant_randomly |
| enchanted book (`minecraft:enchanted_book`) | 20 | 10.00 % | Función: minecraft:set_nbt |
| enchanted book (`minecraft:enchanted_book`) | 15 | 7.50 % | Función: minecraft:set_nbt |
| enchanted book (`minecraft:enchanted_book`) | 10 | 5.00 % | Función: minecraft:set_nbt |

## minecraft — ancient city

Tabla: `minecraft:chests/ancient_city` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 10.0, "min": 5.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| enchanted golden apple (`minecraft:enchanted_golden_apple`) | 1 | 1.16 % | Cantidad: {"type": "minecraft:uniform", "max": 2.0, "min": 1.0} |
| music disc otherside (`minecraft:music_disc_otherside`) | 1 | 1.16 % | 1 por resultado; puede variar por funciones de la tabla |
| compass (`minecraft:compass`) | 2 | 2.33 % | Cantidad: 1.0 |
| sculk catalyst (`minecraft:sculk_catalyst`) | 2 | 2.33 % | Cantidad: {"type": "minecraft:uniform", "max": 2.0, "min": 1.0} |
| name tag (`minecraft:name_tag`) | 2 | 2.33 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond hoe (`minecraft:diamond_hoe`) | 2 | 2.33 % | Cantidad: 1.0; Función: minecraft:set_damage; Función: minecraft:enchant_with_levels |
| lead (`minecraft:lead`) | 2 | 2.33 % | Cantidad: 1.0 |
| diamond horse armor (`minecraft:diamond_horse_armor`) | 2 | 2.33 % | Cantidad: 1.0 |
| saddle (`minecraft:saddle`) | 2 | 2.33 % | Cantidad: 1.0 |
| music disc 13 (`minecraft:music_disc_13`) | 2 | 2.33 % | 1 por resultado; puede variar por funciones de la tabla |
| music disc cat (`minecraft:music_disc_cat`) | 2 | 2.33 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond leggings (`minecraft:diamond_leggings`) | 2 | 2.33 % | Función: minecraft:enchant_with_levels |
| book (`minecraft:book`) | 3 | 3.49 % | Función: minecraft:enchant_randomly |
| sculk (`minecraft:sculk`) | 3 | 3.49 % | Cantidad: {"type": "minecraft:uniform", "max": 10.0, "min": 4.0} |
| sculk sensor (`minecraft:sculk_sensor`) | 3 | 3.49 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| candle (`minecraft:candle`) | 3 | 3.49 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| amethyst shard (`minecraft:amethyst_shard`) | 3 | 3.49 % | Cantidad: {"type": "minecraft:uniform", "max": 15.0, "min": 1.0} |
| experience bottle (`minecraft:experience_bottle`) | 3 | 3.49 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| glow berries (`minecraft:glow_berries`) | 3 | 3.49 % | Cantidad: {"type": "minecraft:uniform", "max": 15.0, "min": 1.0} |
| iron leggings (`minecraft:iron_leggings`) | 3 | 3.49 % | Función: minecraft:enchant_with_levels |
| echo shard (`minecraft:echo_shard`) | 4 | 4.65 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| disc fragment 5 (`minecraft:disc_fragment_5`) | 4 | 4.65 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| potion (`minecraft:potion`) | 5 | 5.81 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0}; Función: minecraft:set_potion |
| book (`minecraft:book`) | 5 | 5.81 % | Función: minecraft:enchant_randomly |
| book (`minecraft:book`) | 5 | 5.81 % | Cantidad: {"type": "minecraft:uniform", "max": 10.0, "min": 3.0} |
| bone (`minecraft:bone`) | 5 | 5.81 % | Cantidad: {"type": "minecraft:uniform", "max": 15.0, "min": 1.0} |
| soul torch (`minecraft:soul_torch`) | 5 | 5.81 % | Cantidad: {"type": "minecraft:uniform", "max": 15.0, "min": 1.0} |
| coal (`minecraft:coal`) | 7 | 8.14 % | Cantidad: {"type": "minecraft:uniform", "max": 15.0, "min": 6.0} |

**Grupo 2** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 75 | 93.75 % | 1 por resultado; puede variar por funciones de la tabla |
| ward armor trim smithing template (`minecraft:ward_armor_trim_smithing_template`) | 4 | 5.00 % | 1 por resultado; puede variar por funciones de la tabla |
| silence armor trim smithing template (`minecraft:silence_armor_trim_smithing_template`) | 1 | 1.25 % | 1 por resultado; puede variar por funciones de la tabla |

## minecraft — ancient city ice box

Tabla: `minecraft:chests/ancient_city_ice_box` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 10.0, "min": 4.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| suspicious stew (`minecraft:suspicious_stew`) | 1 | 11.11 % | Función: minecraft:set_stew_effect; Cantidad: {"type": "minecraft:uniform", "max": 6.0, "min": 2.0} |
| golden carrot (`minecraft:golden_carrot`) | 1 | 11.11 % | Cantidad: {"type": "minecraft:uniform", "max": 10.0, "min": 1.0} |
| baked potato (`minecraft:baked_potato`) | 1 | 11.11 % | Cantidad: {"type": "minecraft:uniform", "max": 10.0, "min": 1.0} |
| packed ice (`minecraft:packed_ice`) | 2 | 22.22 % | Cantidad: {"type": "minecraft:uniform", "max": 6.0, "min": 2.0} |
| snowball (`minecraft:snowball`) | 4 | 44.44 % | Cantidad: {"type": "minecraft:uniform", "max": 6.0, "min": 2.0} |

## minecraft — bastion bridge

Tabla: `minecraft:chests/bastion_bridge` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| lodestone (`minecraft:lodestone`) | 1 | 100.00 % | Cantidad: 1.0 |

**Grupo 2** · tiradas: `{"type": "minecraft:uniform", "max": 2.0, "min": 1.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| crossbow (`minecraft:crossbow`) | 1 | 7.69 % | Función: minecraft:set_damage; Función: minecraft:enchant_randomly |
| spectral arrow (`minecraft:spectral_arrow`) | 1 | 7.69 % | Cantidad: {"type": "minecraft:uniform", "max": 28.0, "min": 10.0} |
| gilded blackstone (`minecraft:gilded_blackstone`) | 1 | 7.69 % | Cantidad: {"type": "minecraft:uniform", "max": 12.0, "min": 8.0} |
| crying obsidian (`minecraft:crying_obsidian`) | 1 | 7.69 % | Cantidad: {"type": "minecraft:uniform", "max": 8.0, "min": 3.0} |
| gold block (`minecraft:gold_block`) | 1 | 7.69 % | Cantidad: 1.0 |
| gold ingot (`minecraft:gold_ingot`) | 1 | 7.69 % | Cantidad: {"type": "minecraft:uniform", "max": 9.0, "min": 4.0} |
| iron ingot (`minecraft:iron_ingot`) | 1 | 7.69 % | Cantidad: {"type": "minecraft:uniform", "max": 9.0, "min": 4.0} |
| golden sword (`minecraft:golden_sword`) | 1 | 7.69 % | Cantidad: 1.0 |
| golden chestplate (`minecraft:golden_chestplate`) | 1 | 7.69 % | Cantidad: 1.0; Función: minecraft:enchant_randomly |
| golden helmet (`minecraft:golden_helmet`) | 1 | 7.69 % | Cantidad: 1.0; Función: minecraft:enchant_randomly |
| golden leggings (`minecraft:golden_leggings`) | 1 | 7.69 % | Cantidad: 1.0; Función: minecraft:enchant_randomly |
| golden boots (`minecraft:golden_boots`) | 1 | 7.69 % | Cantidad: 1.0; Función: minecraft:enchant_randomly |
| golden axe (`minecraft:golden_axe`) | 1 | 7.69 % | Cantidad: 1.0; Función: minecraft:enchant_randomly |

**Grupo 3** · tiradas: `{"type": "minecraft:uniform", "max": 4.0, "min": 2.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| string (`minecraft:string`) | 1 | 20.00 % | Cantidad: {"type": "minecraft:uniform", "max": 6.0, "min": 1.0} |
| leather (`minecraft:leather`) | 1 | 20.00 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| arrow (`minecraft:arrow`) | 1 | 20.00 % | Cantidad: {"type": "minecraft:uniform", "max": 17.0, "min": 5.0} |
| iron nugget (`minecraft:iron_nugget`) | 1 | 20.00 % | Cantidad: {"type": "minecraft:uniform", "max": 6.0, "min": 2.0} |
| gold nugget (`minecraft:gold_nugget`) | 1 | 20.00 % | Cantidad: {"type": "minecraft:uniform", "max": 6.0, "min": 2.0} |

**Grupo 4** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 11 | 91.67 % | 1 por resultado; puede variar por funciones de la tabla |
| snout armor trim smithing template (`minecraft:snout_armor_trim_smithing_template`) | 1 | 8.33 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 5** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 9 | 90.00 % | 1 por resultado; puede variar por funciones de la tabla |
| netherite upgrade smithing template (`minecraft:netherite_upgrade_smithing_template`) | 1 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |

## minecraft — bastion hoglin stable

Tabla: `minecraft:chests/bastion_hoglin_stable` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| diamond shovel (`minecraft:diamond_shovel`) | 15 | 15.00 % | Función: minecraft:set_damage; Función: minecraft:enchant_randomly |
| diamond pickaxe (`minecraft:diamond_pickaxe`) | 12 | 12.00 % | Función: minecraft:set_damage; Cantidad: 1.0; Función: minecraft:enchant_randomly |
| netherite scrap (`minecraft:netherite_scrap`) | 8 | 8.00 % | Cantidad: 1.0 |
| ancient debris (`minecraft:ancient_debris`) | 12 | 12.00 % | Cantidad: 1.0 |
| ancient debris (`minecraft:ancient_debris`) | 5 | 5.00 % | Cantidad: 2.0 |
| saddle (`minecraft:saddle`) | 12 | 12.00 % | Cantidad: 1.0 |
| gold block (`minecraft:gold_block`) | 16 | 16.00 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 2.0} |
| golden carrot (`minecraft:golden_carrot`) | 10 | 10.00 % | Cantidad: {"type": "minecraft:uniform", "max": 17.0, "min": 8.0} |
| golden apple (`minecraft:golden_apple`) | 10 | 10.00 % | Cantidad: 1.0 |

**Grupo 2** · tiradas: `{"type": "minecraft:uniform", "max": 4.0, "min": 3.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| golden axe (`minecraft:golden_axe`) | 1 | 7.14 % | Cantidad: 1.0; Función: minecraft:enchant_randomly |
| crying obsidian (`minecraft:crying_obsidian`) | 1 | 7.14 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 1.0} |
| glowstone (`minecraft:glowstone`) | 1 | 7.14 % | Cantidad: {"type": "minecraft:uniform", "max": 6.0, "min": 3.0} |
| gilded blackstone (`minecraft:gilded_blackstone`) | 1 | 7.14 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 2.0} |
| soul sand (`minecraft:soul_sand`) | 1 | 7.14 % | Cantidad: {"type": "minecraft:uniform", "max": 7.0, "min": 2.0} |
| crimson nylium (`minecraft:crimson_nylium`) | 1 | 7.14 % | Cantidad: {"type": "minecraft:uniform", "max": 7.0, "min": 2.0} |
| gold nugget (`minecraft:gold_nugget`) | 1 | 7.14 % | Cantidad: {"type": "minecraft:uniform", "max": 8.0, "min": 2.0} |
| leather (`minecraft:leather`) | 1 | 7.14 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| arrow (`minecraft:arrow`) | 1 | 7.14 % | Cantidad: {"type": "minecraft:uniform", "max": 17.0, "min": 5.0} |
| string (`minecraft:string`) | 1 | 7.14 % | Cantidad: {"type": "minecraft:uniform", "max": 8.0, "min": 3.0} |
| porkchop (`minecraft:porkchop`) | 1 | 7.14 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 2.0} |
| cooked porkchop (`minecraft:cooked_porkchop`) | 1 | 7.14 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 2.0} |
| crimson fungus (`minecraft:crimson_fungus`) | 1 | 7.14 % | Cantidad: {"type": "minecraft:uniform", "max": 7.0, "min": 2.0} |
| crimson roots (`minecraft:crimson_roots`) | 1 | 7.14 % | Cantidad: {"type": "minecraft:uniform", "max": 7.0, "min": 2.0} |

**Grupo 3** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 11 | 91.67 % | 1 por resultado; puede variar por funciones de la tabla |
| snout armor trim smithing template (`minecraft:snout_armor_trim_smithing_template`) | 1 | 8.33 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 4** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 9 | 90.00 % | 1 por resultado; puede variar por funciones de la tabla |
| netherite upgrade smithing template (`minecraft:netherite_upgrade_smithing_template`) | 1 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |

## minecraft — bastion other

Tabla: `minecraft:chests/bastion_other` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| diamond pickaxe (`minecraft:diamond_pickaxe`) | 6 | 6.74 % | Cantidad: 1.0; Función: minecraft:enchant_randomly |
| diamond shovel (`minecraft:diamond_shovel`) | 6 | 6.74 % | Cantidad: 1.0 |
| crossbow (`minecraft:crossbow`) | 6 | 6.74 % | Función: minecraft:set_damage; Función: minecraft:enchant_randomly |
| ancient debris (`minecraft:ancient_debris`) | 12 | 13.48 % | Cantidad: 1.0 |
| netherite scrap (`minecraft:netherite_scrap`) | 4 | 4.49 % | Cantidad: 1.0 |
| spectral arrow (`minecraft:spectral_arrow`) | 10 | 11.24 % | Cantidad: {"type": "minecraft:uniform", "max": 22.0, "min": 10.0} |
| piglin banner pattern (`minecraft:piglin_banner_pattern`) | 9 | 10.11 % | Cantidad: 1.0 |
| music disc pigstep (`minecraft:music_disc_pigstep`) | 5 | 5.62 % | Cantidad: 1.0 |
| golden carrot (`minecraft:golden_carrot`) | 12 | 13.48 % | Cantidad: {"type": "minecraft:uniform", "max": 17.0, "min": 6.0} |
| golden apple (`minecraft:golden_apple`) | 9 | 10.11 % | Cantidad: 1.0 |
| book (`minecraft:book`) | 10 | 11.24 % | Función: minecraft:enchant_randomly |

**Grupo 2** · tiradas: `2.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| iron sword (`minecraft:iron_sword`) | 2 | 10.00 % | Función: minecraft:set_damage; Cantidad: 1.0; Función: minecraft:enchant_randomly |
| iron block (`minecraft:iron_block`) | 2 | 10.00 % | Cantidad: 1.0 |
| golden boots (`minecraft:golden_boots`) | 1 | 5.00 % | Cantidad: 1.0; Función: minecraft:enchant_randomly |
| golden axe (`minecraft:golden_axe`) | 1 | 5.00 % | Cantidad: 1.0; Función: minecraft:enchant_randomly |
| gold block (`minecraft:gold_block`) | 2 | 10.00 % | Cantidad: 1.0 |
| crossbow (`minecraft:crossbow`) | 1 | 5.00 % | Cantidad: 1.0 |
| gold ingot (`minecraft:gold_ingot`) | 2 | 10.00 % | Cantidad: {"type": "minecraft:uniform", "max": 6.0, "min": 1.0} |
| iron ingot (`minecraft:iron_ingot`) | 2 | 10.00 % | Cantidad: {"type": "minecraft:uniform", "max": 6.0, "min": 1.0} |
| golden sword (`minecraft:golden_sword`) | 1 | 5.00 % | Cantidad: 1.0 |
| golden chestplate (`minecraft:golden_chestplate`) | 1 | 5.00 % | Cantidad: 1.0 |
| golden helmet (`minecraft:golden_helmet`) | 1 | 5.00 % | Cantidad: 1.0 |
| golden leggings (`minecraft:golden_leggings`) | 1 | 5.00 % | Cantidad: 1.0 |
| golden boots (`minecraft:golden_boots`) | 1 | 5.00 % | Cantidad: 1.0 |
| crying obsidian (`minecraft:crying_obsidian`) | 2 | 10.00 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 1.0} |

**Grupo 3** · tiradas: `{"type": "minecraft:uniform", "max": 4.0, "min": 3.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| gilded blackstone (`minecraft:gilded_blackstone`) | 2 | 15.38 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 1.0} |
| chain (`minecraft:chain`) | 1 | 7.69 % | Cantidad: {"type": "minecraft:uniform", "max": 10.0, "min": 2.0} |
| magma cream (`minecraft:magma_cream`) | 2 | 15.38 % | Cantidad: {"type": "minecraft:uniform", "max": 6.0, "min": 2.0} |
| bone block (`minecraft:bone_block`) | 1 | 7.69 % | Cantidad: {"type": "minecraft:uniform", "max": 6.0, "min": 3.0} |
| iron nugget (`minecraft:iron_nugget`) | 1 | 7.69 % | Cantidad: {"type": "minecraft:uniform", "max": 8.0, "min": 2.0} |
| obsidian (`minecraft:obsidian`) | 1 | 7.69 % | Cantidad: {"type": "minecraft:uniform", "max": 6.0, "min": 4.0} |
| gold nugget (`minecraft:gold_nugget`) | 1 | 7.69 % | Cantidad: {"type": "minecraft:uniform", "max": 8.0, "min": 2.0} |
| string (`minecraft:string`) | 1 | 7.69 % | Cantidad: {"type": "minecraft:uniform", "max": 6.0, "min": 4.0} |
| arrow (`minecraft:arrow`) | 2 | 15.38 % | Cantidad: {"type": "minecraft:uniform", "max": 17.0, "min": 5.0} |
| cooked porkchop (`minecraft:cooked_porkchop`) | 1 | 7.69 % | Cantidad: 1.0 |

**Grupo 4** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 11 | 91.67 % | 1 por resultado; puede variar por funciones de la tabla |
| snout armor trim smithing template (`minecraft:snout_armor_trim_smithing_template`) | 1 | 8.33 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 5** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 9 | 90.00 % | 1 por resultado; puede variar por funciones de la tabla |
| netherite upgrade smithing template (`minecraft:netherite_upgrade_smithing_template`) | 1 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |

## minecraft — bastion treasure

Tabla: `minecraft:chests/bastion_treasure` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `3.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| netherite ingot (`minecraft:netherite_ingot`) | 15 | 15.00 % | Cantidad: 1.0 |
| ancient debris (`minecraft:ancient_debris`) | 10 | 10.00 % | Cantidad: 1.0 |
| netherite scrap (`minecraft:netherite_scrap`) | 8 | 8.00 % | Cantidad: 1.0 |
| ancient debris (`minecraft:ancient_debris`) | 4 | 4.00 % | Cantidad: 2.0 |
| diamond sword (`minecraft:diamond_sword`) | 6 | 6.00 % | Función: minecraft:set_damage; Función: minecraft:enchant_randomly |
| diamond chestplate (`minecraft:diamond_chestplate`) | 6 | 6.00 % | Función: minecraft:set_damage; Función: minecraft:enchant_randomly |
| diamond helmet (`minecraft:diamond_helmet`) | 6 | 6.00 % | Función: minecraft:set_damage; Función: minecraft:enchant_randomly |
| diamond leggings (`minecraft:diamond_leggings`) | 6 | 6.00 % | Función: minecraft:set_damage; Función: minecraft:enchant_randomly |
| diamond boots (`minecraft:diamond_boots`) | 6 | 6.00 % | Función: minecraft:set_damage; Función: minecraft:enchant_randomly |
| diamond sword (`minecraft:diamond_sword`) | 6 | 6.00 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond chestplate (`minecraft:diamond_chestplate`) | 5 | 5.00 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond helmet (`minecraft:diamond_helmet`) | 5 | 5.00 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond boots (`minecraft:diamond_boots`) | 5 | 5.00 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond leggings (`minecraft:diamond_leggings`) | 5 | 5.00 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond (`minecraft:diamond`) | 5 | 5.00 % | Cantidad: {"type": "minecraft:uniform", "max": 6.0, "min": 2.0} |
| enchanted golden apple (`minecraft:enchanted_golden_apple`) | 2 | 2.00 % | Cantidad: 1.0 |

**Grupo 2** · tiradas: `{"type": "minecraft:uniform", "max": 4.0, "min": 3.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| spectral arrow (`minecraft:spectral_arrow`) | 1 | 11.11 % | Cantidad: {"type": "minecraft:uniform", "max": 25.0, "min": 12.0} |
| gold block (`minecraft:gold_block`) | 1 | 11.11 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 2.0} |
| iron block (`minecraft:iron_block`) | 1 | 11.11 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 2.0} |
| gold ingot (`minecraft:gold_ingot`) | 1 | 11.11 % | Cantidad: {"type": "minecraft:uniform", "max": 9.0, "min": 3.0} |
| iron ingot (`minecraft:iron_ingot`) | 1 | 11.11 % | Cantidad: {"type": "minecraft:uniform", "max": 9.0, "min": 3.0} |
| crying obsidian (`minecraft:crying_obsidian`) | 1 | 11.11 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 3.0} |
| quartz (`minecraft:quartz`) | 1 | 11.11 % | Cantidad: {"type": "minecraft:uniform", "max": 23.0, "min": 8.0} |
| gilded blackstone (`minecraft:gilded_blackstone`) | 1 | 11.11 % | Cantidad: {"type": "minecraft:uniform", "max": 15.0, "min": 5.0} |
| magma cream (`minecraft:magma_cream`) | 1 | 11.11 % | Cantidad: {"type": "minecraft:uniform", "max": 8.0, "min": 3.0} |

**Grupo 3** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 11 | 91.67 % | 1 por resultado; puede variar por funciones de la tabla |
| snout armor trim smithing template (`minecraft:snout_armor_trim_smithing_template`) | 1 | 8.33 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 4** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| netherite upgrade smithing template (`minecraft:netherite_upgrade_smithing_template`) | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

## minecraft — buried treasure

Tabla: `minecraft:chests/buried_treasure` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| heart of the sea (`minecraft:heart_of_the_sea`) | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 2** · tiradas: `{"type": "minecraft:uniform", "max": 8.0, "min": 5.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| iron ingot (`minecraft:iron_ingot`) | 20 | 57.14 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| gold ingot (`minecraft:gold_ingot`) | 10 | 28.57 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| tnt (`minecraft:tnt`) | 5 | 14.29 % | Cantidad: {"type": "minecraft:uniform", "max": 2.0, "min": 1.0} |

**Grupo 3** · tiradas: `{"type": "minecraft:uniform", "max": 3.0, "min": 1.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| emerald (`minecraft:emerald`) | 5 | 33.33 % | Cantidad: {"type": "minecraft:uniform", "max": 8.0, "min": 4.0} |
| diamond (`minecraft:diamond`) | 5 | 33.33 % | Cantidad: {"type": "minecraft:uniform", "max": 2.0, "min": 1.0} |
| prismarine crystals (`minecraft:prismarine_crystals`) | 5 | 33.33 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 1.0} |

**Grupo 4** · tiradas: `{"type": "minecraft:uniform", "max": 1.0, "min": 0.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| leather chestplate (`minecraft:leather_chestplate`) | 1 | 50.00 % | 1 por resultado; puede variar por funciones de la tabla |
| iron sword (`minecraft:iron_sword`) | 1 | 50.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 5** · tiradas: `2.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| cooked cod (`minecraft:cooked_cod`) | 1 | 50.00 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 2.0} |
| cooked salmon (`minecraft:cooked_salmon`) | 1 | 50.00 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 2.0} |

**Grupo 6** · tiradas: `{"type": "minecraft:uniform", "max": 2.0, "min": 0.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| potion (`minecraft:potion`) | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

## minecraft — desert pyramid

Tabla: `minecraft:chests/desert_pyramid` · fuente: `TheOptimizer_AdventureLoot.zip`.

Hay varias versiones de esta tabla; se ha priorizado el datapack del mundo y después el datapack global. Confirma el orden de carga si el mundo usa otros datapacks.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 3.0, "max": 5.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| gold ingot (`minecraft:gold_ingot`) | 25 | 13.37 % | Cantidad: {"min": 3, "max": 8} |
| iron ingot (`minecraft:iron_ingot`) | 20 | 10.70 % | Cantidad: {"min": 2, "max": 6} |
| diamond (`minecraft:diamond`) | 10 | 5.35 % | Cantidad: {"min": 1, "max": 3} |
| emerald (`minecraft:emerald`) | 20 | 10.70 % | Cantidad: {"min": 3, "max": 8} |
| experience bottle (`minecraft:experience_bottle`) | 15 | 8.02 % | Cantidad: {"min": 2, "max": 6} |
| book (`minecraft:book`) | 15 | 8.02 % | Función: minecraft:enchant_randomly |
| enchanted book (`minecraft:enchanted_book`) | 15 | 8.02 % | Función: minecraft:set_nbt |
| enchanted book (`minecraft:enchanted_book`) | 12 | 6.42 % | Función: minecraft:set_nbt |
| enchanted book (`minecraft:enchanted_book`) | 10 | 5.35 % | Función: minecraft:set_nbt |
| enchanted book (`minecraft:enchanted_book`) | 12 | 6.42 % | Función: minecraft:set_nbt |
| enchanted book (`minecraft:enchanted_book`) | 10 | 5.35 % | Función: minecraft:set_nbt |
| golden apple (`minecraft:golden_apple`) | 20 | 10.70 % | 1 por resultado; puede variar por funciones de la tabla |
| enchanted golden apple (`minecraft:enchanted_golden_apple`) | 3 | 1.60 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 2** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| gunpowder (`minecraft:gunpowder`) | 10 | 55.56 % | Cantidad: {"min": 3, "max": 8} |
| bone (`minecraft:bone`) | 8 | 44.44 % | Cantidad: {"min": 2, "max": 5} |

**Grupo 3** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 2 | 66.67 % | 1 por resultado; puede variar por funciones de la tabla |
| dune armor trim smithing template (`minecraft:dune_armor_trim_smithing_template`) | 1 | 33.33 % | 1 por resultado; puede variar por funciones de la tabla |

## minecraft — end city treasure

Tabla: `minecraft:chests/end_city_treasure` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 6.0, "min": 2.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| diamond (`minecraft:diamond`) | 5 | 5.88 % | Cantidad: {"type": "minecraft:uniform", "max": 7.0, "min": 2.0} |
| iron ingot (`minecraft:iron_ingot`) | 10 | 11.76 % | Cantidad: {"type": "minecraft:uniform", "max": 8.0, "min": 4.0} |
| gold ingot (`minecraft:gold_ingot`) | 15 | 17.65 % | Cantidad: {"type": "minecraft:uniform", "max": 7.0, "min": 2.0} |
| emerald (`minecraft:emerald`) | 2 | 2.35 % | Cantidad: {"type": "minecraft:uniform", "max": 6.0, "min": 2.0} |
| beetroot seeds (`minecraft:beetroot_seeds`) | 5 | 5.88 % | Cantidad: {"type": "minecraft:uniform", "max": 10.0, "min": 1.0} |
| saddle (`minecraft:saddle`) | 3 | 3.53 % | 1 por resultado; puede variar por funciones de la tabla |
| iron horse armor (`minecraft:iron_horse_armor`) | 1 | 1.18 % | 1 por resultado; puede variar por funciones de la tabla |
| golden horse armor (`minecraft:golden_horse_armor`) | 1 | 1.18 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond horse armor (`minecraft:diamond_horse_armor`) | 1 | 1.18 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond sword (`minecraft:diamond_sword`) | 3 | 3.53 % | Función: minecraft:enchant_with_levels |
| diamond boots (`minecraft:diamond_boots`) | 3 | 3.53 % | Función: minecraft:enchant_with_levels |
| diamond chestplate (`minecraft:diamond_chestplate`) | 3 | 3.53 % | Función: minecraft:enchant_with_levels |
| diamond leggings (`minecraft:diamond_leggings`) | 3 | 3.53 % | Función: minecraft:enchant_with_levels |
| diamond helmet (`minecraft:diamond_helmet`) | 3 | 3.53 % | Función: minecraft:enchant_with_levels |
| diamond pickaxe (`minecraft:diamond_pickaxe`) | 3 | 3.53 % | Función: minecraft:enchant_with_levels |
| diamond shovel (`minecraft:diamond_shovel`) | 3 | 3.53 % | Función: minecraft:enchant_with_levels |
| iron sword (`minecraft:iron_sword`) | 3 | 3.53 % | Función: minecraft:enchant_with_levels |
| iron boots (`minecraft:iron_boots`) | 3 | 3.53 % | Función: minecraft:enchant_with_levels |
| iron chestplate (`minecraft:iron_chestplate`) | 3 | 3.53 % | Función: minecraft:enchant_with_levels |
| iron leggings (`minecraft:iron_leggings`) | 3 | 3.53 % | Función: minecraft:enchant_with_levels |
| iron helmet (`minecraft:iron_helmet`) | 3 | 3.53 % | Función: minecraft:enchant_with_levels |
| iron pickaxe (`minecraft:iron_pickaxe`) | 3 | 3.53 % | Función: minecraft:enchant_with_levels |
| iron shovel (`minecraft:iron_shovel`) | 3 | 3.53 % | Función: minecraft:enchant_with_levels |

**Grupo 2** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 14 | 93.33 % | 1 por resultado; puede variar por funciones de la tabla |
| spire armor trim smithing template (`minecraft:spire_armor_trim_smithing_template`) | 1 | 6.67 % | 1 por resultado; puede variar por funciones de la tabla |

## minecraft — igloo chest

Tabla: `minecraft:chests/igloo_chest` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 8.0, "min": 2.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| apple (`minecraft:apple`) | 15 | 23.81 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| coal (`minecraft:coal`) | 15 | 23.81 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| gold nugget (`minecraft:gold_nugget`) | 10 | 15.87 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| stone axe (`minecraft:stone_axe`) | 2 | 3.17 % | 1 por resultado; puede variar por funciones de la tabla |
| rotten flesh (`minecraft:rotten_flesh`) | 10 | 15.87 % | 1 por resultado; puede variar por funciones de la tabla |
| emerald (`minecraft:emerald`) | 1 | 1.59 % | 1 por resultado; puede variar por funciones de la tabla |
| wheat (`minecraft:wheat`) | 10 | 15.87 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 2.0} |

**Grupo 2** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| golden apple (`minecraft:golden_apple`) | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

## minecraft — jungle temple

Tabla: `minecraft:chests/jungle_temple` · fuente: `TheOptimizer_AdventureLoot.zip`.

Hay varias versiones de esta tabla; se ha priorizado el datapack del mundo y después el datapack global. Confirma el orden de carga si el mundo usa otros datapacks.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 3.0, "max": 5.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| gold ingot (`minecraft:gold_ingot`) | 25 | 16.67 % | Cantidad: {"min": 3, "max": 8} |
| diamond (`minecraft:diamond`) | 8 | 5.33 % | Cantidad: {"min": 1, "max": 3} |
| emerald (`minecraft:emerald`) | 20 | 13.33 % | Cantidad: {"min": 3, "max": 8} |
| bamboo (`minecraft:bamboo`) | 15 | 10.00 % | Cantidad: {"min": 6, "max": 16} |
| experience bottle (`minecraft:experience_bottle`) | 15 | 10.00 % | Cantidad: {"min": 2, "max": 5} |
| golden apple (`minecraft:golden_apple`) | 15 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |
| book (`minecraft:book`) | 15 | 10.00 % | Función: minecraft:enchant_randomly |
| enchanted book (`minecraft:enchanted_book`) | 15 | 10.00 % | Función: minecraft:set_nbt |
| enchanted book (`minecraft:enchanted_book`) | 12 | 8.00 % | Función: minecraft:set_nbt |
| enchanted book (`minecraft:enchanted_book`) | 10 | 6.67 % | Función: minecraft:set_nbt |

**Grupo 2** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 2 | 66.67 % | 1 por resultado; puede variar por funciones de la tabla |
| wild armor trim smithing template (`minecraft:wild_armor_trim_smithing_template`) | 1 | 33.33 % | 1 por resultado; puede variar por funciones de la tabla |

## minecraft — jungle temple dispenser

Tabla: `minecraft:chests/jungle_temple_dispenser` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 2.0, "min": 1.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| arrow (`minecraft:arrow`) | 30 | 100.00 % | Cantidad: {"type": "minecraft:uniform", "max": 7.0, "min": 2.0} |

## minecraft — nether bridge

Tabla: `minecraft:chests/nether_bridge` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 4.0, "min": 2.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| diamond (`minecraft:diamond`) | 5 | 6.85 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| iron ingot (`minecraft:iron_ingot`) | 5 | 6.85 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 1.0} |
| gold ingot (`minecraft:gold_ingot`) | 15 | 20.55 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| golden sword (`minecraft:golden_sword`) | 5 | 6.85 % | 1 por resultado; puede variar por funciones de la tabla |
| golden chestplate (`minecraft:golden_chestplate`) | 5 | 6.85 % | 1 por resultado; puede variar por funciones de la tabla |
| flint and steel (`minecraft:flint_and_steel`) | 5 | 6.85 % | 1 por resultado; puede variar por funciones de la tabla |
| nether wart (`minecraft:nether_wart`) | 5 | 6.85 % | Cantidad: {"type": "minecraft:uniform", "max": 7.0, "min": 3.0} |
| saddle (`minecraft:saddle`) | 10 | 13.70 % | 1 por resultado; puede variar por funciones de la tabla |
| golden horse armor (`minecraft:golden_horse_armor`) | 8 | 10.96 % | 1 por resultado; puede variar por funciones de la tabla |
| iron horse armor (`minecraft:iron_horse_armor`) | 5 | 6.85 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond horse armor (`minecraft:diamond_horse_armor`) | 3 | 4.11 % | 1 por resultado; puede variar por funciones de la tabla |
| obsidian (`minecraft:obsidian`) | 2 | 2.74 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 2.0} |

**Grupo 2** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 14 | 93.33 % | 1 por resultado; puede variar por funciones de la tabla |
| rib armor trim smithing template (`minecraft:rib_armor_trim_smithing_template`) | 1 | 6.67 % | 1 por resultado; puede variar por funciones de la tabla |

## minecraft — pillager outpost

Tabla: `minecraft:chests/pillager_outpost` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 1.0, "min": 0.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| crossbow (`minecraft:crossbow`) | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 2** · tiradas: `{"type": "minecraft:uniform", "max": 3.0, "min": 2.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| wheat (`minecraft:wheat`) | 7 | 41.18 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 3.0} |
| potato (`minecraft:potato`) | 5 | 29.41 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 2.0} |
| carrot (`minecraft:carrot`) | 5 | 29.41 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 3.0} |

**Grupo 3** · tiradas: `{"type": "minecraft:uniform", "max": 3.0, "min": 1.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| dark oak log (`minecraft:dark_oak_log`) | 1 | 100.00 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 2.0} |

**Grupo 4** · tiradas: `{"type": "minecraft:uniform", "max": 3.0, "min": 2.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| experience bottle (`minecraft:experience_bottle`) | 7 | 31.82 % | 1 por resultado; puede variar por funciones de la tabla |
| string (`minecraft:string`) | 4 | 18.18 % | Cantidad: {"type": "minecraft:uniform", "max": 6.0, "min": 1.0} |
| arrow (`minecraft:arrow`) | 4 | 18.18 % | Cantidad: {"type": "minecraft:uniform", "max": 7.0, "min": 2.0} |
| tripwire hook (`minecraft:tripwire_hook`) | 3 | 13.64 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| iron ingot (`minecraft:iron_ingot`) | 3 | 13.64 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| book (`minecraft:book`) | 1 | 4.55 % | Función: minecraft:enchant_randomly |

**Grupo 5** · tiradas: `{"type": "minecraft:uniform", "max": 1.0, "min": 0.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| goat horn (`minecraft:goat_horn`) | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 6** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 3 | 75.00 % | 1 por resultado; puede variar por funciones de la tabla |
| sentry armor trim smithing template (`minecraft:sentry_armor_trim_smithing_template`) | 1 | 25.00 % | Cantidad: 2.0 |

## minecraft — ruined portal

Tabla: `minecraft:chests/ruined_portal` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 8.0, "min": 4.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| obsidian (`minecraft:obsidian`) | 40 | 10.05 % | Cantidad: {"type": "minecraft:uniform", "max": 2.0, "min": 1.0} |
| flint (`minecraft:flint`) | 40 | 10.05 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| iron nugget (`minecraft:iron_nugget`) | 40 | 10.05 % | Cantidad: {"type": "minecraft:uniform", "max": 18.0, "min": 9.0} |
| flint and steel (`minecraft:flint_and_steel`) | 40 | 10.05 % | 1 por resultado; puede variar por funciones de la tabla |
| fire charge (`minecraft:fire_charge`) | 40 | 10.05 % | 1 por resultado; puede variar por funciones de la tabla |
| golden apple (`minecraft:golden_apple`) | 15 | 3.77 % | 1 por resultado; puede variar por funciones de la tabla |
| gold nugget (`minecraft:gold_nugget`) | 15 | 3.77 % | Cantidad: {"type": "minecraft:uniform", "max": 24.0, "min": 4.0} |
| golden sword (`minecraft:golden_sword`) | 15 | 3.77 % | Función: minecraft:enchant_randomly |
| golden axe (`minecraft:golden_axe`) | 15 | 3.77 % | Función: minecraft:enchant_randomly |
| golden hoe (`minecraft:golden_hoe`) | 15 | 3.77 % | Función: minecraft:enchant_randomly |
| golden shovel (`minecraft:golden_shovel`) | 15 | 3.77 % | Función: minecraft:enchant_randomly |
| golden pickaxe (`minecraft:golden_pickaxe`) | 15 | 3.77 % | Función: minecraft:enchant_randomly |
| golden boots (`minecraft:golden_boots`) | 15 | 3.77 % | Función: minecraft:enchant_randomly |
| golden chestplate (`minecraft:golden_chestplate`) | 15 | 3.77 % | Función: minecraft:enchant_randomly |
| golden helmet (`minecraft:golden_helmet`) | 15 | 3.77 % | Función: minecraft:enchant_randomly |
| golden leggings (`minecraft:golden_leggings`) | 15 | 3.77 % | Función: minecraft:enchant_randomly |
| glistering melon slice (`minecraft:glistering_melon_slice`) | 5 | 1.26 % | Cantidad: {"type": "minecraft:uniform", "max": 12.0, "min": 4.0} |
| golden horse armor (`minecraft:golden_horse_armor`) | 5 | 1.26 % | 1 por resultado; puede variar por funciones de la tabla |
| light weighted pressure plate (`minecraft:light_weighted_pressure_plate`) | 5 | 1.26 % | 1 por resultado; puede variar por funciones de la tabla |
| golden carrot (`minecraft:golden_carrot`) | 5 | 1.26 % | Cantidad: {"type": "minecraft:uniform", "max": 12.0, "min": 4.0} |
| clock (`minecraft:clock`) | 5 | 1.26 % | 1 por resultado; puede variar por funciones de la tabla |
| gold ingot (`minecraft:gold_ingot`) | 5 | 1.26 % | Cantidad: {"type": "minecraft:uniform", "max": 8.0, "min": 2.0} |
| bell (`minecraft:bell`) | 1 | 0.25 % | 1 por resultado; puede variar por funciones de la tabla |
| enchanted golden apple (`minecraft:enchanted_golden_apple`) | 1 | 0.25 % | 1 por resultado; puede variar por funciones de la tabla |
| gold block (`minecraft:gold_block`) | 1 | 0.25 % | Cantidad: {"type": "minecraft:uniform", "max": 2.0, "min": 1.0} |

## minecraft — shipwreck map

Tabla: `minecraft:chests/shipwreck_map` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| map (`minecraft:map`) | 1 | 100.00 % | Función: minecraft:exploration_map; Función: minecraft:set_name |

**Grupo 2** · tiradas: `3.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| compass (`minecraft:compass`) | 1 | 2.63 % | 1 por resultado; puede variar por funciones de la tabla |
| map (`minecraft:map`) | 1 | 2.63 % | 1 por resultado; puede variar por funciones de la tabla |
| clock (`minecraft:clock`) | 1 | 2.63 % | 1 por resultado; puede variar por funciones de la tabla |
| paper (`minecraft:paper`) | 20 | 52.63 % | Cantidad: {"type": "minecraft:uniform", "max": 10.0, "min": 1.0} |
| feather (`minecraft:feather`) | 10 | 26.32 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 1.0} |
| book (`minecraft:book`) | 5 | 13.16 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 1.0} |

**Grupo 3** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 5 | 83.33 % | 1 por resultado; puede variar por funciones de la tabla |
| coast armor trim smithing template (`minecraft:coast_armor_trim_smithing_template`) | 1 | 16.67 % | Cantidad: 2.0 |

## minecraft — shipwreck supply

Tabla: `minecraft:chests/shipwreck_supply` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 10.0, "min": 3.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| paper (`minecraft:paper`) | 8 | 9.52 % | Cantidad: {"type": "minecraft:uniform", "max": 12.0, "min": 1.0} |
| potato (`minecraft:potato`) | 7 | 8.33 % | Cantidad: {"type": "minecraft:uniform", "max": 6.0, "min": 2.0} |
| moss block (`minecraft:moss_block`) | 7 | 8.33 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| poisonous potato (`minecraft:poisonous_potato`) | 7 | 8.33 % | Cantidad: {"type": "minecraft:uniform", "max": 6.0, "min": 2.0} |
| carrot (`minecraft:carrot`) | 7 | 8.33 % | Cantidad: {"type": "minecraft:uniform", "max": 8.0, "min": 4.0} |
| wheat (`minecraft:wheat`) | 7 | 8.33 % | Cantidad: {"type": "minecraft:uniform", "max": 21.0, "min": 8.0} |
| suspicious stew (`minecraft:suspicious_stew`) | 10 | 11.90 % | Función: minecraft:set_stew_effect |
| coal (`minecraft:coal`) | 6 | 7.14 % | Cantidad: {"type": "minecraft:uniform", "max": 8.0, "min": 2.0} |
| rotten flesh (`minecraft:rotten_flesh`) | 5 | 5.95 % | Cantidad: {"type": "minecraft:uniform", "max": 24.0, "min": 5.0} |
| pumpkin (`minecraft:pumpkin`) | 2 | 2.38 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| bamboo (`minecraft:bamboo`) | 2 | 2.38 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| gunpowder (`minecraft:gunpowder`) | 3 | 3.57 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 1.0} |
| tnt (`minecraft:tnt`) | 1 | 1.19 % | Cantidad: {"type": "minecraft:uniform", "max": 2.0, "min": 1.0} |
| leather helmet (`minecraft:leather_helmet`) | 3 | 3.57 % | Función: minecraft:enchant_randomly |
| leather chestplate (`minecraft:leather_chestplate`) | 3 | 3.57 % | Función: minecraft:enchant_randomly |
| leather leggings (`minecraft:leather_leggings`) | 3 | 3.57 % | Función: minecraft:enchant_randomly |
| leather boots (`minecraft:leather_boots`) | 3 | 3.57 % | Función: minecraft:enchant_randomly |

**Grupo 2** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 5 | 83.33 % | 1 por resultado; puede variar por funciones de la tabla |
| coast armor trim smithing template (`minecraft:coast_armor_trim_smithing_template`) | 1 | 16.67 % | Cantidad: 2.0 |

## minecraft — shipwreck treasure

Tabla: `minecraft:chests/shipwreck_treasure` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 6.0, "min": 3.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| iron ingot (`minecraft:iron_ingot`) | 90 | 60.00 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 1.0} |
| gold ingot (`minecraft:gold_ingot`) | 10 | 6.67 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 1.0} |
| emerald (`minecraft:emerald`) | 40 | 26.67 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 1.0} |
| diamond (`minecraft:diamond`) | 5 | 3.33 % | 1 por resultado; puede variar por funciones de la tabla |
| experience bottle (`minecraft:experience_bottle`) | 5 | 3.33 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 2** · tiradas: `{"type": "minecraft:uniform", "max": 5.0, "min": 2.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| iron nugget (`minecraft:iron_nugget`) | 50 | 62.50 % | Cantidad: {"type": "minecraft:uniform", "max": 10.0, "min": 1.0} |
| gold nugget (`minecraft:gold_nugget`) | 10 | 12.50 % | Cantidad: {"type": "minecraft:uniform", "max": 10.0, "min": 1.0} |
| lapis lazuli (`minecraft:lapis_lazuli`) | 20 | 25.00 % | Cantidad: {"type": "minecraft:uniform", "max": 10.0, "min": 1.0} |

**Grupo 3** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 5 | 83.33 % | 1 por resultado; puede variar por funciones de la tabla |
| coast armor trim smithing template (`minecraft:coast_armor_trim_smithing_template`) | 1 | 16.67 % | Cantidad: 2.0 |

## minecraft — simple dungeon

Tabla: `minecraft:chests/simple_dungeon` · fuente: `TheOptimizer_AdventureLoot.zip`.

Hay varias versiones de esta tabla; se ha priorizado el datapack del mundo y después el datapack global. Confirma el orden de carga si el mundo usa otros datapacks.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 2.0, "max": 4.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| gold ingot (`minecraft:gold_ingot`) | 20 | 21.51 % | Cantidad: {"min": 2, "max": 6} |
| iron ingot (`minecraft:iron_ingot`) | 20 | 21.51 % | Cantidad: {"min": 2, "max": 6} |
| diamond (`minecraft:diamond`) | 8 | 8.60 % | Cantidad: {"min": 1, "max": 2} |
| lapis lazuli (`minecraft:lapis_lazuli`) | 15 | 16.13 % | Cantidad: {"min": 4, "max": 10} |
| experience bottle (`minecraft:experience_bottle`) | 15 | 16.13 % | Cantidad: {"min": 2, "max": 5} |
| redstone (`minecraft:redstone`) | 15 | 16.13 % | Cantidad: {"min": 4, "max": 10} |

**Grupo 2** · tiradas: `{"type": "minecraft:uniform", "min": 1.0, "max": 2.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| golden apple (`minecraft:golden_apple`) | 25 | 16.13 % | 1 por resultado; puede variar por funciones de la tabla |
| enchanted golden apple (`minecraft:enchanted_golden_apple`) | 3 | 1.94 % | 1 por resultado; puede variar por funciones de la tabla |
| saddle (`minecraft:saddle`) | 15 | 9.68 % | 1 por resultado; puede variar por funciones de la tabla |
| name tag (`minecraft:name_tag`) | 15 | 9.68 % | 1 por resultado; puede variar por funciones de la tabla |
| book (`minecraft:book`) | 15 | 9.68 % | Función: minecraft:enchant_randomly |
| enchanted book (`minecraft:enchanted_book`) | 15 | 9.68 % | Función: minecraft:set_nbt |
| enchanted book (`minecraft:enchanted_book`) | 12 | 7.74 % | Función: minecraft:set_nbt |
| enchanted book (`minecraft:enchanted_book`) | 10 | 6.45 % | Función: minecraft:set_nbt |
| enchanted book (`minecraft:enchanted_book`) | 12 | 7.74 % | Función: minecraft:set_nbt |
| enchanted book (`minecraft:enchanted_book`) | 10 | 6.45 % | Función: minecraft:set_nbt |
| music disc otherside (`minecraft:music_disc_otherside`) | 3 | 1.94 % | 1 por resultado; puede variar por funciones de la tabla |
| music disc cat (`minecraft:music_disc_cat`) | 10 | 6.45 % | 1 por resultado; puede variar por funciones de la tabla |
| music disc 13 (`minecraft:music_disc_13`) | 10 | 6.45 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 3** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| gunpowder (`minecraft:gunpowder`) | 10 | 38.46 % | Cantidad: {"min": 2, "max": 5} |
| bone (`minecraft:bone`) | 8 | 30.77 % | Cantidad: {"min": 2, "max": 4} |
| string (`minecraft:string`) | 8 | 30.77 % | Cantidad: {"min": 1, "max": 3} |

## minecraft — spawn bonus chest

Tabla: `minecraft:chests/spawn_bonus_chest` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| stone axe (`minecraft:stone_axe`) | 1 | 25.00 % | 1 por resultado; puede variar por funciones de la tabla |
| wooden axe (`minecraft:wooden_axe`) | 3 | 75.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 2** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| stone pickaxe (`minecraft:stone_pickaxe`) | 1 | 25.00 % | 1 por resultado; puede variar por funciones de la tabla |
| wooden pickaxe (`minecraft:wooden_pickaxe`) | 3 | 75.00 % | 1 por resultado; puede variar por funciones de la tabla |

**Grupo 3** · tiradas: `3.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| apple (`minecraft:apple`) | 5 | 45.45 % | Cantidad: {"type": "minecraft:uniform", "max": 2.0, "min": 1.0} |
| bread (`minecraft:bread`) | 3 | 27.27 % | Cantidad: {"type": "minecraft:uniform", "max": 2.0, "min": 1.0} |
| salmon (`minecraft:salmon`) | 3 | 27.27 % | Cantidad: {"type": "minecraft:uniform", "max": 2.0, "min": 1.0} |

**Grupo 4** · tiradas: `4.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| stick (`minecraft:stick`) | 10 | 24.39 % | Cantidad: {"type": "minecraft:uniform", "max": 12.0, "min": 1.0} |
| oak planks (`minecraft:oak_planks`) | 10 | 24.39 % | Cantidad: {"type": "minecraft:uniform", "max": 12.0, "min": 1.0} |
| oak log (`minecraft:oak_log`) | 3 | 7.32 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| spruce log (`minecraft:spruce_log`) | 3 | 7.32 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| birch log (`minecraft:birch_log`) | 3 | 7.32 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| jungle log (`minecraft:jungle_log`) | 3 | 7.32 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| acacia log (`minecraft:acacia_log`) | 3 | 7.32 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| dark oak log (`minecraft:dark_oak_log`) | 3 | 7.32 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| mangrove log (`minecraft:mangrove_log`) | 3 | 7.32 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |

## minecraft — stronghold corridor

Tabla: `minecraft:chests/stronghold_corridor` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 3.0, "min": 2.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| ender pearl (`minecraft:ender_pearl`) | 10 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond (`minecraft:diamond`) | 3 | 3.00 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| iron ingot (`minecraft:iron_ingot`) | 10 | 10.00 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 1.0} |
| gold ingot (`minecraft:gold_ingot`) | 5 | 5.00 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| redstone (`minecraft:redstone`) | 5 | 5.00 % | Cantidad: {"type": "minecraft:uniform", "max": 9.0, "min": 4.0} |
| bread (`minecraft:bread`) | 15 | 15.00 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| apple (`minecraft:apple`) | 15 | 15.00 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| iron pickaxe (`minecraft:iron_pickaxe`) | 5 | 5.00 % | 1 por resultado; puede variar por funciones de la tabla |
| iron sword (`minecraft:iron_sword`) | 5 | 5.00 % | 1 por resultado; puede variar por funciones de la tabla |
| iron chestplate (`minecraft:iron_chestplate`) | 5 | 5.00 % | 1 por resultado; puede variar por funciones de la tabla |
| iron helmet (`minecraft:iron_helmet`) | 5 | 5.00 % | 1 por resultado; puede variar por funciones de la tabla |
| iron leggings (`minecraft:iron_leggings`) | 5 | 5.00 % | 1 por resultado; puede variar por funciones de la tabla |
| iron boots (`minecraft:iron_boots`) | 5 | 5.00 % | 1 por resultado; puede variar por funciones de la tabla |
| golden apple (`minecraft:golden_apple`) | 1 | 1.00 % | 1 por resultado; puede variar por funciones de la tabla |
| saddle (`minecraft:saddle`) | 1 | 1.00 % | 1 por resultado; puede variar por funciones de la tabla |
| iron horse armor (`minecraft:iron_horse_armor`) | 1 | 1.00 % | 1 por resultado; puede variar por funciones de la tabla |
| golden horse armor (`minecraft:golden_horse_armor`) | 1 | 1.00 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond horse armor (`minecraft:diamond_horse_armor`) | 1 | 1.00 % | 1 por resultado; puede variar por funciones de la tabla |
| music disc otherside (`minecraft:music_disc_otherside`) | 1 | 1.00 % | 1 por resultado; puede variar por funciones de la tabla |
| book (`minecraft:book`) | 1 | 1.00 % | Función: minecraft:enchant_with_levels |

**Grupo 2** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 9 | 90.00 % | 1 por resultado; puede variar por funciones de la tabla |
| eye armor trim smithing template (`minecraft:eye_armor_trim_smithing_template`) | 1 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |

## minecraft — stronghold crossing

Tabla: `minecraft:chests/stronghold_crossing` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 4.0, "min": 1.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| iron ingot (`minecraft:iron_ingot`) | 10 | 16.13 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 1.0} |
| gold ingot (`minecraft:gold_ingot`) | 5 | 8.06 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| redstone (`minecraft:redstone`) | 5 | 8.06 % | Cantidad: {"type": "minecraft:uniform", "max": 9.0, "min": 4.0} |
| coal (`minecraft:coal`) | 10 | 16.13 % | Cantidad: {"type": "minecraft:uniform", "max": 8.0, "min": 3.0} |
| bread (`minecraft:bread`) | 15 | 24.19 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| apple (`minecraft:apple`) | 15 | 24.19 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| iron pickaxe (`minecraft:iron_pickaxe`) | 1 | 1.61 % | 1 por resultado; puede variar por funciones de la tabla |
| book (`minecraft:book`) | 1 | 1.61 % | Función: minecraft:enchant_with_levels |

## minecraft — stronghold library

Tabla: `minecraft:chests/stronghold_library` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 10.0, "min": 2.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| book (`minecraft:book`) | 20 | 38.46 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| paper (`minecraft:paper`) | 20 | 38.46 % | Cantidad: {"type": "minecraft:uniform", "max": 7.0, "min": 2.0} |
| map (`minecraft:map`) | 1 | 1.92 % | 1 por resultado; puede variar por funciones de la tabla |
| compass (`minecraft:compass`) | 1 | 1.92 % | 1 por resultado; puede variar por funciones de la tabla |
| book (`minecraft:book`) | 10 | 19.23 % | Función: minecraft:enchant_with_levels |

**Grupo 2** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| eye armor trim smithing template (`minecraft:eye_armor_trim_smithing_template`) | 1 | 100.00 % | 1 por resultado; puede variar por funciones de la tabla |

## minecraft — underwater ruin big

Tabla: `minecraft:chests/underwater_ruin_big` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 8.0, "min": 2.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| coal (`minecraft:coal`) | 10 | 32.26 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| gold nugget (`minecraft:gold_nugget`) | 10 | 32.26 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| emerald (`minecraft:emerald`) | 1 | 3.23 % | 1 por resultado; puede variar por funciones de la tabla |
| wheat (`minecraft:wheat`) | 10 | 32.26 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 2.0} |

**Grupo 2** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| golden apple (`minecraft:golden_apple`) | 1 | 4.35 % | 1 por resultado; puede variar por funciones de la tabla |
| book (`minecraft:book`) | 5 | 21.74 % | Función: minecraft:enchant_randomly |
| leather chestplate (`minecraft:leather_chestplate`) | 1 | 4.35 % | 1 por resultado; puede variar por funciones de la tabla |
| golden helmet (`minecraft:golden_helmet`) | 1 | 4.35 % | 1 por resultado; puede variar por funciones de la tabla |
| fishing rod (`minecraft:fishing_rod`) | 5 | 21.74 % | Función: minecraft:enchant_randomly |
| map (`minecraft:map`) | 10 | 43.48 % | Función: minecraft:exploration_map; Función: minecraft:set_name |

## minecraft — underwater ruin small

Tabla: `minecraft:chests/underwater_ruin_small` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 8.0, "min": 2.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| coal (`minecraft:coal`) | 10 | 35.71 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| stone axe (`minecraft:stone_axe`) | 2 | 7.14 % | 1 por resultado; puede variar por funciones de la tabla |
| rotten flesh (`minecraft:rotten_flesh`) | 5 | 17.86 % | 1 por resultado; puede variar por funciones de la tabla |
| emerald (`minecraft:emerald`) | 1 | 3.57 % | 1 por resultado; puede variar por funciones de la tabla |
| wheat (`minecraft:wheat`) | 10 | 35.71 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 2.0} |

**Grupo 2** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| leather chestplate (`minecraft:leather_chestplate`) | 1 | 8.33 % | 1 por resultado; puede variar por funciones de la tabla |
| golden helmet (`minecraft:golden_helmet`) | 1 | 8.33 % | 1 por resultado; puede variar por funciones de la tabla |
| fishing rod (`minecraft:fishing_rod`) | 5 | 41.67 % | Función: minecraft:enchant_randomly |
| map (`minecraft:map`) | 5 | 41.67 % | Función: minecraft:exploration_map; Función: minecraft:set_name |

## minecraft — village/village armorer

Tabla: `minecraft:chests/village/village_armorer` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 5.0, "min": 1.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| iron ingot (`minecraft:iron_ingot`) | 2 | 25.00 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| bread (`minecraft:bread`) | 4 | 50.00 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| iron helmet (`minecraft:iron_helmet`) | 1 | 12.50 % | 1 por resultado; puede variar por funciones de la tabla |
| emerald (`minecraft:emerald`) | 1 | 12.50 % | 1 por resultado; puede variar por funciones de la tabla |

## minecraft — village/village butcher

Tabla: `minecraft:chests/village/village_butcher` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 5.0, "min": 1.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| emerald (`minecraft:emerald`) | 1 | 3.57 % | 1 por resultado; puede variar por funciones de la tabla |
| porkchop (`minecraft:porkchop`) | 6 | 21.43 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| wheat (`minecraft:wheat`) | 6 | 21.43 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| beef (`minecraft:beef`) | 6 | 21.43 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| mutton (`minecraft:mutton`) | 6 | 21.43 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| coal (`minecraft:coal`) | 3 | 10.71 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |

## minecraft — village/village cartographer

Tabla: `minecraft:chests/village/village_cartographer` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 5.0, "min": 1.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| map (`minecraft:map`) | 10 | 20.00 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| paper (`minecraft:paper`) | 15 | 30.00 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 1.0} |
| compass (`minecraft:compass`) | 5 | 10.00 % | 1 por resultado; puede variar por funciones de la tabla |
| bread (`minecraft:bread`) | 15 | 30.00 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| stick (`minecraft:stick`) | 5 | 10.00 % | Cantidad: {"type": "minecraft:uniform", "max": 2.0, "min": 1.0} |

## minecraft — village/village desert house

Tabla: `minecraft:chests/village/village_desert_house` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 8.0, "min": 3.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| clay ball (`minecraft:clay_ball`) | 1 | 2.78 % | 1 por resultado; puede variar por funciones de la tabla |
| green dye (`minecraft:green_dye`) | 1 | 2.78 % | 1 por resultado; puede variar por funciones de la tabla |
| cactus (`minecraft:cactus`) | 10 | 27.78 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| wheat (`minecraft:wheat`) | 10 | 27.78 % | Cantidad: {"type": "minecraft:uniform", "max": 7.0, "min": 1.0} |
| bread (`minecraft:bread`) | 10 | 27.78 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| book (`minecraft:book`) | 1 | 2.78 % | 1 por resultado; puede variar por funciones de la tabla |
| dead bush (`minecraft:dead_bush`) | 2 | 5.56 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| emerald (`minecraft:emerald`) | 1 | 2.78 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |

## minecraft — village/village fisher

Tabla: `minecraft:chests/village/village_fisher` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 5.0, "min": 1.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| emerald (`minecraft:emerald`) | 1 | 9.09 % | 1 por resultado; puede variar por funciones de la tabla |
| cod (`minecraft:cod`) | 2 | 18.18 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| salmon (`minecraft:salmon`) | 1 | 9.09 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| water bucket (`minecraft:water_bucket`) | 1 | 9.09 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| barrel (`minecraft:barrel`) | 1 | 9.09 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| wheat seeds (`minecraft:wheat_seeds`) | 3 | 27.27 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| coal (`minecraft:coal`) | 2 | 18.18 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |

## minecraft — village/village fletcher

Tabla: `minecraft:chests/village/village_fletcher` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 5.0, "min": 1.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| emerald (`minecraft:emerald`) | 1 | 4.35 % | 1 por resultado; puede variar por funciones de la tabla |
| arrow (`minecraft:arrow`) | 2 | 8.70 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| feather (`minecraft:feather`) | 6 | 26.09 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| egg (`minecraft:egg`) | 2 | 8.70 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| flint (`minecraft:flint`) | 6 | 26.09 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| stick (`minecraft:stick`) | 6 | 26.09 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |

## minecraft — village/village mason

Tabla: `minecraft:chests/village/village_mason` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 5.0, "min": 1.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| clay ball (`minecraft:clay_ball`) | 1 | 7.69 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| flower pot (`minecraft:flower_pot`) | 1 | 7.69 % | 1 por resultado; puede variar por funciones de la tabla |
| stone (`minecraft:stone`) | 2 | 15.38 % | 1 por resultado; puede variar por funciones de la tabla |
| stone bricks (`minecraft:stone_bricks`) | 2 | 15.38 % | 1 por resultado; puede variar por funciones de la tabla |
| bread (`minecraft:bread`) | 4 | 30.77 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| yellow dye (`minecraft:yellow_dye`) | 1 | 7.69 % | 1 por resultado; puede variar por funciones de la tabla |
| smooth stone (`minecraft:smooth_stone`) | 1 | 7.69 % | 1 por resultado; puede variar por funciones de la tabla |
| emerald (`minecraft:emerald`) | 1 | 7.69 % | 1 por resultado; puede variar por funciones de la tabla |

## minecraft — village/village plains house

Tabla: `minecraft:chests/village/village_plains_house` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 8.0, "min": 3.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| gold nugget (`minecraft:gold_nugget`) | 1 | 2.33 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| dandelion (`minecraft:dandelion`) | 2 | 4.65 % | 1 por resultado; puede variar por funciones de la tabla |
| poppy (`minecraft:poppy`) | 1 | 2.33 % | 1 por resultado; puede variar por funciones de la tabla |
| potato (`minecraft:potato`) | 10 | 23.26 % | Cantidad: {"type": "minecraft:uniform", "max": 7.0, "min": 1.0} |
| bread (`minecraft:bread`) | 10 | 23.26 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| apple (`minecraft:apple`) | 10 | 23.26 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 1.0} |
| book (`minecraft:book`) | 1 | 2.33 % | 1 por resultado; puede variar por funciones de la tabla |
| feather (`minecraft:feather`) | 1 | 2.33 % | 1 por resultado; puede variar por funciones de la tabla |
| emerald (`minecraft:emerald`) | 2 | 4.65 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| oak sapling (`minecraft:oak_sapling`) | 5 | 11.63 % | Cantidad: {"type": "minecraft:uniform", "max": 2.0, "min": 1.0} |

## minecraft — village/village savanna house

Tabla: `minecraft:chests/village/village_savanna_house` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 8.0, "min": 3.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| gold nugget (`minecraft:gold_nugget`) | 1 | 2.17 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| grass (`minecraft:grass`) | 5 | 10.87 % | 1 por resultado; puede variar por funciones de la tabla |
| tall grass (`minecraft:tall_grass`) | 5 | 10.87 % | 1 por resultado; puede variar por funciones de la tabla |
| bread (`minecraft:bread`) | 10 | 21.74 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| wheat seeds (`minecraft:wheat_seeds`) | 10 | 21.74 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 1.0} |
| emerald (`minecraft:emerald`) | 2 | 4.35 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| acacia sapling (`minecraft:acacia_sapling`) | 10 | 21.74 % | Cantidad: {"type": "minecraft:uniform", "max": 2.0, "min": 1.0} |
| saddle (`minecraft:saddle`) | 1 | 2.17 % | 1 por resultado; puede variar por funciones de la tabla |
| torch (`minecraft:torch`) | 1 | 2.17 % | Cantidad: {"type": "minecraft:uniform", "max": 2.0, "min": 1.0} |
| bucket (`minecraft:bucket`) | 1 | 2.17 % | 1 por resultado; puede variar por funciones de la tabla |

## minecraft — village/village shepherd

Tabla: `minecraft:chests/village/village_shepherd` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 5.0, "min": 1.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| white wool (`minecraft:white_wool`) | 6 | 26.09 % | Cantidad: {"type": "minecraft:uniform", "max": 8.0, "min": 1.0} |
| black wool (`minecraft:black_wool`) | 3 | 13.04 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| gray wool (`minecraft:gray_wool`) | 2 | 8.70 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| brown wool (`minecraft:brown_wool`) | 2 | 8.70 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| light gray wool (`minecraft:light_gray_wool`) | 2 | 8.70 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| emerald (`minecraft:emerald`) | 1 | 4.35 % | 1 por resultado; puede variar por funciones de la tabla |
| shears (`minecraft:shears`) | 1 | 4.35 % | 1 por resultado; puede variar por funciones de la tabla |
| wheat (`minecraft:wheat`) | 6 | 26.09 % | Cantidad: {"type": "minecraft:uniform", "max": 6.0, "min": 1.0} |

## minecraft — village/village snowy house

Tabla: `minecraft:chests/village/village_snowy_house` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 8.0, "min": 3.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| blue ice (`minecraft:blue_ice`) | 1 | 1.89 % | 1 por resultado; puede variar por funciones de la tabla |
| snow block (`minecraft:snow_block`) | 4 | 7.55 % | 1 por resultado; puede variar por funciones de la tabla |
| potato (`minecraft:potato`) | 10 | 18.87 % | Cantidad: {"type": "minecraft:uniform", "max": 7.0, "min": 1.0} |
| bread (`minecraft:bread`) | 10 | 18.87 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| beetroot seeds (`minecraft:beetroot_seeds`) | 10 | 18.87 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 1.0} |
| beetroot soup (`minecraft:beetroot_soup`) | 1 | 1.89 % | 1 por resultado; puede variar por funciones de la tabla |
| furnace (`minecraft:furnace`) | 1 | 1.89 % | 1 por resultado; puede variar por funciones de la tabla |
| emerald (`minecraft:emerald`) | 1 | 1.89 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| snowball (`minecraft:snowball`) | 10 | 18.87 % | Cantidad: {"type": "minecraft:uniform", "max": 7.0, "min": 1.0} |
| coal (`minecraft:coal`) | 5 | 9.43 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |

## minecraft — village/village taiga house

Tabla: `minecraft:chests/village/village_taiga_house` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 8.0, "min": 3.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| iron nugget (`minecraft:iron_nugget`) | 1 | 1.85 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 1.0} |
| fern (`minecraft:fern`) | 2 | 3.70 % | 1 por resultado; puede variar por funciones de la tabla |
| large fern (`minecraft:large_fern`) | 2 | 3.70 % | 1 por resultado; puede variar por funciones de la tabla |
| potato (`minecraft:potato`) | 10 | 18.52 % | Cantidad: {"type": "minecraft:uniform", "max": 7.0, "min": 1.0} |
| sweet berries (`minecraft:sweet_berries`) | 5 | 9.26 % | Cantidad: {"type": "minecraft:uniform", "max": 7.0, "min": 1.0} |
| bread (`minecraft:bread`) | 10 | 18.52 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| pumpkin seeds (`minecraft:pumpkin_seeds`) | 5 | 9.26 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 1.0} |
| pumpkin pie (`minecraft:pumpkin_pie`) | 1 | 1.85 % | 1 por resultado; puede variar por funciones de la tabla |
| emerald (`minecraft:emerald`) | 2 | 3.70 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| spruce sapling (`minecraft:spruce_sapling`) | 5 | 9.26 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 1.0} |
| spruce sign (`minecraft:spruce_sign`) | 1 | 1.85 % | 1 por resultado; puede variar por funciones de la tabla |
| spruce log (`minecraft:spruce_log`) | 10 | 18.52 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 1.0} |

## minecraft — village/village tannery

Tabla: `minecraft:chests/village/village_tannery` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 5.0, "min": 1.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| leather (`minecraft:leather`) | 1 | 6.25 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| leather chestplate (`minecraft:leather_chestplate`) | 2 | 12.50 % | 1 por resultado; puede variar por funciones de la tabla |
| leather boots (`minecraft:leather_boots`) | 2 | 12.50 % | 1 por resultado; puede variar por funciones de la tabla |
| leather helmet (`minecraft:leather_helmet`) | 2 | 12.50 % | 1 por resultado; puede variar por funciones de la tabla |
| bread (`minecraft:bread`) | 5 | 31.25 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| leather leggings (`minecraft:leather_leggings`) | 2 | 12.50 % | 1 por resultado; puede variar por funciones de la tabla |
| saddle (`minecraft:saddle`) | 1 | 6.25 % | 1 por resultado; puede variar por funciones de la tabla |
| emerald (`minecraft:emerald`) | 1 | 6.25 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |

## minecraft — village/village temple

Tabla: `minecraft:chests/village/village_temple` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 8.0, "min": 3.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| redstone (`minecraft:redstone`) | 2 | 10.53 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| bread (`minecraft:bread`) | 7 | 36.84 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| rotten flesh (`minecraft:rotten_flesh`) | 7 | 36.84 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| lapis lazuli (`minecraft:lapis_lazuli`) | 1 | 5.26 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| gold ingot (`minecraft:gold_ingot`) | 1 | 5.26 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| emerald (`minecraft:emerald`) | 1 | 5.26 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |

## minecraft — village/village toolsmith

Tabla: `minecraft:chests/village/village_toolsmith` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 8.0, "min": 3.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| diamond (`minecraft:diamond`) | 1 | 1.89 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| iron ingot (`minecraft:iron_ingot`) | 5 | 9.43 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 1.0} |
| gold ingot (`minecraft:gold_ingot`) | 1 | 1.89 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| bread (`minecraft:bread`) | 15 | 28.30 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| iron pickaxe (`minecraft:iron_pickaxe`) | 5 | 9.43 % | 1 por resultado; puede variar por funciones de la tabla |
| coal (`minecraft:coal`) | 1 | 1.89 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| stick (`minecraft:stick`) | 20 | 37.74 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| iron shovel (`minecraft:iron_shovel`) | 5 | 9.43 % | 1 por resultado; puede variar por funciones de la tabla |

## minecraft — village/village weaponsmith

Tabla: `minecraft:chests/village/village_weaponsmith` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 8.0, "min": 3.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| diamond (`minecraft:diamond`) | 3 | 3.19 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| iron ingot (`minecraft:iron_ingot`) | 10 | 10.64 % | Cantidad: {"type": "minecraft:uniform", "max": 5.0, "min": 1.0} |
| gold ingot (`minecraft:gold_ingot`) | 5 | 5.32 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| bread (`minecraft:bread`) | 15 | 15.96 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| apple (`minecraft:apple`) | 15 | 15.96 % | Cantidad: {"type": "minecraft:uniform", "max": 3.0, "min": 1.0} |
| iron pickaxe (`minecraft:iron_pickaxe`) | 5 | 5.32 % | 1 por resultado; puede variar por funciones de la tabla |
| iron sword (`minecraft:iron_sword`) | 5 | 5.32 % | 1 por resultado; puede variar por funciones de la tabla |
| iron chestplate (`minecraft:iron_chestplate`) | 5 | 5.32 % | 1 por resultado; puede variar por funciones de la tabla |
| iron helmet (`minecraft:iron_helmet`) | 5 | 5.32 % | 1 por resultado; puede variar por funciones de la tabla |
| iron leggings (`minecraft:iron_leggings`) | 5 | 5.32 % | 1 por resultado; puede variar por funciones de la tabla |
| iron boots (`minecraft:iron_boots`) | 5 | 5.32 % | 1 por resultado; puede variar por funciones de la tabla |
| obsidian (`minecraft:obsidian`) | 5 | 5.32 % | Cantidad: {"type": "minecraft:uniform", "max": 7.0, "min": 3.0} |
| oak sapling (`minecraft:oak_sapling`) | 5 | 5.32 % | Cantidad: {"type": "minecraft:uniform", "max": 7.0, "min": 3.0} |
| saddle (`minecraft:saddle`) | 3 | 3.19 % | 1 por resultado; puede variar por funciones de la tabla |
| iron horse armor (`minecraft:iron_horse_armor`) | 1 | 1.06 % | 1 por resultado; puede variar por funciones de la tabla |
| golden horse armor (`minecraft:golden_horse_armor`) | 1 | 1.06 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond horse armor (`minecraft:diamond_horse_armor`) | 1 | 1.06 % | 1 por resultado; puede variar por funciones de la tabla |

## minecraft — woodland mansion

Tabla: `minecraft:chests/woodland_mansion` · fuente: `server-1.20.1-20230612.114412-extra.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "max": 3.0, "min": 1.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| lead (`minecraft:lead`) | 20 | 15.75 % | 1 por resultado; puede variar por funciones de la tabla |
| golden apple (`minecraft:golden_apple`) | 15 | 11.81 % | 1 por resultado; puede variar por funciones de la tabla |
| enchanted golden apple (`minecraft:enchanted_golden_apple`) | 2 | 1.57 % | 1 por resultado; puede variar por funciones de la tabla |
| music disc 13 (`minecraft:music_disc_13`) | 15 | 11.81 % | 1 por resultado; puede variar por funciones de la tabla |
| music disc cat (`minecraft:music_disc_cat`) | 15 | 11.81 % | 1 por resultado; puede variar por funciones de la tabla |
| name tag (`minecraft:name_tag`) | 20 | 15.75 % | 1 por resultado; puede variar por funciones de la tabla |
| chainmail chestplate (`minecraft:chainmail_chestplate`) | 10 | 7.87 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond hoe (`minecraft:diamond_hoe`) | 15 | 11.81 % | 1 por resultado; puede variar por funciones de la tabla |
| diamond chestplate (`minecraft:diamond_chestplate`) | 5 | 3.94 % | 1 por resultado; puede variar por funciones de la tabla |
| book (`minecraft:book`) | 10 | 7.87 % | Función: minecraft:enchant_randomly |

**Grupo 2** · tiradas: `{"type": "minecraft:uniform", "max": 4.0, "min": 1.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| iron ingot (`minecraft:iron_ingot`) | 10 | 8.00 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| gold ingot (`minecraft:gold_ingot`) | 5 | 4.00 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| bread (`minecraft:bread`) | 20 | 16.00 % | 1 por resultado; puede variar por funciones de la tabla |
| wheat (`minecraft:wheat`) | 20 | 16.00 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| bucket (`minecraft:bucket`) | 10 | 8.00 % | 1 por resultado; puede variar por funciones de la tabla |
| redstone (`minecraft:redstone`) | 15 | 12.00 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| coal (`minecraft:coal`) | 15 | 12.00 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 1.0} |
| melon seeds (`minecraft:melon_seeds`) | 10 | 8.00 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 2.0} |
| pumpkin seeds (`minecraft:pumpkin_seeds`) | 10 | 8.00 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 2.0} |
| beetroot seeds (`minecraft:beetroot_seeds`) | 10 | 8.00 % | Cantidad: {"type": "minecraft:uniform", "max": 4.0, "min": 2.0} |

**Grupo 3** · tiradas: `3.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| bone (`minecraft:bone`) | 10 | 25.00 % | Cantidad: {"type": "minecraft:uniform", "max": 8.0, "min": 1.0} |
| gunpowder (`minecraft:gunpowder`) | 10 | 25.00 % | Cantidad: {"type": "minecraft:uniform", "max": 8.0, "min": 1.0} |
| rotten flesh (`minecraft:rotten_flesh`) | 10 | 25.00 % | Cantidad: {"type": "minecraft:uniform", "max": 8.0, "min": 1.0} |
| string (`minecraft:string`) | 10 | 25.00 % | Cantidad: {"type": "minecraft:uniform", "max": 8.0, "min": 1.0} |

**Grupo 4** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Nada | 1 | 50.00 % | 1 por resultado; puede variar por funciones de la tabla |
| vex armor trim smithing template (`minecraft:vex_armor_trim_smithing_template`) | 1 | 50.00 % | 1 por resultado; puede variar por funciones de la tabla |

## ribbits — fisherman main

Tabla: `ribbits:chests/fisherman_main` · fuente: `Ribbits-1.20.1-Forge-3.0.5.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 2.0, "max": 4.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| cod (`minecraft:cod`) | 5 | 25.00 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 3.0} |
| salmon (`minecraft:salmon`) | 5 | 25.00 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 3.0} |
| kelp (`minecraft:kelp`) | 5 | 25.00 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 4.0} |
| Nenúfar gigante (`ribbits:giant_lilypad`) | 5 | 25.00 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 2.0} |

**Grupo 2** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| air (`minecraft:air`) | 15 | 83.33 % | 1 por resultado; puede variar por funciones de la tabla |
| fishing rod (`minecraft:fishing_rod`) | 1 | 5.56 % | Función: minecraft:enchant_with_levels |
| fishing rod (`minecraft:fishing_rod`) | 1 | 5.56 % | Función: minecraft:enchant_with_levels |
| fishing rod (`minecraft:fishing_rod`) | 1 | 5.56 % | Función: minecraft:enchant_with_levels |

## ribbits — fisherman storage

Tabla: `ribbits:chests/fisherman_storage` · fuente: `Ribbits-1.20.1-Forge-3.0.5.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 1.0, "max": 4.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| cod (`minecraft:cod`) | 5 | 12.50 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 4.0} |
| salmon (`minecraft:salmon`) | 5 | 12.50 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 4.0} |
| tropical fish (`minecraft:tropical_fish`) | 5 | 12.50 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 4.0} |
| kelp (`minecraft:kelp`) | 5 | 12.50 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 4.0} |
| dried kelp (`minecraft:dried_kelp`) | 5 | 12.50 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 4.0} |
| Nenúfar gigante (`ribbits:giant_lilypad`) | 5 | 12.50 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 4.0} |
| nautilus shell (`minecraft:nautilus_shell`) | 5 | 12.50 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 1.0} |
| amethyst shard (`minecraft:amethyst_shard`) | 5 | 12.50 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 3.0} |

## ribbits — gardener

Tabla: `ribbits:chests/gardener` · fuente: `Ribbits-1.20.1-Forge-3.0.5.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 4.0, "max": 6.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| red mushroom (`minecraft:red_mushroom`) | 5 | 27.78 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 5.0} |
| brown mushroom (`minecraft:brown_mushroom`) | 5 | 27.78 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 5.0} |
| Nenúfar gigante (`ribbits:giant_lilypad`) | 5 | 27.78 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 2.0} |
| amethyst shard (`minecraft:amethyst_shard`) | 3 | 16.67 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 2.0} |

## ribbits — merchant

Tabla: `ribbits:chests/merchant` · fuente: `Ribbits-1.20.1-Forge-3.0.5.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 3.0, "max": 4.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| amethyst shard (`minecraft:amethyst_shard`) | 8 | 88.89 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 4.0} |
| amethyst block (`minecraft:amethyst_block`) | 1 | 11.11 % | Cantidad: 1 |

## ribbits — nitwit

Tabla: `ribbits:chests/nitwit` · fuente: `Ribbits-1.20.1-Forge-3.0.5.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 3.0, "max": 4.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| red mushroom (`minecraft:red_mushroom`) | 5 | 27.78 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 3.0} |
| brown mushroom (`minecraft:brown_mushroom`) | 5 | 27.78 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 3.0} |
| Nenúfar gigante (`ribbits:giant_lilypad`) | 5 | 27.78 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 3.0} |
| amethyst shard (`minecraft:amethyst_shard`) | 3 | 16.67 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 3.0} |

## ribbits — sorcerer

Tabla: `ribbits:chests/sorcerer` · fuente: `Ribbits-1.20.1-Forge-3.0.5.jar`.

**Grupo 1** · tiradas: `{"type": "minecraft:uniform", "min": 4.0, "max": 6.0}`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| cobweb (`minecraft:cobweb`) | 5 | 16.67 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 2.0} |
| candle (`minecraft:candle`) | 5 | 16.67 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 4.0} |
| glass bottle (`minecraft:glass_bottle`) | 5 | 16.67 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 4.0} |
| fermented spider eye (`minecraft:fermented_spider_eye`) | 5 | 16.67 % | Cantidad: {"type": "minecraft:uniform", "min": 1.0, "max": 2.0} |
| amethyst shard (`minecraft:amethyst_shard`) | 5 | 16.67 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 6.0} |
| slime ball (`minecraft:slime_ball`) | 5 | 16.67 % | Cantidad: {"type": "minecraft:uniform", "min": 2.0, "max": 5.0} |

**Grupo 2** · tiradas: `1.0`.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| air (`minecraft:air`) | 1 | 50.00 % | 1 por resultado; puede variar por funciones de la tabla |
| potion (`minecraft:potion`) | 1 | 50.00 % | Función: minecraft:set_nbt |

## theoptimizer — yungs nether cinder

Tabla: `theoptimizer:chests/yungs_nether_cinder` · fuente: `TheOptimizer_AdventureLoot.zip`.

**Grupo 1** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Esencia de Ceniza (`irons_spellbooks:cinder_essence`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.5}]`.

## theoptimizer — yungs tier 1

Tabla: `theoptimizer:chests/yungs_tier_1` · fuente: `TheOptimizer_AdventureLoot.zip`.

**Grupo 1** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| enchanted book (`minecraft:enchanted_book`) | 1 | Condicionada; sin cifra única | Función: minecraft:set_nbt |
| enchanted book (`minecraft:enchanted_book`) | 1 | Condicionada; sin cifra única | Función: minecraft:set_nbt |
| enchanted book (`minecraft:enchanted_book`) | 1 | Condicionada; sin cifra única | Función: minecraft:set_nbt |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.35}]`.

**Grupo 2** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tinta Común (`irons_spellbooks:common_ink`) | 6 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |
| Tinta Inusual (`irons_spellbooks:uncommon_ink`) | 3 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |
| Esencia Arcana (`irons_spellbooks:arcane_essence`) | 4 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |
| (Pergamino) (`irons_spellbooks:scroll`) | 2 | Condicionada; sin cifra única | Función: irons_spellbooks:randomize_spell |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.65}]`.

## theoptimizer — yungs tier 2

Tabla: `theoptimizer:chests/yungs_tier_2` · fuente: `TheOptimizer_AdventureLoot.zip`.

**Grupo 1** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| enchanted book (`minecraft:enchanted_book`) | 1 | Condicionada; sin cifra única | Función: minecraft:set_nbt |
| enchanted book (`minecraft:enchanted_book`) | 1 | Condicionada; sin cifra única | Función: minecraft:set_nbt |
| enchanted book (`minecraft:enchanted_book`) | 1 | Condicionada; sin cifra única | Función: minecraft:set_nbt |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.6}]`.

**Grupo 2** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tinta Inusual (`irons_spellbooks:uncommon_ink`) | 6 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |
| Tinta Rara (`irons_spellbooks:rare_ink`) | 3 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |
| Piedra Rúnica en blanco (`irons_spellbooks:blank_rune`) | 3 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |
| (Pergamino) (`irons_spellbooks:scroll`) | 4 | Condicionada; sin cifra única | Función: irons_spellbooks:randomize_spell |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.85}]`.

## theoptimizer — yungs tier 3

Tabla: `theoptimizer:chests/yungs_tier_3` · fuente: `TheOptimizer_AdventureLoot.zip`.

**Grupo 1** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| enchanted book (`minecraft:enchanted_book`) | 1 | Condicionada; sin cifra única | Función: minecraft:set_nbt |
| enchanted book (`minecraft:enchanted_book`) | 1 | Condicionada; sin cifra única | Función: minecraft:set_nbt |
| enchanted book (`minecraft:enchanted_book`) | 1 | Condicionada; sin cifra única | Función: minecraft:set_nbt |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 0.8}]`.

**Grupo 2** · tiradas: `1` · condicionado.

| Objeto o recompensa | Peso | Probabilidad por tirada | Cantidad y condiciones |
|---|---:|---:|---|
| Tinta Rara (`irons_spellbooks:rare_ink`) | 10 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |
| Tinta Épica (`irons_spellbooks:epic_ink`) | 4 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |
| Tinta Legendaria (`irons_spellbooks:legendary_ink`) | 1 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |
| Piedra Rúnica en blanco (`irons_spellbooks:blank_rune`) | 5 | Condicionada; sin cifra única | 1 por resultado; puede variar por funciones de la tabla |
| (Pergamino) (`irons_spellbooks:scroll`) | 4 | Condicionada; sin cifra única | Función: irons_spellbooks:randomize_spell |

Condiciones del grupo: `[{"condition": "minecraft:random_chance", "chance": 1}]`.

## Botín añadido por Ampere en estructuras de YUNG’s

Estas probabilidades son **adicionales** al contenido nativo de los cofres cubiertos. Cada material de la tabla supone una sola tirada del grupo arcano, con la probabilidad de activación ya aplicada.

| Recompensa | Nivel 1 | Nivel 2 | Nivel 3 |
|---|---:|---:|---:|
| Libro de cada tipo permitido, nivel I | 11,67 % | 20 % | 26,67 % |
| Tinta común | 26 % | — | — |
| Tinta poco común | 13 % | 31,88 % | — |
| Esencia arcana | 17,33 % | — | — |
| Pergamino | 8,67 % | 21,25 % | 16,67 % |
| Tinta rara | — | 15,94 % | 41,67 % |
| Runa en blanco | — | 15,94 % | 20,83 % |
| Tinta épica | — | — | 16,67 % |
| Tinta legendaria | — | — | 4,17 % |

En fortalezas, incluida la delegación vanilla `nether_bridge`, se añade además una posibilidad independiente del 50 % de esencia ígnea. La lista de cofres por nivel está en [LOOT.md](LOOT.md). Estos porcentajes no incorporan fuentes adicionales del botín nativo ni otros modificadores.

Para revisar datos completos y modificadores, consulta [INVENTARIO_BOTIN_ESTRUCTURAS.md](INVENTARIO_BOTIN_ESTRUCTURAS.md).
