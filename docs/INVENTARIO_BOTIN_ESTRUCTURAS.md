# Inventario de botín de estructuras

Extracción estática de tablas encontradas en los JAR del servidor, bibliotecas vanilla y datapacks activos. Incluye todas las versiones encontradas: cuando un ID aparece varias veces, comprobar prioridad de datapacks antes de tomarlo como resultado efectivo. No se ha resuelto el orden de carga del mundo ni la generación dinámica de mods.

El peso es relativo a las demás entradas elegibles del mismo pool; no es un porcentaje. Las condiciones, tiradas, funciones, referencias a tablas, calidad y entradas vacías aparecen íntegras en cada JSON. Los modifiers pueden añadir botín después de generar la tabla.

Tablas encontradas: 199; modifiers encontrados: 78.

## Tablas por ID y fuente

<details>
<summary>ae2:blocks/chests/meteorite — appliedenergistics2-forge-15.4.12.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\appliedenergistics2-forge-15.4.12.jar` · `data/ae2/loot_tables/blocks/chests/meteorite.json`

```json
{
  "type": "minecraft:block",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "ae2:sky_stone_block"
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 3.0,
        "min": 1.0
      }
    }
  ]
}
```

</details>

<details>
<summary>betterdeserttemples:chests/food_storage — YungsBetterDesertTemples-1.20-Forge-3.0.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterDesertTemples-1.20-Forge-3.0.3.jar` · `data/betterdeserttemples/loot_tables/chests/food_storage.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 5.0,
        "max": 7.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 6.0,
                "max": 12.0
              },
              "add": false
            }
          ],
          "name": "minecraft:potato"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:poisonous_potato"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 6.0,
                "max": 12.0
              },
              "add": false
            }
          ],
          "name": "minecraft:wheat"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 4.0,
                "max": 6.0
              },
              "add": false
            }
          ],
          "name": "minecraft:bread"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:golden_apple"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:enchanted_golden_apple"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 3.0,
                "max": 6.0
              },
              "add": false
            }
          ],
          "name": "minecraft:dried_kelp"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:honey_bottle"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 5.0
              },
              "add": false
            }
          ],
          "name": "minecraft:beetroot_soup"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 6.0,
                "max": 12.0
              },
              "add": false
            }
          ],
          "name": "minecraft:melon_seeds"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterdeserttemples:chests/lab — YungsBetterDesertTemples-1.20-Forge-3.0.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterDesertTemples-1.20-Forge-3.0.3.jar` · `data/betterdeserttemples/loot_tables/chests/lab.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 3.0,
        "max": 5.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 3.0
              },
              "add": false
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion:\"minecraft:water\"}"
            }
          ],
          "name": "minecraft:potion"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:fermented_spider_eye"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 5.0
              },
              "add": false
            }
          ],
          "name": "minecraft:melon_slice"
        },
        {
          "type": "minecraft:item",
          "weight": 4,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:glistering_melon_slice"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:rabbit_foot"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 3.0,
                "max": 8.0
              },
              "add": false
            }
          ],
          "name": "minecraft:carrot"
        },
        {
          "type": "minecraft:item",
          "weight": 4,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 3.0,
                "max": 8.0
              },
              "add": false
            }
          ],
          "name": "minecraft:golden_carrot"
        },
        {
          "type": "minecraft:item",
          "weight": 6,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:gunpowder"
        }
      ]
    },
    {
      "rolls": 4,
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:coal"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 4.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:stick"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:cobweb"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterdeserttemples:chests/library — YungsBetterDesertTemples-1.20-Forge-3.0.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterDesertTemples-1.20-Forge-3.0.3.jar` · `data/betterdeserttemples/loot_tables/chests/library.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 2.0,
        "max": 10.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 3.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:book"
        },
        {
          "type": "minecraft:item",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 7.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:paper"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:map"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:compass"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 10,
              "treasure": true
            }
          ],
          "name": "minecraft:book"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 20,
              "treasure": true
            }
          ],
          "name": "minecraft:book"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterdeserttemples:chests/pharaoh_hidden — YungsBetterDesertTemples-1.20-Forge-3.0.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterDesertTemples-1.20-Forge-3.0.3.jar` · `data/betterdeserttemples/loot_tables/chests/pharaoh_hidden.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30,
              "treasure": true
            },
            {
              "function": "minecraft:enchant_randomly",
              "enchantments": [
                "vanishing_curse"
              ]
            }
          ],
          "name": "minecraft:golden_sword"
        }
      ]
    },
    {
      "rolls": 4,
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 4.0,
                "max": 8.0
              },
              "add": false
            }
          ],
          "name": "minecraft:sand"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterdeserttemples:chests/pot — YungsBetterDesertTemples-1.20-Forge-3.0.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterDesertTemples-1.20-Forge-3.0.3.jar` · `data/betterdeserttemples/loot_tables/chests/pot.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 4.0,
        "max": 6.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 6.0,
                "max": 12.0
              },
              "add": false
            }
          ],
          "name": "minecraft:terracotta"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 6.0,
                "max": 12.0
              },
              "add": false
            }
          ],
          "name": "minecraft:dirt"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:emerald"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 6.0,
                "max": 12.0
              },
              "add": false
            }
          ],
          "name": "minecraft:potato"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 6.0,
                "max": 12.0
              },
              "add": false
            }
          ],
          "name": "minecraft:wheat"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 4.0,
                "max": 6.0
              },
              "add": false
            }
          ],
          "name": "minecraft:gunpowder"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 6.0,
                "max": 12.0
              },
              "add": false
            }
          ],
          "name": "minecraft:melon_seeds"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterdeserttemples:chests/statue — YungsBetterDesertTemples-1.20-Forge-3.0.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterDesertTemples-1.20-Forge-3.0.3.jar` · `data/betterdeserttemples/loot_tables/chests/statue.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 1.0,
        "max": 2.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:emerald"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:gold_ingot"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterdeserttemples:chests/storage — YungsBetterDesertTemples-1.20-Forge-3.0.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterDesertTemples-1.20-Forge-3.0.3.jar` · `data/betterdeserttemples/loot_tables/chests/storage.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 2.0,
        "max": 4.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 4.0,
                "max": 8.0
              },
              "add": false
            }
          ],
          "name": "minecraft:sand"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 2.0
              },
              "add": false
            }
          ],
          "name": "minecraft:emerald"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:lapis_lazuli"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:weathered_copper"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:oxidized_copper"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 6.0
              },
              "add": false
            }
          ],
          "name": "minecraft:gunpowder"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 5.0
              },
              "add": false
            }
          ],
          "name": "minecraft:bone"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:string"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:rotten_flesh"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:book"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "name": "minecraft:golden_apple"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "name": "minecraft:saddle"
        },
        {
          "type": "minecraft:item",
          "weight": 15,
          "name": "minecraft:iron_horse_armor"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "name": "minecraft:golden_horse_armor"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "name": "minecraft:diamond_horse_armor"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterdeserttemples:chests/tomb — YungsBetterDesertTemples-1.20-Forge-3.0.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterDesertTemples-1.20-Forge-3.0.3.jar` · `data/betterdeserttemples/loot_tables/chests/tomb.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 1.0,
        "max": 3.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 7.0
              },
              "add": false
            }
          ],
          "name": "minecraft:gold_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:emerald"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:saddle"
        },
        {
          "type": "minecraft:item",
          "weight": 15,
          "name": "minecraft:cobweb"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:book"
        },
        {
          "type": "minecraft:empty",
          "weight": 10
        }
      ]
    },
    {
      "rolls": 4,
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:bone"
        },
        {
          "type": "minecraft:item",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:bone_meal"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:gunpowder"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:rotten_flesh"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:string"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 8.0
              },
              "add": false
            }
          ],
          "name": "minecraft:sand"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterdeserttemples:chests/tomb_pharaoh — YungsBetterDesertTemples-1.20-Forge-3.0.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterDesertTemples-1.20-Forge-3.0.3.jar` · `data/betterdeserttemples/loot_tables/chests/tomb_pharaoh.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 3.0,
        "max": 4.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 3.0,
                "max": 8.0
              },
              "add": false
            }
          ],
          "name": "minecraft:gold_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 3.0,
                "max": 6.0
              },
              "add": false
            }
          ],
          "name": "minecraft:emerald"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:book"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 3.0,
                "max": 6.0
              },
              "add": false
            }
          ],
          "name": "minecraft:diamond"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:enchant_randomly",
              "enchantments": [
                "vanishing_curse"
              ]
            },
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:golden_sword"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:enchanted_golden_apple"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:diamond_horse_armor"
        }
      ]
    },
    {
      "rolls": 4,
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:bone"
        },
        {
          "type": "minecraft:item",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:bone_meal"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:gunpowder"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:rotten_flesh"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:string"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 8.0
              },
              "add": false
            }
          ],
          "name": "minecraft:sand"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterdeserttemples:chests/wardrobe — YungsBetterDesertTemples-1.20-Forge-3.0.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterDesertTemples-1.20-Forge-3.0.3.jar` · `data/betterdeserttemples/loot_tables/chests/wardrobe.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 3.0,
        "max": 6.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 3.0,
                "max": 6.0
              },
              "add": false
            }
          ],
          "name": "minecraft:yellow_wool"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 3.0,
                "max": 6.0
              },
              "add": false
            }
          ],
          "name": "minecraft:blue_wool"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 3.0,
                "max": 6.0
              },
              "add": false
            }
          ],
          "name": "minecraft:leather"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:leather_helmet"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:leather_chestplate"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:leather_leggings"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:leather_boots"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_randomly",
              "enchantments": [
                "binding_curse",
                "vanishing_curse"
              ]
            },
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:leather_helmet"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_randomly",
              "enchantments": [
                "binding_curse",
                "vanishing_curse"
              ]
            },
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:leather_chestplate"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_randomly",
              "enchantments": [
                "binding_curse",
                "vanishing_curse"
              ]
            },
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:leather_leggings"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_randomly",
              "enchantments": [
                "binding_curse",
                "vanishing_curse"
              ]
            },
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:leather_boots"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:leather_helmet"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:leather_chestplate"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:leather_leggings"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:leather_boots"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 6.0
              },
              "add": false
            }
          ],
          "name": "minecraft:orange_dye"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 3.0,
                "max": 6.0
              },
              "add": false
            }
          ],
          "name": "minecraft:yellow_dye"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 3.0,
                "max": 6.0
              },
              "add": false
            }
          ],
          "name": "minecraft:blue_dye"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 3.0,
                "max": 6.0
              },
              "add": false
            }
          ],
          "name": "minecraft:green_dye"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 4.0,
                "max": 6.0
              },
              "add": false
            }
          ],
          "name": "minecraft:feather"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterdungeons:skeleton_dungeon/chests/common — YungsBetterDungeons-1.20-Forge-4.0.4.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterDungeons-1.20-Forge-4.0.4.jar` · `data/betterdungeons/loot_tables/skeleton_dungeon/chests/common.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 2.0,
        "max": 4.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:golden_apple"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:enchanted_golden_apple"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:enchant_randomly",
              "enchantments": [
                "smite"
              ]
            }
          ],
          "name": "minecraft:book"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:book"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:bow"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion: \"minecraft:slowness\"}"
            }
          ],
          "name": "minecraft:tipped_arrow"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion: \"minecraft:leaping\"}"
            }
          ],
          "name": "minecraft:tipped_arrow"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion: \"minecraft:fire_resistance\"}"
            }
          ],
          "name": "minecraft:tipped_arrow"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion: \"minecraft:swiftness\"}"
            }
          ],
          "name": "minecraft:tipped_arrow"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion: \"minecraft:long_swiftness\"}"
            }
          ],
          "name": "minecraft:tipped_arrow"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion: \"minecraft:harming\"}"
            }
          ],
          "name": "minecraft:tipped_arrow"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion: \"minecraft:poison\"}"
            }
          ],
          "name": "minecraft:tipped_arrow"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion: \"minecraft:weakness\"}"
            }
          ],
          "name": "minecraft:tipped_arrow"
        }
      ]
    },
    {
      "rolls": {
        "min": 1.0,
        "max": 3.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:iron_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 4.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:gold_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 4.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:redstone"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:name_tag"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:lead"
        }
      ]
    },
    {
      "rolls": 2,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 8.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:bone"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 8.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:bone_meal"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterdungeons:skeleton_dungeon/chests/middle — YungsBetterDungeons-1.20-Forge-4.0.4.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterDungeons-1.20-Forge-4.0.4.jar` · `data/betterdungeons/loot_tables/skeleton_dungeon/chests/middle.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 3.0,
        "max": 5.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 4.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:charcoal"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 4.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:coal"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 4.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:torch"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3.0,
                "max": 5.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:stick"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "name": "minecraft:diamond"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterdungeons:small_dungeon/chests/loot_piles — YungsBetterDungeons-1.20-Forge-4.0.4.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterDungeons-1.20-Forge-4.0.4.jar` · `data/betterdungeons/loot_tables/small_dungeon/chests/loot_piles.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 2.0,
        "max": 3.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 5.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:cobweb"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 5.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:dirt"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 5.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:cobblestone"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterdungeons:small_nether_dungeon/chests/common — YungsBetterDungeons-1.20-Forge-4.0.4.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterDungeons-1.20-Forge-4.0.4.jar` · `data/betterdungeons/loot_tables/small_nether_dungeon/chests/common.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 2.0,
        "max": 6.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "name": "minecraft:coal",
          "type": "minecraft:item",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 4.0,
                "type": "minecraft:uniform"
              }
            }
          ]
        },
        {
          "name": "minecraft:rotten_flesh",
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 8.0,
                "type": "minecraft:uniform"
              }
            }
          ]
        },
        {
          "name": "minecraft:quartz",
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 7.0,
                "type": "minecraft:uniform"
              }
            }
          ]
        },
        {
          "name": "minecraft:iron_ingot",
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4.0,
                "max": 8.0,
                "type": "minecraft:uniform"
              }
            }
          ]
        },
        {
          "name": "minecraft:gold_ingot",
          "type": "minecraft:item",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 7.0,
                "type": "minecraft:uniform"
              }
            }
          ]
        },
        {
          "name": "minecraft:redstone",
          "type": "minecraft:item",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            }
          ]
        },
        {
          "name": "minecraft:nether_wart",
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 10.0,
                "type": "minecraft:uniform"
              }
            }
          ]
        },
        {
          "name": "minecraft:saddle",
          "type": "minecraft:item",
          "weight": 3
        },
        {
          "name": "minecraft:golden_horse_armor",
          "type": "minecraft:item"
        },
        {
          "name": "minecraft:golden_sword",
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "min": 5.0,
                "max": 25.0,
                "type": "minecraft:uniform"
              }
            }
          ]
        },
        {
          "name": "minecraft:golden_boots",
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "min": 5.0,
                "max": 25.0,
                "type": "minecraft:uniform"
              }
            }
          ]
        },
        {
          "name": "minecraft:golden_chestplate",
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "min": 5.0,
                "max": 25.0,
                "type": "minecraft:uniform"
              }
            }
          ]
        },
        {
          "name": "minecraft:golden_leggings",
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "min": 5.0,
                "max": 25.0,
                "type": "minecraft:uniform"
              }
            }
          ]
        },
        {
          "name": "minecraft:golden_helmet",
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "min": 5.0,
                "max": 25.0,
                "type": "minecraft:uniform"
              }
            }
          ]
        },
        {
          "name": "minecraft:iron_sword",
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "min": 10.0,
                "max": 25.0,
                "type": "minecraft:uniform"
              }
            }
          ]
        },
        {
          "name": "minecraft:chainmail_boots",
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "min": 10.0,
                "max": 25.0,
                "type": "minecraft:uniform"
              }
            }
          ]
        },
        {
          "name": "minecraft:chainmail_chestplate",
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "min": 10.0,
                "max": 25.0,
                "type": "minecraft:uniform"
              }
            }
          ]
        },
        {
          "name": "minecraft:chainmail_leggings",
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "min": 10.0,
                "max": 25.0,
                "type": "minecraft:uniform"
              }
            }
          ]
        },
        {
          "name": "minecraft:chainmail_helmet",
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "min": 10.0,
                "max": 25.0,
                "type": "minecraft:uniform"
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:music_disc_otherside"
        }
      ]
    },
    {
      "rolls": {
        "min": 1.0,
        "max": 3.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "name": "minecraft:saddle",
          "type": "minecraft:item",
          "weight": 20
        },
        {
          "name": "minecraft:music_disc_13",
          "type": "minecraft:item",
          "weight": 15
        },
        {
          "name": "minecraft:music_disc_blocks",
          "type": "minecraft:item",
          "weight": 15
        },
        {
          "name": "minecraft:music_disc_chirp",
          "type": "minecraft:item",
          "weight": 15
        },
        {
          "name": "minecraft:music_disc_pigstep",
          "type": "minecraft:item",
          "weight": 4
        },
        {
          "name": "minecraft:name_tag",
          "type": "minecraft:item",
          "weight": 20
        },
        {
          "name": "minecraft:enchanted_golden_apple",
          "type": "minecraft:item",
          "weight": 2
        },
        {
          "name": "minecraft:book",
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ]
        }
      ]
    },
    {
      "rolls": {
        "min": 1.0,
        "max": 3.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "name": "minecraft:coal",
          "type": "minecraft:item",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 9.0,
                "type": "minecraft:uniform"
              }
            }
          ]
        },
        {
          "name": "minecraft:rotten_flesh",
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 5.0,
                "type": "minecraft:uniform"
              }
            }
          ]
        },
        {
          "name": "minecraft:quartz",
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 9.0,
                "type": "minecraft:uniform"
              }
            }
          ]
        },
        {
          "name": "minecraft:gold_nugget",
          "type": "minecraft:item",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4.0,
                "max": 8.0,
                "type": "minecraft:uniform"
              }
            }
          ]
        },
        {
          "name": "minecraft:gold_ingot",
          "type": "minecraft:item",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3.0,
                "max": 9.0,
                "type": "minecraft:uniform"
              }
            }
          ]
        },
        {
          "name": "minecraft:redstone",
          "type": "minecraft:item",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 9.0,
                "type": "minecraft:uniform"
              }
            }
          ]
        },
        {
          "name": "minecraft:nether_wart",
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 6.0,
                "max": 10.0,
                "type": "minecraft:uniform"
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterdungeons:spider_dungeon/chests/egg_room — YungsBetterDungeons-1.20-Forge-4.0.4.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterDungeons-1.20-Forge-4.0.4.jar` · `data/betterdungeons/loot_tables/spider_dungeon/chests/egg_room.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 1.0,
        "max": 2.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:golden_apple"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:saddle"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:enchanted_golden_apple"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:diamond"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:enchant_randomly",
              "enchantments": [
                "bane_of_arthropods"
              ]
            }
          ],
          "name": "minecraft:book"
        },
        {
          "type": "minecraft:item",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:book"
        }
      ]
    },
    {
      "rolls": {
        "min": 3.0,
        "max": 6.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion: \"minecraft:weakness\"}"
            }
          ],
          "name": "minecraft:potion"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion: \"minecraft:slowness\"}"
            }
          ],
          "name": "minecraft:potion"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion: \"minecraft:harming\"}"
            }
          ],
          "name": "minecraft:potion"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion: \"minecraft:strong_harming\"}"
            }
          ],
          "name": "minecraft:potion"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion: \"minecraft:invisibility\"}"
            }
          ],
          "name": "minecraft:potion"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion: \"minecraft:weakness\"}"
            }
          ],
          "name": "minecraft:splash_potion"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion: \"minecraft:slowness\"}"
            }
          ],
          "name": "minecraft:splash_potion"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion: \"minecraft:harming\"}"
            }
          ],
          "name": "minecraft:splash_potion"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion: \"minecraft:strong_harming\"}"
            }
          ],
          "name": "minecraft:splash_potion"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion: \"minecraft:invisibility\"}"
            }
          ],
          "name": "minecraft:splash_potion"
        }
      ]
    },
    {
      "rolls": {
        "min": 3.0,
        "max": 4.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 5.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:spider_eye"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 5.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:coal"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 5.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:beetroot_seeds"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 5.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:pumpkin_seeds"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 5.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:melon_seeds"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:lead"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:name_tag"
        }
      ]
    },
    {
      "rolls": 3,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:cobweb"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:string"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterdungeons:zombie_dungeon/chests/common — YungsBetterDungeons-1.20-Forge-4.0.4.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterDungeons-1.20-Forge-4.0.4.jar` · `data/betterdungeons/loot_tables/zombie_dungeon/chests/common.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 0.0,
        "max": 2.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:golden_apple"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:saddle"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:name_tag"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "name": "minecraft:experience_bottle"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:enchanted_golden_apple"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:enchant_randomly",
              "enchantments": [
                "sweeping",
                "fire_aspect"
              ]
            }
          ],
          "name": "minecraft:book"
        },
        {
          "type": "minecraft:item",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:book"
        }
      ]
    },
    {
      "rolls": {
        "min": 1.0,
        "max": 2.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:stone_sword"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:stone_axe"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:stone_shovel"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:iron_sword"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:iron_axe"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:iron_shovel"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:iron_helmet"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:iron_chestplate"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:iron_leggings"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:iron_boots"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:iron_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:gold_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:diamond_sword"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:diamond_axe"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:diamond_shovel"
        }
      ]
    },
    {
      "rolls": {
        "min": 3.0,
        "max": 4.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 3.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:apple"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:coal"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:torch"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 4.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:beetroot_seeds"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 4.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:wheat_seeds"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:cornflower"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:brown_mushroom"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:red_mushroom"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:dead_bush"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:poppy"
        }
      ]
    },
    {
      "rolls": {
        "min": 1.0,
        "max": 3.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 3.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:rotten_flesh"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 2.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:carrot"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 2.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:potato"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterdungeons:zombie_dungeon/chests/special — YungsBetterDungeons-1.20-Forge-4.0.4.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterDungeons-1.20-Forge-4.0.4.jar` · `data/betterdungeons/loot_tables/zombie_dungeon/chests/special.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 0.0,
        "max": 2.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:golden_apple"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:saddle"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:name_tag"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "name": "minecraft:experience_bottle"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:enchanted_golden_apple"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:enchant_randomly",
              "enchantments": [
                "sweeping",
                "fire_aspect"
              ]
            }
          ],
          "name": "minecraft:book"
        },
        {
          "type": "minecraft:item",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:book"
        }
      ]
    },
    {
      "rolls": {
        "min": 1.0,
        "max": 2.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:stone_sword"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:stone_axe"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:stone_shovel"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:iron_sword"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:iron_axe"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:iron_shovel"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:iron_helmet"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:iron_chestplate"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:iron_leggings"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:iron_boots"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:iron_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:gold_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:diamond_sword"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:diamond_axe"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:diamond_shovel"
        }
      ]
    },
    {
      "rolls": {
        "min": 3.0,
        "max": 4.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 3.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:apple"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:coal"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:torch"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 4.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:beetroot_seeds"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 4.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:wheat_seeds"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:cornflower"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:brown_mushroom"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:red_mushroom"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:dead_bush"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:poppy"
        }
      ]
    },
    {
      "rolls": {
        "min": 1.0,
        "max": 3.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 3.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:rotten_flesh"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 2.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:carrot"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 2.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:potato"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterdungeons:zombie_dungeon/chests/tombstone — YungsBetterDungeons-1.20-Forge-4.0.4.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterDungeons-1.20-Forge-4.0.4.jar` · `data/betterdungeons/loot_tables/zombie_dungeon/chests/tombstone.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 4.0,
        "max": 6.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:bone"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:bone_meal"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:emerald"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:diamond"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_randomly",
              "enchantments": [
                "smite",
                "sweeping",
                "fire_aspect"
              ]
            }
          ],
          "name": "minecraft:diamond_sword"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterfortresses:chests/beacon — YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar` · `data/betterfortresses/loot_tables/chests/beacon.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 2.0,
        "max": 4.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 4.0,
                "max": 8.0
              },
              "add": false
            }
          ],
          "name": "minecraft:arrow"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:fire_charge"
        }
      ]
    },
    {
      "rolls": 1,
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 20,
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:bow"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 10,
              "treasure": true
            },
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:bow"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 20,
              "treasure": true
            },
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:bow"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterfortresses:chests/extra — YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar` · `data/betterfortresses/loot_tables/chests/extra.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 2.0,
        "max": 5.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 25,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:iron_nugget"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:gold_nugget"
        },
        {
          "type": "minecraft:item",
          "weight": 25,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:iron_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:gold_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:leather"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:string"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 3.0,
                "max": 6.0
              },
              "add": false
            }
          ],
          "name": "minecraft:glowstone_dust"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 3.0,
                "max": 6.0
              },
              "add": false
            }
          ],
          "name": "minecraft:quartz"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterfortresses:chests/hall — YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar` · `data/betterfortresses/loot_tables/chests/hall.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 2.0,
        "max": 5.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:iron_nugget"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:gold_nugget"
        },
        {
          "type": "minecraft:item",
          "weight": 25,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 2.0
              },
              "add": false
            }
          ],
          "name": "minecraft:iron_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:gold_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:leather"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:string"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 3.0,
                "max": 6.0
              },
              "add": false
            }
          ],
          "name": "minecraft:glowstone_dust"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterfortresses:chests/keep — YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar` · `data/betterfortresses/loot_tables/chests/keep.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 2.0,
        "max": 4.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 100,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:flint"
        },
        {
          "type": "minecraft:item",
          "weight": 100,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:coal"
        },
        {
          "type": "minecraft:item",
          "weight": 100,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:string"
        },
        {
          "type": "minecraft:item",
          "weight": 100,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:gunpowder"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "name": "minecraft:saddle"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:iron_horse_armor"
        },
        {
          "type": "minecraft:item",
          "weight": 7,
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:golden_horse_armor"
        },
        {
          "type": "minecraft:item",
          "weight": 4,
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:diamond_horse_armor"
        },
        {
          "type": "minecraft:item",
          "weight": 20,
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:stone_sword"
        },
        {
          "type": "minecraft:item",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 10,
              "treasure": true
            },
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:stone_sword"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:iron_sword"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 20,
              "treasure": true
            },
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:iron_sword"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:golden_sword"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30,
              "treasure": true
            },
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:golden_sword"
        },
        {
          "type": "minecraft:item",
          "weight": 20,
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:leather_helmet"
        },
        {
          "type": "minecraft:item",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 10,
              "treasure": true
            },
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:leather_helmet"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:chainmail_helmet"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 20,
              "treasure": true
            },
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:chainmail_helmet"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:golden_helmet"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30,
              "treasure": true
            },
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:golden_helmet"
        },
        {
          "type": "minecraft:item",
          "weight": 20,
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:leather_chestplate"
        },
        {
          "type": "minecraft:item",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 10,
              "treasure": true
            },
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:leather_chestplate"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:chainmail_chestplate"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 20,
              "treasure": true
            },
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:chainmail_chestplate"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:golden_chestplate"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30,
              "treasure": true
            },
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:golden_chestplate"
        },
        {
          "type": "minecraft:item",
          "weight": 20,
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:leather_leggings"
        },
        {
          "type": "minecraft:item",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 10,
              "treasure": true
            },
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:leather_leggings"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:chainmail_leggings"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 20,
              "treasure": true
            },
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:chainmail_leggings"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:golden_leggings"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30,
              "treasure": true
            },
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:golden_leggings"
        },
        {
          "type": "minecraft:item",
          "weight": 20,
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:leather_boots"
        },
        {
          "type": "minecraft:item",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 10,
              "treasure": true
            },
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:leather_boots"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:chainmail_boots"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 20,
              "treasure": true
            },
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:chainmail_boots"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:golden_boots"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30,
              "treasure": true
            },
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            }
          ],
          "name": "minecraft:golden_boots"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterfortresses:chests/obsidian — YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar` · `data/betterfortresses/loot_tables/chests/obsidian.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 1.0,
        "max": 2.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 5.0
              },
              "add": false
            }
          ],
          "name": "minecraft:obsidian"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:crying_obsidian"
        }
      ]
    },
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 0.0,
        "max": 1.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 10,
          "name": "minecraft:flint_and_steel"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:diamond"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterfortresses:chests/puzzle — YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar` · `data/betterfortresses/loot_tables/chests/puzzle.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 3.0,
        "max": 6.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 5.0
              },
              "add": false
            }
          ],
          "name": "minecraft:iron_nugget"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 5.0
              },
              "add": false
            }
          ],
          "name": "minecraft:gold_nugget"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 5.0
              },
              "add": false
            }
          ],
          "name": "minecraft:iron_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 5.0
              },
              "add": false
            }
          ],
          "name": "minecraft:gold_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:nether_wart"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 2.0
              },
              "add": false
            }
          ],
          "name": "minecraft:diamond"
        }
      ]
    },
    {
      "rolls": {
        "type": "minecraft:constant",
        "value": 1
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:blaze_rod"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterfortresses:chests/quarters — YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar` · `data/betterfortresses/loot_tables/chests/quarters.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 3.0,
        "max": 6.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 5.0
              },
              "add": false
            }
          ],
          "name": "minecraft:iron_nugget"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 5.0
              },
              "add": false
            }
          ],
          "name": "minecraft:gold_nugget"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 5.0
              },
              "add": false
            }
          ],
          "name": "minecraft:iron_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 5.0
              },
              "add": false
            }
          ],
          "name": "minecraft:gold_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:nether_wart"
        },
        {
          "type": "minecraft:item",
          "weight": 25,
          "name": "minecraft:diamond"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterfortresses:chests/storage — YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar` · `data/betterfortresses/loot_tables/chests/storage.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 1.0,
        "max": 3.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:iron_nugget"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:gold_nugget"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:gold_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:raw_gold"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 3.0,
                "max": 8.0
              },
              "add": false
            }
          ],
          "name": "minecraft:quartz"
        }
      ]
    },
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 1.0,
        "max": 2.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 50,
          "name": "minecraft:magma_cream"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "name": "minecraft:fire_charge"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "name": "minecraft:diamond"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterfortresses:chests/worship — YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterNetherFortresses-1.20-Forge-2.0.6.jar` · `data/betterfortresses/loot_tables/chests/worship.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 3.0,
        "max": 6.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 5.0
              },
              "add": false
            }
          ],
          "name": "minecraft:iron_nugget"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 5.0
              },
              "add": false
            }
          ],
          "name": "minecraft:gold_nugget"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 5.0
              },
              "add": false
            }
          ],
          "name": "minecraft:iron_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 5.0
              },
              "add": false
            }
          ],
          "name": "minecraft:gold_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 50,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:nether_wart"
        }
      ]
    },
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 1.0,
        "max": 2.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 50,
          "name": "minecraft:diamond"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betteroceanmonuments:chests/upper_side_chamber — YungsBetterOceanMonuments-1.20-Forge-3.0.4.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterOceanMonuments-1.20-Forge-3.0.4.jar` · `data/betteroceanmonuments/loot_tables/chests/upper_side_chamber.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 8.0,
        "max": 10.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:nautilus_shell"
        }
      ]
    },
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 3.0,
        "max": 6.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 10.0,
                "max": 16.0
              },
              "add": false
            }
          ],
          "name": "minecraft:prismarine_shard"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 10.0,
                "max": 16.0
              },
              "add": false
            }
          ],
          "name": "minecraft:prismarine_crystals"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterstrongholds:chests/armoury — YungsBetterStrongholds-1.20-Forge-4.0.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterStrongholds-1.20-Forge-4.0.3.jar` · `data/betterstrongholds/loot_tables/chests/armoury.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 1.0,
        "max": 3.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:wooden_sword"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 10,
              "treasure": true
            }
          ],
          "name": "minecraft:wooden_sword"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:iron_sword"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 20,
              "treasure": true
            }
          ],
          "name": "minecraft:iron_sword"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:diamond_sword"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30,
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_sword"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:leather_helmet"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:leather_chestplate"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:leather_leggings"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:leather_boots"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:chainmail_helmet"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:chainmail_chestplate"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:chainmail_leggings"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:chainmail_boots"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:iron_helmet"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 20,
              "treasure": true
            }
          ],
          "name": "minecraft:iron_helmet"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:iron_chestplate"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 20,
              "treasure": true
            }
          ],
          "name": "minecraft:iron_chestplate"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:iron_leggings"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 20,
              "treasure": true
            }
          ],
          "name": "minecraft:iron_leggings"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:iron_boots"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 20,
              "treasure": true
            }
          ],
          "name": "minecraft:iron_boots"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:diamond_helmet"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30,
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_helmet"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:diamond_chestplate"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30,
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_chestplate"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:diamond_leggings"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30,
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_leggings"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:diamond_boots"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30,
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_boots"
        },
        {
          "type": "minecraft:item",
          "weight": 6,
          "name": "minecraft:shield"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:bow"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30,
              "treasure": true
            }
          ],
          "name": "minecraft:bow"
        },
        {
          "type": "minecraft:item",
          "weight": 7,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 7.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:coal"
        },
        {
          "type": "minecraft:item",
          "weight": 7,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 7.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:charcoal"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterstrongholds:chests/cmd_yung — YungsBetterStrongholds-1.20-Forge-4.0.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterStrongholds-1.20-Forge-4.0.3.jar` · `data/betterstrongholds/loot_tables/chests/cmd_yung.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 1.0,
        "max": 1.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30,
              "treasure": true
            },
            {
              "function": "minecraft:set_name",
              "name": "YUNG's Better Sword"
            }
          ],
          "name": "minecraft:diamond_sword"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterstrongholds:chests/common — YungsBetterStrongholds-1.20-Forge-4.0.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterStrongholds-1.20-Forge-4.0.3.jar` · `data/betterstrongholds/loot_tables/chests/common.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 2.0,
        "max": 3.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 5.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:iron_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 3.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:gold_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4.0,
                "max": 9.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:redstone"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3.0,
                "max": 8.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:coal"
        },
        {
          "type": "minecraft:item",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 3.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:bread"
        },
        {
          "type": "minecraft:item",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 3.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:potato"
        },
        {
          "type": "minecraft:item",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 3.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:apple"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 4.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:stick"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_pickaxe"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:wooden_pickaxe"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:ender_pearl"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_horse_armor"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_horse_armor"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_horse_armor"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:saddle"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:cobweb"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 4.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:torch"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30,
              "treasure": true
            }
          ],
          "name": "minecraft:book"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterstrongholds:chests/crypt — YungsBetterStrongholds-1.20-Forge-4.0.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterStrongholds-1.20-Forge-4.0.3.jar` · `data/betterstrongholds/loot_tables/chests/crypt.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 4.0,
        "max": 6.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:bone"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:bone_meal"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:ender_pearl"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:diamond"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:iron_sword"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterstrongholds:chests/grand_library — YungsBetterStrongholds-1.20-Forge-4.0.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterStrongholds-1.20-Forge-4.0.3.jar` · `data/betterstrongholds/loot_tables/chests/grand_library.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 2.0,
        "max": 10.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 3.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:book"
        },
        {
          "type": "minecraft:item",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 7.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:paper"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:map"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:compass"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 10,
              "treasure": true
            }
          ],
          "name": "minecraft:book"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 20,
              "treasure": true
            }
          ],
          "name": "minecraft:book"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30,
              "treasure": true
            }
          ],
          "name": "minecraft:book"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterstrongholds:chests/library_md — YungsBetterStrongholds-1.20-Forge-4.0.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterStrongholds-1.20-Forge-4.0.3.jar` · `data/betterstrongholds/loot_tables/chests/library_md.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 2.0,
        "max": 10.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 3.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:book"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 7.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:paper"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:map"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:compass"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 10,
              "treasure": true
            }
          ],
          "name": "minecraft:book"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 20,
              "treasure": true
            }
          ],
          "name": "minecraft:book"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30,
              "treasure": true
            }
          ],
          "name": "minecraft:book"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterstrongholds:chests/mess — YungsBetterStrongholds-1.20-Forge-4.0.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterStrongholds-1.20-Forge-4.0.3.jar` · `data/betterstrongholds/loot_tables/chests/mess.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 2.0,
        "max": 10.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 3.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:bread"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 3.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:apple"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 3.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:potato"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 2.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:mushroom_stew"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3.0,
                "max": 7.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:cookie"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3.0,
                "max": 7.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:beetroot"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 5.0,
                "max": 7.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:melon_slice"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:golden_apple"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterstrongholds:chests/prison_lg — YungsBetterStrongholds-1.20-Forge-4.0.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterStrongholds-1.20-Forge-4.0.3.jar` · `data/betterstrongholds/loot_tables/chests/prison_lg.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 2.0,
        "max": 6.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 3.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:iron_bars"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 7.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:coal"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 7.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:rotten_flesh"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 4.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:chain"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:diamond"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:emerald"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterstrongholds:chests/trap — YungsBetterStrongholds-1.20-Forge-4.0.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterStrongholds-1.20-Forge-4.0.3.jar` · `data/betterstrongholds/loot_tables/chests/trap.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 4.0,
        "max": 5.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:iron_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:gold_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 2.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:diamond"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 2.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:emerald"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 5.0,
                "max": 7.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:bone"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_apple"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:ender_pearl"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterstrongholds:chests/treasure — YungsBetterStrongholds-1.20-Forge-4.0.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterStrongholds-1.20-Forge-4.0.3.jar` · `data/betterstrongholds/loot_tables/chests/treasure.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 1.0,
        "max": 2.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 3.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:iron_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 7.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:iron_nugget"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 3.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:gold_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 7.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:gold_nugget"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 3.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:diamond"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 2.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:emerald"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:redstone"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:lapis_lazuli"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>betterwitchhuts:chests/hut_0 — YungsBetterWitchHuts-1.20-Forge-3.0.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsBetterWitchHuts-1.20-Forge-3.0.3.jar` · `data/betterwitchhuts/loot_tables/chests/hut_0.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 3.0,
        "max": 5.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 3.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:sugar"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2.0,
                "max": 5.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:gunpowder"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3.0,
                "max": 6.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:carrot"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:rabbit_foot"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:pufferfish"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:phantom_membrane"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4.0,
                "max": 7.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:redstone"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1.0,
                "max": 3.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:spider_eye"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4.0,
                "max": 8.0,
                "type": "minecraft:uniform"
              }
            }
          ],
          "name": "minecraft:slime_ball"
        }
      ]
    },
    {
      "rolls": {
        "min": 2.0,
        "max": 4.0,
        "type": "minecraft:uniform"
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion:\"minecraft:water\"}"
            }
          ],
          "name": "minecraft:potion"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion:\"minecraft:swiftness\"}"
            }
          ],
          "name": "minecraft:potion"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion:\"minecraft:night_vision\"}"
            }
          ],
          "name": "minecraft:potion"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion:\"minecraft:invisibility\"}"
            }
          ],
          "name": "minecraft:potion"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion:\"minecraft:weakness\"}"
            }
          ],
          "name": "minecraft:splash_potion"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion:\"minecraft:harming\"}"
            }
          ],
          "name": "minecraft:splash_potion"
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion:\"minecraft:slowness\"}"
            }
          ],
          "name": "minecraft:splash_potion"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>cataclysm:archaeology/cursed_pyramid — L_Enders_Cataclysm-3.31.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\L_Enders_Cataclysm-3.31.jar` · `data/cataclysm/loot_tables/archaeology/cursed_pyramid.json`

