"""Extrae los atributos base de los mobs vanilla de Minecraft 1.20.1 (Forge SRG) y aplica
los cambios que introduce el pack (TheOptimizer-MobBalance, via EntityAttributeModificationEvent).

Fuente: bytecode real del servidor con javap. Cada entidad define sus atributos en un metodo
estatico que devuelve AttributeSupplier$Builder; las constantes aparecen como
    getstatic Attributes.f_XXXX_ / ldc2_w <doble> / Builder.m_22268_(Attribute, D)
y la jerarquia se resuelve por la cabecera "extends" que imprime javap.

Salida: datos/mobs_hostiles_vanilla.json y docs/MOBS_HOSTILES_VANILLA.md
"""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

JAVAP = r"C:\Users\Metabodiru\AppData\Roaming\PrismLauncher\java\java-runtime-gamma\bin\javap.exe"
JAR = r"C:\Users\Metabodiru\AppData\Roaming\PrismLauncher\instances\TheOptimizer\gestion\datos\servidor\forge-instalado\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-srg.jar"
TSRG = r"C:\Users\Metabodiru\AppData\Roaming\PrismLauncher\instances\TheOptimizer\gestion\datos\servidor\forge-instalado\libraries\de\oceanlabs\mcp\mcp_config\1.20.1-20230612.114412\mcp_config-1.20.1-20230612.114412-mappings-merged.txt"
MOJANG = r"C:\Users\Metabodiru\AppData\Roaming\PrismLauncher\instances\TheOptimizer\gestion\datos\servidor\forge-instalado\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-mappings.txt"

RAIZ = Path(__file__).resolve().parents[1]
DATOS = RAIZ / "datos"
DOCS = RAIZ / "docs"

PKG = "net.minecraft.world.entity."
ATRIBUTOS_CLASS = PKG + "ai.attributes.Attributes"

MOBS = [
    ("monster.Zombie", "Zombi", "hostil"),
    ("monster.Husk", "Zombi momificado", "hostil"),
    ("monster.Drowned", "Ahogado", "hostil"),
    ("monster.ZombieVillager", "Aldeano zombi", "hostil"),
    ("monster.Skeleton", "Esqueleto", "hostil"),
    ("monster.Stray", "Errante", "hostil"),
    ("monster.WitherSkeleton", "Esqueleto del Wither", "hostil"),
    ("monster.Creeper", "Creeper", "hostil"),
    ("monster.Spider", "Arana", "hostil"),
    ("monster.CaveSpider", "Arana de cueva", "hostil"),
    ("monster.Silverfish", "Lepisma", "hostil"),
    ("monster.Endermite", "Endermite", "hostil"),
    ("monster.Slime", "Slime", "hostil"),
    ("monster.MagmaCube", "Cubo de magma", "hostil"),
    ("monster.Ghast", "Ghast", "hostil"),
    ("monster.Blaze", "Blaze", "hostil"),
    ("monster.Witch", "Bruja", "hostil"),
    ("monster.Pillager", "Saqueador", "hostil"),
    ("monster.Vindicator", "Vindicador", "hostil"),
    ("monster.Evoker", "Evocador", "hostil"),
    ("monster.Illusioner", "Ilusionista", "hostil"),
    ("monster.Ravager", "Devastador", "mini-jefe"),
    ("monster.Guardian", "Guardian", "hostil"),
    ("monster.ElderGuardian", "Guardian anciano", "mini-jefe"),
    ("monster.Shulker", "Shulker", "hostil"),
    ("monster.Phantom", "Fantasma", "hostil"),
    ("monster.EnderMan", "Enderman", "hostil"),
    ("monster.Vex", "Vex", "hostil"),
    ("monster.hoglin.Hoglin", "Hoglin", "hostil"),
    ("monster.Zoglin", "Zoglin", "hostil"),
    ("monster.piglin.Piglin", "Piglin", "hostil"),
    ("monster.piglin.PiglinBrute", "Piglin bruto", "hostil"),
    ("monster.piglin.ZombifiedPiglin", "Piglin zombificado", "hostil"),
    ("monster.Giant", "Gigante", "hostil"),
    ("monster.warden.Warden", "Warden", "jefe"),
    ("boss.wither.WitherBoss", "Wither", "jefe"),
    ("boss.enderdragon.EnderDragon", "Dragon del End", "jefe"),
]

