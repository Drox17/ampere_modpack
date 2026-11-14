# Auditoría y contrato de botín determinista (local, 2026-11-14)

## Fase 1: evidencia antes de editar balance

`TheOptimizerMods/botin_magia_aventura/audit_determinismo_antes.json` conserva las definiciones, fuentes, hashes, modificadores, objetos y referencias examinados. Se descubrieron 197 raíces por tipo CHЕST o ruta, 205 tablas alcanzables y cero referencias ausentes. La clasificación anterior dejaba fuera tablas de YUNG's Extras y Kaleidoscope Cookery (`chest/`, singular). Los perfiles añadían RNG sobre tablas base también aleatorias. `randomize_spell`, anillos aleatorios y mapas/cartas podían introducir propiedades variables; `sanitizeChestLoot` sorteaba 3–6 pepitas de un bloque. Los documentos 1.24.4 ya no describían el estado real.

La raíz AE2 `blocks/chests/meteorite` es un drop de bloque, no un contenedor; `magic_items/great_ink` y `reward_ink` están compartidas con entidades. Se excluyen como objetivos directos para conservar drops de mobs/jefes. Las referencias de cofres se reemplazan por objetos fijos; no quedan llamadas desde cofres a esas tablas compartidas.

## Fases 2 y 3: contrato y revisión adversarial

La matriz completa está en `TheOptimizerMods/botin_magia_aventura/matriz_determinista.json`: por ID, perfil, tema, cantidades, NBT fijo, razón y sustituciones. Es la entrada de implementación; no una descripción reconstruida de la salida. Perfiles heredados revisados por función: despensas/barriles/vasijas bajan a R1, asentamientos a R0. F4 identifica una tabla de tesoro, no una victoria acreditada: no se presupone una protección contra abrirlo antes del jefe.

Cada recompensa ocupa una pool de una entrada, una tirada, cantidad entera fija y cero bonus por suerte. No hay referencias, elecciones, condiciones ni proveedores variables en tablas cubiertas. Los modificadores de cofres se desactivan individualmente; se preservan los de entidades, bloques y pesca y las recetas ajenas al alcance.

| Perfil | Premio fijo principal | Límite |
|---|---|---|
| R0 | 3 alimentos; oficio/tema modesto | Sin magia, anillos ni diamantes |
| R1 / despensa | 3 alimentos, 8 antorchas, 4 pepitas hierro, cuero y tema | Sin tintas; ni agua ni botellas vacías |
| R2 | 4 alimentos, 8 antorchas, 8 pepitas hierro, tema y 1 tinta común | Sin tintas raras/épicas |
| R3 | 4 alimentos, 12 antorchas, 10 pepitas hierro, tema y 1 poco común | Pergamino fijo solo estructuras YUNG/Iron's; nivel 1 |
| R4 | 4 alimentos, 12 antorchas, 12 pepitas hierro y 1 poco común | No épica garantizada en cada cofre |
| F2 | Base R2 + 1 pepita diamante | Un libro fijo donde proceda |
| F3 | Base R3 + 2 pepitas diamante + 1 tinta rara | Recompensa de tabla, sin afirmar finalización |
| F4 | Base R4 + 3 pepitas diamante + 1 rara + 1 runa | Nunca legendaria; caldero conserva utilidad |

La identidad añade mar (prismarina/algas), mina (raíles/carbón), biblioteca (papel/libros), desierto (terracota/pepitas esmeralda), hielo (hielo compacto/hilo), cripta (huesos/pólvora), combate (flechas/pólvora), Nether (oro/verruga y 2 polvos blaze; solo final añade 1 vara) y End (chorus/perla). Coleccionables y objetos especiales conservan funciones; equipos/curios nativos se redistribuyen por ID para evitar convertir alternativas aleatorias en un arsenal garantizado. La matriz enumera cada ubicación. Los objetos procedentes de funciones aleatorias se reemplazan por propiedades explícitas o por componentes útiles.

### Revisión de seis estilos

- Explorador: suministros garantizados; no hace falta perseguir una probabilidad diminuta.
- Combatiente: munición/mantenimiento y roles originales intactos; cofres sin equipo vanilla.
- Mago: comunes/poco comunes y raras finales; épica por combinación 3:1, legendaria exige jefe. Evita épicas gratuitas en todos los cofres altos.
- Constructor: raíces de mina/mar/desierto dan recursos temáticos y logística; no hay lingotes de equipo gratis.
- Técnico: Lootr sin renovación; no se añaden recetas ni conversiones de metales. Explorar sigue siendo repetible en nuevas estructuras, deliberadamente.
- Cooperativo: Lootr individual multiplica el total del grupo por jugadores; no se afirma presupuesto global compartido. Se conservan las mismas cantidades por persona.

### Ataques y correcciones

Demostrado: garantizar cada alternativa de una tabla de Cataclysm entregaría seis objetos especiales juntos. Corregido repartiendo espada/hacha/pala/botas y accesorios entre cuatro IDs. Demostrado: anillos de barriles R1 serían una ruta barata; trasladados a cofres hostiles R3/F3/F4. Demostrado: equipo de curio anidado desaparecería al quitar referencias; redistribuidos los trece accesorios básicos en trece tablas concretas, sin tocar la tabla compartida usada por entidades.

Riesgos plausibles: abrir tesoros evitando combate, rutas rápidas de saqueo, muchas tablas repetidas por estructura. No se conocen recuentos máximos por todas las variantes ni tiempos reales: no se promete ausencia universal de estrategias dominantes. No se bloquean construcción ni redstone. La clasificación es una estimación a validar in-game, no una medida de dificultad.

Las plantillas/decoración/discos no sustituyen suministros útiles, y el carbón permanece. Se eliminan agua y botellas vacías. Se conserva `lootr:chests/elytra`. Arqueología, pesca y recompensas de jefes están fuera del cambio.

## Criterios obligatorios de aceptación

Generación real Forge bajo semillas y suerte distintas debe producir exactamente IDs, cantidades y NBT de matriz tras los GLMs y la sanitización. No basta inspeccionar JSON. Ninguna tabla cubierta puede perderse del gestor cargado, registrar objetos inexistentes o depender de funciones aleatorias. Se compara además el hash de recetas/entidades/bloques/tags ajenos al alcance contra la salida previa del generador para conservar cambios preexistentes.