```json
{
  "type": "minecraft:archaeology",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:archer_pottery_sherd"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:miner_pottery_sherd"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:prize_pottery_sherd"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:skull_pottery_sherd"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:tnt"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:gunpowder"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald"
        },
        {
          "type": "minecraft:item",
          "name": "cataclysm:necklace_of_the_desert"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "cataclysm:archaeology/cursed_pyramid"
}
```

</details>

<details>
<summary>cataclysm:archaeology/cursed_pyramid_necklace — L_Enders_Cataclysm-3.31.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\L_Enders_Cataclysm-3.31.jar` · `data/cataclysm/loot_tables/archaeology/cursed_pyramid_necklace.json`

```json
{
  "type": "minecraft:archaeology",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "cataclysm:necklace_of_the_desert"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "cataclysm:archaeology/cursed_pyramid_necklace"
}
```

</details>

<details>
<summary>cataclysm:chests/abandoned — L_Enders_Cataclysm-3.31.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\L_Enders_Cataclysm-3.31.jar` · `data/cataclysm/loot_tables/chests/abandoned.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "cataclysm:sturdy_boots",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:leather",
          "weight": 12
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_ingot",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "cataclysm:black_steel_ingot",
          "weight": 7
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_ingot",
          "weight": 7
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:saddle",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_horse_armor"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_horse_armor"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_horse_armor"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 10.0,
                "min": 5.0
              }
            }
          ],
          "name": "minecraft:iron_sword",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 10.0,
                "min": 5.0
              }
            }
          ],
          "name": "minecraft:iron_boots",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 10.0,
                "min": 5.0
              }
            }
          ],
          "name": "minecraft:iron_chestplate",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 10.0,
                "min": 5.0
              }
            }
          ],
          "name": "minecraft:iron_leggings",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 10.0,
                "min": 5.0
              }
            }
          ],
          "name": "minecraft:iron_helmet",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 10.0,
                "min": 5.0
              }
            }
          ],
          "name": "minecraft:iron_pickaxe",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 10.0,
                "min": 5.0
              }
            }
          ],
          "name": "minecraft:iron_shovel",
          "weight": 3
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 6.0,
        "min": 2.0
      }
    }
  ]
}
```

</details>

<details>
<summary>cataclysm:chests/abandoned_treasure — L_Enders_Cataclysm-3.31.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\L_Enders_Cataclysm-3.31.jar` · `data/cataclysm/loot_tables/chests/abandoned_treasure.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "cataclysm:sturdy_boots",
          "weight": 4
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:leather",
          "weight": 12
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_ingot",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "cataclysm:black_steel_ingot",
          "weight": 7
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_ingot",
          "weight": 7
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:emerald",
          "weight": 4
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:saddle",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_horse_armor"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_horse_armor"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_horse_armor"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 12.0,
                "min": 6.0
              }
            }
          ],
          "name": "minecraft:iron_sword",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 12.0,
                "min": 6.0
              }
            }
          ],
          "name": "minecraft:iron_boots",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 12.0,
                "min": 6.0
              }
            }
          ],
          "name": "minecraft:iron_chestplate",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 12.0,
                "min": 6.0
              }
            }
          ],
          "name": "minecraft:iron_leggings",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 12.0,
                "min": 6.0
              }
            }
          ],
          "name": "minecraft:iron_helmet",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 12.0,
                "min": 6.0
              }
            }
          ],
          "name": "minecraft:iron_pickaxe",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 10.0,
                "min": 5.0
              }
            }
          ],
          "name": "cataclysm:black_steel_sword",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 10.0,
                "min": 5.0
              }
            }
          ],
          "name": "cataclysm:black_steel_axe",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 10.0,
                "min": 5.0
              }
            }
          ],
          "name": "cataclysm:black_steel_shovel",
          "weight": 3
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 6.0,
        "min": 2.0
      }
    },
    {
      "rolls": 1.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "cataclysm:ring_of_grudged",
          "weight": 1
        },
        {
          "type": "minecraft:item",
          "name": "cataclysm:berserker_soul_amulet",
          "weight": 1
        },
        {
          "type": "minecraft:empty",
          "weight": 2
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>cataclysm:chests/acropolis_treasure — L_Enders_Cataclysm-3.31.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\L_Enders_Cataclysm-3.31.jar` · `data/cataclysm/loot_tables/chests/acropolis_treasure.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 9.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:diamond",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:copper_ingot",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 3.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "cataclysm:lacrima",
          "weight": 6
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 32.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:book",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_apple",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_golden_apple",
          "weight": 1
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_ingot",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 9.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:emerald",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:nautilus_shell",
          "weight": 7
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:scute",
          "weight": 12
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_sword",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_boots",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_chestplate",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_leggings",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_helmet",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_pickaxe",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_shovel",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:golden_sword",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:trident",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:golden_shovel",
          "weight": 3
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 6.0,
        "min": 2.0
      }
    }
  ],
  "random_sequence": "cataclysm:chests/acropolis_treasure"
}
```

</details>

<details>
<summary>cataclysm:chests/amethyst_nest_chest — L_Enders_Cataclysm-3.31.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\L_Enders_Cataclysm-3.31.jar` · `data/cataclysm/loot_tables/chests/amethyst_nest_chest.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_apple",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_golden_apple"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:name_tag",
          "weight": 30
        },
        {
          "type": "minecraft:empty",
          "weight": 5
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "cataclysm:amethyst_crab_meat",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "cataclysm:amethyst_crab_shell",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 9.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:redstone",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 9.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:lapis_lazuli",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:diamond",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 3.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:coal",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bread",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 6.0,
                "min": 3.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:glow_berries",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:melon_seeds",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:pumpkin_seeds",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:beetroot_seeds",
          "weight": 10
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 4.0,
        "min": 2.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 16.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:amethyst_shard",
          "weight": 15
        }
      ],
      "rolls": 3.0
    }
  ]
}
```