# Cambios del pack: TheOptimizer-MobBalance (EntityAttributeModificationEvent)
CAMBIOS_PACK = {
    "Esqueleto": {"max_health": 12.0},
    "Errante": {"max_health": 12.0},
    "Arana": {"max_health": 14.0},
    "Fantasma": {"max_health": 10.0},
    "Bruja": {"max_health": 20.0},
}

COLUMNAS = [
    ("max_health", "Vida", "vida"),
    ("attack_damage", "Daño", "danio"),
    ("armor", "Armadura", "armadura"),
    ("armor_toughness", "Dureza", "dureza"),
    ("knockback_resistance", "Res. empuje", "res_empuje"),
    ("movement_speed", "Velocidad", "velocidad"),
    ("follow_range", "Seguimiento", "seguimiento"),
]


def cargar_mapa_atributos() -> dict[str, str]:
    nombre_a_obf: dict[str, str] = {}
    dentro = False
    for linea in Path(MOJANG).read_text(encoding="utf-8", errors="replace").splitlines():
        if linea.startswith("    ") or linea.startswith("\t"):
            if dentro:
                partes = linea.strip().split()
                if len(partes) >= 3 and partes[-2] == "->":
                    nombre = partes[-3].split(".")[-1]
                    if re.fullmatch(r"[A-Za-z_$][A-Za-z0-9_$]*", nombre):
                        nombre_a_obf.setdefault(nombre, partes[-1])
            continue
        partes = linea.split()
        dentro = len(partes) == 3 and partes[0] == ATRIBUTOS_CLASS and partes[1] == "->"

    obf_a_srg: dict[str, str] = {}
    dentro = False
    for linea in Path(TSRG).read_text(encoding="utf-8", errors="replace").splitlines():
        if linea.startswith("\t"):
            if dentro:
                partes = linea.strip().split()
                if len(partes) == 2:
                    obf_a_srg.setdefault(partes[0], partes[1])
            continue
        partes = linea.split()
        dentro = len(partes) == 2 and partes[1] == "net/minecraft/world/entity/ai/attributes/Attributes"

    return {srg: nombre for nombre, obf in nombre_a_obf.items() if (srg := obf_a_srg.get(obf))}


_cache_javap: dict[str, list[str]] = {}


