# BALANCE.md — memoria profunda del sistema de sets

> Se lee **solo al diseñar** (cambiar reglas, añadir sets, revisar números). Para `/sync`
> usa `verificar_estado.ps1` + `estado.json`. Este archivo explica el porqué y el backlog.

## 1. Números de referencia

### 1.1 Armaduras 1.23.0: Coloso vs. Enjambre

Esta revisión sustituye el escalado pasivo de 15/20 puntos y dureza. Todos los sets físicos vanilla y Cataclysm comparten 16 (casco 2, peto 5, grebas 6, botas 3). Las túnicas de Iron's/Alex's Caves y cualquier armadura detectada con `spell_power` usan 10 (1/3/4/2); Cursium usa 12 (2/4/4/2). La dureza es 0 para todo ArmorItem, eliminada también de los modificadores externos sin borrar sus atributos mágicos.

Coloso aplica `D - max(0, D - umbral) × absorción` sobre el daño bruto del impacto, antes de armadura y escudo de hambre; las reducciones de otros roles se componen como factores sin cambiar la clasificación del golpe. Umbral 10 y absorción 50 % con cuatro piezas de diamante/netherita. Cada pieza aporta una cuarta parte, incluidos sets mixtos; Ignitium aporta la mitad. Monstrous duplica el coeficiente combinado hasta 100 % del excedente. Ejemplo de daño entrante 20: normal 15, Ignitium completo 17.5, Monstrous con tres piezas de netherita 10, Cursium 20, antes de las demás defensas.

Brecha usa una ventana móvil de 30 ticks: el segundo impacto de combate aceptado reduce a la mitad la armadura efectiva usada por CombatRules. No altera permanentemente el atributo, no cambia el HUD y no multiplica directamente el daño. Los impactos antiguos caducan individualmente. Inanición, fuego y caídas no activan brecha; proyectiles y explosiones sí. Cursium queda fuera del cómputo pesado; una mezcla con piezas pesadas sí puede abrir brecha.

### 1.2 Roles y costes

Los roles ligeros conservan sus reducciones de caída/proyectiles/magia/explosiones y velocidad de malla. El hierro pierde su dureza adicional.

| Familia | Rol | Coste |
|---|---|---|
| Diamante | Coloso 50 % del excedente | ataque −15 % con set, brecha, agotamiento, reparación 25 % |
| Netherita y linaje | Coloso; fuego/wither −25 % por pieza; repulsión −6.25 % por pieza | ataque −20 % con set, brecha, daño +10 % con luz ambiental <8 a cuatro piezas, agotamiento, reparación 25 % |
| Monstrous (casco) | Coloso combinado ×2 | movimiento −10 % y ataque −30 % por casco; se combina multiplicativamente con los costes de otras piezas |
| Ignitium | Coloso reducido a la mitad; fuego reactivo de 3 s | mismo coste pesado; contraataque solo cuerpo a cuerpo, recarga global de 40 ticks por jugador |
| Cursium | herencia térmica, movilidad de ataque | armadura 12; sin Coloso, brecha ni agotamiento cinético; conserva debilidad por luz baja y reparación 25 % |
| Túnicas | hechizos; netherite_mage conserva linaje pesado | armadura 10 y daño cuerpo a cuerpo −5 % por pieza |

Las penalizaciones de ataque usan modificadores Forge `MULTIPLY_TOTAL` por slot, visibles en rojo. Para diamante/netherita, cada pieza usa la raíz cuarta del factor del set: cuatro piezas componen exactamente −15 %/−20 %, también sobre el enfriamiento real del arma. Monstrous es un casco único: su −30 % se añade al coste de las otras piezas, no constituye un set de cuatro piezas ficticio.

La inmunidad a fuego y marchitamiento requiere cuatro piezas del linaje; la inmunidad al efecto impide también aplicarlo. Se sustituye la antigua debilidad por golpes <8 por la debilidad ambiental solicitada en esta revisión. La reparación y el coste de agotamiento existentes se conservan salvo la exención de Cursium.

STARVE conserva su daño de servidor. El paquete vanilla de daño transporta el tipo: en cliente se sustituye su animación/sonido por un latido suave, sin cambiar la respuesta a ataques. Al cruzar el mínimo del escudo de hambre (8 a 7 de comida) se reproduce otro aviso con recarga de 100 ticks. El aviso es por ticks, independiente de los FPS, y no se repite mientras la reserva siga baja. Se usa la alternativa sonora solicitada; GuiMixin sigue ocultando XP sin añadir un render incompatible con ForgeGui.

