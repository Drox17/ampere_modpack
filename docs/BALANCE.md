# BALANCE.md — memoria profunda del sistema de sets

## Revisión local 1.24.8 / AdventureLoot 1.6.0 (2026-11-14, sin publicar)

[Segunda iteración y evidencias](LOOT_SEGUNDA_ITERACION.md): destruir un generador mediante minería legítima entrega un fragmento; cuatro fabrican el catalizador arcano, alternativa al catalizador de jefe en 750 mB épica → 250 mB legendaria. Libros 61→18 tablas; aleación 79 ubicaciones con 4/6/8, excepciones conservadoras. 194 tablas, 131 claves sin cambios, 31.075 pruebas de botín y 2.062 de equipo. Integración de transportes y cliente pendiente. Las secciones inferiores conservan el historial anterior.

## Revisión local 1.24.7 / AdventureLoot 1.5.0 (2026-11-14, sin publicar)

El contrato vigente de cofres es determinista: ver [matriz completa](LOOT_DETERMINISTA_MATRIZ.md), [auditoría](LOOT_DETERMINISTA_AUDITORIA.md) y [LOOT.md](LOOT.md). Sustituye los pesos, rangos y probabilidades históricos de cofres descritos debajo. Los cambios locales de equipo anteriores a esta misión se conservan: esta revisión Java solo hace fija la conversión defensiva de bloques a pepitas. No modifica drops de jefes, entidades, pesca, arqueología ni recetas. 194 tablas con contenido independiente de semilla y suerte; 131 claves actuales de configuración (ninguna añadida aquí).


> Se lee **solo al diseñar** (cambiar reglas, añadir sets, revisar números). Para `/sync`
> usa `verificar_estado.ps1` + `estado.json`. Este archivo explica el porqué y el backlog.

## Referencia histórica: EquipmentBalance 1.24.2 (sanitización de cofres 1.24.6 / AdventureLoot 1.4.0)

Esta revisión prevalece sobre los registros históricos 1.23.x/1.24.0/1.24.1 de abajo. No cambia la paridad 16/10/12 ni Coloso/Enjambre. Conserva la instantánea del equipo vestido y el HUD sin clases sintéticas Args. La política vigente de cofres, pepitas (`Nuggets For All`) y límites mágicos está en las secciones `1.24.5` y `1.24.6` al final y en [docs/LOOT.md](LOOT.md).

| Arquetipo | Recolección | Combate y coste |
|---|---|---|
| Explorador: cuero/madera | hojas por tag sin desgaste; madera/cultivos +25%; vegetación 10% polvo de hueso | madera ×2 a artrópodos; baja durabilidad 80. Cuero completo da proyectil +30%, carga de ballesta ×2 y perforación de un objetivo extra; no aporta Coloso |
| Espeleólogo: malla/piedra | +20% en piedra/menas; cantera común sin desgaste; las menas sí consumen | control por piedra: sin penalización de velocidad en espada; cancela la preparación del conjuro y su señal, no solo el uso de ítems. Reserva 160 fuera de cantera |
| Constructor/infantería: hierro | área 3 por 3 por defecto, agachado un bloque; medio desgaste; ≥2 armaduras +0.5 alcance de bloques | hacha desactiva escudo 5 s; si esprinta, daño +15%. Cada activación cuesta 1 agotamiento y 1 durabilidad fija extra; no se divide por la pasiva de hierro |
| Alquimista/diplomático: oro | autofundición, suerte, reparación 100%; azada de daño 1 | único material que da tregua de piglins. Bonus directo a no-muertos: nivel configurado por 2.5 de daño; completa, sin duplicar, el bono ya presente en NBT real. Durabilidad 160 |
| Cazador: diamante | extracción intacta y doble velocidad en pizarra/obsidiana | conserva críticos y alcance; pierde 15% del daño ofensivo contra armadura ≥8. Reparación 25% |
| Conquistador: netherita | más recursos y doble velocidad en escombros | +15% contra objetivos con armadura; no ralentiza ni da tregua. Reparación 50% por lingote. Material netherita (incluido Monstrous) admite fragmento al 15%; Ignitium/Cursium mantienen sus materiales al 50% |

La cantera gratuita reconoce solo minecraft:stone, cobblestone, deepslate, cobbled_deepslate, tuff, andesite, diorite, granite y netherrack. No añade recompensas automáticas ni reglas que cancelen construcción/redstone. El desgaste de hojas usa #minecraft:leaves para picos, hachas, palas, azadas, espadas y tijeras. LeafDurabilityMixin envuelve la llamada virtual desde ItemStack.m_41686_ a Item.m_6813_; MiningDurability mantiene un ámbito por stack y try/finally. El ItemStackMixin anula solo el desgaste dentro del ámbito: no omite el minado ni los overrides.

