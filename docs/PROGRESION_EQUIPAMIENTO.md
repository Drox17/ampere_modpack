# Progresión de equipamiento: auditoría horizontal vs vertical

> Estado real del código en 1.20.1 (módulo `balance_equipamiento`, 1.12.0).
> Este documento responde a una pregunta: **¿queda margen de mejora entre el grupo de
> armas/herramientas y el grupo de armaduras?** Sí, y está cuantificado abajo.

## 1. Cómo está construida la progresión hoy

### 1.1 Eje vertical (tier)

| Material | Daño espada | Daño hacha | Durabilidad | Alcance | Puntos de armadura | Dureza |
|---|---:|---:|---:|---:|---:|---:|
| Madera | 4 | 7 | 59 | — | — | — |
| Piedra | 5 | 9 | 131 | — | — | — |
| Cuero | — | — | (×15) | — | **15** | 0 |
| Cota de malla | — | — | vanilla | — | **15** | 0 |
| Hierro | 6 | 9 | 250 | +0.5 | **15** | 0 |
| Oro | 4 | 7 | 250 | — | **15** | 0 |
| Diamante | 7 | 9 | 1561 | +1.0 | **20** | 2 |
| Netherita | 8 | 10 | 2031 | +1.0 | **20** | 3 |

- La **velocidad de minado está unificada a 6.0** para todas las herramientas (`unified_harvest_speed`).
  El tier no da velocidad, solo durabilidad, alcance y encantamiento innato.