</details>

<details>
<summary>cataclysm:chests/desert_treasure — L_Enders_Cataclysm-3.31.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\L_Enders_Cataclysm-3.31.jar` · `data/cataclysm/loot_tables/chests/desert_treasure.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond",
          "weight": 4
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_ingot",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "cataclysm:ancient_metal_ingot",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:emerald",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_horse_armor",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_horse_armor",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_horse_armor",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:book",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_apple",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_golden_apple",
          "weight": 3
        },
        {
          "type": "minecraft:empty",
          "weight": 15
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 4.0,
        "min": 2.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 6
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 2.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:dune_armor_trim_smithing_template"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "cataclysm:unbreakable_skull",
          "weight": 1
        },
        {
          "type": "minecraft:item",
          "name": "cataclysm:vitality_ankh",
          "weight": 1
        },
        {
          "type": "minecraft:empty",
          "weight": 2
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>cataclysm:chests/frosted_prison_treasure — L_Enders_Cataclysm-3.31.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\L_Enders_Cataclysm-3.31.jar` · `data/cataclysm/loot_tables/chests/frosted_prison_treasure.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 9.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:diamond",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_ingot",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 9.0,
                "min": 5.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "cataclysm:black_steel_ingot",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_ingot",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 9.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:emerald",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:saddle",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_horse_armor"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_horse_armor"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_horse_armor"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_sword",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_boots",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_chestplate",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_leggings",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_helmet",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_pickaxe",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_shovel",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "cataclysm:black_steel_sword",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "cataclysm:black_steel_axe",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:iron_shovel",
          "weight": 3
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 6.0,
        "min": 2.0
      }
    }
  ],
  "random_sequence": "cataclysm:chests/frosted_prison_treasure"
}
```

</details>

<details>
<summary>irons_spellbooks:chests/additional_ancient_city_loot — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/additional_ancient_city_loot.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 7
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.15
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.3,
                "max": 1
              }
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.7
        }
      ]
    },
    {
      "rolls": {
        "min": 1,
        "max": 3
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/good_ink"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.35
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "irons_spellbooks:ruined_book"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.1
        }
      ]
    },
    {
      "rolls": 3,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:ancient_knowledge_fragment",
          "conditions": [
            {
              "condition": "minecraft:random_chance",
              "chance": 0.25
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "irons_spellbooks:blank_rune"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.25
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/additional_end_city_loot — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/additional_end_city_loot.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 0,
                "max": 15
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": {
        "min": 0,
        "max": 2
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.4,
                "max": 1.0
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.4,
                "max": 1.0
              },
              "spell_filter": {
                "school": "irons_spellbooks:ender"
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": {
        "min": 0,
        "max": 2
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/random_elixir",
          "weight": 8
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:potion",
          "functions": [
            {
              "function": "minecraft:set_potion",
              "id": "irons_spellbooks:instant_mana_one"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:potion",
          "functions": [
            {
              "function": "minecraft:set_potion",
              "id": "irons_spellbooks:instant_mana_two"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:potion",
          "functions": [
            {
              "function": "minecraft:set_potion",
              "id": "irons_spellbooks:instant_mana_three"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:potion",
          "functions": [
            {
              "function": "minecraft:set_potion",
              "id": "irons_spellbooks:instant_mana_four"
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.3
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.5
        }
      ]
    },
    {
      "rolls": 3,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/good_ink"
        },
        {
          "type": "minecraft:empty"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:ancient_knowledge_fragment",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 0,
                "max": 3
              }
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.2
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/additional_generic_loot — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\ampere\datapacks\TheOptimizer_AdventureLoot.zip` · `data/irons_spellbooks/loot_tables/chests/additional_generic_loot.json`

```json
{
  "pools": [
    {
      "rolls": {
        "min": 1,
        "max": 3
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 2,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "weight": 2,
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.1,
                "max": 0.45
              }
            }
          ]
        },
        {
          "type": "minecraft:empty",
          "weight": 1
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.45
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.25
        }
      ]
    },
    {
      "rolls": {
        "min": 1,
        "max": 3
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/decent_ink"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/additional_generic_loot — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/additional_generic_loot.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.35
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3,
                "max": 10
              }
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.15
        }
      ]
    },
    {
      "rolls": 2,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.0,
                "max": 0.3
              }
            }
          ]
        },
        {
          "type": "minecraft:empty",
          "weight": 3
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.75
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:rotten_spell_book"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.01
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.04
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.05
        }
      ]
    },
    {
      "rolls": 2,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/poor_ink"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.1
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/additional_generic_loot — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\moonlight-global-datapacks\TheOptimizer_AdventureLoot.zip` · `data/irons_spellbooks/loot_tables/chests/additional_generic_loot.json`