El agotamiento cinético requiere entidad/proyectil y excluye caída, magia ambiental, fuego y marchitamiento. STARVE, señales de hambre y curación conservan su comportamiento previo. El rompeguardias se resuelve en LivingAttackEvent, antes del bloqueo; su multiplicador de daño se consume en el LivingHurtEvent del mismo DamageSource. Se aplica recarga al escudo y se impide reiniciarlo durante esa ventana. Las reglas numéricas compartidas están en EquipmentCombatRules.

Se eliminan afirmaciones de materiales y armaduras externas, AE2 y pico de acero negro, y el borrado por coincidencias textuales del anillo. Solo quedan decoración de mesa, amatista, contraataque propio del peto rocoso y restricción de cofre del End. El filtro inspecciona el stack y capacidades de inventario; reconoce cañas, tijeras, bundles y almacenamiento de bloques. Las capacidades temporales del bloque de prueba se invalidan y el resultado se cachea de forma sincronizada.

Reparación: madera admite el ingrediente de tablones vanilla y piedra el de materiales vanilla (adoquín/pizarra empedrada (cobbled_deepslate)/piedra negra); ambos restauran 100%. Cero en la política significa fallback, nunca se muestra como 0% ni se inventa 25% para tridentes. Los ítems especiales tienen tarjetas. El retorno del tridente depende de que no lleve impulso acuático. Tortuga se cuenta como 1/1; la pasiva de almas solo se anuncia en botas vanilla de netherita. Sinergia de cuero y alcance de hierro muestran su valor actual, incluido cero si no se cumplen las piezas.

Validación: 1506 comprobaciones JVM (70 armadura, 667 hambre, 44 HUD, 513 tarjetas y 212 armonización), además de contratos de firmas/bytecode reales. Las pruebas de minado ejecutan el Redirect y el ModifyVariable de producción con dobles aislados, incluidos overrides de DiggerItem/SwordItem, ámbitos anidados/errores y hojas de mods por tag. No equivalen a un arranque completo de Forge: sigue pendiente la prueba visual y de combate en juego. Configuración: 104 claves en Java/default_cfg/pack/servidor/instancia/estado.

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

### 1.2.1 Aviso continuo de hambre (EquipmentBalance 1.23.2)

Se sustituye el aviso puntual 8→7. Con `low_hunger_warning_food = 6` o menos, el HUD usa los sprites vanilla de `MobEffects.HUNGER` de `icons.png`, sin aplicar el efecto. El fondo U=16 pasa a U=133, el icono lleno U=52 a U=88 y el medio U=61 a U=97 (V=27, tamaño 9×9). Si el efecto real ya seleccionó esos sprites, no se desplazan otra vez.

El desplazamiento vertical conserva el rango vanilla de −1 a +1 píxel, cada `low_hunger_jitter_interval_ticks = 4`. Al llegar a `low_hunger_critical_food = 2`, `low_hunger_critical_interval_multiplier = 0.5` acorta la cadencia a 2 ticks. El offset se calcula por tick y posición del icono; permanece estable entre frames, incluso con saturación positiva. Al superar el umbral se conserva íntegro el render vanilla.

Forge 47.4.28 utiliza `ForgeGui.renderFood(int,int,GuiGraphics)`, no `Gui` para este overlay. `ForgeGuiMixin` captura la base `height - rightHeight` antes del incremento nativo y intercepta con `@Redirect` los tres blits existentes y los remite a un adaptador con parámetros nativos, que dibuja exactamente una vez por llamada. Conserva el orden de render, `rightHeight`, el perfilador y la pila/estado de render. `GuiMixin` mantiene oculta la XP y adapta únicamente los sprites de comida del método vanilla `m_280173_` como fallback. Ninguna ruta cancela ni reemplaza el render completo.

`LocalPlayerMixin` ejecuta el temporizador en `m_8119_` (tick), con el sonido nativo `SNIFFER_IDLE`, volumen `low_hunger_growl_volume = 0.20` y tono `low_hunger_growl_pitch = 0.55`. Se repite cada `low_hunger_growl_interval_ticks = 160` ticks mientras haya 1–6 puntos; a 1–2, cada 80. El temporizador se reinicia al superar el umbral, llegar a cero, cambiar de mundo/jugador, morir, entrar en creativo/espectador o desactivar el aviso. No depende de FPS ni de la activación del escudo de hambre. `low_hunger_warning` permite desactivarlo.

STARVE conserva exactamente el handler, el tipo de sonido y la cancelación de animación de 1.23.0. El nuevo gruñido no suena a cero. Ningún aviso modifica FoodData, agotamiento, esprint ni efectos de poción.

