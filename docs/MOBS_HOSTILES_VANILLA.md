# Mobs hostiles vanilla (1.20.1): atributos base y efecto del pack

Extraido del bytecode del servidor (SRG, `javap`) resolviendo la herencia de clases, y
cruzado con los cambios de `TheOptimizer-MobBalance` (`EntityAttributeModificationEvent`).
`Vida pack` es la vida **efectiva** en el modpack; el resto de atributos no los modifica el pack.

| Mob | Grupo | Vida vanilla | Vida pack | Daño | Armadura | Dureza | Res. empuje | Velocidad | Seguimiento |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Zombi | hostil | 20 | 20 | 3 | 2 | 0 | 0 | 0.23 | 35 |
| Zombi momificado | hostil | 20 | 20 | 3 | 2 | 0 | 0 | 0.23 | 35 |
| Ahogado | hostil | 20 | 20 | 3 | 2 | 0 | 0 | 0.23 | 35 |
| Aldeano zombi | hostil | 20 | 20 | 3 | 2 | 0 | 0 | 0.23 | 35 |
| Esqueleto | hostil | 20 | 12 *(pack)* | 2 | 0 | 0 | 0 | 0.25 | 16 |
| Errante | hostil | 20 | 12 *(pack)* | 2 | 0 | 0 | 0 | 0.25 | 16 |
| Esqueleto del Wither | hostil | 20 | 20 | 2 | 0 | 0 | 0 | 0.25 | 16 |
| Creeper | hostil | 20 | 20 | 2 | 0 | 0 | 0 | 0.25 | 16 |
| Arana | hostil | 16 | 14 *(pack)* | 2 | 0 | 0 | 0 | 0.3 | 16 |
| Arana de cueva | hostil | 12 | 12 | 2 | 0 | 0 | 0 | 0.3 | 16 |
| Lepisma | hostil | 8 | 8 | 2 | 0 | 0 | 0 | 0.25 | 16 |
| Endermite | hostil | 8 | 8 | 2 | 0 | 0 | 0 | 0.25 | 16 |
| Slime | hostil | 20 | 20 | - | 0 | 0 | 0 | 0.7 | 16 |
| Cubo de magma | hostil | 20 | 20 | - | 0 | 0 | 0 | 0.2 | 16 |
| Ghast | hostil | 10 | 10 | - | 0 | 0 | 0 | 0.7 | 100 |
| Blaze | hostil | 20 | 20 | 6 | 0 | 0 | 0 | 0.23 | 48 |
| Bruja | hostil | 26 | 20 *(pack)* | 2 | 0 | 0 | 0 | 0.25 | 16 |
| Saqueador | hostil | 24 | 24 | 5 | 0 | 0 | 0 | 0.35 | 32 |
| Vindicador | hostil | 24 | 24 | 5 | 0 | 0 | 0 | 0.35 | 12 |
| Evocador | hostil | 24 | 24 | 2 | 0 | 0 | 0 | 0.5 | 12 |
| Ilusionista | hostil | 32 | 32 | 2 | 0 | 0 | 0 | 0.5 | 18 |
| Devastador | mini-jefe | 100 | 100 | 12 | 0 | 0 | 0.75 | 0.3 | 32 |
| Guardian | hostil | 30 | 30 | 6 | 0 | 0 | 0 | 0.5 | 16 |
| Guardian anciano | mini-jefe | 80 | 80 | 8 | 0 | 0 | 0 | 0.3 | 16 |
| Shulker | hostil | 30 | 30 | - | 0 | 0 | 0 | 0.7 | 16 |
| Fantasma | hostil | 20 | 10 *(pack)* | - | 0 | 0 | 0 | 0.7 | 16 |
| Enderman | hostil | 40 | 40 | 7 | 0 | 0 | 0 | 0.3 | 64 |
| Vex | hostil | 14 | 14 | 4 | 0 | 0 | 0 | 0.7 | 16 |
| Hoglin | hostil | 40 | 40 | 6 | 0 | 0 | 0.6 | 0.3 | 16 |
| Zoglin | hostil | 40 | 40 | 6 | 0 | 0 | 0.6 | 0.3 | 16 |
| Piglin | hostil | 16 | 16 | 5 | 0 | 0 | 0 | 0.35 | 16 |
| Piglin bruto | hostil | 50 | 50 | 7 | 0 | 0 | 0 | 0.35 | 16 |
| Piglin zombificado | hostil | - | - | - | - | - | - | - | - |
| Gigante | hostil | 100 | 100 | 50 | 0 | 0 | 0 | 0.5 | 16 |
| Warden | jefe | 500 | 500 | 30 | 0 | 0 | 0 | 0.3 | 16 |
| Wither | jefe | 300 | 300 | 2 | 4 | 0 | 0 | 0.6 | 40 |
| Dragon del End | jefe | 200 | 200 | - | 0 | 0 | 0 | 0.7 | 16 |

## Cambios del pack (MobBalance)

| Mob | Vida vanilla | Vida pack |
|---|---:|---:|
| Esqueleto | 20 | 12 |
| Errante | 20 | 12 |
| Arana | 16 | 14 |
| Fantasma | 20 | 10 |
| Bruja | 26 | 20 |

## Notas

- `danio` es el ataque cuerpo a cuerpo base; la dificultad lo escala en el cálculo del golpe (x0.5 a x1.5),
  no en el atributo.
- `res_empuje` = 1.0 significa inmune al empuje (Warden, Wither, Devastador).
- `velocidad` es el multiplicador por tick (0.25 ≈ jugador caminando).
- Los grupos `jefe` se incluyen como referencia; el análisis de no jefes usa `hostil` y `mini-jefe`.
- Reejecutar: `python herramientas/extraer_atributos_vanilla.py`.
