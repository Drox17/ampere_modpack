§6§l===================================
§e§l  THEOPTIMIZER — ESTADO VIGENTE
§6§l===================================§r
§7Pack §f1.24.6§r · Minecraft §f1.20.1§r · Forge §f47.4.28§r · §f368§r entradas · verificador §f16 comprobaciones§r.
§7Este archivo describe lo que está §fvigente§r hoy, contrastado con el Minecraft vanilla. El historial de versiones va al final.

-----------------------------------
§6§l[EQUIPMENTBALANCE 1.24.6 & ADVENTURELOOT 1.4.0]
-----------------------------------
§aCofres sanitizados 1.24.6: §fcero§r equipamiento vanilla en cofres (salvo §felytra§r), máximo §f1 encantamiento vanilla§r permitido nivel I por cofre, y §fcero§r lingotes, bloques o minerales enteros (todo mineral salvo carbón/carbón vegetal cae en §fpepitas§r con §fNuggets For All§r).
§aRecetas Nuggets For All: §f16§r conversiones §f1 ↔ 9§r habilitadas en formato MC 1.20.1 (`nuggets_for_all:recipes`).
§aIron's Spellbooks (`defaultconfigs/irons_spellbooks-server.toml`): §fscrollRecycleChance = 1.0§r (§f100 %§r de éxito al reciclar pergaminos en tinta).
§aArmaduras físicas: §f16 puntos (2/5/6/3)§r. Túnicas: §f10§r. Cursium: §f12§r. Dureza: §f0§r en todos los materiales.
§aColoso: absorbe §f50 %§r del excedente de cada golpe sobre §f10§r, proporcional a piezas pesadas.
§cEnjambre: §f2 impactos de combate en 1,5 s§r reducen la armadura efectiva al §f50 %§r. Ataque: diamante §f−15 %§r y netherita §f−20 %§r con set completo.
§aMonstrous duplica Coloso; su casco resta §f10 %§r de movimiento y §f30 %§r de ataque, compuesto con las otras piezas. Ignitium aporta la mitad de Coloso y prende al atacante cuerpo a cuerpo §f3 s§r (recarga §f2 s§r). Cursium no tiene Coloso, brecha ni penalización de ataque.
§aEl linaje completo gana inmunidad a fuego y marchitamiento y §f25 %§r de firmeza; paga daño §f+10 %§r con luz ambiental §f<8§r y reparación §f50 %§r.
§aArquetipos 1.24.2: madera §f×2§r contra artrópodos; piedra §f+20 %§r y cantera gratuita; hierro §f3×3 / agachado 1×1§r y rompeguardias con coste; oro contra no-muertos y tregua exclusiva; diamante §f−15 %§r frente a armadura ≥8; netherita sin lentitud, reparación §f50 %§r y fragmentos §f15 %§r en material netherita.
§aCorrecciones: hojas por tag sin desgaste real, conjuros cancelados, reparación básica §f100 %§r, sin porcentajes de reparación ficticios ni prosa especulativa sobre mods externos. Tarjetas de ítems especiales y tortuga §f1/1§r.
§aHambre baja: con §f3 muslitos o menos§r, iconos vanilla verdosos y temblor. Gruñido suave cada §f8 s§r; con §f1 muslito o menos§r, cada §f4 s§r y temblor más frecuente. Comer reinicia el aviso. A cero, la inanición conserva el latido sin sacudón de cámara.
§aTooltips: resumen breve de rol y costes; mantén §fShift§r para ver cifras, condiciones y ejemplos del §fequipo que llevas puesto§r. Cuero: §f3 piezas, −20 %§r de daño de caída; §f4 piezas, −35 %§r. Tiempos en segundos, daño en corazones y consumo equivalente de comida en muslitos. Atributos alineados y alcance traducido.
§7Esta revisión sustituye las cifras anteriores de armadura, dureza y golpes fuertes/débiles de la sección [2]. Pendiente validación visual y sonora en juego.

-----------------------------------
§6§l[GUIA] CÓMO LEERLO
-----------------------------------
§7Cada bloque tiene dos columnas de texto: §8vanilla§r y §aAmpere§r. Si algo no aparece aquí, no está en el pack.
§7Los números salen del código (invariante C6): no hay prosa con cifras inventadas.