Todos los umbrales nuevos viven en EquipmentConfig y default_cfg, con paridad exacta de 90 claves; se retiran las cuatro claves del aviso anterior y tres declaraciones obsoletas del rechazo de Wither que no tenían consumidores ni formaban parte de la configuración distribuida. Verificación: 781 comprobaciones JVM (70 de armaduras, 667 de hambre y 44 de enlace/dibujo del HUD), 59 firmas de dependencias y contratos de targets de Gui/ForgeGui/LocalPlayer. La prueba del adaptador usa dobles mínimos de Minecraft y un classpath sin Mixin; esos dobles nunca se empaquetan en el mod. La inspección visual y sonora completa queda pendiente de la prueba en juego.

#### Corrección de arranque 1.23.2

El cliente 1.23.1 falló durante la inicialización con `NoClassDefFoundError: org.spongepowered.asm.synthetic.args.Args$1`. El debug.log mostró que Mixin generó esa clase para el descriptor del blit al aplicar nuestro GuiMixin; después Forge/ModLauncher no pudo resolverla. La traza de Create era una consecuencia de la carga del HUD, no evidencia para retirar Create u Oculus.

Se sustituyen `@ModifyArgs` y el parámetro `Args` de ambos adaptadores por `@Redirect` y parámetros nativos de GuiGraphics/ResourceLocation/primitivos. Las pruebas previas de reglas y firmas no cubrían este fallo del cargador; ahora se rechazan todas las referencias a Args o ModifyArgs del mod compilado y se prueba que el helper enlaza sin Mixin y conserva exactamente un blit. STARVE, el temporizador de gruñidos, las reglas visuales y EquipmentConfig conservan idéntico bytecode respecto a 1.23.1. Esto valida la corrección de la causa concreta; el arranque completo del pack requiere confirmación en cliente.

### 1.2.2 Orden y alineamiento de tooltips (EquipmentBalance 1.23.3)

Se corrige que `appendArmorRules` añadía viñetas antes del encabezado Ampere. Ahora se construye primero el bloque de rol, con su línea en blanco y encabezado, y después se añaden las reglas numéricas mediante `addLine`, con la misma sangría para todas las viñetas. Las piezas físicas externas normalizadas que no tienen rol específico reciben un encabezado genérico con el nombre traducido del ítem; no quedan estadísticas huérfanas pegadas a los atributos vanilla.

Los detalles largos de Monstrous y del linaje se dividen por tema. La reparación no se repite en el mismo bloque. Valores, clasificaciones, colores y atributos nativos se conservan. Compilación y suite de 781 comprobaciones verificadas; la geometría final depende de la fuente y escala del cliente y requiere inspección visual en juego.

### 1.2.3 Resumen y detalles con Shift (EquipmentBalance 1.24.0)

Las tarjetas de armaduras y herramientas muestran un resumen de beneficios y costes sin Shift. Mantener cualquiera de las dos teclas Shift sustituye ese resumen por cifras y condiciones; soltarla lo restaura. El coste no se oculta en la vista breve. Las botas de netherita pasan a cinco líneas, más encabezado y aviso de Shift; los atributos básicos de Minecraft se conservan.

El jugador lee segundos, corazones y muslitos: 30 ticks se presentan como 1,5 s y 10 puntos de daño como 5 corazones. El ejemplo de Coloso distingue el daño previo a otros efectos. El agotamiento se explica como comida equivalente consumida de la reserva, no como pérdida inmediata de iconos. Los datos salen de EquipmentConfig, ArmorBalanceRules y EquipmentValues; las constantes compartidas sustituyen literales equivalentes en la lógica, sin cambios de balance. Se corrige la documentación del cuero a su reducción real preexistente de 5/12/20/35 %.

Minecraft colorea en verde los valores base y en azul los modificadores positivos. Las filas nativas no tenían la misma sangría y Forge solo incluía nombres ingleses de alcance. TooltipComponents reconoce componentes y claves de atributos en vez de buscar texto o el formato decimal de +1: uniforma la sangría y preserva colores y anotaciones ajenas. Solo se omiten filas cuyo atributo pertenece íntegramente a TheOptimizer y ya está explicado en la tarjeta. Se añaden traducciones de alcance para es_mx y es_es. El evento se ejecuta solo en cliente y no añade Mixins ni altera el HUD.

Validación: compilación contra los JAR instalados y 1268 comprobaciones JVM (70 armaduras, 667 hambre, 44 HUD y 487 tooltips), incluidas ambas vistas, unidades, valores configurables, atributos ajenos, estilos y teclas Shift reales. EquipmentConfig/default_cfg conservan sus 90 claves. La inspección visual en el cliente queda pendiente.

### 1.2.4 Valores del equipo vestido (EquipmentBalance 1.24.1)

Corrige la vista Shift de 1.24.0: el contador mostraba las piezas vestidas pero las cifras eran una vista previa de cuatro piezas. Ahora EquipmentTooltips toma una instantánea de las ranuras de armadura, el atributo real de armadura, la luz local y EquipmentPolicy.colossalAbsorption. La pieza bajo el cursor nunca se añade al cálculo. El título incluye 0/4 si no se viste ninguna pieza correspondiente; sin jugador, se indica que no hay equipo actual disponible.

