# BALANCE.md — memoria profunda del sistema de sets

> Se lee **solo al diseñar** (cambiar reglas, añadir sets, revisar números). Para `/sync`
> usa `verificar_estado.ps1` + `estado.json`. Este archivo explica el porqué y el backlog.

## 1. Números de referencia

### 1.1 Reducciones por set (escalan 1p/2p/3p/4p)

| Set | Eje | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Cuero | caída | 5 % | 12 % | 20 % | 35 % |
| Malla | proyectiles | 5 % | 10 % | 18 % | 30 % |
| Malla | velocidad | +2 % | +4 % | +7 % | +10 % |
| Hierro | empuje | 5 % | 10 % | 18 % | 30 % |
| Hierro | explosiones | 4 % | 8 % | 15 % | 25 % |
| Oro | magia/pociones | 4 % | 8 % | 15 % | 25 % |
| Diamante | golpes ≥8 | 6 % | 12 % | 19 % | 25 % |
| Netherita | fuego/lava | 5 % | 12 % | 20 % | 35 % |
| Netherita | wither | 10 % | 20 % | 35 % | 50 % |
| Netherita | golpes ≥8 | 4 % | 8 % | 13 % | 18 % |

Umbral de "golpe fuerte": `HEAVY_HIT_THRESHOLD = 8.0`.
Debilidad de sets pesados: diamante +10 % y netherita +5 % de daño recibido por golpes <8
(escalado por pieza: `/4`).

### 1.2 Costes por eje

| Coste | Dónde | Valor |
|---|---|---|
| Agotamiento por golpe pesado | diamante / netherita | base 0.5 / 0.6 + 3 % del daño × piezas |
| Daño recibido de golpes débiles | diamante / netherita | +10 % / +5 % a 4 piezas |
| Daño cuerpo a cuerpo | túnicas (rol mago) | −5 % por pieza, máx −20 % |
| Reparación | baratos / caros | 100 % / 25 % por unidad |

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

## 2. Backlog con criterio de aceptación

### T1. Rediseño de herramientas y armas (**hecho en 1.10.0 y 1.11.0**)
Quitar de herramientas la velocidad de movimiento y de armas la guardia de armadura; dar
identidad de recolección (madera +25 % madera/hojas/cultivos; piedra +15 % piedra y menas;
hierro alcance; oro suerte; diamante toque de seda + ×2 pizarra/obsidiana; netherita botín +
×2 escombros) y de combate (piedra aturdimiento 0.4 s; diamante +10 % crítico; hierro barrido
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

1. Editar fuente en `gestion/.../balance_equipamiento`.
2. `python -m gestion.herramientas.reparaciones.balance_equipamiento.instalar` (desde la instancia).
3. `python -m gestion.herramientas.reparaciones.balance_equipamiento.probar` → `VERIFICACION EXITOSA`.
4. En el repo: `packwiz refresh` (o commit; el hook lo hace) y `.\validar.ps1`.
5. Si cambió comportamiento visible: ampliar `changelog.md` y regenerar `version.txt`
   (`MD5(changelog.md)` primeros 8 en minúsculas).
6. `git commit` + `git push`; comprobar que Pages sirve el `version.txt` nuevo.
7. Nunca copiar jars a la instancia de Prism: los baja el updater.

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