Todos los umbrales nuevos viven en EquipmentConfig y default_cfg; los tooltips consultan las mismas reglas. Verificación: 75 comprobaciones JVM sobre clases del JAR real, 53 firmas contra dependencias instaladas y 86 defaults/config sincronizados. La respuesta visual/sonora y compatibilidad completa de mods quedan sujetas a prueba en juego.

### 1.3 Herramientas (estado actual, pendiente de rediseño)

Velocidad de minado unificada 6.0 para todos los tiers. Extras actuales: madera +7 %
movimiento y +0.35 vel. ataque (armas), piedra +25 % resist. empuje y +0.5 empuje (armas),
hierro +0.5 alcance y +1 armadura con arma, oro +1 Suerte, diamante +1.0 alcance y toque de
seda, netherita +1.0 alcance y más botín.

**Problema conocido**: una herramienta no debería dar movimiento ni armadura (es eje de
armadura). Ver backlog T1.

### 1.4 Hostiles no jefes (1.20.1, atributos base)

Datos completos en `docs/MOBS_HOSTILES_VANILLA.md` (bytecode real, reejecutable). Lo que cambia el pack
(`TheOptimizer-MobBalance`, `EntityAttributeModificationEvent`):

| Mob | Vida vanilla | Vida pack |
|---|---:|---:|
| Esqueleto | 20 | 12 |
| Errante | 20 | 12 |
| Araña | 16 | 14 |
| Fantasma | 20 | 10 |
| Bruja | 26 | 20 |

Referencias del resto: casi todos los básicos tienen 20 de vida y 2-3 de daño base; los pesados son
Devastador (100/12, empuje 0.75), Guardián anciano (80/8), Piglin bruto (50/7), Zoglin/Hoglin/Enderman (40/6-7).
El daño base se escala ×0.5 / ×1.0 / ×1.5 por dificultad al golpear. Creeper, Ghast, Blaze y Shulker
no tienen daño cuerpo a cuerpo (explosión, bola de fuego, proyectil).

> Auditoría del eje horizontal/vertical y márgenes de mejora: `docs/PROGRESION_EQUIPAMIENTO.md`.

### 1.6 Respuestas reactivas de jefes (anti-cheese)

`TheOptimizer-MobBalance` (1.2.0) no prohíbe bloques ni cancela invocaciones: cambia las reglas del
combate cuando se intenta abusar. Todo vive en `AntiCheeseBossHandler` (`@EventBusSubscriber`).

| Abuso | Respuesta | Detalle |
|---|---|---|
| Encerrar al Wither en bedrock/techo | Escapa sobre el jugador | 60 ticks atrapado → teleport + Lentitud I |
| Búnker acuático | El Wither evapora el agua | Radio 4, cada 20 ticks |
| Wither vs Warden | No se dañan y redirigen el agro | Al jugador más cercano (48 bloques) |
| Camas / TNT en cadena | Tope explosivo por segundo | 12 de daño por ventana de 20 ticks; el resto se descarta |
| Trident killer | Tridente viejo no daña | Cualquier tridente con más de 60 ticks |
| Granja de raids (lava/caída/gólem) | Sin premios gordos | Sin tótem, esmeraldas ni libros si el golpe letal no es de un jugador activo |
| Warden en nieve en polvo / pilar | Limpia y derriba | Rompe nieve y trampillas de su hitbox; a 16-40 bloques aplica Lentitud III y un tirón |
| TNT al monumento | Prismarina protegida | Inmune a explosiones mientras quede un Guardián anciano vivo |

Criterio: un jugador que pelea de forma normal no nota nada; el que abusa pierde la ventaja sin que se le
prohíba construir. Es la aplicación directa de P12 (juego tradicional primero) y P13 (el técnico deja de
tener la mejor opción).


### 1.5 Armadura real de mobs pesados (1.18.0)

El `+15 %` de la netherita contra enemigos con armadura necesita objetivos con armadura real:

| Mob | Armadura añadida |
|---|---:|
| Devastador | **10** |
| Guardián anciano | **8** |
| Piglin bruto | **8** |
| Guardián | **4** |
| Vindicador | **4** |
| Zoglin | **4** |