EquipmentTooltipCards recibe esa instantánea: cuero 3/4 muestra caída −20 % (4/4, −35 %), los roles ligeros usan sus escalas actuales, la suerte de oro requiere cuatro piezas y el coste de las túnicas suma solo las vestidas. El linaje mixto escala fuego/marchitamiento y firmeza; la inmunidad no se anuncia con piezas insuficientes. Coloso usa la combinación real de diamante/netherita, Ignitium y Monstrous; Cursium no aporta peso pesado. Los costes de ataque se componen multiplicativamente. La brecha muestra la armadura actual que quedaría al activarse; el coste por oscuridad responde a la luz presente.

El cálculo de agotamiento por impacto pasa a ArmorBalanceRules.impactExhaustion, compartido por evento y tarjeta con los mismos valores y orden de operaciones. La reparación sigue siendo una propiedad del objeto consultado. Se conserva la vista breve y no se cambia el balance. Suite: 1294 comprobaciones JVM (513 de tooltips), con regresiones para 0–4 piezas, la captura sin casco, conjuntos mixtos, luz, túnicas y ausencia de jugador. Configuración: 90 claves, sin cambios.

### 1.3 Herramientas: referencia actual

La referencia vigente es la tabla 1.24.2 al inicio y docs/EQUIPAMIENTO.md. No hay movimiento +7% de madera ni armadura +1 por empuñar hierro. La velocidad base de DiggerItem vanilla es 6.0; los nichos por bloque se aplican después. Las herramientas de netherita no ralentizan y el oro es el único diplomático con piglins.

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

**Nota de auditoría 2026-11-13:** el inventario siguiente es histórico. Alshanex Familiars y su parche de tags se retiraron localmente en el pack 1.24.3. El inventario por registro y los atributos efectivos actuales se documentan en `../reporte.md`; no se ha cambiado el balance de los equipables.
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
6. Publicar solo cuando esté autorizado. La sesión 1.23.1 autoriza explícitamente commit y git push en AmpereRepo y TheOptimizerMods después de completar la verificación; sustituye la espera de publicación de 1.23.0.
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



## Compatibilidad externa — EquipmentBalance 1.24.3 (2026-11-13)

Se mantiene el balance vanilla de 1.24.2. ItemAttributeModifierEvent se procesa en LOWEST: se retiran todos los aportes físicos previos de Cataclysm antes de insertar Ampere. Ignitium aporta 2/5/6/3 (16), Cursium 2/4/4/2 (12), dureza cero y 0.0625 de resistencia al empuje por pieza de linaje. Bone Reptile y Bloom Stone son excepciones externas expresamente solicitadas: casco Bone 3, peto Bone 6, peto Bloom 6, sin dureza ni repulsión física residual. Las pasivas y atributos ajenos a esos tres se conservan.

Unbreakable Skull conserva armadura +1 y su inmunidad nativa al aturdimiento, pero no añade dureza. Se retira también la dureza del efecto temporal Monstrous, conservando sus otros modificadores y regeneración; así no reaparece mitigación oculta desde un efecto.

Emerald Stoneplate añade suerte solo en ranura ring. La cifra del tooltip procede de emerald_ring_luck; se sustituye la descripción nativa en su origen para evitar depender del orden de renderizado. Su coste visible es ocupar esa ranura de anillo. No se altera la supresión global de orbes. Las herramientas Fluix DiggerItem usan velocidad efectiva unificada cuando el bloque es adecuado, conservando su comportamiento lento en bloques inadecuados y sus otras propiedades. Rocky ya no recibe el golpe artificial ni niveles virtuales de reflejo de Ampere; permanecen las habilidades de Alex’s Mobs.

Las pasivas de combate se limitan a espadas/hachas, incluidos los cuchillos que sean SwordItem. Grave Key se excluye por ID incluso cuando su clase nativa hereda de SwordItem. No se cambian extracción o reparación vanilla para conseguir esta separación.

Claves nuevas, con paridad Java/instalador/pack/servidor/instancia: bone_reptile_armor_helmet=3, bone_reptile_armor_chest=6, bloom_stone_armor_chest=6, emerald_ring_luck=1.0. Total 108.

FamiliarsLib se retira tras comprobar que no quedan consumidores obligatorios. La publicación incluye la retirada anterior de Alshanex y FamiliarsTagFix. No se modifican las 27 tablas de loot registradas.

La suite incluye una JVM de Forge aislada con Cataclysm/Curios reales: comprueba orden del evento, eliminación de aportes duplicados, suma de armadura/dureza/repulsión, suerte y su tooltip, Fluix, clave de tumba, Rocky y regresión de las familias vanilla. Usa copias temporales; no abre el mundo real ni genera chunks. Las advertencias de anotaciones ausentes en classfiles de terceros se excluyen del lint de compilación; las advertencias de fuentes propias siguen siendo errores.

