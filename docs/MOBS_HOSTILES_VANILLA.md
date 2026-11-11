# Mobs hostiles vanilla (1.20.1): atributos base y efecto del pack

> Generado por `herramientas/extraer_atributos_vanilla.py`. No editar a mano.

## Cómo se obtuvieron estos datos

1. Se lee el **bytecode** del servidor Forge (jar SRG) con `javap`, sin depender de la wiki.
2. Cada entidad define sus atributos en un método estático que devuelve `AttributeSupplier$Builder`;
   las constantes aparecen como `getstatic Attributes.f_XXXX_` + `ldc2_w` + `Builder.m_22268_(Attribute, D)`.
3. La **herencia** se resuelve por la cabecera `extends` (p. ej. Zombi → Monster → PathfinderMob → Mob → LivingEntity).
4. Los atributos añadidos sin valor (`Builder.m_22266_`) usan el **valor por defecto** del atributo,
   que se extrae del inicializador estático de `Attributes`.
5. Se cruza con el único mod del pack que toca atributos de hostiles:
   `TheOptimizer-MobBalance` (`EntityAttributeModificationEvent`).

Reejecutar: `python herramientas/extraer_atributos_vanilla.py`.

## Cambios del pack (MobBalance)

| Mob | Vida vanilla | Vida pack |
|---|---:|---:|
| Esqueleto | 20 | 12 |
| Errante | 20 | 12 |
| Arana | 16 | 14 |
| Fantasma | 20 | 10 |
| Bruja | 26 | 20 |

## Hostiles (no jefes)

| Mob | Vida vanilla | Vida pack | Daño | Armadura | Dureza | Res. empuje | Velocidad | Seguimiento |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Zombi | 20 | 20 | 3 | 2 | 0 | 0 | 0.23 | 35 |
| Zombi momificado | 20 | 20 | 3 | 2 | 0 | 0 | 0.23 | 35 |
| Ahogado | 20 | 20 | 3 | 2 | 0 | 0 | 0.23 | 35 |
| Aldeano zombi | 20 | 20 | 3 | 2 | 0 | 0 | 0.23 | 35 |
| Esqueleto | 20 | 12 *(pack)* | 2 | 0 | 0 | 0 | 0.25 | 16 |
| Errante | 20 | 12 *(pack)* | 2 | 0 | 0 | 0 | 0.25 | 16 |
| Esqueleto del Wither | 20 | 20 | 2 | 0 | 0 | 0 | 0.25 | 16 |
| Creeper | 20 | 20 | 2 | 0 | 0 | 0 | 0.25 | 16 |
| Arana | 16 | 14 *(pack)* | 2 | 0 | 0 | 0 | 0.3 | 16 |
| Arana de cueva | 12 | 12 | 2 | 0 | 0 | 0 | 0.3 | 16 |
| Lepisma | 8 | 8 | 2 | 0 | 0 | 0 | 0.25 | 16 |
| Endermite | 8 | 8 | 2 | 0 | 0 | 0 | 0.25 | 16 |
| Slime | 20 | 20 | - | 0 | 0 | 0 | 0.7 | 16 |
| Cubo de magma | 20 | 20 | - | 0 | 0 | 0 | 0.2 | 16 |
| Ghast | 10 | 10 | - | 0 | 0 | 0 | 0.7 | 100 |
| Blaze | 20 | 20 | 6 | 0 | 0 | 0 | 0.23 | 48 |
| Bruja | 26 | 20 *(pack)* | 2 | 0 | 0 | 0 | 0.25 | 16 |
| Saqueador | 24 | 24 | 5 | 0 | 0 | 0 | 0.35 | 32 |
| Vindicador | 24 | 24 | 5 | 0 | 0 | 0 | 0.35 | 12 |
| Evocador | 24 | 24 | 2 | 0 | 0 | 0 | 0.5 | 12 |
| Ilusionista | 32 | 32 | 2 | 0 | 0 | 0 | 0.5 | 18 |
| Guardian | 30 | 30 | 6 | 0 | 0 | 0 | 0.5 | 16 |
| Shulker | 30 | 30 | - | 0 | 0 | 0 | 0.7 | 16 |
| Fantasma | 20 | 10 *(pack)* | - | 0 | 0 | 0 | 0.7 | 16 |
| Enderman | 40 | 40 | 7 | 0 | 0 | 0 | 0.3 | 64 |
| Vex | 14 | 14 | 4 | 0 | 0 | 0 | 0.7 | 16 |
| Hoglin | 40 | 40 | 6 | 0 | 0 | 0.6 | 0.3 | 16 |
| Zoglin | 40 | 40 | 6 | 0 | 0 | 0.6 | 0.3 | 16 |
| Piglin | 16 | 16 | 5 | 0 | 0 | 0 | 0.35 | 16 |
| Piglin bruto | 50 | 50 | 7 | 0 | 0 | 0 | 0.35 | 16 |
| Piglin zombificado | - | - | - | - | - | - | - | - |
| Gigante | 100 | 100 | 50 | 0 | 0 | 0 | 0.5 | 16 |

