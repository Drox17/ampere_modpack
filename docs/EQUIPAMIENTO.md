# Equipamiento 1.24.2: arquetipos y mantenimiento

La configuración activa contiene 104 claves; los tooltips calculan desde las mismas constantes/config y desde el equipo realmente vestido. Sin Shift: resumen y costes. Con Shift: cifras en segundos, corazones y comida equivalente; no se simula equipar el objeto bajo el cursor.

## Armaduras

Orden: casco/peto/grebas/botas. Dureza cero también en atributos de ArmorItem externos.

| Familia | Armadura | Durabilidad | Reparación por unidad |
|---|---|---|---|
| Cuero, malla, hierro, oro | 2/5/6/3 = 16 | 165/240/225/195 | 100% |
| Diamante | 2/5/6/3 = 16 | 363/528/495/429 | 25% por diamante |
| Netherita | 2/5/6/3 = 16 | 407/592/555/481 | 50% por lingote, 15% por fragmento |
| Ignitium | 2/5/6/3 = 16 | conserva material externo | 50% por lingote de Ignitium |
| Cursium | 2/4/4/2 = 12 | conserva material externo | 50% por lingote de Cursium |
| Monstrous | casco 2 | 407 | 50% lingote netherita, 15% fragmento |
| Túnicas | 1/3/4/2 = 10 | conserva material externo | Netherite Mage 50%; otras familias, estándar |
| Tortuga | casco 2; contador 1/1 | 275 | estándar |

| Set | Ventajas | Costes |
|---|---|---|
| Cuero: explorador | caída −5/12/20/35%; completo: proyectil +30%, ballesta carga ×2 y perforación | no aporta Coloso |
| Malla: espeleólogo | proyectiles −5/10/18/30%; velocidad +4/8/12/16% | no aporta Coloso |
| Hierro: constructor/infantería | explosiones −4/8/15/25%; empuje −5/10/18/30%; dos piezas añaden alcance a bloques +0.5 | no aporta Coloso |
| Oro: alquimista | magia −4/8/15/25%; suerte +1 con cuatro piezas; tregua de piglins | no aporta Coloso |
| Diamante: cazador | Coloso proporcional, 50% del excedente sobre 5 corazones con cuatro piezas | ataque −15%, brecha, agotamiento de combate y reparación 25% |
| Netherita: conquistador | Coloso y linaje térmico progresivo | ataque −20%, brecha, agotamiento de combate, oscuridad y reparación 50% |

Linaje: fuego/marchitamiento −25% por pieza, inmunidad a cuatro; firmeza +6.25% por pieza. Con luz menor que 8 recibe daño extra proporcional, hasta +10%. Monstrous duplica Coloso combinado y cuesta movimiento −10% y ataque −30% por casco; Ignitium aporta medio Coloso y prende al atacante 3 s con recarga 2 s. Cursium no aporta Coloso, brecha, ataque lento ni agotamiento cinético. Túnicas pierden 5% de daño cuerpo a cuerpo por pieza. Solo botas vanilla de netherita reciben/anuncian velocidad sobre almas; el linaje no pacifica piglins.

## Herramientas y armas

| Material | Durabilidad | Recolección | Combate / coste |
|---|---:|---|---|
| Madera | 80 | madera/cultivos +25%, vegetación 10% polvo de hueso | daño ×2 a artrópodos; frágil fuera de especialidad |
| Piedra | 160 | piedra/menas +20%; cantera común sin desgaste | control e interrupción de mechas, bebidas y conjuros; espada sin −0.2 de ataque; otros bloques gastan durabilidad |
| Hierro | 300 | área 3×3, agachado 1×1; mitad del desgaste medio | alcance +0.5, espada con barrido; hacha rompe escudo 5 s, daño +15% si esprinta; cuesta 1 agotamiento y 1 durabilidad extra por activación |
| Oro | 160 | autofundición y suerte | bonus directo contra no-muertos 7.5 puntos con nivel configurado 3; único diplomático; azada daño 1; baja durabilidad |
| Diamante | 1561 | extracción intacta; pico ×2 pizarra/obsidiana | crítico 15% ×1.5; alcance +1; daño −15% contra armadura ≥8; reparación 25% |
| Netherita | 2031 | más recursos; pico ×2 escombros | daño +15% contra armadura y alcance +1; sin lentitud ni tregua; reparación 50%/15% |

La cantera exacta es stone, cobblestone, deepslate, cobbled_deepslate, tuff, andesite, diorite, granite y netherrack del namespace minecraft. No incluye menas ni roca de otro namespace. Las hojas del tag vanilla no desgastan DiggerItem, SwordItem ni tijeras. La velocidad base de los DiggerItem vanilla es 6.0; los bonus de nicho son posteriores.

Madera y piedra restauran 100% en yunque con sus ingredientes vanilla: tablones o materiales de piedra (adoquín, pizarra empedrada (cobbled_deepslate), piedra negra). Hierro/oro restauran 100%. Arco/ballesta/caña: cuerda; escudo: tablón de roble; tijeras: lingote, todos al 100%. Tridente y familias externas sin override dicen reparación estándar, nunca 0%. La pérdida por muerte se mantiene en 10%, sin romper.

## Ítems especiales y límites

Tridente: el cambio de daño por humedad es cuerpo a cuerpo; con impulso acuático no promete retorno. Arco y ballesta muestran la sinergia del cuero que se lleva actualmente. Escudo, caña y tijeras tienen resumen y Shift. Las tijeras tienen alcance a bloques +0.5 y medio desgaste, pero no 3×3.

El cofre del End rechaza equipo, cañas, tijeras, bundles/sacos, inventarios portátiles por capacidad y bloques de almacenamiento. Solo guarda materiales/recursos/consumibles compatibles. No se añaden afirmaciones sobre poderes de materiales de otros mods ni se borran sus líneas por texto.

## Validación

1506 comprobaciones JVM: 212 nuevas de armonización y las 1294 anteriores. Incluye minado con overrides reales de los adaptadores de producción, cero desgaste por tag, cantera limitada, agachado, daño de oro sin NBT, penalización de diamante, reparación sin centinelas visibles, retorno de tridente y especiales. Los targets se contrastan con los JAR instalados; no se introducen Args. Prueba completa en juego pendiente.