Alcance: esta versión implementa los ítems y reglas enumerados en la petición. H3 (otras familias físicas externas) y los poderes/costes nativos restantes de H6 no reciben un rediseño adicional; siguen documentados en el backlog. No se afirma haber armonizado todos los poderes de todos los mods.

Resultado de la suite 1.24.3: 1606 comprobaciones JVM, incluidas 100 de compatibilidad sobre Forge real, además de 59 descriptores/firmas de enlace contrastados con los JAR.

## Migración YUNG’s 1.24.4

Se retiran referencias activas a Alex’s Mobs/Caves, su extensión de Spellbooks y Caves Cookery. EquipmentBalance 1.24.4 conserva las reglas vanilla y excluye las compatibilidades eliminadas; MobBalance 1.5.1 ya no emite el tag de cocodrilos; WildlifeRepopulation 1.6.1 elimina exclusiones de biomas y entidades ausentes, sin alterar las constantes 55/45. Sus pruebas se alinean con ese balance vigente (antes conservaban expectativas de 1.4.0). Se eliminan rutas antiguas de despliegue bajo gestion de PrismLauncher.

AdventureLoot 1.2.0 preserva los overrides activos y usa fuentes JSON versionables, evitando regenerar desde el instalador antiguo que contenía botellas de XP. Cobertura, tasas, ausencias y hashes: docs/LOOT.md y loot.json. Sin publicación remota automática en esta operación.

## Botín y contención mágica — EquipmentBalance 1.24.5 / AdventureLoot 1.3.0 (2026-11-13)

Se integra la propuesta revisada de botín por perfiles de riesgo (`AdventureLoot 1.3.0`, `111` entradas en `loot.json`) junto con la horizontalización y contención mágica de `irons_spellbooks` (`EquipmentBalance 1.24.5`, `117` claves de config).

- **Armas cuerpo a cuerpo de `irons_spellbooks` (11 ítems en `EventPriority.LOWEST`):** purga modificadores previos de daño, velocidad y armadura e impone valores totales exactos (con base de jugador `1.0` daño y `4.0` velocidad), tarjeta de rol en español y reparación del `25%` por material a `0 XP`:
  - `amethyst_rapier` `5.5 / 2.1` (`amethyst_shard`), `misery` `6.0 / 1.8` (`weapon_parts`), `magehunter` `6.0 / 1.6` (conserva `+15%` resistencia mágica; `arcane_ingot`), `spellbreaker` `6.5 / 1.6` (conserva `+15%` reducción de enfriamiento; `diamond`), `keeper_flamberge` `6.5 / 1.3` (`0` armadura purgada; `cinder_essence`), `legionnaire_flamberge` `7.0 / 1.4` (`0` armadura purgada; `cinder_essence`), `claymore` `7.0 / 1.3` (`iron_ingot`), `decrepit_scythe` `7.0 / 1.4` (`blood_vial`), `hellrazor` `7.5 / 1.3` (`cinder_essence`), `twilight_gale` `7.5 / 1.3` (`weapon_parts`) y `boreal_blade` `7.5 / 1.1` (`icy_fang`).
- **Contención mágica por armadura física pesada:** las piezas `IRON`, `DIAMOND`, `NETHERITE` y `cataclysm:*` (excluyendo cuero, malla, oro, tortuga y túnicas de `irons_spellbooks`) duplican el coste de maná (`×2.0` / `+100%`) con `1–2` piezas vestidas (`SpellOnCastEvent`) y bloquean el lanzamiento con `3+` piezas (`SpellPreCastEvent`).
- **Anillos protectores elementales (`fireward_ring`, `frostward_ring`, `poisonward_ring`):** los Mixins (`ServerPlayerEventsMixin`, `FrostwardRingMixin`, `PoisonwardRingMixin`) desactivan las inmunidades totales; `LivingHurtEvent` aplica `-25%` de reducción elemental, `EquipmentCuriosEvents` aplica `-5%` de velocidad de ataque en ranura Curios `ring` y el tooltip expone ambos efectos y costes (`C5`).
- **Exclusividad legendaria y lista cerrada de jefes:** el caldero convierte tintas en proporción `3:1` (`750 mB → 250 mB`) exigiendo `#theoptimizer:boss_legendary_catalysts` para `legendary_ink`; todos los cofres y `RandomizeSpellFunctionMixin` mantienen `0%` tintas/pergaminos legendarios; `EquipmentEvents` otorga sin escalar por Botín y con participación de jugador activo `1 legendary_ink` (`ignis`, `the_leviathan`, `ender_guardian`, `maledictus`, `scylla`, `ender_dragon`, `wither`, `dead_king`) o `2 epic_ink` (`netherite_monstrosity`, `the_harbinger`, `ancient_remnant`).
- **Claves nuevas de config (9, total 117):** `normalize_irons_weapons`, `irons_weapon_repair_fraction`, `heavy_armor_spell_containment`, `heavy_armor_spell_mana_multiplier`, `heavy_armor_spell_block_pieces`, `nerf_ward_rings`, `ward_ring_damage_reduction`, `ward_ring_attack_speed_penalty`, `clamp_chest_scroll_rarity`.
- **Verificación:** `141` comprobaciones en `botin_magia_aventura.probar` y `1699` comprobaciones JVM en `balance_equipamiento.probar` (incluidas `182` reales sobre Forge/Cataclysm/Curios y `62` firmas Mixin). Sin commit ni push automático.