-----------------------------------
§6§l[1] FILOSOFÍA (13 PRINCIPIOS)
-----------------------------------
§aP1§r Progresión horizontal (roles) + vertical (tier) §fcon coste§r.
§aP2§r Todo poder tiene coste explícito: agotamiento, daño recibido, reparación cara.
§aP3§r La XP está §ferradicada§r: sin orbes, costes ni progresión por niveles.
§aP4§r Mesa de encantamientos §fdecorativa§r (interacción cancelada).
§aP5§r Solo §f3§r encantamientos looteables nivel I (máx. §f1§r por cofre), §fcero§r equipo vanilla y minerales solo en §fpepitas§r salvo carbón.
§aP6§r Velocidad de minado §funificada a 6.0§r para todas las herramientas.
§aP7§r Ninguna pieza opaca a otra: cada material es el mejor en algo.
§aP8§r Spawns adulterados a propósito: §f55/45§r vanilla-mods, tope de criaturas §f16§r.
§aP9§r Yunque reworkeado: §f0 XP§r, sin "demasiado caro", reparación por familia.
§aP10§r Iron's Spellbooks looteable por cofres (no por granja).
§aP11§r Se aceptan sugerencias que respeten P1–P10.
§aP12§r Juego tradicional primero: explorar, pelear, construir, coleccionar.
§aP13§r Desincentivar al jugador técnico: granjas, AFK y min-max deben ser §fpeores§r, no prohibidos.

-----------------------------------
§6§l[2] ARMADURAS
-----------------------------------
§e§l> COLUMNA VANILLA§r
§8- Durabilidad por material: cuero §f55/80/75/65§8 · cota y hierro §f165/240/225/195§8 · oro §f77/112/105/91§8 · diamante §f363/528/495/429§8 · netherita §f407/592/555/481§8.
§8- 15 armadura: cuero, cota, oro, hierro. 20 armadura: diamante y netherita.
§8- Reparación de yunque: 25 % por material. Todo encantable.

§e§l> COLUMNA AMPERE§r
§a- Sets base (cuero, cota, oro, hierro): durabilidad §funificada§r §f165 / 240 / 225 / 195§r por pieza (§f825§r el set); armadura §f16§r.
§a- Sets de diamante y netherita: durabilidad de élite intacta; armadura §f16§r, dureza §f0§r.
§a- Reparación: §f100 %§r en tiers base (madera, piedra, cuero, cota, oro, hierro) ; diamante §f25 %§r y netherita/linaje §f50 %§r.
§a- Pérdida al morir: §f10 %§r de durabilidad, también sobre las piezas de 15.

§e§l> ROLES DE SET§r
§7- §fCuero§r: caída −5/12/20/35 % (1/2/3/4 piezas), paso fluido sobre hojas.
§7- §fCota§r: proyectiles −5/10/18/30 % y velocidad +4/8/12/16 %.
§7- §fHierro§r: empuje −5/10/18/30 %, explosiones −4/8/15/25 %; ≥2 piezas añaden alcance de bloques +0.5.
§7- §fOro§r: magia −4/8/15/25 %, Suerte +1, piglins pacificados.
§7- §fDiamante§r: Coloso sobre 10 de daño; a cambio ataque −15 %, brecha, agotamiento de combate y reparación 25 %.
§7- §fNetherita§r: Coloso y herencia térmica; a cambio ataque −20 %, brecha, daño +10 % con luz <8, agotamiento de combate y reparación 50 %.
§7- §fTortuga§r: respiración acuática y minado submarino.
§7- §fLinaje netherita§r (ignitium, cursium, monstrous_helm, netherite_mage): hereda el set de netherita completo.
§7- §fTúnicas de mago§r: −5 % de daño cuerpo a cuerpo por pieza (máximo −20 %).

-----------------------------------
§6§l[3] HERRAMIENTAS Y ARMAS
-----------------------------------
§e§l> COLUMNA VANILLA§r
§8- Durabilidad: madera §f59§8 · piedra §f131§8 · hierro §f250§8 · oro §f32§8 · diamante §f1561§8 · netherita §f2031§8.
§8- Velocidad de minado por tier: §f2 / 4 / 6 / 8 / 9 / 12§8 (madera → oro).
§8- Espada: daño §f4 / 5 / 6 / 4 / 7 / 8§8 y velocidad §f1.6§8 en todas.

§e§l> COLUMNA AMPERE§r
§a- Durabilidad: madera §f80§r · piedra §f160§r · hierro §f300§r · oro §f160§r (frágil) · diamante §f1561§r · netherita §f2031§r.
§a- Velocidad de minado: §f6.0§r para todos los tiers. El tier solo abre bloques, da aguante y el innato.
§a- Espada: daño §f4 / 5 / 6 / 6 / 7 / 8§r y velocidad §f1.95 / 1.6 / 1.6 / 2.0 / 1.6 / 1.5§r.