```json
{
  "pools": [
    {
      "rolls": {
        "min": 1,
        "max": 3
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 2,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "weight": 2,
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.1,
                "max": 0.45
              }
            }
          ]
        },
        {
          "type": "minecraft:empty",
          "weight": 1
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.45
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.25
        }
      ]
    },
    {
      "rolls": {
        "min": 1,
        "max": 3
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/decent_ink"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/additional_good_loot — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\ampere\datapacks\TheOptimizer_AdventureLoot.zip` · `data/irons_spellbooks/loot_tables/chests/additional_good_loot.json`

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 5
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 2,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "weight": 3,
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.1,
                "max": 0.6
              }
            }
          ]
        },
        {
          "type": "minecraft:empty",
          "weight": 1
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:rotten_spell_book"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.35
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.75
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.4
        }
      ]
    },
    {
      "rolls": {
        "min": 2,
        "max": 4
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/good_ink"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/additional_good_loot — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/additional_good_loot.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 10
              }
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.85
        }
      ]
    },
    {
      "rolls": 2,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.0,
                "max": 0.6
              }
            }
          ]
        },
        {
          "type": "minecraft:empty",
          "weight": 2
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:rotten_spell_book"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.01
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.1
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.15
        }
      ]
    },
    {
      "rolls": {
        "min": 1,
        "max": 4
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/good_ink"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.25
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/additional_good_loot — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\moonlight-global-datapacks\TheOptimizer_AdventureLoot.zip` · `data/irons_spellbooks/loot_tables/chests/additional_good_loot.json`

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 5
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 2,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "weight": 3,
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.1,
                "max": 0.6
              }
            }
          ]
        },
        {
          "type": "minecraft:empty",
          "weight": 1
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:rotten_spell_book"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.35
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.75
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.4
        }
      ]
    },
    {
      "rolls": {
        "min": 2,
        "max": 4
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/good_ink"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/additional_library_loot — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/additional_library_loot.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 15
              }
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.3
        }
      ]
    },
    {
      "rolls": {
        "min": 3,
        "max": 5
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.0,
                "max": 1.0
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.0,
                "max": 1.0
              },
              "spell_filter": {
                "school": "irons_spellbooks:ender"
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.3
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.5
        }
      ]
    },
    {
      "rolls": 5,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/good_ink"
        },
        {
          "type": "minecraft:empty"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:ancient_knowledge_fragment",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.8
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/additional_nether_loot — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/additional_nether_loot.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 7
              }
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.75
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.075
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.2,
                "max": 0.8
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.2,
                "max": 0.8
              },
              "spell_filter": {
                "school": "irons_spellbooks:fire"
              }
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.6
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "irons_spellbooks:blank_rune"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.15
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/additional_treasure_loot — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\ampere\datapacks\TheOptimizer_AdventureLoot.zip` · `data/irons_spellbooks/loot_tables/chests/additional_treasure_loot.json`

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4,
                "max": 8
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": {
        "min": 2,
        "max": 3
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "weight": 4,
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.2,
                "max": 0.7
              }
            }
          ]
        },
        {
          "type": "minecraft:empty",
          "weight": 1
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 3
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.6
        }
      ]
    },
    {
      "rolls": {
        "min": 2,
        "max": 4
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/great_ink"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:ancient_knowledge_fragment",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.75
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/additional_treasure_loot — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/additional_treasure_loot.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 15
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 2,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.0,
                "max": 0.7
              }
            }
          ]
        },
        {
          "type": "minecraft:empty",
          "weight": 1
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.3
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.8
        }
      ]
    },
    {
      "rolls": {
        "min": 1,
        "max": 3
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/great_ink"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.3
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:ancient_knowledge_fragment",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 0,
                "max": 3
              }
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.1
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/additional_treasure_loot — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\moonlight-global-datapacks\TheOptimizer_AdventureLoot.zip` · `data/irons_spellbooks/loot_tables/chests/additional_treasure_loot.json`

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4,
                "max": 8
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": {
        "min": 2,
        "max": 3
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "weight": 4,
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.2,
                "max": 0.7
              }
            }
          ]
        },
        {
          "type": "minecraft:empty",
          "weight": 1
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 3
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.6
        }
      ]
    },
    {
      "rolls": {
        "min": 2,
        "max": 4
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/great_ink"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:ancient_knowledge_fragment",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.75
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/battleground/burial_loot — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/battleground/burial_loot.json`

```json
{
  "pools": [
    {
      "rolls": 2,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:bone",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:cobweb",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:flint",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_brick",
          "weight": 4,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4,
                "max": 9
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:gunpowder",
          "weight": 6,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3,
                "max": 5
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:wither_rose",
          "weight": 3
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:cinder_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 0,
                "max": 1
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:wither_skeleton_skull"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:potion",
          "functions": [
            {
              "function": "minecraft:set_potion",
              "id": "minecraft:healing"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:potion",
          "functions": [
            {
              "function": "minecraft:set_potion",
              "id": "minecraft:strong_healing"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:netherite_scrap",
          "weight": 1
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:copper_ingot",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3,
                "max": 12
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_sword",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.5,
                "max": 1
              }
            },
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_sword",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.5,
                "max": 1
              }
            },
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:netherite_sword",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.5,
                "max": 1
              }
            },
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_helmet",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 20.0,
                "min": 10.0
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_chestplate",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 20.0,
                "min": 10.0
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_leggings",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 20.0,
                "min": 10.0
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_boots",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 20.0,
                "min": 10.0
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        },
        {
          "type": "minecraft:empty",
          "weight": 14
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/battleground/piglin_camp — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/battleground/piglin_camp.json`

```json
{
  "pools": [
    {
      "rolls": 3,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:porkchop",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4,
                "max": 12
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:crimson_fungus",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:flint",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:nether_brick",
          "weight": 4,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4,
                "max": 9
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:gunpowder",
          "weight": 6,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3,
                "max": 5
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:soul_soil",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 8,
                "max": 22
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 2,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:gold_nugget",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4,
                "max": 12
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_nugget",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4,
                "max": 12
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": {
        "min": 1,
        "max": 3
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_shovel"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_pickaxe"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/bookshelf_loot — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/bookshelf_loot.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 2,
        "max": 3
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 8,
          "name": "minecraft:paper",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 6
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:book",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:writable_book"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30.0,
              "options": "#minecraft:on_random_loot"
            }
          ],
          "name": "minecraft:book",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.0,
                "max": 0.5
              }
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.7
        }
      ]
    },
    {
      "rolls": {
        "min": 0,
        "max": 5
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/poor_ink"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.7
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/catacombs/armory_loot — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/catacombs/armory_loot.json`

```json
{
  "pools": [
    {
      "rolls": {
        "min": 3,
        "max": 4
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:stone_sword"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_sword"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:bow"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:crossbow"
        }
      ]
    },
    {
      "rolls": {
        "min": 1,
        "max": 2
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:chainmail_chestplate"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:leather_helmet"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:leather_boots"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_helmet"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:leather_chestplate"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:arrow",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 0,
                "max": 32
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/catacombs/coffin_loot — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/catacombs/coffin_loot.json`

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:rotten_spell_book"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.15
        }
      ]
    },
    {
      "rolls": 5,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:bone",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3,
                "max": 5
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:cobweb",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:gold_ingot",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 5
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond",
          "weight": 1
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": {
        "min": 1,
        "max": 2
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.0,
                "max": 0.5
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 5,
                "max": 16
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 2,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_sword",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.2,
                "max": 0.75
              }
            },
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_sword",
          "weight": 2,
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.2,
                "max": 0.75
              }
            },
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_sword",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.2,
                "max": 0.75
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_helmet",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 20.0,
                "min": 10.0
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_chestplate",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 20.0,
                "min": 10.0
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_leggings",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 20.0,
                "min": 10.0
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_boots",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 20.0,
                "min": 10.0
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_helmet",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 20.0,
                "min": 10.0
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_chestplate",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 20.0,
                "min": 10.0
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_leggings",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 20.0,
                "min": 10.0
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_boots",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 20.0,
                "min": 10.0
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        },
        {
          "type": "minecraft:empty",
          "weight": 7
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/catacombs/crypt_loot — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/catacombs/crypt_loot.json`

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.25
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:ancient_knowledge_fragment"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.5
        }
      ]
    },
    {
      "rolls": 3,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:gold_ingot",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 5
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond"
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:magic_cloth",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_ingot",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 6
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "weight": 3,
          "type": "minecraft:item",
          "name": "minecraft:golden_apple"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_golden_apple"
        }
      ]
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.5,
                "max": 1
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune"
        }
      ],
      "rolls": 2
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/reward_ink"
        }
      ],
      "rolls": 3
    },
    {
      "rolls": 2,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blood_vial",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:dead_king_phylactery_shard",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/catacombs/dead_king_vault — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/catacombs/dead_king_vault.json`

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.25
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:ancient_knowledge_fragment"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.5
        }
      ]
    },
    {
      "rolls": 3,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:gold_ingot",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 5
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond"
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:magic_cloth",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_ingot",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 6
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "weight": 3,
          "type": "minecraft:item",
          "name": "minecraft:golden_apple"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_golden_apple"
        }
      ]
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.5,
                "max": 1
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune"
        }
      ],
      "rolls": 2
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/reward_ink"
        }
      ],
      "rolls": 3
    },
    {
      "rolls": 2,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blood_vial",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:dead_king_phylactery_shard",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/catacombs/hidden_trough_treasure — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/catacombs/hidden_trough_treasure.json`

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:rotten_spell_book"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.05
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "weight": 2,
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.3,
                "max": 1
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune"
        }
      ]
    },
    {
      "rolls": 12,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:wheat",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:hay_block"
        }
      ]
    },
    {
      "rolls": 3,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:emerald",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:diamond"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/catacombs/pot — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/catacombs/pot.json`

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "weight": 9,
          "type": "minecraft:empty"
        },
        {
          "weight": 4,
          "type": "minecraft:item",
          "functions": [
            {
              "count": {
                "min": 1,
                "max": 5
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:emerald"
        },
        {
          "weight": 3,
          "type": "minecraft:item",
          "functions": [
            {
              "count": {
                "min": 2,
                "max": 7
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "irons_spellbooks:arcane_essence"
        },
        {
          "weight": 4,
          "type": "minecraft:item",
          "functions": [
            {
              "count": {
                "min": 1,
                "max": 3
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bone"
        },
        {
          "weight": 4,
          "type": "minecraft:item",
          "functions": [
            {
              "count": {
                "min": 1,
                "max": 2
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:cobweb"
        },
        {
          "weight": 1,
          "type": "minecraft:item",
          "name": "irons_spellbooks:music_disc_dead_king_lullaby"
        },
        {
          "weight": 1,
          "type": "minecraft:item",
          "name": "minecraft:diamond"
        },
        {
          "weight": 1,
          "type": "minecraft:item",
          "name": "minecraft:skeleton_skull"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/catacombs/wall_loot — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/catacombs/wall_loot.json`

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 0,
                "max": 4
              }
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.25
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:ancient_knowledge_fragment"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.05
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.15,
                "max": 0.65
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune",
          "weight": 2
        },
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.35
        }
      ]
    },
    {
      "rolls": 2,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_ingot",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:rotten_flesh",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:cobweb",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:bone",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 5
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:chain",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 5
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:skeleton_skull"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.35
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:rotten_spell_book"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_sword",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.2,
                "max": 0.75
              }
            },
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 10.0,
                "min": 1.0
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_sword",
          "weight": 2,
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.2,
                "max": 0.75
              }
            },
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 10.0,
                "min": 1.0
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:iron_sword",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.2,
                "max": 0.75
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:chainmail_helmet",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 20.0,
                "min": 10.0
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:chainmail_chestplate",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 20.0,
                "min": 10.0
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_leggings",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 20.0,
                "min": 10.0
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_boots",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 20.0,
                "min": 10.0
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.35
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/citadel/citadel_bookshelf — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/citadel/citadel_bookshelf.json`

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:paper",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 8,
                "max": 16
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:ancient_knowledge_fragment",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:binomial",
                "n": 5,
                "p": 0.05
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:chained_book",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:binomial",
                "n": 2,
                "p": 0.15
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:ruined_book"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.01
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:disc_fragment_flame_still_burns"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.2
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:furled_map",
          "functions": [
            {
              "function": "irons_spellbooks:set_furled_map",
              "destination": "irons_spellbooks:ancient_battleground",
              "dimension": "minecraft:the_nether",
              "description_translation": "item.irons_spellbooks.ancient_battleground_map"
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.05
        }
      ]
    },
    {
      "rolls": {
        "type": "minecraft:binomial",
        "n": 3,
        "p": 0.25
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.0,
                "max": 1.0
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.0,
                "max": 1.0
              },
              "spell_filter": {
                "school": "irons_spellbooks:fire"
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:book",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:binomial",
                "n": 8,
                "p": 0.25
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:chests/citadel/citadel_tomes"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.5
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/citadel/citadel_tomes — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/citadel/citadel_tomes.json`

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:written_book",
          "functions": [
            {
              "function": "minecraft:set_name",
              "name": {
                "translate": "lore.citadel_book.title",
                "italic": false
              }
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{title:'Citadel Tome',author:'Unknown',pages:['{\"translate\":\"lore.citadel_book.construction_ledger\",\"color\":\"dark_gray\",\"italic\":true}']}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:written_book",
          "functions": [
            {
              "function": "minecraft:set_name",
              "name": {
                "translate": "lore.citadel_book.title",
                "italic": false
              }
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{title:'Citadel Tome',author:'Unknown',pages:['{\"translate\":\"lore.citadel_book.soul_research\",\"color\":\"dark_gray\",\"italic\":true}']}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:written_book",
          "functions": [
            {
              "function": "minecraft:set_name",
              "name": {
                "translate": "lore.citadel_book.title",
                "italic": false
              }
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{title:'Citadel Tome',author:'Unknown',pages:['{\"translate\":\"lore.citadel_book.planar_travel\",\"color\":\"dark_gray\",\"italic\":true}']}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:written_book",
          "functions": [
            {
              "function": "minecraft:set_name",
              "name": {
                "translate": "lore.citadel_book.title",
                "italic": false
              }
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{title:'Citadel Tome',author:'Unknown',pages:['{\"translate\":\"lore.citadel_book.legion_war_journal\",\"color\":\"dark_gray\",\"italic\":true}']}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:written_book",
          "functions": [
            {
              "function": "minecraft:set_name",
              "name": {
                "translate": "lore.citadel_book.title",
                "italic": false
              }
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{title:'Citadel Tome',author:'Unknown',pages:['{\"translate\":\"lore.citadel_book.armory_ledger\",\"color\":\"dark_gray\",\"italic\":true}']}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:written_book",
          "functions": [
            {
              "function": "minecraft:set_name",
              "name": {
                "translate": "lore.citadel_book.title",
                "italic": false
              }
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{title:'Citadel Tome',author:'Unknown',pages:['{\"translate\":\"lore.citadel_book.training_manual\",\"color\":\"dark_gray\",\"italic\":true}']}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:written_book",
          "functions": [
            {
              "function": "minecraft:set_name",
              "name": {
                "translate": "lore.citadel_book.title",
                "italic": false
              }
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{title:'Citadel Tome',author:'Unknown',pages:['{\"translate\":\"lore.citadel_book.cinderous_rituals\",\"color\":\"dark_gray\",\"italic\":true}']}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:written_book",
          "functions": [
            {
              "function": "minecraft:set_name",
              "name": {
                "translate": "lore.citadel_book.title",
                "italic": false
              }
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{title:'Citadel Tome',author:'Unknown',pages:['{\"translate\":\"lore.citadel_book.architectural_diagrams\",\"color\":\"dark_gray\",\"italic\":true}']}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:written_book",
          "functions": [
            {
              "function": "minecraft:set_name",
              "name": {
                "translate": "lore.citadel_book.title",
                "italic": false
              }
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{title:'Citadel Tome',author:'Unknown',pages:['{\"translate\":\"lore.citadel_book.fire_notes\",\"color\":\"dark_gray\",\"italic\":true}']}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:written_book",
          "functions": [
            {
              "function": "minecraft:set_name",
              "name": {
                "translate": "lore.citadel_book.title",
                "italic": false
              }
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{title:'Citadel Tome',author:'Unknown',pages:['{\"translate\":\"lore.citadel_book.quarry\",\"color\":\"dark_gray\",\"italic\":true}']}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:written_book",
          "functions": [
            {
              "function": "minecraft:set_name",
              "name": {
                "translate": "lore.citadel_book.title",
                "italic": false
              }
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{title:'Citadel Tome',author:'Unknown',pages:['{\"translate\":\"lore.citadel_book.complaint\",\"color\":\"dark_gray\",\"italic\":true}']}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:written_book",
          "functions": [
            {
              "function": "minecraft:set_name",
              "name": {
                "translate": "lore.citadel_book.title",
                "italic": false
              }
            },
            {
              "function": "minecraft:set_nbt",
              "tag": "{title:'Citadel Tome',author:'Unknown',pages:['{\"translate\":\"lore.citadel_book.soul_warning\",\"color\":\"dark_gray\",\"italic\":true}']}"
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/citadel/citadel_vault — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/citadel/citadel_vault.json`

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:ancient_knowledge_fragment",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:binomial",
                "n": 4,
                "p": 0.25
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:disc_fragment_flame_still_burns"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.4
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:pyrium_ingot"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 5,
                "max": 16
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": {
        "min": 2,
        "max": 4
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.5,
                "max": 1.0
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.5,
                "max": 1.0
              },
              "spell_filter": {
                "school": "irons_spellbooks:fire"
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.0,
                "max": 0.5
              },
              "spell_filter": {
                "spells": [
                  "irons_spellbooks:raise_hell"
                ]
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 4,
          "name": "irons_spellbooks:blank_rune"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.5
        }
      ]
    },
    {
      "rolls": 4,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/reward_ink"
        }
      ]
    },
    {
      "rolls": 4,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 6,
          "name": "minecraft:diamond",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "irons_spellbooks:mithril_scrap",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:netherite_scrap",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:ancient_debris",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:netherite_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 8,
          "name": "minecraft:emerald",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 10,
          "name": "minecraft:gold_ingot",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4,
                "max": 8
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/citadel/rampart_chest — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/citadel/rampart_chest.json`

```json
{
  "pools": [
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.25
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "irons_spellbooks:ominous_bottle"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:keeper_flamberge",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_damage",
              "damage": {
                "min": 0.01,
                "max": 0.23
              },
              "add": false
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:random_chance",
              "chance": 0.25
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:flint_and_steel",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_damage",
              "damage": {
                "min": 0.1,
                "max": 0.4
              },
              "add": false
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:random_chance",
              "chance": 0.55
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:lantern",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 0,
                "max": 8
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 3,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:soul_sand",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 4,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:bone",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 4,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:flint",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 4,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2,
                "max": 5
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 4,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:ancient_debris"
        },
        {
          "type": "minecraft:empty"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 4,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "minecraft:empty",
          "weight": 7
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.2,
                "max": 0.5
              },
              "spell_filter": {
                "school": "irons_spellbooks:fire"
              }
            }
          ],
          "weight": 13
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/citadel/rampart_supplies — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/citadel/rampart_supplies.json`

```json
{
  "pools": [
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.1
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "irons_spellbooks:ominous_bottle"
        }
      ],
      "rolls": 1.0
    },
    {
      "rolls": {
        "min": 1,
        "max": 2
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:crossbow",
          "weight": 2,
          "functions": [
            {
              "function": "minecraft:set_damage",
              "damage": {
                "min": 0.15,
                "max": 0.35
              },
              "add": false
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:arrow",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 0,
                "max": 32
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:lantern",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 0,
                "max": 8
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 3,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:soul_sand",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 4,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:bone",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 4,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:flint",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 4,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2,
                "max": 5
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/citadel/spawner_reward — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/citadel/spawner_reward.json`

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:cinder_essence"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/component_storage — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/component_storage.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 2,
        "max": 3
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "irons_spellbooks:shriving_stone"
        },
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/all_focuses",
          "weight": 4,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 5
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/evoker_fort — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/evoker_fort.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 15,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:raw_iron",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 0,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:experience_bottle"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:diamond"
        },
        {
          "type": "minecraft:item",
          "weight": 6,
          "name": "minecraft:arrow",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 0,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 8,
          "name": "minecraft:emerald"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:goat_horn",
          "functions": [
            {
              "function": "minecraft:set_instrument",
              "options": "#minecraft:goat_horns"
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.45
        }
      ]
    },
    {
      "rolls": {
        "min": 1,
        "max": 2
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.1,
                "max": 0.75
              },
              "spell_filter": {
                "school": "irons_spellbooks:evocation"
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": {
        "min": 0,
        "max": 5
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/poor_ink"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.2
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/evoker_fort/guard_tower — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/evoker_fort/guard_tower.json`

```json
{
  "pools": [
    {
      "rolls": {
        "min": 1,
        "max": 3
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_axe"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:crossbow",
          "weight": 2
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:arrow",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 0,
                "max": 32
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:torch",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 0,
                "max": 8
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:goat_horn",
          "functions": [
            {
              "function": "minecraft:set_instrument",
              "options": "#minecraft:goat_horns"
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/filler_storage_loot — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/filler_storage_loot.json`

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 0,
                "max": 4
              }
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.35
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.3,
                "max": 1
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.02
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/poor_ink"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.25
        }
      ]
    },
    {
      "rolls": 4,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:emerald"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:book"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:apple"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:rotten_flesh"
        },
        {
          "type": "minecraft:item",
          "weight": 8,
          "name": "minecraft:cobweb"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:charcoal"
        },
        {
          "type": "minecraft:empty",
          "weight": 6
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/generic_magic_treasure — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/generic_magic_treasure.json`

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3,
                "max": 13
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": {
        "min": 1,
        "max": 2
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.0,
                "max": 0.6
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune",
          "conditions": [
            {
              "condition": "minecraft:random_chance",
              "chance": 0.3
            }
          ]
        }
      ]
    },
    {
      "rolls": {
        "min": 1,
        "max": 2
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/all_focuses",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.2
        }
      ]
    },
    {
      "rolls": {
        "min": 1,
        "max": 4
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/decent_ink"
        }
      ]
    },
    {
      "rolls": 6,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:diamond"
        },
        {
          "type": "minecraft:item",
          "weight": 8,
          "name": "minecraft:copper_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:gold_ingot",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:emerald",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 12,
          "name": "minecraft:iron_ingot",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_sword",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.2,
                "max": 0.75
              }
            },
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 10.0
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_sword",
          "weight": 2,
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.2,
                "max": 0.75
              }
            },
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 10.0
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_sword",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.2,
                "max": 0.75
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_helmet",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_chestplate",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_leggings",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_boots",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_helmet"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_chestplate"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_leggings"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_boots"
        }
      ],
      "functions": [
        {
          "function": "irons_spellbooks:randomize_spell",
          "quality": {
            "min": 0.0,
            "max": 0.5
          }
        },
        {
          "function": "minecraft:enchant_with_levels",
          "levels": {
            "type": "minecraft:uniform",
            "max": 15.0,
            "min": 1.0
          },
          "options": "#minecraft:on_random_loot"
        },
        {
          "function": "minecraft:set_damage",
          "damage": {
            "min": 0.3,
            "max": 1.0
          },
          "add": false
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.4
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/ice_spider_den/basement — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/ice_spider_den/basement.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.25
        }
      ]
    },
    {
      "rolls": {
        "min": 0,
        "max": 2
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:ice_venom_vial"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.6
        }
      ]
    },
    {
      "rolls": {
        "min": 6,
        "max": 12
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:snowball",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:ice",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:cobweb",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:frozen_bone"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 10,
                "max": 30
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 5,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 8
        },
        {
          "type": "minecraft:item",
          "weight": 4,
          "name": "minecraft:emerald",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:diamond"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/ice_spider_den/cask — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/ice_spider_den/cask.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:honey_bottle",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:glass_bottle",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4,
                "max": 10
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:sweet_berries",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 5,
                "max": 16
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:ice",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 15,
                "max": 25
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/ice_spider_den/dungeon — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\ampere\datapacks\TheOptimizer_AdventureLoot.zip` · `data/irons_spellbooks/loot_tables/chests/ice_spider_den/dungeon.json`

```json
{
  "pools": [
    {
      "rolls": {
        "min": 2,
        "max": 3
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/good_ink"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.7
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.15,
                "max": 0.6
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/ice_spider_den/dungeon — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/ice_spider_den/dungeon.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30.0,
              "options": "#minecraft:on_random_loot"
            }
          ],
          "name": "minecraft:book"
        },
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/decent_ink"
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.2,
                "max": 0.5
              },
              "spell_filter": {
                "school": "irons_spellbooks:ice"
              }
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.75
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.1
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.25
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:invisibility_elixir"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.15
        }
      ]
    },
    {
      "rolls": {
        "min": 6,
        "max": 12
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:snowball",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:ice",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:cobweb",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:frozen_bone"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3,
                "max": 12
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 3,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 8
        },
        {
          "type": "minecraft:item",
          "weight": 4,
          "name": "minecraft:iron_ingot",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 6,
          "name": "minecraft:emerald",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:diamond"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/ice_spider_den/dungeon — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\moonlight-global-datapacks\TheOptimizer_AdventureLoot.zip` · `data/irons_spellbooks/loot_tables/chests/ice_spider_den/dungeon.json`

```json
{
  "pools": [
    {
      "rolls": {
        "min": 2,
        "max": 3
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/good_ink"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.7
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.15,
                "max": 0.6
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/ice_spider_den/pot — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/ice_spider_den/pot.json`

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "weight": 6,
          "type": "minecraft:empty"
        },
        {
          "weight": 4,
          "type": "minecraft:item",
          "functions": [
            {
              "count": {
                "min": 1,
                "max": 5
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:emerald"
        },
        {
          "weight": 3,
          "type": "minecraft:item",
          "functions": [
            {
              "count": {
                "min": 2,
                "max": 7
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "irons_spellbooks:arcane_essence"
        },
        {
          "weight": 4,
          "type": "minecraft:item",
          "functions": [
            {
              "count": {
                "min": 1,
                "max": 3
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:cobweb"
        },
        {
          "weight": 7,
          "type": "minecraft:item",
          "name": "irons_spellbooks:frozen_bone"
        },
        {
          "weight": 1,
          "type": "minecraft:item",
          "name": "minecraft:iron_ingot"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/ice_spider_den/spawner_reward — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/ice_spider_den/spawner_reward.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 15.0,
              "options": "#minecraft:on_random_loot"
            }
          ],
          "name": "minecraft:book"
        },
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/decent_ink"
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.0,
                "max": 0.5
              },
              "spell_filter": {
                "school": "irons_spellbooks:ice"
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/ice_spider_den/tower — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/ice_spider_den/tower.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.25
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:spyglass"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.25
        }
      ]
    },
    {
      "rolls": 2,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.0,
                "max": 0.5
              },
              "spell_filter": {
                "school": "irons_spellbooks:ice"
              }
            }
          ]
        },
        {
          "type": "minecraft:empty"
        }
      ]
    },
    {
      "rolls": {
        "min": 6,
        "max": 12
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:snowball",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:ice",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:cobweb",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 5,
                "max": 20
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/impaled_icebreaker/captain_quarters — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/impaled_icebreaker/captain_quarters.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.25
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:bundle",
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{Items:[{id:\"minecraft:paper\",Count:1b,tag:{display:{Name:'{\"translate\":\"item.irons_spellbooks.handwritten_invoice\"}',Lore:['{\"translate\":\"item.irons_spellbooks.handwritten_invoice.desc\",\"color\":\"gray\"}']}}},{id:\"minecraft:emerald\",Count:48b}]}"
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:permafrost_shard"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:spyglass"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:epic_ink"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:goat_horn",
          "functions": [
            {
              "function": "minecraft:set_instrument",
              "options": "#irons_spellbooks:fog_horn"
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:paper",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 27,
                "max": 35
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/impaled_icebreaker/food_barrel — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/impaled_icebreaker/food_barrel.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "min": 2,
        "max": 4
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:mushroom_stew"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:beetroot_soup"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:rabbit_stew"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:suspicious_stew",
          "functions": [
            {
              "function": "minecraft:set_stew_effect",
              "effects": [
                {
                  "type": "irons_spellbooks:chilled",
                  "duration": 30
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:fishing_rod"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:bucket"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:pufferfish"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:bread",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 5,
                "max": 9
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:cod",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3,
                "max": 6
              },
              "add": false
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/magic_bookshelf_loot — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/magic_bookshelf_loot.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 9
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.05
        }
      ]
    },
    {
      "rolls": {
        "min": 2,
        "max": 3
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 8,
          "name": "minecraft:paper",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 6
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:book",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": {
        "min": 1,
        "max": 3
      },
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30.0,
              "options": "#minecraft:on_random_loot"
            }
          ],
          "name": "minecraft:book",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.1,
                "max": 0.75
              }
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.8
        }
      ]
    },
    {
      "rolls": {
        "min": 1,
        "max": 5
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/decent_ink"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:ancient_knowledge_fragment",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.05
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/mangrove_hut — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/mangrove_hut.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 10,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:nether_wart"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:brown_mushroom"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:copper_ingot"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:red_mushroom"
        },
        {
          "type": "minecraft:item",
          "weight": 8,
          "name": "minecraft:fern"
        }
      ]
    },
    {
      "rolls": {
        "min": 1,
        "max": 3
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/random_potion_or_elixir"
        }
      ]
    },
    {
      "rolls": {
        "min": 0,
        "max": 5
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/poor_ink"
        }
      ]
    },
    {
      "rolls": {
        "min": 0,
        "max": 2
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.1,
                "max": 0.65
              },
              "spell_filter": {
                "school": "irons_spellbooks:nature"
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.4
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/mangrove_hut/hidden_potion_storage — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/mangrove_hut/hidden_potion_storage.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 15,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": 2
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": 2
            }
          ]
        }
      ]
    },
    {
      "rolls": {
        "min": 3,
        "max": 5
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/random_potion_or_elixir"
        }
      ]
    },
    {
      "rolls": {
        "min": 2,
        "max": 5
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:netherward_tincture"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/mangrove_hut/potion_ingredient_storage — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/mangrove_hut/potion_ingredient_storage.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 10,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 20,
          "name": "minecraft:glass_bottle"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:potion",
          "functions": [
            {
              "function": "minecraft:set_potion",
              "id": "minecraft:water"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:emerald"
        }
      ]
    },
    {
      "rolls": {
        "min": 0,
        "max": 2
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/random_potion_or_elixir"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/mountain_tower/ice_barrel — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/mountain_tower/ice_barrel.json`

```json
{
  "pools": [
    {
      "rolls": 2,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.0,
                "max": 0.75
              },
              "spell_filter": {
                "school": "irons_spellbooks:ice"
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 4,
          "name": "irons_spellbooks:affinity_ring",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_ring_enhancement",
              "school": "irons_spellbooks:ice"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "irons_spellbooks:frostward_ring"
        },
        {
          "type": "minecraft:empty",
          "weight": 2
        }
      ]
    },
    {
      "rolls": {
        "min": 6,
        "max": 12
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:snowball",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:ice",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/mountain_tower/mountain_tower — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\ampere\datapacks\TheOptimizer_AdventureLoot.zip` · `data/irons_spellbooks/loot_tables/chests/mountain_tower/mountain_tower.json`

```json
{
  "pools": [
    {
      "rolls": 8,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 4,
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 5
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:lapis_lazuli",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4,
                "max": 10
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:amethyst_shard",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 6
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": {
        "min": 2,
        "max": 4
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/good_ink"
        }
      ]
    },
    {
      "rolls": {
        "min": 1,
        "max": 2
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.2,
                "max": 0.65
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:ice_rune"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.65
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.5
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/mountain_tower/mountain_tower — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/mountain_tower/mountain_tower.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 15,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:paper",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 5
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:rabbit_stew"
        },
        {
          "type": "minecraft:item",
          "weight": 6,
          "name": "minecraft:amethyst_shard"
        },
        {
          "type": "minecraft:item",
          "weight": 8,
          "name": "irons_spellbooks:frozen_bone"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:goat_horn",
          "functions": [
            {
              "function": "minecraft:set_instrument",
              "options": "#minecraft:goat_horns"
            }
          ]
        }
      ]
    },
    {
      "rolls": {
        "min": 1,
        "max": 2
      },
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.1,
                "max": 0.75
              },
              "spell_filter": {
                "school": "irons_spellbooks:ice"
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:furled_map",
          "functions": [
            {
              "function": "irons_spellbooks:set_furled_map",
              "destination": "irons_spellbooks:impaled_icebreaker",
              "description_translation": "item.irons_spellbooks.failed_arctic_voyage_map"
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.3
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.3
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/mountain_tower/mountain_tower — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\moonlight-global-datapacks\TheOptimizer_AdventureLoot.zip` · `data/irons_spellbooks/loot_tables/chests/mountain_tower/mountain_tower.json`

```json
{
  "pools": [
    {
      "rolls": 8,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 4,
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 5
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:lapis_lazuli",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4,
                "max": 10
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:amethyst_shard",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 6
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": {
        "min": 2,
        "max": 4
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/good_ink"
        }
      ]
    },
    {
      "rolls": {
        "min": 1,
        "max": 2
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.2,
                "max": 0.65
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:ice_rune"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.65
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.5
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/priest_house — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/priest_house.json`

```json
{
  "pools": [
    {
      "rolls": {
        "min": 1,
        "max": 3
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:potion",
          "functions": [
            {
              "function": "minecraft:set_potion",
              "id": "minecraft:strong_healing"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:potion",
          "functions": [
            {
              "function": "minecraft:set_potion",
              "id": "minecraft:healing"
            }
          ]
        }
      ]
    },
    {
      "rolls": {
        "min": 0,
        "max": 4
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/poor_ink"
        }
      ]
    },
    {
      "rolls": {
        "min": 0,
        "max": 2
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "spell_filter": {
                "school": "irons_spellbooks:holy"
              },
              "quality": {
                "min": 0.1,
                "max": 0.65
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 12,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald"
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:divine_pearl"
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:paper"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/pyromancer_tower/burnt_chest — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/pyromancer_tower/burnt_chest.json`

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:gunpowder",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 7,
                "max": 16
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:charcoal",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 7,
                "max": 16
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:ghast_tear"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:affinity_ring",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_ring_enhancement",
              "spell_filter": {
                "school": "irons_spellbooks:fire"
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.6,
                "max": 1.0
              },
              "spell_filter": {
                "school": "irons_spellbooks:fire"
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/pyromancer_tower/fire_ale_cask — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/pyromancer_tower/fire_ale_cask.json`

```json
{
  "pools": [
    {
      "rolls": {
        "min": 0,
        "max": 2
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:fire_ale"
        }
      ]
    },
    {
      "rolls": {
        "min": 3,
        "max": 9
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:glass_bottle"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:potion",
          "functions": [
            {
              "function": "minecraft:set_potion",
              "id": "minecraft:water"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:pumpkin"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:sugar"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:honeycomb"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:fermented_spider_eye"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:wheat"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:water_bucket"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/pyromancer_tower/fire_ale_trove — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/pyromancer_tower/fire_ale_trove.json`

```json
{
  "pools": [
    {
      "rolls": {
        "min": 5,
        "max": 9
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:fire_ale"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:glass_bottle",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 5,
                "max": 9
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 8,
                "max": 17
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/pyromancer_tower/old_cask — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/pyromancer_tower/old_cask.json`

```json
{
  "pools": [
    {
      "rolls": {
        "min": 1,
        "max": 3
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:honeycomb",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:fermented_spider_eye"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:wheat",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:sugar",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:beetroot_seeds",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:glass_bottle",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 8,
                "max": 24
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 3,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:potion",
          "functions": [
            {
              "function": "minecraft:set_potion",
              "id": "minecraft:water"
            }
          ],
          "conditions": [
            {
              "condition": "minecraft:random_chance",
              "chance": 0.2
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/pyromancer_tower/pot — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/pyromancer_tower/pot.json`

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "weight": 6,
          "type": "minecraft:empty"
        },
        {
          "weight": 4,
          "type": "minecraft:item",
          "functions": [
            {
              "count": {
                "min": 1,
                "max": 5
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:emerald"
        },
        {
          "weight": 3,
          "type": "minecraft:item",
          "functions": [
            {
              "count": {
                "min": 2,
                "max": 7
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "irons_spellbooks:arcane_essence"
        },
        {
          "weight": 4,
          "type": "minecraft:item",
          "functions": [
            {
              "count": {
                "min": 1,
                "max": 3
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:charcoal"
        },
        {
          "weight": 2,
          "type": "minecraft:item",
          "functions": [
            {
              "count": {
                "min": 1,
                "max": 2
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:cobweb"
        },
        {
          "weight": 7,
          "type": "minecraft:item",
          "name": "irons_spellbooks:fire_ale"
        },
        {
          "weight": 1,
          "type": "minecraft:item",
          "name": "minecraft:gold_ingot"
        },
        {
          "weight": 1,
          "type": "minecraft:item",
          "name": "minecraft:copper_ingot"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/pyromancer_tower/pyromancer_basic_storage — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/pyromancer_tower/pyromancer_basic_storage.json`

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.0,
                "max": 0.4
              },
              "spell_filter": {
                "school": "irons_spellbooks:fire"
              }
            }
          ]
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.4
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:magic_cloth"
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.1
        }
      ]
    },
    {
      "rolls": {
        "min": 0,
        "max": 3
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/poor_ink"
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 0,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:book",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:paper",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 8,
          "name": "minecraft:cobweb",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "minecraft:empty",
          "weight": 6
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:candle",
          "weight": 6,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.075
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/pyromancer_tower/pyromancer_supplies — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\ampere\datapacks\TheOptimizer_AdventureLoot.zip` · `data/irons_spellbooks/loot_tables/chests/pyromancer_tower/pyromancer_supplies.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 10,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 4,
          "name": "minecraft:blaze_rod",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:obsidian",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 4,
          "name": "minecraft:paper",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3,
                "max": 8
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": {
        "min": 2,
        "max": 4
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/good_ink"
        }
      ]
    },
    {
      "rolls": {
        "min": 1,
        "max": 2
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "spell_filter": {
                "school": "irons_spellbooks:fire"
              },
              "quality": {
                "min": 0.2,
                "max": 0.65
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:fire_rune"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.65
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.5
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/pyromancer_tower/pyromancer_supplies — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/pyromancer_tower/pyromancer_supplies.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 15,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:candle"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:paper"
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "minecraft:pumpkin"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:obsidian"
        },
        {
          "type": "minecraft:item",
          "weight": 8,
          "name": "minecraft:blaze_rod"
        }
      ]
    },
    {
      "rolls": {
        "min": 0,
        "max": 5
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/poor_ink"
        }
      ]
    },
    {
      "rolls": {
        "min": 0,
        "max": 2
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "spell_filter": {
                "school": "irons_spellbooks:fire"
              },
              "quality": {
                "min": 0.1,
                "max": 0.65
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.4
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/pyromancer_tower/pyromancer_supplies — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\moonlight-global-datapacks\TheOptimizer_AdventureLoot.zip` · `data/irons_spellbooks/loot_tables/chests/pyromancer_tower/pyromancer_supplies.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 10,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 4,
          "name": "minecraft:blaze_rod",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "name": "minecraft:obsidian",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 4,
          "name": "minecraft:paper",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3,
                "max": 8
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": {
        "min": 2,
        "max": 4
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/good_ink"
        }
      ]
    },
    {
      "rolls": {
        "min": 1,
        "max": 2
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "spell_filter": {
                "school": "irons_spellbooks:fire"
              },
              "quality": {
                "min": 0.2,
                "max": 0.65
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:fire_rune"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.65
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.5
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/sewer_loot — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/sewer_loot.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:emerald",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:diamond"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:turtle_egg"
        },
        {
          "type": "minecraft:empty",
          "weight": 5
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 12
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 3,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:rotten_flesh",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:slime_ball",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 6
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:bone",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/trial_chambers/additional_ominous_spawner_consumable_loot — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/trial_chambers/additional_ominous_spawner_consumable_loot.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 25
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:potion",
          "weight": 6,
          "functions": [
            {
              "function": "minecraft:set_potion",
              "id": "irons_spellbooks:instant_mana_two"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:potion",
          "weight": 8,
          "functions": [
            {
              "function": "minecraft:set_potion",
              "id": "irons_spellbooks:instant_mana_three"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:potion",
          "weight": 4,
          "functions": [
            {
              "function": "minecraft:set_potion",
              "id": "irons_spellbooks:instant_mana_four"
            }
          ]
        },
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/random_elixir",
          "weight": 4
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/trial_chambers/additional_ominous_vault_loot — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/trial_chambers/additional_ominous_vault_loot.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 25
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:autoloader_crossbow",
          "weight": 8
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:weapon_parts",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:upgrade_orb",
          "weight": 7
        },
        {
          "type": "minecraft:item",
          "weight": 12,
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.8,
                "max": 1.0
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 8
        },
        {
          "type": "minecraft:item",
          "weight": 8,
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.5,
                "max": 1.0
              }
            }
          ]
        },
        {
          "weight": 5,
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/great_ink"
        },
        {
          "weight": 3,
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 10,
                "max": 20
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:visibility_ring"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.075
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/trial_chambers/additional_regular_spawner_consumable_loot — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/trial_chambers/additional_regular_spawner_consumable_loot.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 25
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:potion",
          "weight": 8,
          "functions": [
            {
              "function": "minecraft:set_potion",
              "id": "irons_spellbooks:instant_mana_one"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:potion",
          "weight": 8,
          "functions": [
            {
              "function": "minecraft:set_potion",
              "id": "irons_spellbooks:instant_mana_two"
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/trial_chambers/additional_regular_vault_loot — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/trial_chambers/additional_regular_vault_loot.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "weight": 8,
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.25,
                "max": 0.75
              }
            }
          ]
        },
        {
          "weight": 5,
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/good_ink",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "weight": 3,
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        },
        {
          "weight": 3,
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 10,
                "max": 20
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 8
        },
        {
          "type": "minecraft:item",
          "weight": 2,
          "name": "irons_spellbooks:blank_rune"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/trial_chambers/additional_trial_chest_loot — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/trial_chambers/additional_trial_chest_loot.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 2,
      "entries": [
        {
          "weight": 4,
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:magic_cloth"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.35
        }
      ]
    },
    {
      "rolls": 2,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.0,
                "max": 0.7
              }
            }
          ]
        },
        {
          "type": "minecraft:empty",
          "weight": 3
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.75
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.08
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/basic_curios"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.075
        }
      ]
    },
    {
      "rolls": 2,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/random_elixir"
        },
        {
          "type": "minecraft:empty",
          "weight": 1
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.2
        }
      ]
    },
    {
      "rolls": {
        "min": 1,
        "max": 4
      },
      "entries": [
        {
          "type": "minecraft:loot_table",
          "name": "irons_spellbooks:magic_items/good_ink"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.25
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/trial_chambers/pot_replacement — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/trial_chambers/pot_replacement.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 15,
          "name": "irons_spellbooks:arcane_essence",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 7
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 4,
          "name": "irons_spellbooks:scroll",
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.0,
                "max": 0.75
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>irons_spellbooks:chests/wheat — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar` · `data/irons_spellbooks/loot_tables/chests/wheat.json`

```json
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:pumpkin"
        }
      ],
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.25
        }
      ]
    },
    {
      "rolls": 12,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "name": "minecraft:wheat",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:hay_block"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>kaleidoscope_end:archaeology/suspicious_dragon_egg — kaleidoscope_end-1.0.14-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_end-1.0.14-forge+mc1.20.1.jar` · `data/kaleidoscope_end/loot_tables/archaeology/suspicious_dragon_egg.json`

```json
{
  "type": "minecraft:archaeology",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "kaleidoscope_end:dragon_egg_liquid"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "kaleidoscope_end:dragon_dust"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "kaleidoscope_end:archaeology/suspicious_dragon_egg"
}
```

</details>

<details>
<summary>kaleidoscope_end:archaeology/suspicious_end_stone — kaleidoscope_end-1.0.14-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_end-1.0.14-forge+mc1.20.1.jar` · `data/kaleidoscope_end/loot_tables/archaeology/suspicious_end_stone.json`

```json
{
  "type": "minecraft:archaeology",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:diamond"
        },
        {
          "type": "minecraft:item",
          "name": "kaleidoscope_end:void_conch"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "enchantments": {
                "minecraft:sharpness": {
                  "type": "minecraft:uniform",
                  "max": 3.0,
                  "min": 1.0
                }
              },
              "function": "minecraft:set_enchantments"
            }
          ],
          "name": "minecraft:enchanted_book"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "enchantments": {
                "minecraft:protection": {
                  "type": "minecraft:uniform",
                  "max": 3.0,
                  "min": 1.0
                }
              },
              "function": "minecraft:set_enchantments"
            }
          ],
          "name": "minecraft:enchanted_book"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "enchantments": {
                "minecraft:unbreaking": {
                  "type": "minecraft:uniform",
                  "max": 3.0,
                  "min": 1.0
                }
              },
              "function": "minecraft:set_enchantments"
            }
          ],
          "name": "minecraft:enchanted_book"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_ingot"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "kaleidoscope_end:archaeology/suspicious_end_stone"
}
```

</details>

<details>
<summary>kaleidoscope_nether:chests/bastion_hoglin_stable — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar` · `data/kaleidoscope_nether/loot_tables/chests/bastion_hoglin_stable.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:set_damage",
              "damage": {
                "min": 0.15,
                "max": 0.8
              }
            },
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "kaleidoscope_cookery:diamond_kitchen_knife"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "kaleidoscope_cookery:gold_kitchen_knife",
          "weight": 2
        },
        {
          "type": "minecraft:empty",
          "weight": 3
        }
      ],
      "rolls": 1
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 6.0,
                "min": 3.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "kaleidoscope_nether:soul_pepper",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "kaleidoscope_nether:ham",
          "weight": 4
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "kaleidoscope_nether:roasted_ham",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "kaleidoscope_nether:nether_caterpillar"
        },
        {
          "type": "minecraft:empty",
          "weight": 3
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 2.0,
        "min": 1.0
      }
    }
  ],
  "random_sequence": "kaleidoscope_nether:chests/bastion_hoglin_stable"
}
```

</details>

<details>
<summary>kaleidoscope_nether:chests/bastion_treasure — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar` · `data/kaleidoscope_nether/loot_tables/chests/bastion_treasure.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:set_damage",
              "damage": {
                "min": 0.8,
                "max": 1.0
              }
            },
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "kaleidoscope_cookery:diamond_kitchen_knife"
        },
        {
          "type": "minecraft:item",
          "name": "kaleidoscope_cookery:diamond_kitchen_knife"
        },
        {
          "type": "minecraft:empty",
          "weight": 6
        }
      ],
      "rolls": 1
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "kaleidoscope_nether:star_dust"
        },
        {
          "type": "minecraft:item",
          "name": "kaleidoscope_nether:ghast_pendant"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "kaleidoscope_nether:gilded_fragment",
          "weight": 4
        },
        {
          "type": "minecraft:empty",
          "weight": 6
        }
      ],
      "rolls": 1
    }
  ],
  "random_sequence": "kaleidoscope_nether:chests/bastion_treasure"
}
```

</details>

<details>
<summary>kaleidoscope_nether:integration/dungeonsmobs/fungus_thrower — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar` · `data/kaleidoscope_nether/loot_tables/integration/dungeonsmobs/fungus_thrower.json`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "condition": "kaleidoscope_cookery:advance_entity_match_tool",
          "predicate": {
            "tag": "kaleidoscope_cookery:kitchen_knife"
          },
          "slot": "mainhand"
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "kaleidoscope_cookery:oil"
        }
      ],
      "rolls": 2.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "conditions": [
                {
                  "condition": "minecraft:entity_properties",
                  "entity": "this",
                  "predicate": {
                    "flags": {
                      "is_on_fire": true
                    }
                  }
                }
              ],
              "function": "minecraft:furnace_smelt"
            },
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "kaleidoscope_nether:raw_piglin_meat"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "kaleidoscope_nether:integration/dungeonsmobs/fungus_thrower"
}
```

</details>

<details>
<summary>kaleidoscope_nether:integration/dungeonsmobs/wildfire — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar` · `data/kaleidoscope_nether/loot_tables/integration/dungeonsmobs/wildfire.json`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "condition": "kaleidoscope_cookery:advance_entity_match_tool",
          "predicate": {
            "tag": "kaleidoscope_cookery:kitchen_knife"
          },
          "slot": "mainhand"
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "kaleidoscope_nether:blaze_heart"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "kaleidoscope_nether:blaze_heart"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "kaleidoscope_nether:integration/dungeonsmobs/wildfire"
}
```

</details>

<details>
<summary>kaleidoscope_nether:integration/dungeonsmobs/zombified_fungus_thrower — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar` · `data/kaleidoscope_nether/loot_tables/integration/dungeonsmobs/zombified_fungus_thrower.json`