## Botín en pepitas, cero equipo vanilla y límite de encantamientos — EquipmentBalance 1.24.6 / AdventureLoot 1.4.0 (2026-11-13)

Sustituye los lingotes, diamantes y fragmentos enteros introducidos en `1.24.5` (`mat_f*`, `pkg_mat_*`) y sella todas las tablas de cofres del pack (`AdventureLoot 1.4.0`, `228` entradas en `loot.json`, + `EquipmentBalance 1.24.6`, `118` claves de config):

- **`Nuggets For All` (`nuggets_for_all-1.0.0-forge-1.20.1.jar`, proyecto `wMBsm3EI`):** añadido al repo packwiz, servidor e instancia. Como el JAR original empaquetaba recetas con formato 1.21 (`data/nuggets_for_all/recipe/*.json` con `"id"`), `AdventureLoot 1.4.0` genera las `16` recetas MC `1.20.1` correctas en `data/nuggets_for_all/recipes/*.json` (`"item"`, uniformizando también `lapisnuggetr` a `1 ↔ 9`).
- **Cero equipamiento vanilla en cofres:** elimina armas, herramientas, armaduras, arcos, ballestas, escudos, tridentes, cañas, tijeras, mecheros y armaduras de caballo de `minecraft:*` tanto en los JSON base de vanilla/mods como en ejecución (`LootTableMixin` -> `EquipmentPolicy.sanitizeChestLoot`); `minecraft:elytra` en `lootr:chests/elytra` queda preservada.
- **Máximo 1 encantamiento vanilla por cofre:** elimina entradas `enchanted_book`, `enchant_randomly` y `enchant_with_levels` de tablas base (solo `theoptimizer:chests/book_*` aporta ≤`1` libro nivel I de `unbreaking`/`looting`/`efficiency`); `LootTableMixin` recorta duplicados y despoja encantamientos vanilla de ítems no-libro. Además, `scroll_pouch.json` y `filler_storage_loot.json` quedan limitados a `quality.max = 0.65`.
- **Minerales en pepitas salvo carbón:** sustituye lingotes, bloques minerales, menas en bruto y gemas enteras por pepitas vanilla (`iron_nugget`, `gold_nugget`), `nuggets_for_all:*`, pepitas de Cataclysm o esencias de Iron's en todas las tablas y en ejecución (`coal`/`charcoal` intactos; `cmd_yung` recibe respaldo `2–5 diamondnugget`).
- **Clave nueva (`1`, total `118`):** `sanitize_chest_loot = true`.
- **Verificación:** `457` comprobaciones en `botin_magia_aventura.probar` y `1780` comprobaciones JVM en `balance_equipamiento.probar` (incluidas `263` reales sobre Forge/Cataclysm/Curios/Nuggets y `70` descriptores Mixin). Sin commit ni push automático.

## Acotamiento de Create + AE2 a construcción y logística (`1.24.6`)

Se ajusta **Create** para que funcione junto a **Applied Energistics 2** como motor de construcción y logística sin romper la economía de reparación ni el erradicado de XP (`P2`, `P3`, `P9`, `P12`, `P13`):

