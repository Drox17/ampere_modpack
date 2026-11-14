# Entrega de rebalance determinista (2026-11-14)

## A. Resumen de cambios

Implementado y desplegado localmente AdventureLoot 1.5.0 y EquipmentBalance 1.24.7. Se conservó el trabajo de fuentes preexistente. El cambio Java funcional de esta misión es una sola conversión de bloques: 3 pepitas fijas en la salvaguarda de cofres. Los cambios anteriores de equipo, habilidades y jefes no se rediseñaron. El instalador estándar recompiló y renovó los artefactos y su registro de validación (1.24.6 -> 1.24.7). No hubo commit, push ni publicación.

## B. Balance final

[Contrato humano por ID](LOOT_DETERMINISTA_MATRIZ.md), [auditoría de fases 1–3](LOOT_DETERMINISTA_AUDITORIA.md). R0 no da magia; despensas/barriles se limitan a R1; R2 entrega común; R3/R4 poco común; F3/F4 añaden una rara y pepitas de diamante. Se eliminó la épica garantizada en cada cofre alto para preservar valor del caldero. Los suministros y temas son fijos: mar/mina/desierto/biblioteca/cripta/hielo/Nether/End/combate. Los objetos especiales y trece accesorios anidados tienen ubicaciones explícitas; el equipo modded se reparte para evitar entregar todas las alternativas originales juntas.

## C. Determinismo

194 tablas (147 con premios, 47 auxiliares inactivos). Se eliminaron del contrato pesos, rangos, probabilidades, referencias, funciones de encantamiento aleatorio, randomize_spell y bonus por suerte. Un objeto por pool, cantidad y NBT explícitos. Los GLMs de cofres se desactivan individualmente; no se borra el registro de otros mods. Se consultó el gestor de tablas efectivo de Forge para detectar omisiones. Para cada tabla se generó el botín con 32 semillas y suerte -5/0/+5, comparando multiconjuntos con la matriz antes y después de una segunda sanitización: variación cero. Se valida hechizo cargado, rareza no legendaria y capacidad de 27 ranuras. Las posiciones cosméticas de las ranuras quedan fuera de la comparación.

## D. Economía y progresión

Agua y botellas vacías fuera. No equipo vanilla salvo élitros, no XP ni minerales completos prohibidos, un solo libro nivel I autorizado, no legendarios ni catalizadores de jefe. Los materiales no-cofre y recetas siguen idénticos. Se limitan las varas a una por final del Nether; no se añaden varas a todas las despensas. Riesgos plausibles no eliminados: rutas de saqueo evitando combate, repetición de tablas en estructuras grandes y especialización de rutas por jugador técnico. La matriz no prueba que se haya vencido al jefe ni garantiza ausencia absoluta de granjas o de una ruta dominante. Lootr continúa sin renovación automática.

## E. Compatibilidad

Forge 1.20.1 con mods reales: Lootr, YUNG's, Cataclysm, Iron's, Nuggets For All, Create y AE2. Se verificaron tablas efectivas, IDs y NBT. 208 recursos de recetas, entidades, bloques y tags comparados byte por byte con el generador previo al contrato: idénticos. Excluidos meteorito AE2 como bloque y great_ink/reward_ink compartidas con entidades. Las tablas de cofre ya no referencian esas fuentes. Datapack con idéntico SHA-256 en pack, mundo/global del servidor e instancia global de Prism. Reiniciar o recargar recursos es necesario para una sesión ya abierta; no se abrió ni modificó el mundo del jugador para las pruebas.

Los logs de arranque muestran avisos/errores de recetas nativas que referencian ítems Kaleidoscope ausentes. No son una declaración de que todo el modpack esté libre de avisos; esas recetas no se modificaron (la comparación de recursos fuera de cofres pasó). La prueba aislada sí llegó a ServerStartedEvent y terminó con éxito.

## F. Pruebas

- Compilación Java 17 con advertencias tratadas como errores: pasó.
- AdventureLoot: 1.833 checks estructurales/regresión + 29.006 Forge real = **30.839 aprobados**, cero fallos finales. Última ejecución sobre el JAR 1.24.7 empaquetado.
- EquipmentBalance: **2.062 JVM aprobados**, incluidas 409 de compatibilidad real y 97 descriptores/firmas Mixin. La primera ejecución se detuvo por estado.json desfasado; se corrigió y la repetición completa pasó.
- Integridad local: **362/362** entradas, **440/440** hashes de loot, 131 claves sincronizadas; paridad de JAR repo/servidor/índice y sin CRLF de publicación.
- Verificador final: **14/16**, solo pages.version (público anterior, no publicado) y git.limpio (cambios locales autorizados). La última pasada usó -SkipTests; la suite de 2.062 había pasado por separado y también en la pasada completa previa. No se presenta ese SKIP como una ejecución adicional.
- git diff --check sin errores de espacios. Los avisos LF/CRLF del repositorio de código no afectan al índice del pack.