§e§l> PASIVAS INNATAS (aplican a todo §fDiggerItem§r: pico, pala, hacha y azada)§r
§7- §fMadera§r: +25 % en madera/cultivos, hojas por tag sin desgaste, 10 % de polvo de hueso al romper vegetación; armas ×2 a artrópodos y +0.5 de empuje. Durabilidad 80, reparación 100 %.
§7- §fPiedra§r: +20 % en piedra/menas; cantera común sin desgaste, las menas sí gastan. Control de enemigos e interrupción real de preparación de conjuros. Espada sin penalización de ataque; reparación 100 %.
§7- §fHierro§r: área 3×3; agachado, un bloque. Mitad del desgaste medio por bloque; alcance +0.5 y espada con barrido. Hacha rompe escudo 5 s; al esprintar, daño +15 %; coste 1 agotamiento y 1 durabilidad extra.
§7- §fOro§r: autofundición eficiente, Suerte +1 y extracción de hierro. Bono directo +7.5 a no-muertos con nivel 3, sin depender de NBT. Único diplomático con piglins; azada de daño 1; durabilidad 160.
§7- §fDiamante§r: extracción intacta, alcance +1, críticos 15 % ×1.5; daño −15 % frente a armadura ≥8. Pico ×2 en pizarra/obsidiana. El anclaje a Enderman/Shulker de 3 s procede de MobBalance.
§7- §fNetherita§r: más recursos, alcance +1, pico ×2 en escombros; armas +15 % contra armadura, sin lentitud ni tregua. Reparación 50 % por lingote y 15 % por fragmento en material netherita.
§c- El área consume desgaste por cada bloque; respeta eficiencia, dureza, bloques protegidos y entidades de bloque. Agacharse evita el área.
§7- Las hachas comparten combate y recolección; las espadas no reciben el trabajo en área/autofundición de DiggerItem.

-----------------------------------
§6§l[4] COMBATE Y MOBS
-----------------------------------
§8Vanilla§r: esqueletos y stray 20 de vida, araña 16, phantom 20, bruja 26; sin armadura en jefes salvo la suya.
§aAmpere§r:
§7- Vida ajustada: esqueleto/stray §f12§r · araña §f14§r · phantom §f10§r · bruja §f20§r.
§7- Armadura real: Ravager §f10§r · Elder Guardian §f8§r · Piglin Brute §f8§r · Guardian §f4§r · Vindicator §f4§r · Zoglin §f4§r.
§7- Familias y counters: arañas esquivan 25 % (mitad de daño) → §fMadera§r las ignora y pega ×2; hordas de 3+ zombis empujan +25 % y cobran 1.5 de agotamiento → §fHierro§r (área) y §fOro§r (Castigo) responden; esqueletos y saqueadores aplican Lentitud I a más de 8 bloques → §fCota§r con 2+ piezas lo evita; Enderman y Shulker se teletransportan → §fDiamante§r los ancla 3 s; creeper, bruja y evocador se interrumpen con §fPiedra§r.
§7- Lealtad del tridente: solo vuelve a jugadores; los mobs no la recuperan.
§7- Equipo de spawn: la armadura/arma generada al aparecer §fno se dropea§r; la que entrega el jugador sí.
§7- Jefes: respuestas reactivas (no prohibiciones): el Wither no escapa ni se ahoga, el agua se evapora, el Warden pierde agro, las explosiones tienen tope, los raiders sueltan botín y el monumento conserva prismarine.

-----------------------------------
§6§l[5] HAMBRE, SATURACIÓN Y CURACIÓN
-----------------------------------
§8Vanilla§r: correr 0.1/m, caminar 0.01/m, salto 0.05, salto corriendo 0.2, ataque 0.1, romper bloque 0.005, recibir daño 0.1 y regeneración de 6.0 por medio corazón (rápida cada 10 ticks con saturación).
§aAmpere§r:
§7- Movimiento §f÷5§r: correr §f0.02/m§r, caminar/nadar §f0.002/m§r, salto §f0.01§r, salto corriendo §f0.04§r. Atacar, minar, recibir daño, escudo y sets pesados §fno cambian§r.
§7- Regeneración vanilla §fcancelada§r: no existe la "aspiradora" de 6.0 por medio corazón.
§7- Curación de Ampere: §f1 HP cada 40 ticks (2 s)§r con comida y herido, por §f2.0 de agotamiento§r. Un corazón completo cuesta §f4.0§r (1 punto de saturación) repartido en 4 s.
§7- Escudo de hambre: §f2.0 de agotamiento por cada 1.0 de daño físico absorbido§r (mínimo 8 de comida).
§7- Sets pesados al golpear: §f0.5§r (diamante) / §f0.6§r (netherita) + §f0.03 × daño§r por pieza.
§7- Sprint libre: se puede correr con cualquier nivel de comida.