- **Retiro de `Create Repair`:** eliminado del modpack, servidor e instancia local para que toda reparación siga pasando por el yunque de Ampere (`P9`).
- **Cero hierro/oro AFK por lavado o rocas:** `splashing` de `gravel`, `red_sand` y `soul_sand` conserva pedernal, arcilla y cuarzo pero retira `iron_nugget` y `gold_nugget`; `crushing` de `crimsite`, `ochrum` y `tuff` (`y *_recycling`) queda en áridos/cobre/zinc sin hierro, oro ni `electrum_nugget`.
- **Cero `create:experience_nugget` y tope `1:1` en menas de equipo:** deshabilitadas las recetas de bloque de experiencia y armaduras de caballo en triturado; purgados `create:experience_nugget` de todas las recetas `create:crushing`; `iron_ore`, `gold_ore`, `diamond_ore`, `emerald_ore` (y variantes `deepslate_*`) topadas a `1` mineral sin bonos aleatorios, y `nether_gold_ore`/`gilded_blackstone` fijados en `9 gold_nugget`.
- **Puente Create ↔ AE2 y materiales de construcción (`theoptimizer:create_ae2/*`):** molido de `certus_quartz`/`fluix`, triturado de `sky_stone_block`, mezclado de `fluix_crystal`, prensado con `deploying` (`keepHeldItem: true`) de circuitos/silicio, y fabricación renovable de `tuff`, `calcite`, `crimsite`, `ochrum`, `veridium` y `asurine`.
- **Escalado de pepitas por riesgo, `create:andesite_alloy` variable y purga de `cobweb`/basura (`AdventureLoot 1.4.0`):**
  - Mezcla `(suministros, materiales/pepitas, temático)` escalada por riesgo manteniendo `P5` (solo pepitas, sin lingotes/gemas enteras): `R1` `15 %` (`75/15/10`), `R2/F2` `35 %` (`55/35/10`), `R3/F3` `50 %` (`40/50/10`) y `R4/F4` `65 %` (`25/65/10`), retirando `iron_nugget` de `pkg_thematic`.
  - Inyección de `create:andesite_alloy` variable y creciente por riesgo en `pkg_thematic` (`1–3`), `pkg_mat_r1` (`1–2`), `pkg_mat_r23` (`2–5`), `pkg_mat_r4` (`4–8`), `mat_f2` (`2–4`), `mat_f3` (`4–7`) y `mat_f4_*` (`6–10`).
  - Erradicación global de `minecraft:cobweb` en `sanitize_chest_table` sobre todas las tablas base de cofres/barriles/vasijas, override limpio de `irons_spellbooks:chests/filler_storage_loot` sin `cobweb` ni `rotten_flesh` (con suministros útiles y `1–3` `create:andesite_alloy`) e inclusión de `irons_spellbooks:chests/ice_spider_den/tower` en `r2_other`.
- **Verificación (`botin_magia_aventura.probar`):** `861` comprobaciones pasadas sobre `TheOptimizer_AdventureLoot.zip` (`410` entradas en `loot.json`).

## Pergaminos por riesgo, tintas mineras y catalizador de jefe (1.24.6 / AdventureLoot 1.4.0)

Se restringe la aparición de pergaminos y se alinea la economía de tintas entre exploración, minería y jefes:

- **Exclusividad y escalado de pergaminos (`irons_spellbooks:scroll`):** eliminados de todas las tablas base de cofres y de `magic_otros` / `magic_otros_nether`. Solo aparecen mediante los GLM `theoptimizer:scroll_tiers` en dungeons de YUNG’s (`better*`) y estructuras hostiles de Iron’s Spellbooks (tope de `4` hechizos por cofre en ejecución):
  - `scrolls_r1` (`R1`): `1` tirada (`empty 650`, común `320` / `32%`, inusual `30` / `3%`, `0%` raro/épico).
  - `scrolls_r23` (`R2/F2/R3`): `1–2` tiradas (`empty 450`, común `500` / `50%`, inusual `50` / `5%`, `0%` raro/épico).
  - `scrolls_high` (`F3/R4/F4`): `4` tiradas (`empty 25`, común `42%`, inusual `18%`, raro `5%`, épico `10%` por tirada → `0.01%` de obtener los `4` hechizos épicos).
  - **`RandomizeSpellFunctionMixin`:** impone en ejecución la rareza exacta por banda de calidad (`<=0.18` `COMMON`, `<=0.38` `UNCOMMON`, `<=0.52` `RARE`, `>0.52` `EPIC`) y veta `LEGENDARY` fuera de jefes cerrados. `EquipmentPolicy.sanitizeChestLoot` purga `minecraft:cobweb` y topa a `4` pergaminos por cofre.
- **Tintas por riesgo:** `R1/R2/F2/R3` solo sueltan `common_ink` con aparición rara de `uncommon_ink` (`0` raras/épicas); los perfiles de alto riesgo (`F3`, `R4`, `F4`) añaden un pool garantizado de `1× irons_spellbooks:epic_ink` más mayoría de `uncommon_ink`, `rare_ink` y `epic_ink`.
- **Catalizador de jefe y escalera minera en caldero:** registrado el ítem personalizado `theoptimizer_equipment:boss_catalyst` (*Catalizador Arcano de Jefe*, textura de `divine_soulshard` con brillo). Los `11` jefes cerrados lo sueltan (`1×`) además de su botín normal. El caldero alquímico mantiene la conversión `3:1` (`750 mB → 250 mB`) escalando con minería (`copper_ingot` → `uncommon_ink`, `iron_ingot` → `rare_ink`, `gold_ingot` → `epic_ink`) y exigiendo `#theoptimizer:boss_legendary_catalysts` (`theoptimizer_equipment:boss_catalyst`) para fabricar `legendary_ink`.
- **Verificación:** `1945` comprobaciones JVM en `balance_equipamiento.probar` (`296` sobre Forge/Cataclysm/Curios/Nuggets reales y `78` descriptores Mixin) y `875` comprobaciones en `botin_magia_aventura.probar` (`416` entradas registradas en `loot.json`).

