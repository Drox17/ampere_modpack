# Fuentes vanilla de agotamiento (1.20.1)

Extraído del bytecode del servidor (SRG, `javap`) el 11/11/2026. Cada valor es la constante que
vanilla pasa a `Player.causeFoodExhaustion(float)` (que a su vez llama a `FoodData.addExhaustion`).

## Cómo se convierte el agotamiento en hambre/saturación

En `FoodData.tick`:

1. Si `exhaustion > 4.0`: se restan `4.0`.
2. Si hay **saturación**, baja **1 punto de saturación**.
3. Si la saturación ya es 0 y la dificultad no es Pacífico, baja **1 punto de hambre**.

Es decir: **4.0 de agotamiento = 1 punto de saturación**, y cuando la saturación está vacía,
**4.0 de agotamiento = 1 punto de hambre** (medio muslo).

## Fuentes

| Acción | Agotamiento | Equivale a |
|---|---:|---|
| **Correr** (sprint) | **0.1 por metro** | 40 m por punto de saturación |
| **Caminar / nadar** | **0.01 por metro** | 400 m por punto de saturación |
| **Salto normal** | **0.05** | 80 saltos por punto |
| **Salto corriendo** | **0.2** | 20 saltos por punto |
| **Atacar** (golpe cuerpo a cuerpo) | **0.1** | 40 golpes por punto |
| **Romper un bloque** | **0.005** | 800 bloques por punto |
| **Recibir daño** | según el tipo de daño (`DamageType.exhaustion`, habitualmente **0.1**) | 40 golpes recibidos |
| **Regeneración natural** | **6.0 por medio corazón curado** | 1.5 puntos de saturación por medio corazón |

Notas de la extracción:

- `Player.jumpFromGround`: `0.2` si corre, `0.05` si no.
- `Player.checkMovementStatistics`: `0.01` por metro caminando/nadando y `0.1` por metro corriendo.
- `Player.attack`: `0.1`.
- `Block.dropResources` (lambda): `0.005` por bloque roto.
- `FoodData.tick`: `6.0` al curar (regeneración natural).
- `Player.hurt`: usa `DamageSource.getFoodExhaustion()`, que delega en el tipo de daño.

## Cómo lo usa Ampere

| Mecánica del pack | Coste |
|---|---|
| Escudo de hambre | `2.0` de agotamiento por cada punto de daño amortiguado |
| Sets pesados al golpear | `0.5` (diamante) / `0.6` (netherita) base + `0.03 × daño` por pieza |
| Sprint sin hambre | `sprint_independent_of_hunger = true` (no exige comida para correr) |
| Curación constante | `2.0` de agotamiento cada 40 ticks mientras cura |

## Reproducir

`python herramientas/extraer_hambre_vanilla.py` regenera `datos/hambre_vanilla.json` y el volcado`n`docs/HAMBRE_VANILLA_EXTRACCION.md` con las 15
llamadas detectadas en el bytecode y sus constantes.