## Mini-jefes

| Mob | Vida vanilla | Vida pack | Daño | Armadura | Dureza | Res. empuje | Velocidad | Seguimiento |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Devastador | 100 | 100 | 12 | 0 | 0 | 0.75 | 0.3 | 32 |
| Guardian anciano | 80 | 80 | 8 | 0 | 0 | 0 | 0.3 | 16 |

## Jefes (solo referencia, fuera del análisis de no jefes)

| Mob | Vida | Daño | Armadura | Res. empuje | Velocidad | Seguimiento |
|---|---:|---:|---:|---:|---:|---:|
| Warden | 500 | 30 | 0 | 0 | 0.3 | 16 |
| Wither | 300 | 2 | 4 | 0 | 0.6 | 40 |
| Dragon del End | 200 | - | 0 | 0 | 0.7 | 16 |

## Daño cuerpo a cuerpo por dificultad

El atributo `danio` se escala al golpear: ×0.5 (Fácil), ×1.0 (Normal), ×1.5 (Difícil).

| Mob | Base | Fácil | Normal | Difícil |
|---|---:|---:|---:|---:|
| Zombi | 3 | 1.5 | 3 | 4.5 |
| Zombi momificado | 3 | 1.5 | 3 | 4.5 |
| Ahogado | 3 | 1.5 | 3 | 4.5 |
| Aldeano zombi | 3 | 1.5 | 3 | 4.5 |
| Esqueleto | 2 | 1 | 2 | 3 |
| Errante | 2 | 1 | 2 | 3 |
| Esqueleto del Wither | 2 | 1 | 2 | 3 |
| Creeper | 2 | 1 | 2 | 3 |
| Arana | 2 | 1 | 2 | 3 |
| Arana de cueva | 2 | 1 | 2 | 3 |
| Lepisma | 2 | 1 | 2 | 3 |
| Endermite | 2 | 1 | 2 | 3 |
| Blaze | 6 | 3 | 6 | 9 |
| Bruja | 2 | 1 | 2 | 3 |
| Saqueador | 5 | 2.5 | 5 | 7.5 |
| Vindicador | 5 | 2.5 | 5 | 7.5 |
| Evocador | 2 | 1 | 2 | 3 |
| Ilusionista | 2 | 1 | 2 | 3 |
| Devastador | 12 | 6 | 12 | 18 |
| Guardian | 6 | 3 | 6 | 9 |
| Guardian anciano | 8 | 4 | 8 | 12 |
| Enderman | 7 | 3.5 | 7 | 10.5 |
| Vex | 4 | 2 | 4 | 6 |
| Hoglin | 6 | 3 | 6 | 9 |
| Zoglin | 6 | 3 | 6 | 9 |
| Piglin | 5 | 2.5 | 5 | 7.5 |
| Piglin bruto | 7 | 3.5 | 7 | 10.5 |
| Gigante | 50 | 25 | 50 | 75 |

## Notas por mob