```json
{
  "type": "minecraft:entity",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "conditions": [
        {
          "condition": "kaleidoscope_cookery:advance_entity_match_tool",
          "predicate": {
            "tag": "kaleidoscope_cookery:kitchen_knife"
          },
          "slot": "mainhand"
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            },
            {
              "count": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.0
              },
              "function": "minecraft:looting_enchant"
            }
          ],
          "name": "kaleidoscope_cookery:oil"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "kaleidoscope_nether:integration/dungeonsmobs/zombified_fungus_thrower"
}
```

</details>

<details>
<summary>lootr:chests/elytra — lootr-forge-1.20-0.7.35.94.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\lootr-forge-1.20-0.7.35.94.jar` · `data/lootr/loot_tables/chests/elytra.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:elytra"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "lootr:chests/elytra"
}
```

</details>

<details>
<summary>minecraft:archaeology/desert_pyramid — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/archaeology/desert_pyramid.json`

```json
{
  "type": "minecraft:archaeology",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:archer_pottery_sherd"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:miner_pottery_sherd"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:prize_pottery_sherd"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:skull_pottery_sherd"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:tnt"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:gunpowder"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:archaeology/desert_pyramid"
}
```

</details>

<details>
<summary>minecraft:archaeology/desert_well — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/archaeology/desert_well.json`

```json
{
  "type": "minecraft:archaeology",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:arms_up_pottery_sherd",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:brewer_pottery_sherd",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:brick"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:stick"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "effects": [
                {
                  "type": "minecraft:night_vision",
                  "duration": {
                    "type": "minecraft:uniform",
                    "max": 10.0,
                    "min": 7.0
                  }
                },
                {
                  "type": "minecraft:jump_boost",
                  "duration": {
                    "type": "minecraft:uniform",
                    "max": 10.0,
                    "min": 7.0
                  }
                },
                {
                  "type": "minecraft:weakness",
                  "duration": {
                    "type": "minecraft:uniform",
                    "max": 8.0,
                    "min": 6.0
                  }
                },
                {
                  "type": "minecraft:blindness",
                  "duration": {
                    "type": "minecraft:uniform",
                    "max": 7.0,
                    "min": 5.0
                  }
                },
                {
                  "type": "minecraft:poison",
                  "duration": {
                    "type": "minecraft:uniform",
                    "max": 20.0,
                    "min": 10.0
                  }
                },
                {
                  "type": "minecraft:saturation",
                  "duration": {
                    "type": "minecraft:uniform",
                    "max": 10.0,
                    "min": 7.0
                  }
                }
              ],
              "function": "minecraft:set_stew_effect"
            }
          ],
          "name": "minecraft:suspicious_stew"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:archaeology/desert_well"
}
```

</details>

<details>
<summary>minecraft:archaeology/ocean_ruin_cold — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/archaeology/ocean_ruin_cold.json`

```json
{
  "type": "minecraft:archaeology",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:blade_pottery_sherd"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:explorer_pottery_sherd"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:mourner_pottery_sherd"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:plenty_pottery_sherd"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_axe"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:wheat",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:wooden_hoe",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:coal",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:gold_nugget",
          "weight": 2
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:archaeology/ocean_ruin_cold"
}
```

</details>

<details>
<summary>minecraft:archaeology/ocean_ruin_warm — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/archaeology/ocean_ruin_warm.json`

```json
{
  "type": "minecraft:archaeology",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:angler_pottery_sherd"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:shelter_pottery_sherd"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:snort_pottery_sherd"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:sniffer_egg"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_axe"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:wheat",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:wooden_hoe",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:coal",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:gold_nugget",
          "weight": 2
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:archaeology/ocean_ruin_warm"
}
```

</details>

<details>
<summary>minecraft:archaeology/trail_ruins_common — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/archaeology/trail_ruins_common.json`

```json
{
  "type": "minecraft:archaeology",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:wheat",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:wooden_hoe",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:clay",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:brick",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:yellow_dye",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:blue_dye",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:light_blue_dye",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:white_dye",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:orange_dye",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:red_candle",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:green_candle",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:purple_candle",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:brown_candle",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:magenta_stained_glass_pane"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:pink_stained_glass_pane"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:blue_stained_glass_pane"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:light_blue_stained_glass_pane"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:red_stained_glass_pane"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:yellow_stained_glass_pane"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:purple_stained_glass_pane"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:spruce_hanging_sign"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:oak_hanging_sign"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:gold_nugget"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:coal"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:wheat_seeds"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:beetroot_seeds"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:dead_bush"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:flower_pot"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:string"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:lead"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:archaeology/trail_ruins_common"
}
```

</details>

<details>
<summary>minecraft:archaeology/trail_ruins_rare — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/archaeology/trail_ruins_rare.json`

```json
{
  "type": "minecraft:archaeology",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:burn_pottery_sherd"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:danger_pottery_sherd"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:friend_pottery_sherd"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:heart_pottery_sherd"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:heartbreak_pottery_sherd"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:howl_pottery_sherd"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:sheaf_pottery_sherd"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:wayfinder_armor_trim_smithing_template"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:raiser_armor_trim_smithing_template"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:shaper_armor_trim_smithing_template"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:host_armor_trim_smithing_template"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:music_disc_relic"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:archaeology/trail_ruins_rare"
}
```

</details>

<details>
<summary>minecraft:chests/abandoned_mineshaft — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\ampere\datapacks\TheOptimizer_AdventureLoot.zip` · `data/minecraft/loot_tables/chests/abandoned_mineshaft.json`

```json
{
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 2.0,
        "max": 4.0
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:tnt",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 5
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:powered_rail",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4,
                "max": 12
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:rail",
          "weight": 25,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 8,
                "max": 24
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:gold_ingot",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 6
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_ingot",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 6
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond",
          "weight": 8,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:torch",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 8,
                "max": 16
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_apple",
          "weight": 12
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:book",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:efficiency\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:unbreaking\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:looting\",lvl:1s}]}"
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>minecraft:chests/abandoned_mineshaft — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/abandoned_mineshaft.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_apple",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_golden_apple"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:name_tag",
          "weight": 30
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:book",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_pickaxe",
          "weight": 5
        },
        {
          "type": "minecraft:empty",
          "weight": 5
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_ingot",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_ingot",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 9.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:redstone",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 9.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:lapis_lazuli",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:diamond",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 3.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:coal",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bread",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 6.0,
                "min": 3.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:glow_berries",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:melon_seeds",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:pumpkin_seeds",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:beetroot_seeds",
          "weight": 10
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 4.0,
        "min": 2.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:rail",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:powered_rail",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:detector_rail",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:activator_rail",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 16.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:torch",
          "weight": 15
        }
      ],
      "rolls": 3.0
    }
  ],
  "random_sequence": "minecraft:chests/abandoned_mineshaft"
}
```

</details>

<details>
<summary>minecraft:chests/abandoned_mineshaft — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\moonlight-global-datapacks\TheOptimizer_AdventureLoot.zip` · `data/minecraft/loot_tables/chests/abandoned_mineshaft.json`

```json
{
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 2.0,
        "max": 4.0
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:tnt",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 5
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:powered_rail",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4,
                "max": 12
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:rail",
          "weight": 25,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 8,
                "max": 24
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:gold_ingot",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 6
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_ingot",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 6
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond",
          "weight": 8,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:torch",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 8,
                "max": 16
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_apple",
          "weight": 12
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:book",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:efficiency\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:unbreaking\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:looting\",lvl:1s}]}"
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>minecraft:chests/ancient_city — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/ancient_city.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:enchanted_golden_apple"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:music_disc_otherside"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:compass",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:sculk_catalyst",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:name_tag",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            },
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.8
              },
              "function": "minecraft:set_damage"
            },
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 50.0,
                "min": 30.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_hoe",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:lead",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:diamond_horse_armor",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:saddle",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:music_disc_13",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:music_disc_cat",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 50.0,
                "min": 30.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_leggings",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "enchantments": [
                "minecraft:swift_sneak"
              ],
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:book",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 10.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:sculk",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:sculk_sensor",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:candle",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 15.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:amethyst_shard",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:experience_bottle",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 15.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:glow_berries",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:iron_leggings",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:echo_shard",
          "weight": 4
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:disc_fragment_5",
          "weight": 4
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            },
            {
              "function": "minecraft:set_potion",
              "id": "minecraft:strong_regeneration"
            }
          ],
          "name": "minecraft:potion",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:book",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 10.0,
                "min": 3.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:book",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 15.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bone",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 15.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:soul_torch",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 15.0,
                "min": 6.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:coal",
          "weight": 7
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 10.0,
        "min": 5.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 75
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:ward_armor_trim_smithing_template",
          "weight": 4
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:silence_armor_trim_smithing_template"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:chests/ancient_city"
}
```

</details>

<details>
<summary>minecraft:chests/ancient_city_ice_box — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/ancient_city_ice_box.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "effects": [
                {
                  "type": "minecraft:night_vision",
                  "duration": {
                    "type": "minecraft:uniform",
                    "max": 10.0,
                    "min": 7.0
                  }
                },
                {
                  "type": "minecraft:blindness",
                  "duration": {
                    "type": "minecraft:uniform",
                    "max": 7.0,
                    "min": 5.0
                  }
                }
              ],
              "function": "minecraft:set_stew_effect"
            },
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 6.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:suspicious_stew"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 10.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:golden_carrot"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 10.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:baked_potato"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 6.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:packed_ice",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 6.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:snowball",
          "weight": 4
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 10.0,
        "min": 4.0
      }
    }
  ],
  "random_sequence": "minecraft:chests/ancient_city_ice_box"
}
```

</details>

<details>
<summary>minecraft:chests/bastion_bridge — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/bastion_bridge.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:lodestone"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.5,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            },
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:crossbow"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 28.0,
                "min": 10.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:spectral_arrow"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 12.0,
                "min": 8.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gilded_blackstone"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 3.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:crying_obsidian"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_block"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 9.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_ingot"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 9.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_ingot"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:golden_sword"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            },
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:golden_chestplate"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            },
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:golden_helmet"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            },
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:golden_leggings"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            },
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:golden_boots"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            },
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:golden_axe"
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 2.0,
        "min": 1.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 6.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:string"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:leather"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 17.0,
                "min": 5.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:arrow"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 6.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_nugget"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 6.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_nugget"
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 4.0,
        "min": 2.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 11
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:snout_armor_trim_smithing_template"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 9
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:netherite_upgrade_smithing_template"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:chests/bastion_bridge"
}
```

</details>

<details>
<summary>minecraft:chests/bastion_hoglin_stable — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/bastion_hoglin_stable.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.8,
                "min": 0.15
              },
              "function": "minecraft:set_damage"
            },
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:diamond_shovel",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.95,
                "min": 0.15
              },
              "function": "minecraft:set_damage"
            },
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            },
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:diamond_pickaxe",
          "weight": 12
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:netherite_scrap",
          "weight": 8
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:ancient_debris",
          "weight": 12
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 2.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:ancient_debris",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:saddle",
          "weight": 12
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_block",
          "weight": 16
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 17.0,
                "min": 8.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:golden_carrot",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:golden_apple",
          "weight": 10
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            },
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:golden_axe"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:crying_obsidian"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 6.0,
                "min": 3.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:glowstone"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gilded_blackstone"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:soul_sand"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:crimson_nylium"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_nugget"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:leather"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 17.0,
                "min": 5.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:arrow"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 3.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:string"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:porkchop"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:cooked_porkchop"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:crimson_fungus"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:crimson_roots"
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 4.0,
        "min": 3.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 11
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:snout_armor_trim_smithing_template"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 9
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:netherite_upgrade_smithing_template"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:chests/bastion_hoglin_stable"
}
```

</details>