Se añaden por `EntityAttributeModificationEvent` (`MobBalanceEvents`), sumadas a la base 0 que tenían.

### 1.7 Drops cotidianos deterministas (1.18.0)

Regla P12/P13: el recurso base de un mob común no depende de RNG de granja. Tablas del pack en
`TheOptimizer_AdventureLoot`:

| Mob | Drop garantizado | Extra por Saqueo |
|---|---|---|
| Esqueleto del Wither | carbón **1-2** + cráneo al **15 %** | +5 % de cráneo por nivel |
| Blaze | **1-2** varas | +0-1 |
| Creeper | **1-2** pólvora | +0-1 |
| Enderman | **1** perla | +0-1 |
| Shulker | **1** caparazón | — |

### 1.8 Cofre del End (1.18.0)

- **Receta**: 8 obsidiana + **Estrella del Nether** en el centro (antes ojo de ender).
- **Restricción**: rechaza armas, herramientas, armaduras, escudos, tridentes, arcos/ballestas y cajas de
  shulker. Solo admite materiales, recursos y consumibles. Se aplica en `Slot.mayPlace`, así que cubre clic,
  shift-clic y arrastre.
- **Tooltip**: muestra la restricción (Invariante 5).


### 1.9 Identidades tácticas: familias de mobs y counters (1.19.0)

Todo se resuelve en eventos de daño/teletransporte: cero Goals y cero escaneos por tick.

| Familia | Mecánica del mob | Counter | Constantes |
|---|---|---|---|
| **Arañas** | 25 % de esquiva parcial (daño ×0.5 + salto lateral) contra armas que no sean de madera | **Madera**: ignora la esquiva y pega ×1.5 contra artrópodos | `SPIDER_DODGE_CHANCE=0.25`, `SPIDER_DODGE_REDUCTION=0.5` |
| **No-muertos** | Con 3+ zombis en 4 bloques, el golpe empuja +25 % y añade 1.5 de agotamiento | **Hierro** (área) y **Oro** (Castigo III) los limpian sin pagar ese coste | `HORDE_MIN_ZOMBIES=3`, `HORDE_RADIUS=4`, `HORDE_EXHAUSTION=1.5` |
| **Esqueletos y saqueadores** | Proyectil a más de 8 bloques aplica Lentitud I 1 s | **Cota de malla con 2+ piezas**: inmune | `SUPPRESSION_DISTANCE_SQ=64`, `SUPPRESSION_TICKS=20`, `CHAIN_IMMUNITY_PIECES=2` |
| **Enderman y Shulker** | Se teletransportan para huir | **Diamante**: anclaje dimensional 3 s; el teletransporte se cancela con partículas | `DIAMOND_ANCHOR_TICKS=60` |
| **Creeper, bruja y evocador/ilusionista** | Mecha, poción o conjuro en curso | **Piedra**: interrumpe la mecha (`setSwellDir(-1)`), corta la bebida y aplica stun al conjurador | `stone_stun_ticks=8` |


### 1.10 Lealtad del tridente: solo jugadores (1.19.1)

Los encantamientos innatos se calculan desde el ítem, no desde el portador. Eso hacía que un drowned
con tridente heredara **Lealtad III** y sus lanzamientos volvieran en bucle (decenas de tridentes
girando a su alrededor). `ThrownTridentMixin` corta el retorno cuando el dueño no es un jugador
(`m_37594_` + comprobación de `m_19749_`). El jugador conserva su Lealtad III.


### 1.11 Equipo de spawn: se va con el mob (1.20.0)