-----------------------------------
§6§l[6] XP, ENCANTAMIENTOS Y YUNQUE
-----------------------------------
§8Vanilla§r: XP como moneda, mesa de encantamientos, 30+ encantamientos, Mending, yunque que cobra niveles y muela que extrae cualquier encantamiento.
§aAmpere§r:
§7- La XP no tiene función ni progresión: sin orbes, cobros de niveles ni reparación por experiencia.
§7- Mesa de encantamientos §fdecorativa§r; los libros solo salen de cofres de mina/mazmorra/templo (máximo §f1§r por cofre) con §fIrrompibilidad I§r, §fBotín I§r o §fEficiencia I§r.
§7- Sin Mending. La durabilidad se gestiona reparando.
§7- Yunque: §f0 niveles§r, sin "demasiado caro", reparación por familia (100 % base, 25 % diamante, 50 % netherita y linaje) y forja de tridentes.
§7- Muela: solo extrae los §f3§r looteables; los innatos del material (Seda, Fortuna, Castigo, Lealtad…) §fnunca§r se convierten en libros y no cobran XP.
§7- Encantamientos innatos: ligados al material (Seda=hierro, Fortuna=netherita, Castigo=oro, Filo Arrasador=hierro, Suerte=oro…) y solo para jugadores.

-----------------------------------
§6§l[7] LOOT Y ECONOMÍA
-----------------------------------
§8Vanilla§r: cobre 2–5 crudos por mena, botín aleatorio, libros de encantamiento de mesa, tintas de Iron's solo por granja.
§aAmpere§r:
§7- Cobre: §f1 crudo fijo§r por mena (Fortuna sigue aplicando). Se acabó la inundación de inventario.
§7- §f228§r entradas de loot registradas (`AdventureLoot 1.4.0`): perfiles R0–R4 y F2–F4 en pepitas, §fcero§r equipo vanilla en cofres (salvo §felytra§r), máximo §f1§r encantamiento vanilla por cofre, §fcero§r lingotes/gemas enteras salvo carbón (`Nuggets For All`), §f0%§r tinta/pergaminos legendarios, caldero §f3:1§r y drops cerrados en 11 jefes.
§7- Drops cotidianos deterministas con mínimo 1: vara de blaze §f1–2§r, pólvora §f1–2§r, perla de ender §f1§r, caparazón de shulker §f1§r, carbón de wither §f1–2§r, calavera §f15 %§r.
§7- Tintas y materiales de Iron's entran por cofres, no por granja.
§7- Cofre del End: solo materiales, gated por §festrella del Nether§r; rechaza armas, herramientas, armaduras y contenedores (el tooltip lo avisa).

-----------------------------------
§6§l[8] SPAWNS Y FAUNA
-----------------------------------
§8Vanilla§r: reparto y respawn vanilla, sin tope configurable.
§aAmpere§r:
§7- Reparto §f55/45§r vanilla-mods y tope de criaturas §f16§r (`creature_spawn_cap`).
§7- Nigromante de Iron's: §f18 → 2§r por noche.
§7- La fauna vanilla deja de repoblarse y vuelve con respawn cíclico.
§7- Equipo de spawn sin drop; mobs con armadura real (ver §4).

-----------------------------------
§6§l[9] JUGADOR TÉCNICO
-----------------------------------
§7El pack §fno prohíbe§r granjas ni redstone: las hace §fpeores§r que jugar.
§8- Sin Mending ni XP útil: mantener equipo exige reparar, no afkear.
§8- Drops con mínimo fijo: la granja no escala con RNG.
§8- Cobre y menas normalizados: menos inventario, menos automatización rentable.
§8- Cofre del End restringido y muela limitada: menos "almacenamiento infinito" y menos libros infinitos.
§8- Mesa decorativa: el poder viene del material y del combate, no de la mesa.