<details>
<summary>minecraft:chests/bastion_other — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/bastion_other.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            },
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:diamond_pickaxe",
          "weight": 6
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:diamond_shovel",
          "weight": 6
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.9,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            },
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:crossbow",
          "weight": 6
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:ancient_debris",
          "weight": 12
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:netherite_scrap",
          "weight": 4
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 22.0,
                "min": 10.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:spectral_arrow",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:piglin_banner_pattern",
          "weight": 9
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:music_disc_pigstep",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 17.0,
                "min": 6.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:golden_carrot",
          "weight": 12
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:golden_apple",
          "weight": 9
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "enchantments": [
                "minecraft:soul_speed"
              ],
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:book",
          "weight": 10
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.9,
                "min": 0.1
              },
              "function": "minecraft:set_damage"
            },
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            },
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:iron_sword",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_block",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            },
            {
              "enchantments": [
                "minecraft:soul_speed"
              ],
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:golden_boots"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            },
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:golden_axe"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_block",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:crossbow"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 6.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_ingot",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 6.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_ingot",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:golden_sword"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:golden_chestplate"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:golden_helmet"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:golden_leggings"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:golden_boots"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:crying_obsidian",
          "weight": 2
        }
      ],
      "rolls": 2.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gilded_blackstone",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 10.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:chain"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 6.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:magma_cream",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 6.0,
                "min": 3.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bone_block"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_nugget"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 6.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:obsidian"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_nugget"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 6.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:string"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 17.0,
                "min": 5.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:arrow",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:cooked_porkchop"
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 4.0,
        "min": 3.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 11
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:snout_armor_trim_smithing_template"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 9
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:netherite_upgrade_smithing_template"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:chests/bastion_other"
}
```

</details>

<details>
<summary>minecraft:chests/bastion_treasure — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/bastion_treasure.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:netherite_ingot",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:ancient_debris",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:netherite_scrap",
          "weight": 8
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 2.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:ancient_debris",
          "weight": 4
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.8
              },
              "function": "minecraft:set_damage"
            },
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:diamond_sword",
          "weight": 6
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.8
              },
              "function": "minecraft:set_damage"
            },
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:diamond_chestplate",
          "weight": 6
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.8
              },
              "function": "minecraft:set_damage"
            },
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:diamond_helmet",
          "weight": 6
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.8
              },
              "function": "minecraft:set_damage"
            },
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:diamond_leggings",
          "weight": 6
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 1.0,
                "min": 0.8
              },
              "function": "minecraft:set_damage"
            },
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:diamond_boots",
          "weight": 6
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_sword",
          "weight": 6
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_chestplate",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_helmet",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_boots",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_leggings",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 6.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:diamond",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 1.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:enchanted_golden_apple",
          "weight": 2
        }
      ],
      "rolls": 3.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 25.0,
                "min": 12.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:spectral_arrow"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_block"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_block"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 9.0,
                "min": 3.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_ingot"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 9.0,
                "min": 3.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_ingot"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 3.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:crying_obsidian"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 23.0,
                "min": 8.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:quartz"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 15.0,
                "min": 5.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gilded_blackstone"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 3.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:magma_cream"
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 4.0,
        "min": 3.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 11
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:snout_armor_trim_smithing_template"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:netherite_upgrade_smithing_template"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:chests/bastion_treasure"
}
```

</details>

<details>
<summary>minecraft:chests/buried_treasure — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/buried_treasure.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:heart_of_the_sea"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_ingot",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_ingot",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:tnt",
          "weight": 5
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 8.0,
        "min": 5.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:emerald",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:diamond",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:prismarine_crystals",
          "weight": 5
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 3.0,
        "min": 1.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:leather_chestplate"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_sword"
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 1.0,
        "min": 0.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:cooked_cod"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:cooked_salmon"
        }
      ],
      "rolls": 2.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:potion"
        }
      ],
      "functions": [
        {
          "function": "minecraft:set_potion",
          "id": "minecraft:water_breathing"
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 2.0,
        "min": 0.0
      }
    }
  ],
  "random_sequence": "minecraft:chests/buried_treasure"
}
```

</details>

<details>
<summary>minecraft:chests/desert_pyramid — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\ampere\datapacks\TheOptimizer_AdventureLoot.zip` · `data/minecraft/loot_tables/chests/desert_pyramid.json`

```json
{
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 3.0,
        "max": 5.0
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:gold_ingot",
          "weight": 25,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_ingot",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 6
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:experience_bottle",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 6
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:book",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:efficiency\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 12,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:unbreaking\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:looting\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 12,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:unbreaking\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:looting\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_apple",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_golden_apple",
          "weight": 3
        }
      ]
    },
    {
      "rolls": 1.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:gunpowder",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:bone",
          "weight": 8,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 5
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1.0,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:dune_armor_trim_smithing_template",
          "weight": 1
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>minecraft:chests/desert_pyramid — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/desert_pyramid.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:diamond",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_ingot",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_ingot",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:emerald",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 6.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bone",
          "weight": 25
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:spider_eye",
          "weight": 25
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 3.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:rotten_flesh",
          "weight": 25
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:saddle",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_horse_armor",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_horse_armor",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_horse_armor",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:book",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_apple",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_golden_apple",
          "weight": 2
        },
        {
          "type": "minecraft:empty",
          "weight": 15
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 4.0,
        "min": 2.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bone",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gunpowder",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:rotten_flesh",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:string",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:sand",
          "weight": 10
        }
      ],
      "rolls": 4.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 6
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 2.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:dune_armor_trim_smithing_template"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:chests/desert_pyramid"
}
```

</details>

<details>
<summary>minecraft:chests/desert_pyramid — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\moonlight-global-datapacks\TheOptimizer_AdventureLoot.zip` · `data/minecraft/loot_tables/chests/desert_pyramid.json`

```json
{
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 3.0,
        "max": 5.0
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:gold_ingot",
          "weight": 25,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_ingot",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 6
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:experience_bottle",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 6
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:book",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:efficiency\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 12,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:unbreaking\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:looting\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 12,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:unbreaking\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:looting\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_apple",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_golden_apple",
          "weight": 3
        }
      ]
    },
    {
      "rolls": 1.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:gunpowder",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:bone",
          "weight": 8,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 5
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": 1.0,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:dune_armor_trim_smithing_template",
          "weight": 1
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>minecraft:chests/end_city_treasure — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/end_city_treasure.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:diamond",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_ingot",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_ingot",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 6.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:emerald",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 10.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:beetroot_seeds",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:saddle",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_horse_armor"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_horse_armor"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_horse_armor"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_sword",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_boots",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_chestplate",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_leggings",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_helmet",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_pickaxe",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:diamond_shovel",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:iron_sword",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:iron_boots",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:iron_chestplate",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:iron_leggings",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:iron_helmet",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:iron_pickaxe",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": 39.0,
                "min": 20.0
              },
              "treasure": true
            }
          ],
          "name": "minecraft:iron_shovel",
          "weight": 3
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 6.0,
        "min": 2.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 14
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:spire_armor_trim_smithing_template"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:chests/end_city_treasure"
}
```

</details>

<details>
<summary>minecraft:chests/igloo_chest — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/igloo_chest.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:apple",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:coal",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_nugget",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:stone_axe",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:rotten_flesh",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:wheat",
          "weight": 10
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 8.0,
        "min": 2.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_apple"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:chests/igloo_chest"
}
```

</details>

<details>
<summary>minecraft:chests/jungle_temple — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\ampere\datapacks\TheOptimizer_AdventureLoot.zip` · `data/minecraft/loot_tables/chests/jungle_temple.json`

```json
{
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 3.0,
        "max": 5.0
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:gold_ingot",
          "weight": 25,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond",
          "weight": 8,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:bamboo",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 6,
                "max": 16
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:experience_bottle",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 5
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_apple",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:book",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:efficiency\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 12,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:unbreaking\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:looting\",lvl:1s}]}"
            }
          ]
        }
      ]
    },
    {
      "rolls": 1.0,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:wild_armor_trim_smithing_template",
          "weight": 1
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>minecraft:chests/jungle_temple — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/jungle_temple.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:diamond",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_ingot",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_ingot",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bamboo",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:emerald",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 6.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bone",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 3.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:rotten_flesh",
          "weight": 16
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:saddle",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_horse_armor"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_horse_armor"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_horse_armor"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30.0,
              "treasure": true
            }
          ],
          "name": "minecraft:book"
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 6.0,
        "min": 2.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 2.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:wild_armor_trim_smithing_template"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:chests/jungle_temple"
}
```

</details>

<details>
<summary>minecraft:chests/jungle_temple — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\moonlight-global-datapacks\TheOptimizer_AdventureLoot.zip` · `data/minecraft/loot_tables/chests/jungle_temple.json`

```json
{
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 3.0,
        "max": 5.0
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:gold_ingot",
          "weight": 25,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond",
          "weight": 8,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 3,
                "max": 8
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:bamboo",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 6,
                "max": 16
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:experience_bottle",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 5
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_apple",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:book",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:efficiency\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 12,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:unbreaking\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:looting\",lvl:1s}]}"
            }
          ]
        }
      ]
    },
    {
      "rolls": 1.0,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:wild_armor_trim_smithing_template",
          "weight": 1
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>minecraft:chests/jungle_temple_dispenser — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/jungle_temple_dispenser.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:arrow",
          "weight": 30
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 2.0,
        "min": 1.0
      }
    }
  ],
  "random_sequence": "minecraft:chests/jungle_temple_dispenser"
}
```

</details>

<details>
<summary>minecraft:chests/nether_bridge — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/nether_bridge.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:diamond",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_ingot",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_ingot",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_sword",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_chestplate",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:flint_and_steel",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 3.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:nether_wart",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:saddle",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_horse_armor",
          "weight": 8
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_horse_armor",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_horse_armor",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:obsidian",
          "weight": 2
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 4.0,
        "min": 2.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 14
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:rib_armor_trim_smithing_template"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:chests/nether_bridge"
}
```

</details>

<details>
<summary>minecraft:chests/pillager_outpost — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/pillager_outpost.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:crossbow"
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 1.0,
        "min": 0.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 3.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:wheat",
          "weight": 7
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:potato",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 3.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:carrot",
          "weight": 5
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 3.0,
        "min": 2.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:dark_oak_log"
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 3.0,
        "min": 1.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:experience_bottle",
          "weight": 7
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 6.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:string",
          "weight": 4
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:arrow",
          "weight": 4
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:tripwire_hook",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_ingot",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:book"
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 3.0,
        "min": 2.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:goat_horn"
        }
      ],
      "functions": [
        {
          "function": "minecraft:set_instrument",
          "options": "#minecraft:regular_goat_horns"
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 1.0,
        "min": 0.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 2.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:sentry_armor_trim_smithing_template"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:chests/pillager_outpost"
}
```

</details>

<details>
<summary>minecraft:chests/ruined_portal — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/ruined_portal.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:obsidian",
          "weight": 40
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:flint",
          "weight": 40
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 18.0,
                "min": 9.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_nugget",
          "weight": 40
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:flint_and_steel",
          "weight": 40
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:fire_charge",
          "weight": 40
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_apple",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 24.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_nugget",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:golden_sword",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:golden_axe",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:golden_hoe",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:golden_shovel",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:golden_pickaxe",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:golden_boots",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:golden_chestplate",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:golden_helmet",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:golden_leggings",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 12.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:glistering_melon_slice",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_horse_armor",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:light_weighted_pressure_plate",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 12.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:golden_carrot",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:clock",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_ingot",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:bell"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_golden_apple"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_block"
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 8.0,
        "min": 4.0
      }
    }
  ],
  "random_sequence": "minecraft:chests/ruined_portal"
}
```

</details>

<details>
<summary>minecraft:chests/shipwreck_map — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/shipwreck_map.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "decoration": "red_x",
              "function": "minecraft:exploration_map",
              "skip_existing_chunks": false,
              "zoom": 1
            },
            {
              "function": "minecraft:set_name",
              "name": {
                "translate": "filled_map.buried_treasure"
              }
            }
          ],
          "name": "minecraft:map"
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:compass"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:map"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:clock"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 10.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:paper",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:feather",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:book",
          "weight": 5
        }
      ],
      "rolls": 3.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 2.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:coast_armor_trim_smithing_template"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:chests/shipwreck_map"
}
```

</details>

<details>
<summary>minecraft:chests/shipwreck_supply — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/shipwreck_supply.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 12.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:paper",
          "weight": 8
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 6.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:potato",
          "weight": 7
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:moss_block",
          "weight": 7
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 6.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:poisonous_potato",
          "weight": 7
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:carrot",
          "weight": 7
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 21.0,
                "min": 8.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:wheat",
          "weight": 7
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "effects": [
                {
                  "type": "minecraft:night_vision",
                  "duration": {
                    "type": "minecraft:uniform",
                    "max": 10.0,
                    "min": 7.0
                  }
                },
                {
                  "type": "minecraft:jump_boost",
                  "duration": {
                    "type": "minecraft:uniform",
                    "max": 10.0,
                    "min": 7.0
                  }
                },
                {
                  "type": "minecraft:weakness",
                  "duration": {
                    "type": "minecraft:uniform",
                    "max": 8.0,
                    "min": 6.0
                  }
                },
                {
                  "type": "minecraft:blindness",
                  "duration": {
                    "type": "minecraft:uniform",
                    "max": 7.0,
                    "min": 5.0
                  }
                },
                {
                  "type": "minecraft:poison",
                  "duration": {
                    "type": "minecraft:uniform",
                    "max": 20.0,
                    "min": 10.0
                  }
                },
                {
                  "type": "minecraft:saturation",
                  "duration": {
                    "type": "minecraft:uniform",
                    "max": 10.0,
                    "min": 7.0
                  }
                }
              ],
              "function": "minecraft:set_stew_effect"
            }
          ],
          "name": "minecraft:suspicious_stew",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:coal",
          "weight": 6
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 24.0,
                "min": 5.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:rotten_flesh",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:pumpkin",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bamboo",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gunpowder",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:tnt"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:leather_helmet",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:leather_chestplate",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:leather_leggings",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:leather_boots",
          "weight": 3
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 10.0,
        "min": 3.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 2.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:coast_armor_trim_smithing_template"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:chests/shipwreck_supply"
}
```

</details>

<details>
<summary>minecraft:chests/shipwreck_treasure — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/shipwreck_treasure.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_ingot",
          "weight": 90
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_ingot",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:emerald",
          "weight": 40
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:experience_bottle",
          "weight": 5
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 6.0,
        "min": 3.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 10.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_nugget",
          "weight": 50
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 10.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_nugget",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 10.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:lapis_lazuli",
          "weight": 20
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 5.0,
        "min": 2.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": 2.0,
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:coast_armor_trim_smithing_template"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:chests/shipwreck_treasure"
}
```

</details>

<details>
<summary>minecraft:chests/simple_dungeon — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\ampere\datapacks\TheOptimizer_AdventureLoot.zip` · `data/minecraft/loot_tables/chests/simple_dungeon.json`

```json
{
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 2.0,
        "max": 4.0
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:gold_ingot",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 6
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_ingot",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 6
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond",
          "weight": 8,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:lapis_lazuli",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4,
                "max": 10
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:experience_bottle",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 5
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:redstone",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4,
                "max": 10
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 1.0,
        "max": 2.0
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_apple",
          "weight": 25
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_golden_apple",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:saddle",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:name_tag",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:book",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:efficiency\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 12,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:unbreaking\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:looting\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 12,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:unbreaking\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:looting\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:music_disc_otherside",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:music_disc_cat",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:music_disc_13",
          "weight": 10
        }
      ]
    },
    {
      "rolls": 1.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:gunpowder",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 5
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:bone",
          "weight": 8,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:string",
          "weight": 8,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>minecraft:chests/simple_dungeon — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/simple_dungeon.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:saddle",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_apple",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_golden_apple",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:music_disc_otherside",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:music_disc_13",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:music_disc_cat",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:name_tag",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_horse_armor",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_horse_armor",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_horse_armor",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:book",
          "weight": 10
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 3.0,
        "min": 1.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_ingot",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_ingot",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:bread",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:wheat",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:bucket",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:redstone",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:coal",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:melon_seeds",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:pumpkin_seeds",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:beetroot_seeds",
          "weight": 10
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 4.0,
        "min": 1.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bone",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gunpowder",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:rotten_flesh",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:string",
          "weight": 10
        }
      ],
      "rolls": 3.0
    }
  ],
  "random_sequence": "minecraft:chests/simple_dungeon"
}
```

</details>

<details>
<summary>minecraft:chests/simple_dungeon — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\moonlight-global-datapacks\TheOptimizer_AdventureLoot.zip` · `data/minecraft/loot_tables/chests/simple_dungeon.json`

```json
{
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 2.0,
        "max": 4.0
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:gold_ingot",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 6
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_ingot",
          "weight": 20,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 6
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond",
          "weight": 8,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 2
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:lapis_lazuli",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4,
                "max": 10
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:experience_bottle",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 5
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:redstone",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 4,
                "max": 10
              }
            }
          ]
        }
      ]
    },
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 1.0,
        "max": 2.0
      },
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_apple",
          "weight": 25
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_golden_apple",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:saddle",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:name_tag",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:book",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 15,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:efficiency\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 12,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:unbreaking\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:looting\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 12,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:unbreaking\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:looting\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:music_disc_otherside",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:music_disc_cat",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:music_disc_13",
          "weight": 10
        }
      ]
    },
    {
      "rolls": 1.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:gunpowder",
          "weight": 10,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 5
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:bone",
          "weight": 8,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 2,
                "max": 4
              }
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:string",
          "weight": 8,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>minecraft:chests/spawn_bonus_chest — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/spawn_bonus_chest.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:stone_axe"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:wooden_axe",
          "weight": 3
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:stone_pickaxe"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:wooden_pickaxe",
          "weight": 3
        }
      ],
      "rolls": 1.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:apple",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bread",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:salmon",
          "weight": 3
        }
      ],
      "rolls": 3.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 12.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:stick",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 12.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:oak_planks",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:oak_log",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:spruce_log",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:birch_log",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:jungle_log",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:acacia_log",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:dark_oak_log",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:mangrove_log",
          "weight": 3
        }
      ],
      "rolls": 4.0
    }
  ],
  "random_sequence": "minecraft:chests/spawn_bonus_chest"
}
```

</details>

<details>
<summary>minecraft:chests/stronghold_corridor — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/stronghold_corridor.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:ender_pearl",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:diamond",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_ingot",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_ingot",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 9.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:redstone",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bread",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:apple",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_pickaxe",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_sword",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_chestplate",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_helmet",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_leggings",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_boots",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_apple"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:saddle"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_horse_armor"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_horse_armor"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_horse_armor"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:music_disc_otherside"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30.0,
              "treasure": true
            }
          ],
          "name": "minecraft:book"
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 3.0,
        "min": 2.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:empty",
          "weight": 9
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:eye_armor_trim_smithing_template"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:chests/stronghold_corridor"
}
```

</details>

<details>
<summary>minecraft:chests/stronghold_crossing — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/stronghold_crossing.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_ingot",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_ingot",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 9.0,
                "min": 4.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:redstone",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 3.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:coal",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bread",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:apple",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_pickaxe"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30.0,
              "treasure": true
            }
          ],
          "name": "minecraft:book"
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 4.0,
        "min": 1.0
      }
    }
  ],
  "random_sequence": "minecraft:chests/stronghold_crossing"
}
```

</details>

<details>
<summary>minecraft:chests/stronghold_library — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/stronghold_library.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:book",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:paper",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:map"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:compass"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30.0,
              "treasure": true
            }
          ],
          "name": "minecraft:book",
          "weight": 10
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 10.0,
        "min": 2.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:eye_armor_trim_smithing_template"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:chests/stronghold_library"
}
```

</details>

<details>
<summary>minecraft:chests/underwater_ruin_big — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/underwater_ruin_big.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:coal",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_nugget",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:wheat",
          "weight": 10
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 8.0,
        "min": 2.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_apple"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:book",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:leather_chestplate"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_helmet"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:fishing_rod",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "decoration": "red_x",
              "function": "minecraft:exploration_map",
              "skip_existing_chunks": false,
              "zoom": 1
            },
            {
              "function": "minecraft:set_name",
              "name": {
                "translate": "filled_map.buried_treasure"
              }
            }
          ],
          "name": "minecraft:map",
          "weight": 10
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:chests/underwater_ruin_big"
}
```

</details>

<details>
<summary>minecraft:chests/underwater_ruin_small — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/underwater_ruin_small.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:coal",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:stone_axe",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:rotten_flesh",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:wheat",
          "weight": 10
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 8.0,
        "min": 2.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:leather_chestplate"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_helmet"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:fishing_rod",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "decoration": "red_x",
              "function": "minecraft:exploration_map",
              "skip_existing_chunks": false,
              "zoom": 1
            },
            {
              "function": "minecraft:set_name",
              "name": {
                "translate": "filled_map.buried_treasure"
              }
            }
          ],
          "name": "minecraft:map",
          "weight": 5
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:chests/underwater_ruin_small"
}
```

</details>

<details>
<summary>minecraft:chests/village/village_armorer — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/village/village_armorer.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_ingot",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bread",
          "weight": 4
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_helmet"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald"
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 5.0,
        "min": 1.0
      }
    }
  ],
  "random_sequence": "minecraft:chests/village/village_armorer"
}
```

</details>

<details>
<summary>minecraft:chests/village/village_butcher — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/village/village_butcher.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:porkchop",
          "weight": 6
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:wheat",
          "weight": 6
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:beef",
          "weight": 6
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:mutton",
          "weight": 6
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:coal",
          "weight": 3
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 5.0,
        "min": 1.0
      }
    }
  ],
  "random_sequence": "minecraft:chests/village/village_butcher"
}
```

</details>

<details>
<summary>minecraft:chests/village/village_cartographer — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/village/village_cartographer.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:map",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:paper",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:compass",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bread",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:stick",
          "weight": 5
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 5.0,
        "min": 1.0
      }
    }
  ],
  "random_sequence": "minecraft:chests/village/village_cartographer"
}
```

</details>

<details>
<summary>minecraft:chests/village/village_desert_house — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/village/village_desert_house.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:clay_ball"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:green_dye"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:cactus",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:wheat",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bread",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:book"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:dead_bush",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:emerald"
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 8.0,
        "min": 3.0
      }
    }
  ],
  "random_sequence": "minecraft:chests/village/village_desert_house"
}
```

</details>

<details>
<summary>minecraft:chests/village/village_fisher — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/village/village_fisher.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:cod",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:salmon"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:water_bucket"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:barrel"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:wheat_seeds",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:coal",
          "weight": 2
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 5.0,
        "min": 1.0
      }
    }
  ],
  "random_sequence": "minecraft:chests/village/village_fisher"
}
```