- **Zombi**: 20 de vida y armadura 2; el no-muerto más lento (0.23). En Difícil pega ~4.5.
- **Zombi momificado**: Igual que el zombi, pero no se quema de día y aplica Hambre.
- **Ahogado**: Zombi acuático; puede llevar tridente y nada.
- **Aldeano zombi**: Zombi con armadura 2; se cura con debilidad + manzana dorada.
- **Esqueleto**: Pack: 12 de vida (antes 20). Arquero; su cuerpo a cuerpo es flojo.
- **Errante**: Pack: 12 de vida. Flechas de lentitud.
- **Esqueleto del Wither**: 20 de vida; espada de piedra y efecto Wither.
- **Creeper**: 20 de vida; su daño es la explosión, no el atributo de melee.
- **Arana**: Pack: 14 de vida (antes 16). Rápida y escala paredes.
- **Arana de cueva**: 12 de vida; aplica veneno.
- **Lepisma**: 8 de vida; llama a más lepismas al ser golpeada.
- **Endermite**: 8 de vida; aparece al usar perlas del End.
- **Slime**: La vida depende del tamaño; el daño es por contacto.
- **Cubo de magma**: Vida por tamaño; daño de fuego al contacto.
- **Ghast**: 10 de vida; bola de fuego; el mayor seguimiento (100).
- **Blaze**: 20 de vida y 6 de daño base; ataca con bolas de fuego.
- **Bruja**: Pack: 20 de vida (antes 26). Combate con pociones.
- **Saqueador**: 24 de vida; ballesta y seguimiento 32.
- **Vindicador**: 24 de vida, 5 base; en Difícil su hacha pega ~19.
- **Evocador**: 24 de vida; invoca Vex y colmillos.
- **Ilusionista**: 32 de vida; ilusiones y arco.
- **Devastador**: 100 de vida, 12 base y 0.75 de resistencia al empuje; montura de saqueadores.
- **Guardian**: 30 de vida; rayo y seguimiento largo.
- **Guardian anciano**: 80 de vida; aplica fatiga de minería.
- **Shulker**: 30 de vida; proyectiles de levitación.
- **Fantasma**: Pack: 10 de vida (antes 20). Vuela y ataca en picado.
- **Enderman**: 40 de vida y 7 base; se teletransporta y esquiva flechas.
- **Vex**: 14 de vida; atraviesa paredes.
- **Hoglin**: 40 de vida, 6 base y 0.6 de resistencia al empuje.
- **Zoglin**: 40 de vida; inmune al fuego y 0.6 de resistencia al empuje.
- **Piglin**: 16 de vida; trueque y ballesta.
- **Piglin bruto**: 50 de vida y 7 base; hacha y mucha resistencia.
- **Piglin zombificado**: No parseable (clase sin atributos propios); hereda de Zombi: 20 de vida y 3 de daño.
- **Gigante**: 100 de vida y 50 base; no aparece en supervivencia, solo referencia.
- **Warden**: 500 de vida y 30 base; su resistencia al empuje real es 1.0 (inmune), no capturada por el extractor.
- **Wither**: 300 de vida; jefe. Su daño no es cuerpo a cuerpo.
- **Dragon del End**: 200 de vida; jefe. Ataca con aliento y embestidas.

## Limitaciones conocidas

- `danio` es el ataque **base**; la dificultad lo escala al golpear (ver tabla anterior).
- **Creeper, Ghast, Blaze, Shulker, Slime y Cubo de magma** no tienen daño cuerpo a cuerpo:
  usan explosión, bola de fuego, proyectil o daño por tamaño/contacto, que no son atributos.
- La vida de **Slime** y **Cubo de magma** depende del tamaño (la tabla muestra el atributo base).
- **Warden**: su resistencia al empuje real es 1.0 (inmune); el extractor no la captura porque la
  asigna por una vía distinta al patrón `add(Attribute, valor)`.
- **Piglin zombificado** no se pudo parsear (su clase no define atributos); hereda de Zombi: 20 de vida, 3 de daño.
- **Gigante** está incluido como referencia, pero no aparece en supervivencia.
- El daño de los proyectiles (flechas de esqueleto, bolas de blaze) y los efectos (veneno de araña de
  cueva, wither) no son atributos y no están en esta tabla.

## Familias de comportamiento (para balance)

| Familia | Mobs |
|---|---|
| No-muertos básicos | Zombi, Husk, Ahogado, Aldeano zombi, Esqueleto, Errante, Esqueleto del Wither |
| Artrópodos | Araña, Araña de cueva, Lepisma, Endermite |
| Nether | Blaze, Ghast, Cubo de magma, Piglin, Piglin bruto, Hoglin, Zoglin, Piglin zombificado |
| Saqueadores | Saqueador, Vindicador, Evocador, Ilusionista, Bruja, Devastador |
| Acuáticos | Ahogado, Guardián, Guardián anciano |
| Especiales | Creeper, Enderman, Shulker, Fantasma, Vex, Slime, Warden |

## Armadura añadida por el pack (1.18.0)

| Mob | Armadura |
|---|---:|
| Devastador | 10 |
| Guardián anciano | 8 |
| Piglin bruto | 8 |
| Guardián / Vindicador / Zoglin | 4 |

Así el +15 % de la netherita contra enemigos con armadura tiene objetivos reales.