El equipo con el que un mob aparece (dificultad local, spawns aleatorios, invocaciones de nigromante o
del evocador de Iron's) **no se dropea**. `SpawnedGearRule` marca cada pieza al entrar al mundo con
`AmpereSpawnGear` y `LivingDropsEvent` descarta las gotas marcadas.

| Caso | ¿Dropea? |
|---|---|
| Armadura/arma generada por el juego al spawnear | **No** |
| Equipo de invocaciones (nigromante, evocador de Iron's) | **No** |
| Equipo que el jugador entrega o el mob recoge del suelo | **Sí** (sin marca) |
| Estandarte de capitán (raid) | **Sí** (excluido: objeto único) |
| Objeto con nombre personalizado | **Sí** (excluido) |

Motivo (P12/P13): el equipo generado es gratis; si cae, cualquier spawn se convierte en granja de
armas y tridentes. El equipo del jugador sí vuelve para no perder objetos propios.


### 1.12 Muela de afilar: solo se extraen los 3 looteables (1.20.1)

La muela convierte un encantamiento **looteable** en su libro de nivel 1. Nunca extrae encantamientos
innatos del material (Toque de Seda, Fortuna, Castigo, Lealtad, Empuje, Filo Arrasador…): esos son la
identidad del tier, no conocimiento extraíble.

| Objeto en la muela | Resultado |
|---|---|
| Herramienta con Irrompibilidad/Botín/Eficiencia real | Libro de nivel 1 de ese encantamiento |
| Herramienta solo con innatos (pico de diamante, espada de oro, tridente) | **Nada**: sin libro y sin coste |
| Objeto sin encantamientos | Reparación normal de la muela |

Consecuencia: no se pueden fabricar libros de Fortuna, Seda, Castigo o Lealtad con una muela; esos
efectos siguen viviendo en el material. Además desaparece el coste de XP que la muela cobraba por
los innatos.

### 1.13 Agotamiento por movimiento ÷5 y regeneración única (1.21.0)

`MovementExhaustionMixin` aplica `movement_exhaustion_factor = 0.2` **solo** en `jumpFromGround` y
`checkMovementStatistics`. El resto de fuentes conserva su valor nominal.

| Fuente | Antes | Ahora |
|---|---:|---:|
| Correr | 0.1 / m | **0.02 / m** (200 m por saturación) |
| Caminar / nadar | 0.01 / m | **0.002 / m** |
| Salto normal | 0.05 | **0.01** |
| Salto corriendo | 0.2 | **0.04** |
| Atacar | 0.1 | 0.1 (intacto) |
| Daño recibido | según tipo | intacto |
| Escudo de hambre | 2.0 por daño absorbido | **intacto** |
| Sets pesados al golpear | 0.5/0.6 + 0.03×daño | **intacto** |
| Regeneración natural vanilla | 6.0 por medio corazón | **cancelada** |
| Curación de Ampere | 2.0 por HP cada 40 ticks | **única regeneración pasiva** |

`FoodDataMixin` ya cancelaba `FoodData.tick` para implementar la curación constante; eso deja fuera la
regen rápida vanilla de 6.0. La reducción de movimiento no toca ese camino.


### 1.14 Durabilidad unificada y escala de herramientas (1.22.0)

**Armaduras del bloque de 15** (cuero, cota, oro, hierro): misma durabilidad por pieza que el hierro.

| Pieza | Cuero | Cota | Oro | Hierro | Total set |
|---|---:|---:|---:|---:|---:|
| Casco | 165 | 165 | 165 | 165 |
| Peto | 240 | 240 | 240 | 240 |
| Grebas | 225 | 225 | 225 | 225 |
| Botas | 195 | 195 | 195 | 195 |
| **Set** | **825** | **825** | **825** | **825** | 825 |

Diamante y netherita conservan su durabilidad de élite (casco 363/407, peto 528/592, grebas 495/555,
botas 429/481) y su reparación al 25 %.

**Herramientas y armas**: escala 80 → 160 → 300, con diamante y netherita intactos.

| Tier | Antes | Ahora |
|---|---:|---:|
| Madera | 59 | **80** |
| Piedra | 131 | **160** |
| Hierro | 250 | **300** |
| Oro | 250 | **300** |
| Diamante | 1561 | 1561 |
| Netherita | 2031 | 2031 |

Reparación sin cambios: 100 % para madera/piedra/cuero/cota/oro/hierro y 25 % para diamante/netherita.
La pérdida del 10 % al morir se aplica sobre estos valores.

### 1.15 Reasignación de pasivas y cobre fijo (1.23.0)

| Material | Herramientas (DiggerItem completo) | Armas |
|---|---|---|
| **Madera** | Hojas sin desgaste · **10 % de abono** al romper vegetales | ×1.5 artrópodos · **empuje +0.5** · vel 1.95 |
| **Piedra** | +15 % menas, piedra y pizarra | Aturdimiento 0.4 s · empuje +1.0 · **vel 1.4** |
| **Hierro** | **Toque de Seda** innato | Barrido 75 % · alcance +0.5 · vel 1.6 |
| **Oro** | **Auto-Fundición** + Suerte +1 · durabilidad **160** | Castigo III · **vel 2.0** (daño 5) |
| **Diamante** | **Área 3×3** (coste 1 + 4 de durabilidad) · alcance +1.0 | Crítico 15 % ×1.5 · anclaje 3 s · vel 1.6 |
| **Netherita** | **Fortuna III** · alcance +1.0 | Lentitud II · +15 % vs blindados · **vel 1.5** |

**Reglas del área 3×3:** el plano se calcula con la mirada del jugador; solo rompe periféricos con
`0 < dureza <= dureza central`; **excluye** bloques del tag `minecraft:needs_diamond_tool`; no daña la
herramienta por cada bloque, aplica `hurtAndBreak(4)` agrupado (+1 del central = **5 por uso**).

**Alcance del código:** todas las pasivas de recolección se aplican a `DiggerItem` (pico, pala, hacha y
azada), no solo al pico.

**Cobre:** `copper_ore` y `deepslate_copper_ore` sueltan **1 crudo fijo** (antes 2–5), con `apply_bonus`
de Fortuna y `explosion_decay`. El registro de loot pasa a **27 entradas**.
## 2. Backlog con criterio de aceptación

### T1. Rediseño de herramientas y armas (**hecho en 1.10.0 y 1.11.0**)
Quitar de herramientas la velocidad de movimiento y de armas la guardia de armadura; dar
identidad de recolección (madera +25 % madera/hojas/cultivos; piedra +15 % piedra y menas;
hierro alcance; oro suerte; diamante toque de seda + ×2 pizarra/obsidiana; netherita botín +
×2 escombros) y de combate (piedra aturdimiento 0.4 s; diamante 15 % crítico; hierro barrido
100 % + alcance; oro no-muertos ×2.5; netherita lentitud/rompe escudos + 15 % vs armadura).
**Aceptación**: ninguna herramienta altera movimiento ni armadura; cada tier tiene una línea
propia en el tooltip.

### A1. Familias de armaduras huérfanas (~32 piezas)
Inventario: `irons_spellbooks` 52 (cubiertas), `alexscaves` 13, `cataclysm` 12 (cubiertas las
de linaje), `create` 8, `alexsmobs` 8, `alexs_caves_spellbooks` 7 (cubiertas), `alshanex_familiars`
5, `kaleidoscope_cookery` 2; `geckolib` 8 son de mascota.
Familias propuestas: **Profundidad** (diving: aire + velocidad acuática, −velocidad en tierra),
**Supervivencia** (hazmat: radiación/ácido, armadura baja), **Ligero** (rainbounce, roadrunner,
emú, farmer, cardboard: movilidad/sigilo, sin defensa), **Ancestral** (bone reptile, sturdy
boots: anti-empuje).
**Aceptación**: cada familia tiene coste visible y no repite el eje de otra.

### N1. Núcleos de Rol
Transfiere el bonus de un set a otra armadura al 50 % y consume el set original. Requiere
ítems nuevos (registro + texturas + recetas).
**Aceptación**: se puede llevar diamante con rol de explorador sin que el set original siga
siendo mejor.

### J1. Jefes multifase
Rotación físico → mágico → fuego por umbrales de vida para que ningún set sea la respuesta
universal. **No implementar sin sesión de prueba**: rompe el endgame si falla.

### D1. Decisiones tomadas el 2026-11-10 (pendientes de ejecutar)

| ID | Decisión | Estado |
|---|---|---|
| D1.1 | **Quitar `goblintraders`** del pack: sin encantamientos su comercio no aporta | **hecho en 1.4.0** |
| D1.2 | Reparación simple de arco, ballesta, escudo, caña y tijeras al 100 % | **hecho en 1.3.0** |
| D1.3 | Tridente y elytra con tradeoff propio | **hecho: tridente 1.4.0, elytra 1.5.0** |
| D1.4 | **Eliminar la XP** del pack | **hecho en 1.8.0** (yunque 1.7.0, MiningXP retirado, orbes apagados) |
| D1.5 | Rol del beacon | **hecho en 1.6.0**: área de paz (radio 30, todo el eje Y) + escudo de hambre dentro del área |
| D1.6 | Alquimia/pociones como eje de soporte | diseñar |

### S1. Sueltas
`bone_reptile_*`, `sturdy_boots` sin rol. `bard_*` pendiente de confirmar si dan `spell_power`
antes de entrar al rol mago.

## 3. Trampas conocidas

1. `MixinConfigs` solo en `mods.toml` **no registra** el mixin en Forge 47.4.28: debe ir en
   `META-INF/MANIFEST.MF` (nos pasó con MobBalance).
2. `refmap` declarado sin archivo en `*.mixins.json`: quitar la clave.
3. Herencia por `ArmorMaterial` se rompe con materiales custom (Cataclysm, Irons): usar
   `ItemStack` + namespace/path.
4. Sustituir rangos de líneas en `EquipmentEvents.java` se comió
   `cleanInjectedAttributeTooltips`: compilar siempre tras editar.
5. SRG: `ItemStack.getDamageValue()` es `m_41773_` (no `m_41775_`).
6. `probar.py` puede pasar con el jar viejo si el build falló antes: revisar `Empaquetando`.
7. El generador de equipamiento **no normaliza timestamps** del zip: el hash del jar cambia
   en cada build aunque el código no (el de MobBalance sí lo normaliza).
8. `instalar.py` reescribía la config con 17 claves y borraba ajustes: corregido con merge.
   Si reaparece, revisar `default_cfg` y la fusión.

## 4. Procedimiento de publicación

1. Editar fuentes en `C:\Users\Metabodiru\Desktop\TheOptimizerMods\balance_equipamiento`.
2. Desde TheOptimizerMods: `python scripts/compile_quiet.py`, luego `python -m balance_equipamiento.instalar`.
3. `python -m balance_equipamiento.probar` → `VERIFICACION EXITOSA` sobre el artefacto recién desplegado.
4. Actualizar estado.json, AGENTS.md y changelog.md; `version.txt` = primeros 8 caracteres de MD5(changelog.md).
5. En AmpereRepo: `packwiz refresh`, luego `.\verificar_estado.ps1`. Los cambios sin commit y Pages sin publicar son esperables mientras se prueba localmente; no ocultarlos como checks OK.
6. En esta sesión 1.23.0: dejar cambios locales y **no hacer git push** hasta la prueba en juego del usuario.
7. El instalador despliega al servidor y AmpereRepo; no recrear la instancia eliminada de PrismLauncher. Las bibliotecas/JDK de Prism conservadas se usan solo para compilar/verificar.

## 5. Por qué estas reglas (para no re-litigarlas)

- **P3 (XP sin función)**: si la XP no compra nada, ningún sistema nuevo debe cobrar XP.
- **P6 (velocidad unificada)**: evita que el tier alto acelere la recolección y convierta la
  progresión vertical en "minar más rápido".
- **P2 (coste explícito)**: sin coste, el set más fuerte siempre gana y la horizontal muere.
  El agotamiento es la moneda natural porque la curación constante ya lo consume.
- **P10 (Iron's looteable)**: en vanilla las tintas se farmean con granjas; el pack inyecta
  tintas y materiales en cofres para que explorar sea la vía.
## 6. Juego tradicional vs jugador técnico

El objetivo del pack **no es prohibir** granjas ni redstone: es que **jugar sea la vía óptima** y que
la optimización técnica deje de dar una ventaja que rompa la progresión. Las mecánicas se diseñan
para que la máquina sea peor, no para que sea imposible.

**Prueba de diseño (antes de proponer cualquier mecánica):**

1. ¿La forma más eficiente de conseguir X es jugar (explorar, pelear, construir) o dejar una máquina?
2. ¿Un jugador técnico con 200 horas de optimización obtiene una ventaja que rompe la progresión?
3. ¿La mecánica se puede resolver AFK?

Si la respuesta lleva a máquina, optimización extrema o AFK, la propuesta se rediseña.

**Lo que ya desincentiva al técnico:**

- La XP no vale nada y no hay orbes: las granjas de XP y los spawners de XP pierden su razón.
- Mending fuera: no hay reparación infinita; el equipo se mantiene con materiales (100 % baratos, 25 % caros).
- Tintas y materiales mágicos por cofre: explorar rinde más que una granja de mobs.
- Beacon que pacifica su área: menos presión para iluminar/farmear el perímetro de la base.
- La comida como recurso de combate (escudo de hambre) y el agotamiento de los sets pesados: el AFK no cura.
- Elytra consumible y con coste: el transporte infinito deja de existir.

**Candidatos pendientes de revisar con el mismo criterio:** spawners de un solo uso, granjas de hierro
y de raids (tótems), chunk loading, duplicación de cualquier tipo.