</details>

<details>
<summary>minecraft:chests/village/village_fletcher — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/village/village_fletcher.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:arrow",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:feather",
          "weight": 6
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:egg",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:flint",
          "weight": 6
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:stick",
          "weight": 6
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 5.0,
        "min": 1.0
      }
    }
  ],
  "random_sequence": "minecraft:chests/village/village_fletcher"
}
```

</details>

<details>
<summary>minecraft:chests/village/village_mason — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/village/village_mason.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:clay_ball"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:flower_pot"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:stone",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:stone_bricks",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bread",
          "weight": 4
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:yellow_dye"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:smooth_stone"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald"
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 5.0,
        "min": 1.0
      }
    }
  ],
  "random_sequence": "minecraft:chests/village/village_mason"
}
```

</details>

<details>
<summary>minecraft:chests/village/village_plains_house — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/village/village_plains_house.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_nugget"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:dandelion",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:poppy"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:potato",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bread",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:apple",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:book"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:feather"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:emerald",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:oak_sapling",
          "weight": 5
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 8.0,
        "min": 3.0
      }
    }
  ],
  "random_sequence": "minecraft:chests/village/village_plains_house"
}
```

</details>

<details>
<summary>minecraft:chests/village/village_savanna_house — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/village/village_savanna_house.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_nugget"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:grass",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:tall_grass",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bread",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:wheat_seeds",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:emerald",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:acacia_sapling",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:saddle"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:torch"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:bucket"
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 8.0,
        "min": 3.0
      }
    }
  ],
  "random_sequence": "minecraft:chests/village/village_savanna_house"
}
```

</details>

<details>
<summary>minecraft:chests/village/village_shepherd — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/village/village_shepherd.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:white_wool",
          "weight": 6
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:black_wool",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gray_wool",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:brown_wool",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:light_gray_wool",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:shears"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 6.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:wheat",
          "weight": 6
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 5.0,
        "min": 1.0
      }
    }
  ],
  "random_sequence": "minecraft:chests/village/village_shepherd"
}
```

</details>

<details>
<summary>minecraft:chests/village/village_snowy_house — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/village/village_snowy_house.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:blue_ice"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:snow_block",
          "weight": 4
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:potato",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bread",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:beetroot_seeds",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:beetroot_soup"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:furnace"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:emerald"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:snowball",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:coal",
          "weight": 5
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 8.0,
        "min": 3.0
      }
    }
  ],
  "random_sequence": "minecraft:chests/village/village_snowy_house"
}
```

</details>

<details>
<summary>minecraft:chests/village/village_taiga_house — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/village/village_taiga_house.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_nugget"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:fern",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:large_fern",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:potato",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:sweet_berries",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bread",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:pumpkin_seeds",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:pumpkin_pie"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:emerald",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:spruce_sapling",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:spruce_sign"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:spruce_log",
          "weight": 10
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 8.0,
        "min": 3.0
      }
    }
  ],
  "random_sequence": "minecraft:chests/village/village_taiga_house"
}
```

</details>

<details>
<summary>minecraft:chests/village/village_tannery — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/village/village_tannery.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:leather"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:leather_chestplate",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:leather_boots",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:leather_helmet",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bread",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:leather_leggings",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:saddle"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:emerald"
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 5.0,
        "min": 1.0
      }
    }
  ],
  "random_sequence": "minecraft:chests/village/village_tannery"
}
```

</details>

<details>
<summary>minecraft:chests/village/village_temple — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/village/village_temple.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:redstone",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bread",
          "weight": 7
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:rotten_flesh",
          "weight": 7
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:lapis_lazuli"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_ingot"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:emerald"
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 8.0,
        "min": 3.0
      }
    }
  ],
  "random_sequence": "minecraft:chests/village/village_temple"
}
```

</details>

<details>
<summary>minecraft:chests/village/village_toolsmith — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/village/village_toolsmith.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:diamond"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_ingot",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_ingot"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bread",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_pickaxe",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:coal"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:stick",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_shovel",
          "weight": 5
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 8.0,
        "min": 3.0
      }
    }
  ],
  "random_sequence": "minecraft:chests/village/village_toolsmith"
}
```

</details>

<details>
<summary>minecraft:chests/village/village_weaponsmith — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/village/village_weaponsmith.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:diamond",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 5.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_ingot",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_ingot",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bread",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 3.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:apple",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_pickaxe",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_sword",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_chestplate",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_helmet",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_leggings",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_boots",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 3.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:obsidian",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 7.0,
                "min": 3.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:oak_sapling",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:saddle",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:iron_horse_armor"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_horse_armor"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_horse_armor"
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 8.0,
        "min": 3.0
      }
    }
  ],
  "random_sequence": "minecraft:chests/village/village_weaponsmith"
}
```

</details>

<details>
<summary>minecraft:chests/woodland_mansion — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/chests/woodland_mansion.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:lead",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:golden_apple",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_golden_apple",
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:music_disc_13",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:music_disc_cat",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:name_tag",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:chainmail_chestplate",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_hoe",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:diamond_chestplate",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_randomly"
            }
          ],
          "name": "minecraft:book",
          "weight": 10
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 3.0,
        "min": 1.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:iron_ingot",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gold_ingot",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:bread",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:wheat",
          "weight": 20
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:bucket",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:redstone",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:coal",
          "weight": 15
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:melon_seeds",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:pumpkin_seeds",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 4.0,
                "min": 2.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:beetroot_seeds",
          "weight": 10
        }
      ],
      "rolls": {
        "type": "minecraft:uniform",
        "max": 4.0,
        "min": 1.0
      }
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:bone",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:gunpowder",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:rotten_flesh",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 8.0,
                "min": 1.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "name": "minecraft:string",
          "weight": 10
        }
      ],
      "rolls": 3.0
    },
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:empty"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:vex_armor_trim_smithing_template"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:chests/woodland_mansion"
}
```

</details>

<details>
<summary>minecraft:gameplay/fishing/treasure — server-1.20.1-20230612.114412-extra.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-extra.jar` · `data/minecraft/loot_tables/gameplay/fishing/treasure.json`

```json
{
  "type": "minecraft:fishing",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:name_tag"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:saddle"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.25,
                "min": 0.0
              },
              "function": "minecraft:set_damage"
            },
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30.0,
              "treasure": true
            }
          ],
          "name": "minecraft:bow"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "add": false,
              "damage": {
                "type": "minecraft:uniform",
                "max": 0.25,
                "min": 0.0
              },
              "function": "minecraft:set_damage"
            },
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30.0,
              "treasure": true
            }
          ],
          "name": "minecraft:fishing_rod"
        },
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30.0,
              "treasure": true
            }
          ],
          "name": "minecraft:book"
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:nautilus_shell"
        }
      ],
      "rolls": 1.0
    }
  ],
  "random_sequence": "minecraft:gameplay/fishing/treasure"
}
```

</details>

<details>
<summary>ribbits:chests/fisherman_main — Ribbits-1.20.1-Forge-3.0.5.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\Ribbits-1.20.1-Forge-3.0.5.jar` · `data/ribbits/loot_tables/chests/fisherman_main.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 2.0,
        "max": 4.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:cod"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:salmon"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:kelp"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 2.0
              },
              "add": false
            }
          ],
          "name": "ribbits:giant_lilypad"
        }
      ]
    },
    {
      "rolls": 1.0,
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 15,
          "name": "minecraft:air"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 10,
              "treasure": true
            }
          ],
          "name": "minecraft:fishing_rod"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 20,
              "treasure": true
            }
          ],
          "name": "minecraft:fishing_rod"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": 30,
              "treasure": true
            }
          ],
          "name": "minecraft:fishing_rod"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>ribbits:chests/fisherman_storage — Ribbits-1.20.1-Forge-3.0.5.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\Ribbits-1.20.1-Forge-3.0.5.jar` · `data/ribbits/loot_tables/chests/fisherman_storage.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 1.0,
        "max": 4.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:cod"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:salmon"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:tropical_fish"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:kelp"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:dried_kelp"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "ribbits:giant_lilypad"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 1.0
              },
              "add": false
            }
          ],
          "name": "minecraft:nautilus_shell"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:amethyst_shard"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>ribbits:chests/gardener — Ribbits-1.20.1-Forge-3.0.5.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\Ribbits-1.20.1-Forge-3.0.5.jar` · `data/ribbits/loot_tables/chests/gardener.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 4.0,
        "max": 6.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 5.0
              },
              "add": false
            }
          ],
          "name": "minecraft:red_mushroom"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 5.0
              },
              "add": false
            }
          ],
          "name": "minecraft:brown_mushroom"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 2.0
              },
              "add": false
            }
          ],
          "name": "ribbits:giant_lilypad"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 2.0
              },
              "add": false
            }
          ],
          "name": "minecraft:amethyst_shard"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>ribbits:chests/merchant — Ribbits-1.20.1-Forge-3.0.5.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\Ribbits-1.20.1-Forge-3.0.5.jar` · `data/ribbits/loot_tables/chests/merchant.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 3.0,
        "max": 4.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 8,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:amethyst_shard"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": 1,
              "add": false
            }
          ],
          "name": "minecraft:amethyst_block"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>ribbits:chests/nitwit — Ribbits-1.20.1-Forge-3.0.5.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\Ribbits-1.20.1-Forge-3.0.5.jar` · `data/ribbits/loot_tables/chests/nitwit.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 3.0,
        "max": 4.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:red_mushroom"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:brown_mushroom"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "ribbits:giant_lilypad"
        },
        {
          "type": "minecraft:item",
          "weight": 3,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 3.0
              },
              "add": false
            }
          ],
          "name": "minecraft:amethyst_shard"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>ribbits:chests/sorcerer — Ribbits-1.20.1-Forge-3.0.5.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\Ribbits-1.20.1-Forge-3.0.5.jar` · `data/ribbits/loot_tables/chests/sorcerer.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": {
        "type": "minecraft:uniform",
        "min": 4.0,
        "max": 6.0
      },
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 2.0
              },
              "add": false
            }
          ],
          "name": "minecraft:cobweb"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:candle"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 4.0
              },
              "add": false
            }
          ],
          "name": "minecraft:glass_bottle"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 1.0,
                "max": 2.0
              },
              "add": false
            }
          ],
          "name": "minecraft:fermented_spider_eye"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 6.0
              },
              "add": false
            }
          ],
          "name": "minecraft:amethyst_shard"
        },
        {
          "type": "minecraft:item",
          "weight": 5,
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "type": "minecraft:uniform",
                "min": 2.0,
                "max": 5.0
              },
              "add": false
            }
          ],
          "name": "minecraft:slime_ball"
        }
      ]
    },
    {
      "rolls": 1.0,
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:item",
          "weight": 1,
          "name": "minecraft:air"
        },
        {
          "type": "minecraft:item",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{Potion:\"minecraft:strong_leaping\"}"
            }
          ],
          "name": "minecraft:potion"
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>theoptimizer:chests/yungs_nether_cinder — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\ampere\datapacks\TheOptimizer_AdventureLoot.zip` · `data/theoptimizer/loot_tables/chests/yungs_nether_cinder.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.5
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:cinder_essence",
          "weight": 1
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>theoptimizer:chests/yungs_nether_cinder — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\moonlight-global-datapacks\TheOptimizer_AdventureLoot.zip` · `data/theoptimizer/loot_tables/chests/yungs_nether_cinder.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.5
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:cinder_essence",
          "weight": 1
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>theoptimizer:chests/yungs_tier_1 — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\ampere\datapacks\TheOptimizer_AdventureLoot.zip` · `data/theoptimizer/loot_tables/chests/yungs_tier_1.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.35
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:unbreaking\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:looting\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:efficiency\",lvl:1s}]}"
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.65
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:common_ink",
          "weight": 6
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:uncommon_ink",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "weight": 4
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "weight": 2,
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.1,
                "max": 0.35
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>theoptimizer:chests/yungs_tier_1 — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\moonlight-global-datapacks\TheOptimizer_AdventureLoot.zip` · `data/theoptimizer/loot_tables/chests/yungs_tier_1.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.35
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:unbreaking\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:looting\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:efficiency\",lvl:1s}]}"
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.65
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:common_ink",
          "weight": 6
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:uncommon_ink",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:arcane_essence",
          "weight": 4
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "weight": 2,
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.1,
                "max": 0.35
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>theoptimizer:chests/yungs_tier_2 — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\ampere\datapacks\TheOptimizer_AdventureLoot.zip` · `data/theoptimizer/loot_tables/chests/yungs_tier_2.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.6
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:unbreaking\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:looting\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:efficiency\",lvl:1s}]}"
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.85
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:uncommon_ink",
          "weight": 6
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:rare_ink",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "weight": 4,
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.1,
                "max": 0.55
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>theoptimizer:chests/yungs_tier_2 — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\moonlight-global-datapacks\TheOptimizer_AdventureLoot.zip` · `data/theoptimizer/loot_tables/chests/yungs_tier_2.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.6
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:unbreaking\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:looting\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:efficiency\",lvl:1s}]}"
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.85
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:uncommon_ink",
          "weight": 6
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:rare_ink",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune",
          "weight": 3
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "weight": 4,
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.1,
                "max": 0.55
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>theoptimizer:chests/yungs_tier_3 — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\ampere\datapacks\TheOptimizer_AdventureLoot.zip` · `data/theoptimizer/loot_tables/chests/yungs_tier_3.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.8
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:unbreaking\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:looting\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:efficiency\",lvl:1s}]}"
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 1
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:rare_ink",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:epic_ink",
          "weight": 4
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:legendary_ink",
          "weight": 1
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "weight": 4,
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.1,
                "max": 0.7
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>theoptimizer:chests/yungs_tier_3 — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\moonlight-global-datapacks\TheOptimizer_AdventureLoot.zip` · `data/theoptimizer/loot_tables/chests/yungs_tier_3.json`

```json
{
  "type": "minecraft:chest",
  "pools": [
    {
      "rolls": 1,
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 0.8
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:unbreaking\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:looting\",lvl:1s}]}"
            }
          ]
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:enchanted_book",
          "weight": 1,
          "functions": [
            {
              "function": "minecraft:set_nbt",
              "tag": "{StoredEnchantments:[{id:\"minecraft:efficiency\",lvl:1s}]}"
            }
          ]
        }
      ]
    },
    {
      "rolls": 1,
      "conditions": [
        {
          "condition": "minecraft:random_chance",
          "chance": 1
        }
      ],
      "entries": [
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:rare_ink",
          "weight": 10
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:epic_ink",
          "weight": 4
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:legendary_ink",
          "weight": 1
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:blank_rune",
          "weight": 5
        },
        {
          "type": "minecraft:item",
          "name": "irons_spellbooks:scroll",
          "weight": 4,
          "functions": [
            {
              "function": "irons_spellbooks:randomize_spell",
              "quality": {
                "min": 0.1,
                "max": 0.7
              }
            }
          ]
        }
      ]
    }
  ]
}
```

</details>

<details>
<summary>yungscavebiomes:archaeology/sand_snapper_loot — YungsCaveBiomes-1.20.1-Forge-2.0.5.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\YungsCaveBiomes-1.20.1-Forge-2.0.5.jar` · `data/yungscavebiomes/loot_tables/archaeology/sand_snapper_loot.json`

```json
{
  "type": "minecraft:archaeology",
  "pools": [
    {
      "bonus_rolls": 0.0,
      "rolls": 1.0,
      "entries": [
        {
          "type": "minecraft:item",
          "name": "yungscavebiomes:hourglass_pottery_sherd",
          "weight": 1
        },
        {
          "type": "minecraft:item",
          "name": "yungscavebiomes:clock_pottery_sherd",
          "weight": 1
        },
        {
          "type": "minecraft:item",
          "name": "yungscavebiomes:ancient_armor_trim_smithing_template",
          "weight": 1
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:brick",
          "weight": 1
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:emerald",
          "weight": 1
        },
        {
          "type": "minecraft:item",
          "name": "minecraft:stick",
          "weight": 1
        }
      ]
    }
  ],
  "random_sequence": "yungscavebiomes:archaeology/lost_caves_ancient_sand"
}
```

</details>

## Modificadores encontrados

<details>
<summary>data/forge/loot_modifiers/global_loot_modifiers.json — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\ampere\datapacks\TheOptimizer_AdventureLoot.zip`

```json
{
  "replace": false,
  "entries": [
    "theoptimizer:chest_loot/yungs_tier_1",
    "theoptimizer:chest_loot/yungs_tier_2",
    "theoptimizer:chest_loot/yungs_tier_3",
    "theoptimizer:chest_loot/yungs_nether_cinder"
  ]
}
```

</details>

<details>
<summary>data/irons_spellbooks/loot_modifiers/chest_loot/compat_good_loot_modifier.json — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\ampere\datapacks\TheOptimizer_AdventureLoot.zip`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:any_of",
      "terms": [
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/simple_dungeon"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/desert_pyramid"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/jungle_temple"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/woodland_mansion"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/stronghold_corridor"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/stronghold_crossing"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterstrongholds:chests/crypt"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterstrongholds:chests/common"
        }
      ]
    }
  ],
  "key": "irons_spellbooks:chests/additional_good_loot"
}
```

</details>

<details>
<summary>data/irons_spellbooks/loot_modifiers/chest_loot/compat_treasure_loot_modifier.json — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\ampere\datapacks\TheOptimizer_AdventureLoot.zip`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:any_of",
      "terms": [
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/buried_treasure"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/end_city_treasure"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/bastion_treasure"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterstrongholds:chests/treasure"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterstrongholds:chests/armoury"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterstrongholds:chests/grand_library"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterstrongholds:chests/library_md"
        }
      ]
    }
  ],
  "key": "irons_spellbooks:chests/additional_treasure_loot"
}
```

</details>

<details>
<summary>data/irons_spellbooks/loot_modifiers/chest_loot/vanilla_generic_loot_modifier.json — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\ampere\datapacks\TheOptimizer_AdventureLoot.zip`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:any_of",
      "terms": [
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/abandoned_mineshaft"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/pillager_outpost"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/shipwreck_map"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/shipwreck_supply"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/underwater_ruin_big"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/underwater_ruin_small"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/ruined_portal"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/village/village_cartographer"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/village/village_temple"
        }
      ]
    }
  ],
  "key": "irons_spellbooks:chests/additional_generic_loot"
}
```

</details>

<details>
<summary>data/theoptimizer/loot_modifiers/chest_loot/yungs_nether_cinder.json — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\ampere\datapacks\TheOptimizer_AdventureLoot.zip`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:any_of",
      "terms": [
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/beacon"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/extra"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/hall"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/keep"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/obsidian"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/puzzle"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/quarters"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/storage"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/worship"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/nether_bridge"
        }
      ]
    }
  ],
  "key": "theoptimizer:chests/yungs_nether_cinder"
}
```

</details>

<details>
<summary>data/theoptimizer/loot_modifiers/chest_loot/yungs_tier_1.json — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\ampere\datapacks\TheOptimizer_AdventureLoot.zip`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:any_of",
      "terms": [
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdungeons:skeleton_dungeon/chests/common"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdungeons:small_dungeon/chests/loot_piles"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdungeons:small_nether_dungeon/chests/common"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdungeons:spider_dungeon/chests/egg_room"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdungeons:zombie_dungeon/chests/common"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterwitchhuts:chests/hut_0"
        }
      ]
    }
  ],
  "key": "theoptimizer:chests/yungs_tier_1"
}
```

</details>

<details>
<summary>data/theoptimizer/loot_modifiers/chest_loot/yungs_tier_2.json — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\ampere\datapacks\TheOptimizer_AdventureLoot.zip`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:any_of",
      "terms": [
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdeserttemples:chests/food_storage"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdeserttemples:chests/lab"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdeserttemples:chests/library"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdeserttemples:chests/pharaoh_hidden"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdeserttemples:chests/pot"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdeserttemples:chests/statue"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdeserttemples:chests/storage"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdeserttemples:chests/tomb"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdeserttemples:chests/tomb_pharaoh"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdeserttemples:chests/wardrobe"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdungeons:skeleton_dungeon/chests/middle"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdungeons:zombie_dungeon/chests/special"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdungeons:zombie_dungeon/chests/tombstone"
        }
      ]
    }
  ],
  "key": "theoptimizer:chests/yungs_tier_2"
}
```

</details>

<details>
<summary>data/theoptimizer/loot_modifiers/chest_loot/yungs_tier_3.json — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\ampere\datapacks\TheOptimizer_AdventureLoot.zip`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:any_of",
      "terms": [
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/beacon"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/extra"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/hall"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/keep"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/obsidian"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/puzzle"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/quarters"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/storage"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/worship"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betteroceanmonuments:chests/upper_side_chamber"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/nether_bridge"
        }
      ]
    }
  ],
  "key": "theoptimizer:chests/yungs_tier_3"
}
```

</details>

<details>
<summary>data/forge/loot_modifiers/global_loot_modifiers.json — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar`

```json
{
  "replace": false,
  "entries": [
    "irons_spellbooks:entity_drops/stray_modifier",
    "irons_spellbooks:entity_drops/hoglin_modifier",
    "irons_spellbooks:entity_drops/evoker_modifier",
    "irons_spellbooks:entity_drops/blaze_modifier",
    "irons_spellbooks:entity_drops/ender_dragon_modifier",
    "irons_spellbooks:chest_loot/end_city_modifier",
    "irons_spellbooks:chest_loot/stronghold_library_modifier",
    "irons_spellbooks:chest_loot/ancient_city_modifier",
    "irons_spellbooks:chest_loot/nether_loot_modifier",
    "irons_spellbooks:chest_loot/vanilla_generic_loot_modifier",
    "irons_spellbooks:chest_loot/compat_generic_loot_modifier",
    "irons_spellbooks:chest_loot/compat_good_loot_modifier",
    "irons_spellbooks:chest_loot/compat_treasure_loot_modifier"
  ]
}
```

</details>

<details>
<summary>data/irons_spellbooks/loot_modifiers/chest_loot/ancient_city_modifier.json — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:any_of",
      "terms": [
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/ancient_city"
        }
      ]
    }
  ],
  "key": "irons_spellbooks:chests/additional_ancient_city_loot"
}
```