Evidencia de ejecución: TheOptimizerMods/datos/reparaciones/botin_determinista/determinism-result.json y determinism-runtime.log; auditoría JVM de equipo en datos/reparaciones/balance_equipamiento.

## G. Archivos modificados en esta misión

Las rutas siguientes corresponden a esta revisión, no a todos los cambios de equipo ya presentes al comenzar.

### TheOptimizerMods

- botin_magia_aventura/auditar_determinismo.py: descubrimiento de fuentes, referencias y RNG.
- botin_magia_aventura/audit_determinismo_antes.json: snapshot del estado previo, 197 raíces / 205 alcanzables / 0 referencias ausentes.
- botin_magia_aventura/disenar_determinismo.py: diseño por riesgo/tema y redistribución adversarial de especiales.
- botin_magia_aventura/matriz_determinista.json: contrato exacto y razones por objeto.
- botin_magia_aventura/determinista.py: generación fija y desactivación acotada de GLMs de cofre.
- botin_magia_aventura/instalar.py: aplicar contrato al final, versión y fecha de registro.
- botin_magia_aventura/probar.py: contratos, invariantes, recetas y regresiones; invoca Forge real.
- botin_magia_aventura/VerifyDeterministicLoot.java: generación real bajo semillas/suerte distintas y comparación con matriz.
- botin_magia_aventura/verificar_determinismo.py: servidor temporal aislado y evidencia persistente.
- balance_equipamiento/theoptimizer/equipment/EquipmentPolicy.java: respaldo de bloque fijo en 3 pepitas.
- balance_equipamiento/instalar.py y probar.py: versión local 1.24.7.
- Artefactos regenerados: botin_magia_aventura/TheOptimizer_AdventureLoot.zip; datos/reparaciones/balance_equipamiento/TheOptimizer-EquipmentBalance-1.24.7.jar, clases compiladas y validacion_1.24.7.json (el instalador rota validacion_1.24.6.json); datos/reparaciones/botin_determinista/determinism-result.json y determinism-runtime.log.

### AmpereRepo

- AGENTS.md: referencias actuales y nota de revisión; registro histórico conservado.
- docs/LOOT.md y docs/BALANCE.md: contrato vigente y referencias históricas diferenciadas.
- docs/LOOT_DETERMINISTA_AUDITORIA.md, LOOT_DETERMINISTA_MATRIZ.md y este informe: evidencia y entrega.
- estado.json: versiones y conteo real 362 (antes esperaba 360).
- loot.json: 440 hashes regenerados.
- mods/TheOptimizer-EquipmentBalance-1.24.6.jar sustituido por mods/TheOptimizer-EquipmentBalance-1.24.7.jar.
- moonlight-global-datapacks/TheOptimizer_AdventureLoot.zip: 434 archivos.
- pack.toml, index.toml, version.txt y changelog.md: metadatos locales, índice y entrada de cambios (historial previo preservado).

### Despliegues derivados

Servidor: mods/TheOptimizer-EquipmentBalance-1.24.7.jar, AdventureLoot en ampere/datapacks y moonlight-global-datapacks. Instancia Prism activa: mismo JAR y AdventureLoot global / carpetas de datapacks de saves existentes. El instalador estándar volvió a sincronizar también LootFixes y configuraciones existentes sin introducir claves nuevas ni alterar valores de usuario. Estos son artefactos de instalación, no cambios de diseño ajenos.

## H. Pendientes y prueba manual concreta

1. Reiniciar cliente/servidor o recargar datapacks según corresponda.
2. En un mundo de prueba, abrir cofres NUEVOS de aldea, mina, templo, cripta, fortaleza, bastión y End; cotejar IDs/cantidades con la matriz.
3. Comprobar un pergamino fijo (hechizo y nivel) y los élitros de Lootr.
4. Abrir el mismo cofre con dos jugadores: comprobar inventario personal y ausencia de renovación para cada uno.
5. Medir esfuerzo y cofres por variante antes de afirmar balance empírico por hora. Los cofres ya materializados conservan su inventario anterior.
6. Los informes PDF históricos son propuestas de una etapa anterior; la matriz fuente y docs/LOOT.md prevalecen para esta implementación.

## I. Estado final

**Implementado y verificado automáticamente; validación visual y de ritmo de juego pendiente.** Sin bloqueos técnicos conocidos en la composición determinista cubierta. Los dos avisos finales son consecuencia de dejar la revisión local sin publicación, conforme al encargo.