-----------------------------------
§6§l[10] VERIFICACIÓN
-----------------------------------
§7- §a16/16§r comprobaciones del pack (`verificar_estado.ps1`).
§7- §a228/228§r entradas de loot con hash (`loot.json`).
§7- §a1780§r comprobaciones JVM de `balance_equipamiento` (`263` Forge/Cataclysm/Curios/Nuggets reales, `70` descriptores Mixin), §a457§r de `botin_magia_aventura`; §a16/16§r de `balance_mobs`.
§7- §f118§r claves de configuración de equipo; §f367§r entradas de pack (111 metafiles Modrinth + 15 jars locales).
§7- Distribución de cliente y servidor con los mismos jars (`EquipmentBalance 1.24.6`, `MobBalance 1.5.1`, `WildlifeRepopulation 1.6.1`, `Nuggets For All 1.0.0`, `AdventureLoot 1.4.0`); el cliente recibe esta versión al actualizar el pack.

-----------------------------------
§6§l  HISTORIAL DE VERSIONES
-----------------------------------
§7[1.24.6] Cofres sanitizados (`AdventureLoot 1.4.0`, 228 entradas + `LootTableMixin` en `EquipmentBalance 1.24.6`): cero equipamiento vanilla (salvo `elytra`), máximo 1 encantamiento vanilla permitido nivel I por cofre, cero lingotes/minerales completos salvo carbón (añadido `Nuggets For All` + 16 recetas MC 1.20.1), `scroll_pouch`/`filler_storage_loot` ≤0.65. 118 claves, 1780 comprobaciones JVM + 457 de botín.
§7[1.24.5] Botín por riesgo R0–R4/F2–F4 (AdventureLoot 1.3.0, 111 entradas), caldero 3:1, 0% legendario en cofres, 11 jefes cerrados, 11 armas Iron's normalizadas, contención en armadura pesada y anillos protectores −25%/−5%. 117 claves, 1699 comprobaciones JVM.
§7[1.24.2] Armonización de seis arquetipos y correcciones de ejecución Forge. 104 claves sincronizadas, 1506 comprobaciones JVM; conserva Shift real y HUD sin Args.
§7[1.24.1] EquipmentBalance 1.24.1: Shift calcula las cifras del equipo vestido, incluidos conjuntos mixtos y luz actual. Corrige el máximo de cuatro piezas mostrado con equipo incompleto. 1294 comprobaciones JVM; balance intacto.
§7[1.24.0] EquipmentBalance 1.24.0: resumen y detalles con Shift; netherita compacta, segundos/corazones/comida, atributos alineados y alcance traducido. 1268 comprobaciones JVM. Balance intacto; documentación del cuero ajustada al código existente.
§7[1.23.5] EquipmentBalance 1.23.3: corrige el orden de encabezados y estadísticas de armadura; añade encabezado a piezas externas sin rol y divide líneas largas. Balance intacto.
§7[1.23.4] EquipmentBalance 1.23.2: corrige el crash de arranque Args$1 del HUD; conserva el aviso continuo de hambre, sonidos y STARVE.
§7[1.23.3] EquipmentBalance 1.23.1: señal continua de hambre a ≤3 muslitos; sprites y temblor vanilla con ForgeGui, gruñido periódico local, STARVE intacto.
§7[1.23.2] Este changelog reescrito: estado vigente vanilla vs Ampere.
§7[1.23.1] Oro a 160 de durabilidad en la config (el merge conservaba 300).
§7[1.23.0] Pasivas reasignadas: Seda=hierro, Área 3×3=diamante, Auto-Fundición=oro, Fortuna III=netherita. Armas: piedra 1.4, oro 2.0, netherita 1.5, madera +0.5 de empuje. Cobre fijo a 1.
§7[1.22.2] Paridad real cliente-servidor: seis mods de servidor pasan a `both`.
§7[1.22.1] Primer intento de paridad (sin efecto por CRLF en los metafiles).
§7[1.22.0] Durabilidad unificada del bloque de 15 (825 el set) y escala 80/160/300 en herramientas.
§7[1.21.1] Target de mixin corregido (`Player.m_36399_(F)V`); el servidor vuelve a arrancar.
§7[1.21.0] Agotamiento por movimiento ÷5 y regeneración vanilla cancelada; curación constante de Ampere.
§7[1.20.1] La muela solo extrae los 3 looteables; los innatos no son libros.
§7[1.20.0] El equipo generado al spawnear no se dropea.
§7[1.19.1] Lealtad del tridente solo para jugadores.
§7[1.19.0] Identidades tácticas: familias de mobs y counters por material.
§7[1.18.0] Armadura real de mobs pesados, cofre del End con estrella, drops deterministas y cota de malla.
§7[1.17.0] Respuestas reactivas de jefes (sin prohibiciones).
§7[1.16.0] Guardia de invocación del Wither contra bedrock.
§7[1.15.0] Coherencia de equipo: coste real por material (roles, linaje netherita).
§7[1.14.0] Fauna 55/45 y tope de criaturas 16.
§7[1.13.0] La fauna vanilla deja de repoblarse.
§7[1.12.0] Datapack de correcciones de loot con prioridad.
§7[1.11.0] Las hojas no gastan durabilidad.
§7[1.10.0] Separación de recolección, combate y armadura por material.
§7[1.9.0] La muela extrae el encantamiento a libro (después limitado a 3 en 1.20.1).
§7[1.8.0] Orbes de experiencia apagados.
§7[1.7.0] El yunque pasa a equipamiento.
§7[1.6.0] El beacon se aplica como área, no como efecto.
§7[1.5.0] Elytra, escudo de hambre y beacon pacificador.
§7[1.4.0] Tridente de agua, muerte con desgaste y limpieza.
§7[1.3.0] Reparación de equipo sencillo.
§7[1.2.0] Tooltips compactos de equipo y rol mago para las túnicas de Iron's.
§7[1.1.0] Base del rediseño de roles y superpoderes de armaduras.