## Sincronización integral de equipables de Cataclysm (1.24.6)

Se alinea todo el catálogo equipable de `L_Ender's Cataclysm` (`CataclysmBalance` + 6 `@Pseudo` Mixins) con la progresión horizontal, agotamiento, durabilidad finita y yunque `0 XP` de Ampere (`P1`–`P13`, `C1`–`C6`):

- **Armas cuerpo a cuerpo (18 ítems en `EventPriority.LOWEST`):** rango horizontal `6.0–8.0` daño total y `1.0–1.8` velocidad (`ceraunus` `8.0/1.0`, `soul_render` `8.0/1.1`, `brontes`/`infernal_forge`/`void_forge` `7.5/1.0`, `the_incinerator` `7.5/1.3`, `coral_bardiche` `7.5/1.1`, `astrape` `7.0/1.4`, `ancient_spear`/`gauntlet_*`/`the_annihilator`/`the_immolator` `6.5` en `1.4–1.6`, `meat_shredder` `6.0/1.7`, `tidal_claws` `6.0/1.8`, `coral_spear` `6.0/1.3`, `khopesh` `6.0/1.5`).
  - `gauntlet_of_guard`, `gauntlet_of_bulwark` y `gauntlet_of_maelstrom` pierden armadura/dureza/firmeza oculta en mano (`0`).
  - `the_annihilator` y `the_immolator` quedan topadas a `+15.0%` de `cataclysm:additional_critical_damage`.
- **Herramientas duales y `Black Steel`:** `DiggerItemMixin` y `CataclysmBalance.isCataclysmTool` unifican la velocidad de minado a `6.0F` (`unified_harvest_speed`) para `brontes`, `infernal_forge`, `void_forge` y `black_steel_*`.
- **Durabilidad finita real, reparación `0 XP` y desgaste/fatiga activa:**
  - `CataclysmDurabilityMixin` revierte `isDamageable(ItemStack) -> false` en `Cataclysm_Tool_Item`, `Brontes`, `Infernal_forge`, `Void_forge`, `Ignitium_Armor`, `Cursium_Armor` e `Ignitium_Elytra_ChestPlate`; `ItemMixin` fija topes finitos (`2031` armas de jefe, `840` `bulwark_of_the_flame`, `576` arcos/lanzadores de jefe, `384` reliquias activas `sandstorm_in_a_bottle`/`void_core`, `592` `ignitium_elytra_chestplate`).
  - `EquipmentEvents` aplica desgaste manual cuerpo a cuerpo (`m_41622_`) cuando las subclases de Cataclysm lo omiten, y `CataclysmArmorKeyMixin`, `CataclysmRightClickUseMixin`, `CataclysmForgeHammerMixin`, `CataclysmLeftClickMixin`, `LivingEntityMixin` (`releaseUsingItem`), `PlayerInteractEvent.RightClickItem` (`tidal_claws`) y `onUseItemTick` cobran agotamiento (`cataclysm_skill_exhaustion`) + desgaste (`cataclysm_skill_wear`).
  - `IgnitiumElytraMixin` cobra `1` de desgaste cada `20` ticks de vuelo; `esElytra` aplica `elytra_flight_exhaustion`; reparación exclusiva con `2x ignitium_ingot` = `25%` a `0 XP` (sin `phantom_membrane` ni `1` solo lingote). Todo el resto de equipables de jefe/sub-jefe repara `50%` por material temático a `0 XP` (incluido `bulwark_of_the_flame` con `ignitium_ingot` en lugar de tablones).
- **Curios y armaduras restantes (`C5`):**
  - `belt_of_beginner`, `belt_of_monstrosity` y `sturdy_boots`: `-5%` velocidad de movimiento (`MULTIPLY_TOTAL`).
  - `vitality_ankh`: `-5%` daño de ataque.
  - `blazing_grips`, `chitin_claw`, `ring_of_grudged`, `sticky_gloves` y `unbreakable_skull`: `-5%` velocidad de ataque (`unbreakable_skull` además sin dureza oculta).
  - `bone_reptile_helmet`, `bone_reptile_chestplate` y `bloom_stone_pauldrons`: `-4%` velocidad de ataque (`bone_reptile_attack_penalty`) + reparación temática a `0 XP`.
- **Tooltips (`C6`) y Config (`131` claves totales, `+12`):** `CataclysmBalance.appendTooltip` muestra rol, costes y material de reparación; añadidas `12` claves configurables en `EquipmentConfig`, `instalar.py` y JSONs.
- **Verificación:** `2062` comprobaciones JVM en `balance_equipamiento.probar` (incluidas `409` reales sobre Forge/Cataclysm/Curios y `97` descriptores Mixin).