def javap(fqn: str) -> list[str]:
    if fqn in _cache_javap:
        return _cache_javap[fqn]
    resultado = subprocess.run(
        [JAVAP, "-p", "-c", "-classpath", JAR, fqn],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    lineas = resultado.stdout.splitlines() if resultado.returncode == 0 else []
    _cache_javap[fqn] = lineas
    return lineas


def _metodos(lineas: list[str]) -> list[list[str]]:
    """Separa el cuerpo de cada metodo por su firma (linea con dos espacios y parentesis)."""
    bloques: list[list[str]] = []
    actual: list[str] | None = None
    for linea in lineas:
        if re.match(r"^  [A-Za-z][\w<>\[\].$ ]*\(.*\).*;$", linea):
            if actual is not None:
                bloques.append(actual)
            actual = [linea]
        elif actual is not None:
            actual.append(linea)
    if actual is not None:
        bloques.append(actual)
    return bloques


def cargar_defaults() -> dict[str, float]:
    """Valor por defecto de cada atributo, del inicializador estatico de Attributes."""
    lineas = javap(ATRIBUTOS_CLASS)
    defaults: dict[str, float] = {}
    actual: float | None = None
    for linea in lineas:
        if re.search(r"new\s+#\d+\s+// class net/minecraft/world/entity/ai/attributes/(RangedAttribute|Attribute)\b", linea):
            actual = None
            continue
        m = re.search(r"ldc2_w\s+#\d+\s+// double ([\-0-9.E]+)d", linea)
        if m and actual is None:
            actual = float(m.group(1))
            continue
        m = re.search(r"putstatic\s+#\d+\s+// Field (?:net/minecraft/world/entity/ai/attributes/Attributes\.)?(f_\d+_)", linea)
        if m and actual is not None:
            defaults[m.group(1)] = actual
            actual = None
    mapa = cargar_mapa_atributos()
    resultado = {mapa[k].lower(): v for k, v in defaults.items() if k in mapa}
    # defensa: armadura, dureza y resistencia al empuje nacen en 0 (el parser toma el maximo del rango)
    resultado["armor"] = 0.0
    resultado["armor_toughness"] = 0.0
    resultado["knockback_resistance"] = 0.0
    return resultado


def parsear(fqn: str, mapa: dict[str, str]) -> tuple[str | None, dict[str, float | None]]:
    lineas = javap(fqn)
    if not lineas:
        return None, {}

    base = None
    for linea in lineas[:15]:
        m = re.search(r"extends ([\w.$]+)", linea)
        if m:
            base = m.group(1)
            break

    propios: dict[str, float | None] = {}
    for bloque in _metodos(lineas):
        if not any("Attributes.f_" in linea for linea in bloque):
            continue
        pendiente: str | None = None
        pendiente_valor: float | None = None
        for linea in bloque:
            m = re.search(r"Attributes\.(f_\d+_)", linea)
            if m:
                nombre_attr = mapa.get(m.group(1))
                pendiente = nombre_attr.lower() if nombre_attr else None
                pendiente_valor = None
                continue
            if pendiente is None:
                continue
            m = re.search(r"ldc2_w\s+#\d+\s+// double ([\-0-9.E]+)d", linea)
            if m:
                pendiente_valor = float(m.group(1))
                continue
            m = re.search(r"ldc\s+#\d+\s+// float ([\-0-9.E]+)f", linea)
            if m:
                pendiente_valor = float(m.group(1))
                continue
            if "m_22266_" in linea:
                propios.setdefault(pendiente, pendiente_valor)
                pendiente = None
                continue
            if "m_22268_" in linea:
                propios[pendiente] = pendiente_valor
                pendiente = None
                continue
            if not linea.strip().startswith(("getstatic", "ldc", "dup")):
                pendiente = None
    return base, propios


def resolver(fqn: str, mapa: dict[str, str], cache: dict[str, dict[str, float | None]]) -> dict[str, dict]:
    if fqn in cache:
        return cache[fqn]
    base, propios = parsear(fqn, mapa)
    resultado: dict[str, float | None] = {}
    if base and base.startswith(PKG) and base != fqn:
        resultado.update(resolver(base, mapa, cache))
    resultado.update(propios)
    cache[fqn] = resultado
    return resultado


NOTAS = {
    "Zombi": "20 de vida y armadura 2; el no-muerto más lento (0.23). En Difícil pega ~4.5.",
    "Zombi momificado": "Igual que el zombi, pero no se quema de día y aplica Hambre.",
    "Ahogado": "Zombi acuático; puede llevar tridente y nada.",
    "Aldeano zombi": "Zombi con armadura 2; se cura con debilidad + manzana dorada.",
    "Esqueleto": "Pack: 12 de vida (antes 20). Arquero; su cuerpo a cuerpo es flojo.",
    "Errante": "Pack: 12 de vida. Flechas de lentitud.",
    "Esqueleto del Wither": "20 de vida; espada de piedra y efecto Wither.",
    "Creeper": "20 de vida; su daño es la explosión, no el atributo de melee.",
    "Arana": "Pack: 14 de vida (antes 16). Rápida y escala paredes.",
    "Arana de cueva": "12 de vida; aplica veneno.",
    "Lepisma": "8 de vida; llama a más lepismas al ser golpeada.",
    "Endermite": "8 de vida; aparece al usar perlas del End.",
    "Slime": "La vida depende del tamaño; el daño es por contacto.",
    "Cubo de magma": "Vida por tamaño; daño de fuego al contacto.",
    "Ghast": "10 de vida; bola de fuego; el mayor seguimiento (100).",
    "Blaze": "20 de vida y 6 de daño base; ataca con bolas de fuego.",
    "Bruja": "Pack: 20 de vida (antes 26). Combate con pociones.",
    "Saqueador": "24 de vida; ballesta y seguimiento 32.",
    "Vindicador": "24 de vida, 5 base; en Difícil su hacha pega ~19.",
    "Evocador": "24 de vida; invoca Vex y colmillos.",
    "Ilusionista": "32 de vida; ilusiones y arco.",
    "Devastador": "100 de vida, 12 base y 0.75 de resistencia al empuje; montura de saqueadores.",
    "Guardian": "30 de vida; rayo y seguimiento largo.",
    "Guardian anciano": "80 de vida; aplica fatiga de minería.",
    "Shulker": "30 de vida; proyectiles de levitación.",
    "Fantasma": "Pack: 10 de vida (antes 20). Vuela y ataca en picado.",
    "Enderman": "40 de vida y 7 base; se teletransporta y esquiva flechas.",
    "Vex": "14 de vida; atraviesa paredes.",
    "Hoglin": "40 de vida, 6 base y 0.6 de resistencia al empuje.",
    "Zoglin": "40 de vida; inmune al fuego y 0.6 de resistencia al empuje.",
    "Piglin": "16 de vida; trueque y ballesta.",
    "Piglin bruto": "50 de vida y 7 base; hacha y mucha resistencia.",
    "Piglin zombificado": "No parseable (clase sin atributos propios); hereda de Zombi: 20 de vida y 3 de daño.",
    "Gigante": "100 de vida y 50 base; no aparece en supervivencia, solo referencia.",
    "Warden": "500 de vida y 30 base; su resistencia al empuje real es 1.0 (inmune), no capturada por el extractor.",
    "Wither": "300 de vida; jefe. Su daño no es cuerpo a cuerpo.",
    "Dragon del End": "200 de vida; jefe. Ataca con aliento y embestidas.",
}

CLAVES = {c[0] for c in COLUMNAS}

def _escribir(ruta: Path, contenido: str) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(contenido)


def main() -> None:
    mapa = cargar_mapa_atributos()
    defaults = cargar_defaults()
    cache: dict[str, dict[str, float | None]] = {}
    filas = []
    for clase, nombre, grupo in MOBS:
        atributos = resolver(PKG + clase, mapa, cache)
        atributos = {k: (v if v is not None else defaults.get(k)) for k, v in atributos.items()} if atributos else {}
        atributos = {k: v for k, v in atributos.items() if v is not None}
        fila = {
            "mob": nombre,
            "clase": clase,
            "grupo": grupo,
            "vanilla": {k: round(v, 4) for k, v in atributos.items() if k in CLAVES},
        }
        cambios = CAMBIOS_PACK.get(nombre, {})
        efectivo = dict(fila["vanilla"])
        efectivo.update(cambios)
        fila["pack"] = {k: round(v, 4) for k, v in cambios.items()}
        fila["efectivo"] = {k: round(v, 4) for k, v in efectivo.items()}
        fila["nota"] = NOTAS.get(nombre, "")
        filas.append(fila)

    DATOS.mkdir(parents=True, exist_ok=True)
    _escribir(DATOS / "mobs_hostiles_vanilla.json", 
        json.dumps(
            {
                "version": "1.20.1",
                "fuente": "bytecode SRG (javap) + TheOptimizer-MobBalance",
                "nota": "efectivo = vanilla con los cambios del pack aplicados",
                "mobs": filas,
            },
            ensure_ascii=False,
            indent=2,
        ) + "\n",
    )

    def fmt(f: dict, clave: str) -> str:
        valor = f["efectivo"].get(clave)
        return "-" if valor is None else ("%g" % valor)

    lineas = [
        "# Mobs hostiles vanilla (1.20.1): atributos base y efecto del pack",
        "",
        "> Generado por `herramientas/extraer_atributos_vanilla.py`. No editar a mano.",
        "",
        "## Cómo se obtuvieron estos datos",
        "",
        "1. Se lee el **bytecode** del servidor Forge (jar SRG) con `javap`, sin depender de la wiki.",
        "2. Cada entidad define sus atributos en un método estático que devuelve `AttributeSupplier$Builder`;",
        "   las constantes aparecen como `getstatic Attributes.f_XXXX_` + `ldc2_w` + `Builder.m_22268_(Attribute, D)`.",
        "3. La **herencia** se resuelve por la cabecera `extends` (p. ej. Zombi → Monster → PathfinderMob → Mob → LivingEntity).",
        "4. Los atributos añadidos sin valor (`Builder.m_22266_`) usan el **valor por defecto** del atributo,",
        "   que se extrae del inicializador estático de `Attributes`.",
        "5. Se cruza con el único mod del pack que toca atributos de hostiles:",
        "   `TheOptimizer-MobBalance` (`EntityAttributeModificationEvent`).",
        "",
        "Reejecutar: `python herramientas/extraer_atributos_vanilla.py`.",
        "",
        "## Cambios del pack (MobBalance)",
        "",
        "| Mob | Vida vanilla | Vida pack |",
        "|---|---:|---:|",
    ]
    for nombre, cambio in CAMBIOS_PACK.items():
        fila = next(f for f in filas if f["mob"] == nombre)
        vv = fila["vanilla"].get("max_health")
        lineas.append(f"| {nombre} | {('%g' % vv) if vv is not None else '-'} | {'%g' % cambio['max_health']} |")

    lineas += [
        "",
        "## Hostiles (no jefes)",
        "",
        "| Mob | Vida vanilla | Vida pack | Daño | Armadura | Dureza | Res. empuje | Velocidad | Seguimiento |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for f in filas:
        if f["grupo"] != "hostil":
            continue
        vida_vanilla = f["vanilla"].get("max_health")
        vida_pack = f["efectivo"].get("max_health")
        vv = "-" if vida_vanilla is None else ("%g" % vida_vanilla)
        vp = "-" if vida_pack is None else ("%g" % vida_pack)
        cambio = " *(pack)*" if "max_health" in f["pack"] else ""
        lineas.append(
            f"| {f['mob']} | {vv} | {vp}{cambio} | {fmt(f,'attack_damage')} | "
            f"{fmt(f,'armor')} | {fmt(f,'armor_toughness')} | {fmt(f,'knockback_resistance')} | "
            f"{fmt(f,'movement_speed')} | {fmt(f,'follow_range')} |"
        )

    lineas += [
        "",
        "## Mini-jefes",
        "",
        "| Mob | Vida vanilla | Vida pack | Daño | Armadura | Dureza | Res. empuje | Velocidad | Seguimiento |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for f in filas:
        if f["grupo"] != "mini-jefe":
            continue
        vida_vanilla = f["vanilla"].get("max_health")
        vida_pack = f["efectivo"].get("max_health")
        vv = "-" if vida_vanilla is None else ("%g" % vida_vanilla)
        vp = "-" if vida_pack is None else ("%g" % vida_pack)
        cambio = " *(pack)*" if "max_health" in f["pack"] else ""
        lineas.append(
            f"| {f['mob']} | {vv} | {vp}{cambio} | {fmt(f,'attack_damage')} | "
            f"{fmt(f,'armor')} | {fmt(f,'armor_toughness')} | {fmt(f,'knockback_resistance')} | "
            f"{fmt(f,'movement_speed')} | {fmt(f,'follow_range')} |"
        )

    lineas += [
        "",
        "## Jefes (solo referencia, fuera del análisis de no jefes)",
        "",
        "| Mob | Vida | Daño | Armadura | Res. empuje | Velocidad | Seguimiento |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for f in filas:
        if f["grupo"] != "jefe":
            continue
        lineas.append(
            f"| {f['mob']} | {fmt(f,'max_health')} | {fmt(f,'attack_damage')} | {fmt(f,'armor')} | "
            f"{fmt(f,'knockback_resistance')} | {fmt(f,'movement_speed')} | {fmt(f,'follow_range')} |"
        )

    lineas += [
        "",
        "## Daño cuerpo a cuerpo por dificultad",
        "",
        "El atributo `danio` se escala al golpear: ×0.5 (Fácil), ×1.0 (Normal), ×1.5 (Difícil).",
        "",
        "| Mob | Base | Fácil | Normal | Difícil |",
        "|---|---:|---:|---:|---:|",
    ]
    for f in filas:
        if f["grupo"] == "jefe":
            continue
        danio = f["efectivo"].get("attack_damage")
        if danio is None:
            continue
        lineas.append(
            f"| {f['mob']} | {'%g' % danio} | {'%g' % round(danio * 0.5, 2)} | "
            f"{'%g' % round(danio, 2)} | {'%g' % round(danio * 1.5, 2)} |"
        )

    lineas += [
        "",
        "## Notas por mob",
        "",
    ]
    for nombre, nota in NOTAS.items():
        lineas.append(f"- **{nombre}**: {nota}")

    lineas += [
        "",
        "## Limitaciones conocidas",
        "",
        "- `danio` es el ataque **base**; la dificultad lo escala al golpear (ver tabla anterior).",
        "- **Creeper, Ghast, Blaze, Shulker, Slime y Cubo de magma** no tienen daño cuerpo a cuerpo:",
        "  usan explosión, bola de fuego, proyectil o daño por tamaño/contacto, que no son atributos.",
        "- La vida de **Slime** y **Cubo de magma** depende del tamaño (la tabla muestra el atributo base).",
        "- **Warden**: su resistencia al empuje real es 1.0 (inmune); el extractor no la captura porque la",
        "  asigna por una vía distinta al patrón `add(Attribute, valor)`.",
        "- **Piglin zombificado** no se pudo parsear (su clase no define atributos); hereda de Zombi: 20 de vida, 3 de daño.",
        "- **Gigante** está incluido como referencia, pero no aparece en supervivencia.",
        "- El daño de los proyectiles (flechas de esqueleto, bolas de blaze) y los efectos (veneno de araña de",
        "  cueva, wither) no son atributos y no están en esta tabla.",
        "",
        "## Familias de comportamiento (para balance)",
        "",
        "| Familia | Mobs |",
        "|---|---|",
        "| No-muertos básicos | Zombi, Husk, Ahogado, Aldeano zombi, Esqueleto, Errante, Esqueleto del Wither |",
        "| Artrópodos | Araña, Araña de cueva, Lepisma, Endermite |",
        "| Nether | Blaze, Ghast, Cubo de magma, Piglin, Piglin bruto, Hoglin, Zoglin, Piglin zombificado |",
        "| Saqueadores | Saqueador, Vindicador, Evocador, Ilusionista, Bruja, Devastador |",
        "| Acuáticos | Ahogado, Guardián, Guardián anciano |",
        "| Especiales | Creeper, Enderman, Shulker, Fantasma, Vex, Slime, Warden |",
        "",
    ]
    _escribir(DOCS / "MOBS_HOSTILES_VANILLA.md", "\n".join(lineas) + "\n")
    print(f"mobs extraidos: {len(filas)}")
    faltan = [f["mob"] for f in filas if "max_health" not in f["vanilla"]]
    if faltan:
        print("sin vida extraida (revisar): " + ", ".join(faltan))


if __name__ == "__main__":
    main()