-----------------------------------
§6§l[PACK 1.24.3 — RETIRADA LOCAL]§r
§7Se retira Alshanex Familiars 4.1.0 y su parche dependiente TheOptimizer-FamiliarsTagFix. FamiliarsLib se conserva. EquipmentBalance permanece en 1.24.2; sin cambios de balance. Auditoría de equipables externos en reporte.md. Historial de la retirada local previa; incluida ahora en esta publicación.

-----------------------------------
§6§l[EQUIPMENTBALANCE 1.24.3 — COMPATIBILIDAD EXTERNA]§r
§7Se conserva el balance vanilla 1.24.2. Cataclysm deja de acumular atributos físicos: Ignitium 16/0, Cursium 12/0 y firmeza de linaje 25%. Bone Reptile 3/6 y Bloom Stone 6. Skull y Monstrous no añaden dureza. Emerald Stoneplate concede Suerte al equiparlo en anillo; Fluix usa extracción 6.0. Grave Key no activa pasivas de combate. Rocky usa sus efectos nativos, sin reflejo añadido. Se retiran Alshanex, su parche y FamiliarsLib. Configuración: 108 claves.

§6§l[MIGRACIÓN YUNG’S 1.24.4]§r
§7Botín escalonado en 29 cofres propios de YUNG’s: libros permitidos de nivel I y materiales de Iron’s por exploración. Overrides vanilla intactos. Compatibilidades huérfanas de Alex retiradas en EquipmentBalance 1.24.4, MobBalance 1.5.1 y WildlifeRepopulation 1.6.1. TerraBlender sincronizado. Registro: 36 entradas de loot.

§6§l[BOTÍN Y CONTENCIÓN MÁGICA 1.24.5]§r
§7AdventureLoot 1.3.0 (111 entradas): caldero 3:1 (750→250 mB) con #theoptimizer:boss_legendary_catalysts, cofres y RandomizeSpell al 0% legendario, aldeas R0 sin magia, perfiles R1–R4/F2–F4 (F4 culminación 97% rare / 3% epic) y 11 jefes cerrados. EquipmentBalance 1.24.5: 11 armas de Iron's normalizadas (flamberges 0 armadura), contención mágica en armadura pesada (1–2 ×2 maná, 3+ bloquea), anillos protectores −25% daño elemental / −5% vel. ataque. 117 claves; 1699 comprobaciones JVM + 141 de botín.

§6§l[COFRES SIN EQUIPO VANILLA Y PEPITAS 1.24.6]§r
§7Se añade Nuggets For All (`nuggets_for_all-1.0.0-forge-1.20.1.jar`) con 16 recetas 1.20.1 en AdventureLoot 1.4.0 (228 entradas en loot.json, 457 comprobaciones). Ningún cofre otorga equipo vanilla (salvo `elytra`), cada cofre limita a ≤1 encantamiento vanilla permitido nivel I y todos los minerales/lingotes caen en pepitas excepto carbón. EquipmentBalance 1.24.6 añade `LootTableMixin` (`sanitize_chest_loot = true`, 118 claves; 1780 comprobaciones JVM).
