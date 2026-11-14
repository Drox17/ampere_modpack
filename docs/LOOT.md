# Botín determinista local — AdventureLoot 1.5.0 / EquipmentBalance 1.24.7

Revisión 2026-11-14, desplegada localmente; sin commit, push ni publicación. Las probabilidades descritas en auditorías históricas ya no representan los cofres cubiertos.

## Contrato y cobertura

- [Matriz por tabla y cantidad](LOOT_DETERMINISTA_MATRIZ.md): 194 tablas, 147 con premios y 47 auxiliares desactivados.
- [Auditoría, diseño y límites](LOOT_DETERMINISTA_AUDITORIA.md).
- Contrato fuente: `TheOptimizerMods/botin_magia_aventura/matriz_determinista.json`.
- Snapshot anterior: `TheOptimizerMods/botin_magia_aventura/audit_determinismo_antes.json` (no regenerar como si fuera el estado anterior tras instalar).
- 434 archivos de AdventureLoot (433 JSON); 440 hashes en `loot.json`, incluidos los siete de LootFixes.

Cada recompensa usa una pool con una entrada, una tirada, bonus_rolls=0, cantidad entera fija y como única función opcional `set_nbt` explícito. No quedan condiciones aleatorias, referencias anidadas ni funciones de generación aleatoria dentro del contrato. Los 13 accesorios antes anidados se distribuyen entre cofres hostiles específicos; no se borra la tabla compartida que también usa Iron's en muertes de entidades.

Los cofres de aldeas no dan magia; despensas y barriles quedan en R0/R1. Agua y botellas vacías salen. Minas dan raíles/carbón; mar prismarina/algas; bibliotecas papel/libros; desierto terracota y pepitas; criptas huesos/pólvora; Nether oro/verruga y polvo de blaze; End chorus/perla. La matriz enumera cada coleccionable, equipo modded permitido y pergamino fijo. El pergamino almacena hechizo y nivel 1 en NBT nativo de Iron's; no llama a randomize_spell. En cofres altos se elimina la épica anteriormente garantizada en cada apertura: tintas poco comunes y raras de tesoro sostienen el caldero 3:1.

## Invariantes

Cero equipo vanilla salvo élitros en `lootr:chests/elytra`. Cero lingotes/gemas/bloques minerales salvo carbón/carbón vegetal; recompensas en pepitas válidas. Máximo un libro vanilla nivel I permitido por cofre. Cero XP, tinta legendaria, catalizadores de jefe o pergaminos legendarios. Sin cambios a las recetas del caldero, Nuggets For All, Create/AE2, drops de mobs/jefes y bloques. `LootTableMixin` sigue activo; `EquipmentPolicy.sanitizeChestLoot` usa 3 pepitas fijas para un bloque de respaldo.

## Compatibilidad

Las tablas base contienen el presupuesto completo. El registro Forge propio mantiene replace=false con entries vacío. Los modificadores de cofres nativos/de perfiles se desactivan individualmente con `forge:loot_table_id=theoptimizer:disabled`, incluidos Kaleidoscope Cookery y Nether. No se desactivan modificadores de pesca, mobs ni bloques. Se mantiene Lootr individual sin refresco; no se inspecciona ni se abre el mundo existente para probar. La matriz no acredita victoria por abrir una cámara final: siguen siendo posibles rutas de saqueo evitando enemigos.

Exclusiones comprobadas: `ae2:blocks/chests/meteorite` es drop de bloque; `magic_items/great_ink` y `reward_ink` están compartidas con entidades. Se preservan estas tres raíces y se eliminan sus referencias desde cofres. Arqueología y pesca fuera de alcance. Tablas auxiliares trial_chambers presentes en el JAR no prueban generación de estructuras 1.21 en 1.20.1.

## Pruebas reproducibles

Desde TheOptimizerMods: `python -B scripts/compile_quiet.py`, `python -B -m botin_magia_aventura.probar`, `python -B -m balance_equipamiento.probar`.

Resultado botín: 1.833 checks estructurales/regresión, 208 recursos no-cofre idénticos y 29.006 comprobaciones de ejecución Forge (194 tablas × 32 semillas, suerte -5/0/+5, NBT, gestor efectivo y segunda sanitización). Total 30.839; variación de contenido final cero. Equipo: 2.062 JVM con 409 verificaciones de compatibilidad externa y 97 firmas/descriptores Mixin.

El runner crea una copia temporal del servidor, mundo plano nuevo, puerto local efímero y mods reales. Nunca usa el mundo ampere. El log y la prueba JSON quedan en `TheOptimizerMods/datos/reparaciones/botin_determinista/`. La creación de chunks del mundo temporal no valida interacción de un cliente ni todas las variantes de estructuras. Comprobar manualmente un cofre nuevo por familia y Lootr multijugador; los cofres ya materializados no se regeneran.