- Cuero, cota, oro y hierro comparten **15 puntos**: la Invariante C4 ("los sets horizontales no
  reciben armadura extra") se cumple y la diferenciación entre ellos es solo de rol.
- El salto vertical de armadura es 15 → 20 puntos + dureza 2/3 + resistencia al empuje 0.4 (netherita).

### 1.2 Eje horizontal (rol)

**Armas y herramientas** (atributos + encantamiento innato vía `EnchantmentHelperMixin`):

| Material | Rol | Mecánica real |
|---|---|---|
| Madera | velocidad + artrópodos | +0.35 velocidad de ataque · **Bane of Arthropods V** · +25 % en madera/hojas/cultivos · hojas sin desgaste |
| Piedra | control | **Knockback I** + **+0.5 empuje** (atributo) · **aturdimiento 0.4 s** (Lentitud I) · +15 % en cantera/menas |
| Hierro | infantería / área | alcance +0.5 · **Sweeping Edge III** (espada) |
| Oro | anti-no-muertos / suerte | **Smite V** · Suerte +1 · piglins pacificados · durabilidad 250 |
| Diamante | precisión / conservación | alcance +1.0 · **crítico 10 % ×1.5** · **Toque de Seda** en herramientas · ×2 en pizarra/obsidiana |
| Netherita | élite del Nether | alcance +1.0 · **Fortuna III** · ×2 escombros · **Lentitud II 2 s** · **+15 % vs enemigos con armadura** · piglins |

**Armaduras** (reducciones por pieza, escalan 1p/2p/3p/4p):

| Set | Rol | Reducción (1/2/3/4 piezas) | Extras innatos |
|---|---|---|---|
| Cuero | explorador | caída 5/12/20/35 % | botas: Caída de Pluma IV · grebas: Sigilo Veloz III · Paso sobre Hojas |
| Cota de malla | escaramuzador | proyectiles 5/10/18/30 % · velocidad 2/4/7/10 % | — |
| Hierro | infantería | empuje 5/10/18/30 % · explosiones 4/8/15/25 % | — |
| Oro | arcano | magia 4/8/15/25 % | Suerte +1 con set completo |
| Diamante | élite | golpes ≥8 de daño 6/12/19/25 % | coste: −10 % daño en golpes <8, agotamiento, rep. 25 % |
| Netherita | élite del Nether | fuego 5/12/20/35 % · wither 10/20/35/50 % · golpes ≥8: 4/8/13/18 % | botas: Soul Speed II · coste: −5 % en golpes <8, agotamiento, rep. 25 % |

## 2. Diagnóstico: lo que ya funciona

1. **La velocidad de minado no escala por tier** → la progresión vertical de herramientas no
   aplasta la horizontal; el valor del tier es durabilidad, alcance y el innato.
2. **Los cuatro sets de 15 puntos comparten armadura** → elegir cuero/cota/oro/hierro es elegir rol,
   no potencia.
3. **Cada armadura tiene un rol defensivo distinto** con números simétricos (5/12/20/35 y 4/8/15/25).
4. **El diamante y la netherita se reparten los golpes pesados** (6-25 % vs 4-18 %): el diamante
   resiste mejor a jefes, la netherita cubre fuego/wither.

## 3. Hallazgos: dónde hay margen

| # | Hallazgo | Severidad | Por qué |
|---|---|---|---|
| H1 | **Oro es el mejor arma del juego contra no-muertos** | Alta | Smite V = **+12.5 daño plano**; espada de oro 4 + 12.5 = **16.5** vs 8 de netherita. Los no-muertos son la familia más común. Sin coste: se repara al 100 % con oro barato y no tiene agotamiento. Rompe P2 (todo poder tiene coste) y la prioridad horizontal. |
| H2 | **Tooltip de oro miente en la cifra** | Media | Dice "No-muertos: daño ×2.5" pero el efecto real es +12.5 plano (×~4 sobre 4 de daño). Invariante C6 (números del código) se cumple en el código, no en la expectativa del jugador. |
| H3 | **Piedra con empuje doble** | Media | Knockback I (+0.5) **más** +0.5 del atributo = +1.0 real; el tooltip anuncia +0.5. Además aturde 0.4 s: es el mejor control para un tier 2. |
| H4 | **Netherita domina al diamante en combate** | Alta | Más daño (8 vs 7), más durabilidad (2031 vs 1561), control (Lentitud II), +15 % vs blindados, Fortuna III (vs Seda), piglins, y **penalización de golpe débil menor** (−5 % vs −10 %). El diamante solo gana en reducción de golpes pesados. |
| H5 | **La armadura pesada no penaliza movilidad** | Alta | Cota de malla vende "velocidad" (2/4/7/10 %) pero hierro/diamante/netherita no pierden nada de velocidad: la ventaja no compra nada. El coste de los sets pesados es solo agotamiento al golpear. |
| H6 | **Oro armadura = hierro en puntos y durabilidad, y además suerte/magia** | Media | Con 15 puntos y durabilidad 165-240 igual que hierro, el oro añade Suerte +1 y reducción mágica sin coste → domina al hierro salvo explosiones/empuje. |
| H7 | **"Rompe-escudos" anunciado y no implementado** | Baja | Dos tooltips de netherita lo prometen y no hay código (solo un comentario en `EquipmentEvents`). |
| H8 | **Cuero solo aporta en botas/grebas** | Baja | Casco y pecho de cuero dan caída (redundante con las botas) y nada más; su durabilidad ×15 ya no es una desventaja. |

## 4. Márgenes de mejora propuestos (horizontal primero)

### P1 — Coherencia (barato, alto impacto)

1. **Rompe-escudos**: implementarlo (`disableShield` al impactar con netherita) o borrar la línea.
2. **Tooltip de oro**: cambiar "×2.5" por "+12.5 de daño a no-muertos (Castigo V)".
3. **Tooltip de piedra**: "+0.5 empuje" → "+1.0 empuje" (real) o quitar el atributo y dejar solo Knoback I.

### P2 — Poner coste al oro (o dejar de llamarlo barato)

- Bajar **Smite V → Smite III** (+7.5): espada de oro 4 + 7.5 = **11.5** vs no-muertos, por encima de
  diamante (7) y por debajo de netherita (8) sólo contra su nicho. Sigue siendo el mejor anti-undead,
  pero no aplasta el tier.
- Alternativa: mantener Smite V y bajar durabilidad del oro a **150** o aplicar `diamond_repair_fraction`
  también al oro (25 %), que hoy repara gratis.

### P3 — Reequilibrar diamante vs netherita (vertical sin aplastar)

- **Invertir penalizaciones**: diamante −5 %, netherita −10 % (hoy al revés). La élite paga más.
- Dar al diamante un pico de nicho: **crítico 15 % ×1.5** (media +7.5 %) o +5 % de daño a enemigos
  **sin** armadura (la netherita ya tiene +15 % contra blindados).
- Con eso: diamante = precisión contra no blindados; netherita = control y blindados; ninguna domina.

### P4 — Hacer real el rol de la cota de malla

- Penalización de movimiento por peso: hierro −5 %, diamante −8 %, netherita −10 %.
- O subir la cota a **5/9/13/18 %** de velocidad y bajar su reducción de proyectiles a 4/8/15/22 %.
- Sin una de las dos, "escaramuzador" no existe.

### P5 — Diferenciar oro de hierro (armadura)

- Bajar el oro a **12 puntos** (2/5/4/1) manteniendo suerte + magia, o darle −1 dureza por pieza y
  mantener 15 puntos. El hierro conserva explosiones/empuje como nicho.

### P6 — Dar rol al cuero fuera de las botas

- Casco de cuero: +5 % de reducción de daño de caída acumulable (ya hay caída por set) o
  "menos agotamiento al correr" como identidad de explorador.
- Pecho de cuero: mantener solo caída, pero subir su tramo (7/15/25/40 %) para que el 4/4 sea real.

## 5. Resumen

**Sí hay margen**, y no es de "más números", sino de **coherencia y coste**:

- El eje horizontal está **bien construido** en armaduras (roles simétricos, 15 puntos compartidos,
  encantamientos innatos por pieza) y **bien construido** en herramientas (encantamiento innato por
  material, velocidad de minado unificada).
- Los tres problemas de fondo son: **el oro tiene el mejor arma sin coste**, **la netherita domina al
  diamante**, y **la armadura pesada no pesa** (la cota no tiene nicho real).
- Los tres son corregibles sin añadir mecánicas nuevas: cambiar cuatro números de Smite, dos
  penalizaciones y una penalización de movimiento.

## 6. Cómo verificar cada cambio

- Atributos y encantamientos innatos: `EquipmentEvents` + `EnchantmentHelperMixin`.
- Reducciones por rol: arrays `PCT_*` en `EquipmentEvents`.
- Puntos/durabilidad de armadura: `ArmorMaterialsMixin`.
- Claves de config afectadas: `enable_tool_attributes`, `diamond_weak_hit_penalty`,
  `netherite_weak_hit_penalty`, `gold_armor_multiplier`, `diamond_crit_chance`,
  `diamond_crit_multiplier`, `unified_harvest_speed`.
- Tras tocar el módulo: `python -m gestion.herramientas.reparaciones.balance_equipamiento.instalar` y
  `... .probar`, luego `verificar_estado.ps1` (15 comprobaciones).
## 7. Decisiones aplicadas (1.15.0)

| Hallazgo | Decisión | Valor final |
|---|---|---|
| H1 oro aplasta el tier | **Nerfeado** | Castigo V → **III** (+7.5 contra no-muertos); `gold_smite_level = 3` |
| H2 tooltip de oro | **Corregido** | Muestra "+7.5 daño" calculado desde la config |
| H3 empuje doble de piedra | **Corregido** | Tooltip "+1.0 empuje" (real: Knockback I + 0.5 de atributo) |
| H4 netherita domina al diamante | **Invertido** | Diamante −5 % / netherita −10 % en golpes <8; diamante **crítico 15 % ×1.5** |
| H5 armadura pesada sin coste de movilidad | **Rechazado el cambio** | No se penaliza el movimiento (parkour intacto); el coste es el **agotamiento** (daño convertido en hambre) y la reparación al 25 % |
| H6 oro armadura = hierro + extras | **Rechazado el nerf** | El oro no se toca; el hierro gana **dureza +0.5/pieza** (2.0 con set, frente a 8 del diamante) |
| H7 "rompe-escudos" sin código | **Línea borrada** | Queda "Lentitud II al impactar" |
| H8 cuero solo en botas | **Aplicado** | Caída 7/15/25/40 % (antes 5/12/20/35) |

Nota de diseño aceptada: las armaduras de diamante y netherita son **de jefe**, no de horda; su
ineficiencia contra hordas viene del agotamiento, no de frenar al jugador. La cota de malla conserva
su identidad de escaramuzador (velocidad sin coste de hambre) y el hierro la de infantería (dureza + resistencias).