</details>

<details>
<summary>data/irons_spellbooks/loot_modifiers/chest_loot/compat_generic_loot_modifier.json — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:any_of",
      "terms": [
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdungeons:zombie_dungeon/chests/common"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdungeons:skeleton_dungeon/chests/common"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdungeons:spider_dungeon/chests/egg_room"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterstrongholds:chests/common"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterstrongholds:chests/grand_library"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "structory:harvest/graveyard"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "structory:harvest/graveyard2"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "structory:harvest/old_manor/common"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "structory:ruin/swamp/loot"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "structory:ruin/taiga/illager_low"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "structory:ruin/taiga/illager_high"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "structory:harvest/manor2/loot"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "idas:chests/wizardtower/wizardtower_library"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "idas:chests/apothecary_abode/apothecary_abode"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "nova_structures:chests/badland_miner_outpost_towers"
        }
      ]
    }
  ],
  "key": "irons_spellbooks:chests/additional_generic_loot"
}
```

</details>

<details>
<summary>data/irons_spellbooks/loot_modifiers/chest_loot/compat_good_loot_modifier.json — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:any_of",
      "terms": [
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdeserttemples:chests/tomb"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdeserttemples:chests/storage"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdeserttemples:chests/library"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdungeons:zombie_dungeon/chests/tombstone"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterwitchhuts:chests/hut_0"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "structory:library/high"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "structory:library/low"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "structory:ruin/taiga/illager_treasure"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "idas:chests/wizardtower/wizardtower_top"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "idas:chests/tinkers_workshop/tinkers_workshop_vault"
        }
      ]
    }
  ],
  "key": "irons_spellbooks:chests/additional_good_loot"
}
```

</details>

<details>
<summary>data/irons_spellbooks/loot_modifiers/chest_loot/compat_treasure_loot_modifier.json — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:any_of",
      "terms": [
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdeserttemples:chests/pharaoh_hidden"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/worship"
        }
      ]
    }
  ],
  "key": "irons_spellbooks:chests/additional_treasure_loot"
}
```

</details>

<details>
<summary>data/irons_spellbooks/loot_modifiers/chest_loot/end_city_modifier.json — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:any_of",
      "terms": [
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/end_city_treasure"
        }
      ]
    }
  ],
  "key": "irons_spellbooks:chests/additional_end_city_loot"
}
```

</details>

<details>
<summary>data/irons_spellbooks/loot_modifiers/chest_loot/nether_loot_modifier.json — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:any_of",
      "terms": [
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/nether_bridge"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/bastion_treasure"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/bastion_bridge"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/bastion_other"
        }
      ]
    }
  ],
  "key": "irons_spellbooks:chests/additional_nether_loot"
}
```

</details>

<details>
<summary>data/irons_spellbooks/loot_modifiers/chest_loot/stronghold_library_modifier.json — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:any_of",
      "terms": [
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/stronghold_library"
        }
      ]
    }
  ],
  "key": "irons_spellbooks:chests/additional_library_loot"
}
```

</details>

<details>
<summary>data/irons_spellbooks/loot_modifiers/chest_loot/vanilla_generic_loot_modifier.json — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:any_of",
      "terms": [
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/buried_treasure"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/desert_pyramid"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/jungle_temple"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/pillager_outpost"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/shipwreck_map"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/simple_dungeon"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/stronghold_crossing"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/stronghold_corridor"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/underwater_ruin_big"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/underwater_ruin_small"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/woodland_mansion"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/village/village_cartographer"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/village/village_temple"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/ruined_portal"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/abandoned_mineshaft"
        }
      ]
    }
  ],
  "key": "irons_spellbooks:chests/additional_generic_loot"
}
```

</details>

<details>
<summary>data/irons_spellbooks/loot_modifiers/entity_drops/blaze_modifier.json — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:entity_properties",
      "entity": "this",
      "predicate": {
        "type": "minecraft:blaze"
      }
    }
  ],
  "key": "irons_spellbooks:entities/additional_blaze_loot"
}
```

</details>

<details>
<summary>data/irons_spellbooks/loot_modifiers/entity_drops/ender_dragon_modifier.json — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:entity_properties",
      "entity": "this",
      "predicate": {
        "type": "minecraft:ender_dragon"
      }
    }
  ],
  "key": "irons_spellbooks:entities/additional_dragon_loot"
}
```

</details>

<details>
<summary>data/irons_spellbooks/loot_modifiers/entity_drops/evoker_modifier.json — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:entity_properties",
      "entity": "this",
      "predicate": {
        "type": "minecraft:evoker"
      }
    }
  ],
  "key": "irons_spellbooks:entities/additional_evoker_loot"
}
```

</details>

<details>
<summary>data/irons_spellbooks/loot_modifiers/entity_drops/hoglin_modifier.json — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:entity_properties",
      "entity": "this",
      "predicate": {
        "type": "minecraft:hoglin"
      }
    }
  ],
  "key": "irons_spellbooks:entities/additional_hoglin_loot"
}
```

</details>

<details>
<summary>data/irons_spellbooks/loot_modifiers/entity_drops/stray_modifier.json — irons_spellbooks-1.20.1-3.16.3.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\irons_spellbooks-1.20.1-3.16.3.jar`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:entity_properties",
      "entity": "this",
      "predicate": {
        "type": "minecraft:stray"
      }
    }
  ],
  "key": "irons_spellbooks:entities/additional_stray_loot"
}
```

</details>

<details>
<summary>data/forge/loot_modifiers/global_loot_modifiers.json — kaleidoscope_chinesefood-1.1.16-1.20.1-all.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_chinesefood-1.1.16-1.20.1-all.jar`

```json
{
  "entries": [
    "kaleidoscope_chinesefood:grass_eggplant_drop"
  ],
  "replace": false
}
```

</details>

<details>
<summary>data/kaleidoscope_chinesefood/loot_modifiers/grass_eggplant_drop.json — kaleidoscope_chinesefood-1.1.16-1.20.1-all.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_chinesefood-1.1.16-1.20.1-all.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [
    {
      "condition": "minecraft:any_of",
      "terms": [
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:blocks/short_grass"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:blocks/tall_grass"
        }
      ]
    }
  ],
  "loot_table_add": "kaleidoscope_chinesefood:grass_eggplant_drop",
  "loot_table_type": "minecraft:block"
}
```

</details>

<details>
<summary>data/forge/loot_modifiers/global_loot_modifiers.json — kaleidoscope_end-1.0.14-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_end-1.0.14-forge+mc1.20.1.jar`

```json
{
  "replace": false,
  "entries": [
    "kaleidoscope_end:blocks/chorus_plant",
    "kaleidoscope_end:ender_dragon",
    "kaleidoscope_end:enderman",
    "kaleidoscope_end:endermite",
    "kaleidoscope_end:shulker"
  ]
}
```

</details>

<details>
<summary>data/kaleidoscope_end/loot_modifiers/blocks/chorus_plant.json — kaleidoscope_end-1.0.14-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_end-1.0.14-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_end:blocks/chorus_plant",
  "loot_table_id": "minecraft:blocks/chorus_plant",
  "loot_table_type": "minecraft:block"
}
```

</details>

<details>
<summary>data/kaleidoscope_end/loot_modifiers/ender_dragon.json — kaleidoscope_end-1.0.14-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_end-1.0.14-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_end:ender_dragon",
  "loot_table_id": "minecraft:entities/ender_dragon",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_end/loot_modifiers/enderman.json — kaleidoscope_end-1.0.14-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_end-1.0.14-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_end:enderman",
  "loot_table_id": "minecraft:entities/enderman",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_end/loot_modifiers/endermite.json — kaleidoscope_end-1.0.14-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_end-1.0.14-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_end:endermite",
  "loot_table_id": "minecraft:entities/endermite",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_end/loot_modifiers/shulker.json — kaleidoscope_end-1.0.14-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_end-1.0.14-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_end:shulker",
  "loot_table_id": "minecraft:entities/shulker",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/forge/loot_modifiers/global_loot_modifiers.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "replace": false,
  "entries": [
    "kaleidoscope_nether:blocks/nether_wart",
    "kaleidoscope_nether:chests/bastion_hoglin_stable",
    "kaleidoscope_nether:chests/bastion_treasure",
    "kaleidoscope_nether:gameplay/piglin_bartering",
    "kaleidoscope_nether:integration/betternether/flying_pig",
    "kaleidoscope_nether:integration/betternether/naga",
    "kaleidoscope_nether:integration/betternether/skull",
    "kaleidoscope_nether:integration/bygonenether/corpor",
    "kaleidoscope_nether:integration/bygonenether/piglin_hunter",
    "kaleidoscope_nether:integration/bygonenether/piglin_prisoner",
    "kaleidoscope_nether:integration/bygonenether/wex",
    "kaleidoscope_nether:integration/bygonenether/wither_skeleton_horse",
    "kaleidoscope_nether:integration/bygonenether/wither_skeleton_knight",
    "kaleidoscope_nether:integration/bygonenether/wraither",
    "kaleidoscope_nether:integration/dungeonsmobs/fungus_thrower",
    "kaleidoscope_nether:integration/dungeonsmobs/wildfire",
    "kaleidoscope_nether:integration/dungeonsmobs/zombified_fungus_thrower",
    "kaleidoscope_nether:integration/twilightforest/boar",
    "kaleidoscope_nether:integration/twilightforest/carminite_ghastguard",
    "kaleidoscope_nether:integration/twilightforest/carminite_ghastling",
    "kaleidoscope_nether:integration/twilightforest/ur_ghast",
    "kaleidoscope_nether:blaze",
    "kaleidoscope_nether:ghast",
    "kaleidoscope_nether:hoglin",
    "kaleidoscope_nether:magma_cube",
    "kaleidoscope_nether:piglin",
    "kaleidoscope_nether:piglin_brute",
    "kaleidoscope_nether:strider",
    "kaleidoscope_nether:wither",
    "kaleidoscope_nether:wither_skeleton"
  ]
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/blaze.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:blaze",
  "loot_table_id": "minecraft:entities/blaze",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/blocks/nether_wart.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:blocks/nether_wart",
  "loot_table_id": "minecraft:blocks/nether_wart",
  "loot_table_type": "minecraft:block"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/chests/bastion_hoglin_stable.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:chests/bastion_hoglin_stable",
  "loot_table_id": "minecraft:chests/bastion_hoglin_stable",
  "loot_table_type": "minecraft:chest"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/chests/bastion_treasure.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:chests/bastion_treasure",
  "loot_table_id": "minecraft:chests/bastion_treasure",
  "loot_table_type": "minecraft:chest"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/gameplay/piglin_bartering.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:gameplay/piglin_bartering",
  "loot_table_id": "minecraft:gameplay/piglin_bartering",
  "loot_table_type": "minecraft:barter"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/ghast.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:ghast",
  "loot_table_id": "minecraft:entities/ghast",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/hoglin.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:hoglin",
  "loot_table_id": "minecraft:entities/hoglin",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/integration/betternether/flying_pig.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:integration/betternether/flying_pig",
  "loot_table_id": "betternether:entities/flying_pig",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/integration/betternether/naga.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:integration/betternether/naga",
  "loot_table_id": "betternether:entities/naga",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/integration/betternether/skull.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:integration/betternether/skull",
  "loot_table_id": "betternether:entities/skull",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/integration/bygonenether/corpor.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:integration/bygonenether/corpor",
  "loot_table_id": "bygonenether:entities/corpor",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/integration/bygonenether/piglin_hunter.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:integration/bygonenether/piglin_hunter",
  "loot_table_id": "bygonenether:entities/piglin_hunter",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/integration/bygonenether/piglin_prisoner.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:integration/bygonenether/piglin_prisoner",
  "loot_table_id": "bygonenether:entities/piglin_prisoner",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/integration/bygonenether/wex.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:integration/bygonenether/wex",
  "loot_table_id": "bygonenether:entities/wex",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/integration/bygonenether/wither_skeleton_horse.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:integration/bygonenether/wither_skeleton_horse",
  "loot_table_id": "bygonenether:entities/wither_skeleton_horse",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/integration/bygonenether/wither_skeleton_knight.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:integration/bygonenether/wither_skeleton_knight",
  "loot_table_id": "bygonenether:entities/wither_skeleton_knight",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/integration/bygonenether/wraither.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:integration/bygonenether/wraither",
  "loot_table_id": "bygonenether:entities/wraither",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/integration/dungeonsmobs/fungus_thrower.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:integration/dungeonsmobs/fungus_thrower",
  "loot_table_id": "dungeonsmobs:entities/fungus_thrower",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/integration/dungeonsmobs/wildfire.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:integration/dungeonsmobs/wildfire",
  "loot_table_id": "dungeonsmobs:entities/wildfire",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/integration/dungeonsmobs/zombified_fungus_thrower.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:integration/dungeonsmobs/zombified_fungus_thrower",
  "loot_table_id": "dungeonsmobs:entities/zombified_fungus_thrower",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/integration/twilightforest/boar.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:integration/twilightforest/boar",
  "loot_table_id": "twilightforest:entities/boar",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/integration/twilightforest/carminite_ghastguard.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:integration/twilightforest/carminite_ghastguard",
  "loot_table_id": "twilightforest:entities/carminite_ghastguard",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/integration/twilightforest/carminite_ghastling.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:integration/twilightforest/carminite_ghastling",
  "loot_table_id": "twilightforest:entities/carminite_ghastling",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/integration/twilightforest/ur_ghast.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:integration/twilightforest/ur_ghast",
  "loot_table_id": "twilightforest:entities/ur_ghast",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/magma_cube.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:magma_cube",
  "loot_table_id": "minecraft:entities/magma_cube",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/piglin.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:piglin",
  "loot_table_id": "minecraft:entities/piglin",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/piglin_brute.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:piglin_brute",
  "loot_table_id": "minecraft:entities/piglin_brute",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/strider.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:strider",
  "loot_table_id": "minecraft:entities/strider",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/wither.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:wither",
  "loot_table_id": "minecraft:entities/wither",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_nether/loot_modifiers/wither_skeleton.json — kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_nether:wither_skeleton",
  "loot_table_id": "minecraft:entities/wither_skeleton",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/forge/loot_modifiers/global_loot_modifiers.json — kaleidoscopecookery-1.6.0-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscopecookery-1.6.0-forge+mc1.20.1.jar`

```json
{
  "entries": [
    "kaleidoscope_cookery:zombified_piglin",
    "kaleidoscope_cookery:zoglin",
    "kaleidoscope_cookery:piglin",
    "kaleidoscope_cookery:hoglin",
    "kaleidoscope_cookery:donkey",
    "kaleidoscope_cookery:piglin_brute",
    "kaleidoscope_cookery:straw_hat_seed_drop",
    "kaleidoscope_cookery:pig"
  ],
  "replace": false
}
```

</details>

<details>
<summary>data/kaleidoscope_cookery/loot_modifiers/donkey.json — kaleidoscopecookery-1.6.0-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscopecookery-1.6.0-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_cookery:donkey",
  "loot_table_id": "minecraft:entities/donkey",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_cookery/loot_modifiers/hoglin.json — kaleidoscopecookery-1.6.0-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscopecookery-1.6.0-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_cookery:hoglin",
  "loot_table_id": "minecraft:entities/hoglin",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_cookery/loot_modifiers/pig.json — kaleidoscopecookery-1.6.0-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscopecookery-1.6.0-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_cookery:pig",
  "loot_table_id": "minecraft:entities/pig",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_cookery/loot_modifiers/piglin.json — kaleidoscopecookery-1.6.0-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscopecookery-1.6.0-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_cookery:piglin",
  "loot_table_id": "minecraft:entities/piglin",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_cookery/loot_modifiers/piglin_brute.json — kaleidoscopecookery-1.6.0-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscopecookery-1.6.0-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_cookery:piglin_brute",
  "loot_table_id": "minecraft:entities/piglin_brute",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_cookery/loot_modifiers/straw_hat_seed_drop.json — kaleidoscopecookery-1.6.0-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscopecookery-1.6.0-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_cookery:straw_hat_seed_drop",
  "loot_table_id": "minecraft:blocks/grass",
  "loot_table_type": "minecraft:block"
}
```

</details>

<details>
<summary>data/kaleidoscope_cookery/loot_modifiers/zoglin.json — kaleidoscopecookery-1.6.0-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscopecookery-1.6.0-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_cookery:zoglin",
  "loot_table_id": "minecraft:entities/zoglin",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/kaleidoscope_cookery/loot_modifiers/zombified_piglin.json — kaleidoscopecookery-1.6.0-forge+mc1.20.1.jar</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\mods\kaleidoscopecookery-1.6.0-forge+mc1.20.1.jar`

```json
{
  "type": "kaleidoscope_cookery:addition",
  "conditions": [],
  "loot_table_add": "kaleidoscope_cookery:zombified_piglin",
  "loot_table_id": "minecraft:entities/zombified_piglin",
  "loot_table_type": "minecraft:entity"
}
```

</details>

<details>
<summary>data/forge/loot_modifiers/global_loot_modifiers.json — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\moonlight-global-datapacks\TheOptimizer_AdventureLoot.zip`

```json
{
  "replace": false,
  "entries": [
    "theoptimizer:chest_loot/yungs_tier_1",
    "theoptimizer:chest_loot/yungs_tier_2",
    "theoptimizer:chest_loot/yungs_tier_3",
    "theoptimizer:chest_loot/yungs_nether_cinder"
  ]
}
```

</details>

<details>
<summary>data/irons_spellbooks/loot_modifiers/chest_loot/compat_good_loot_modifier.json — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\moonlight-global-datapacks\TheOptimizer_AdventureLoot.zip`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:any_of",
      "terms": [
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/simple_dungeon"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/desert_pyramid"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/jungle_temple"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/woodland_mansion"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/stronghold_corridor"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/stronghold_crossing"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterstrongholds:chests/crypt"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterstrongholds:chests/common"
        }
      ]
    }
  ],
  "key": "irons_spellbooks:chests/additional_good_loot"
}
```

</details>

<details>
<summary>data/irons_spellbooks/loot_modifiers/chest_loot/compat_treasure_loot_modifier.json — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\moonlight-global-datapacks\TheOptimizer_AdventureLoot.zip`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:any_of",
      "terms": [
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/buried_treasure"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/end_city_treasure"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/bastion_treasure"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterstrongholds:chests/treasure"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterstrongholds:chests/armoury"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterstrongholds:chests/grand_library"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterstrongholds:chests/library_md"
        }
      ]
    }
  ],
  "key": "irons_spellbooks:chests/additional_treasure_loot"
}
```

</details>

<details>
<summary>data/irons_spellbooks/loot_modifiers/chest_loot/vanilla_generic_loot_modifier.json — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\moonlight-global-datapacks\TheOptimizer_AdventureLoot.zip`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:any_of",
      "terms": [
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/abandoned_mineshaft"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/pillager_outpost"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/shipwreck_map"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/shipwreck_supply"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/underwater_ruin_big"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/underwater_ruin_small"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/ruined_portal"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/village/village_cartographer"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/village/village_temple"
        }
      ]
    }
  ],
  "key": "irons_spellbooks:chests/additional_generic_loot"
}
```

</details>

<details>
<summary>data/theoptimizer/loot_modifiers/chest_loot/yungs_nether_cinder.json — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\moonlight-global-datapacks\TheOptimizer_AdventureLoot.zip`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:any_of",
      "terms": [
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/beacon"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/extra"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/hall"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/keep"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/obsidian"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/puzzle"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/quarters"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/storage"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/worship"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/nether_bridge"
        }
      ]
    }
  ],
  "key": "theoptimizer:chests/yungs_nether_cinder"
}
```

</details>

<details>
<summary>data/theoptimizer/loot_modifiers/chest_loot/yungs_tier_1.json — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\moonlight-global-datapacks\TheOptimizer_AdventureLoot.zip`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:any_of",
      "terms": [
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdungeons:skeleton_dungeon/chests/common"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdungeons:small_dungeon/chests/loot_piles"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdungeons:small_nether_dungeon/chests/common"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdungeons:spider_dungeon/chests/egg_room"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdungeons:zombie_dungeon/chests/common"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterwitchhuts:chests/hut_0"
        }
      ]
    }
  ],
  "key": "theoptimizer:chests/yungs_tier_1"
}
```

</details>

<details>
<summary>data/theoptimizer/loot_modifiers/chest_loot/yungs_tier_2.json — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\moonlight-global-datapacks\TheOptimizer_AdventureLoot.zip`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:any_of",
      "terms": [
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdeserttemples:chests/food_storage"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdeserttemples:chests/lab"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdeserttemples:chests/library"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdeserttemples:chests/pharaoh_hidden"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdeserttemples:chests/pot"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdeserttemples:chests/statue"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdeserttemples:chests/storage"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdeserttemples:chests/tomb"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdeserttemples:chests/tomb_pharaoh"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdeserttemples:chests/wardrobe"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdungeons:skeleton_dungeon/chests/middle"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdungeons:zombie_dungeon/chests/special"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterdungeons:zombie_dungeon/chests/tombstone"
        }
      ]
    }
  ],
  "key": "theoptimizer:chests/yungs_tier_2"
}
```

</details>

<details>
<summary>data/theoptimizer/loot_modifiers/chest_loot/yungs_tier_3.json — TheOptimizer_AdventureLoot.zip</summary>

Fuente: `C:\Users\Metabodiru\Desktop\servidor-theoptimizer\moonlight-global-datapacks\TheOptimizer_AdventureLoot.zip`

```json
{
  "type": "irons_spellbooks:append_loot",
  "conditions": [
    {
      "condition": "minecraft:any_of",
      "terms": [
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/beacon"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/extra"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/hall"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/keep"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/obsidian"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/puzzle"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/quarters"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/storage"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betterfortresses:chests/worship"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "betteroceanmonuments:chests/upper_side_chamber"
        },
        {
          "condition": "forge:loot_table_id",
          "loot_table_id": "minecraft:chests/nether_bridge"
        }
      ]
    }
  ],
  "key": "theoptimizer:chests/yungs_tier_3"
}
```

</details>
