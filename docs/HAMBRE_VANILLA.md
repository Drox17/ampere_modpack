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

| Acción | Vanilla | En Ampere (÷5) | Equivale en Ampere |
|---|---:|---:|---|
| **Correr** (sprint) | 0.1 / m | **0.02 / m** | 200 m por punto de saturación |
| **Caminar / nadar** | 0.01 / m | **0.002 / m** | 2000 m por punto |
| **Salto normal** | 0.05 | **0.01** | 400 saltos por punto |
| **Salto corriendo** | 0.2 | **0.04** | 100 saltos por punto |
| **Atacar** (golpe cuerpo a cuerpo) | **0.1** | **0.1** (sin cambio) | 40 golpes por punto |
| **Romper un bloque** | **0.005** | **0.005** (sin cambio) | 800 bloques por punto |
| **Recibir daño** | 0.1 según tipo | **sin cambio** | 40 golpes recibidos |
| **Regeneración natural** | 6.0 por medio corazón | **desactivada** | Sustituida por la curación de Ampere |

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

## Regeneración en Ampere (1.21.0)

La rama de regeneración vanilla (`FoodData.tick`) está **cancelada**: no existe la "aspiradora" de 6.0
por medio corazón. La única regeneración pasiva es la del pack:

- **1 HP cada 40 ticks (2 s)** mientras haya comida y el jugador esté herido.
- Coste: **2.0 de agotamiento** por HP → **1 corazón = 4.0 = 1 punto de saturación**, repartido en 4 s.
- Fuego, veneno, wither y punciones siguen bloqueando la regeneración natural por las reglas de
  `naturalRegeneration` y del propio `Player.canHeal`... salvo que el daño no impida curar.

