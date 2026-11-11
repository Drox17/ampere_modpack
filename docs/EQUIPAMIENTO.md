# Equipamiento: durabilidad y escala (1.22.0)

Resumen operativo. Detalle de roles y análisis en `docs/PROGRESION_EQUIPAMIENTO.md`.

## Armaduras

| Material | Puntos | Durabilidad por pieza (casco/peto/grebas/botas) | Total | Reparación |
|---|---:|---|---:|---:|
| Cuero | 15 | 165 / 240 / 225 / 195 | 825 | 100 % |
| Cota de malla | 15 | 165 / 240 / 225 / 195 | 825 | 100 % |
| Oro | 15 | 165 / 240 / 225 / 195 | 825 | 100 % |
| Hierro | 15 | 165 / 240 / 225 / 195 | 825 | 100 % |
| Diamante | 20 | 363 / 528 / 495 / 429 | 1815 | 25 % |
| Netherita | 20 | 407 / 592 / 555 / 481 | 2035 | 25 % |

## Herramientas y armas

| Tier | Durabilidad | Velocidad |
|---|---:|---:|
| Madera | 80 | 6.0 |
| Piedra | 160 | 6.0 |
| Hierro | 300 | 6.0 |
| Oro | 300 | 6.0 |
| Diamante | 1561 | 6.0 |
| Netherita | 2031 | 6.0 |

Reglas: velocidad de minado unificada, reparación 100 % (base) / 25 % (élite), pérdida del 10 % de
durabilidad al morir. Las claves de config son `wood_tool_durability`, `stone_tool_durability`,
`iron_tool_durability`, `gold_tools_durability` y `gold_armor_multiplier`.
