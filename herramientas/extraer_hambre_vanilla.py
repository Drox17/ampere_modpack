"""Extrae las fuentes vanilla que consumen hambre/saturacion desde el bytecode SRG.

Busca las llamadas a:
  - Player.causeFoodExhaustion(float)   -> m_36366_
  - FoodData.addExhaustion(float)       -> m_38703_
y saca la constante float que se pasa en cada punto, con la clase y el metodo que la origina.

Salida: docs/HAMBRE_VANILLA.md y datos/hambre_vanilla.json
"""

from __future__ import annotations

import json
import re
import subprocess
import zipfile
from pathlib import Path

JAVAP = r"C:\Users\Metabodiru\AppData\Roaming\PrismLauncher\java\java-runtime-gamma\bin\javap.exe"
JAR = r"C:\Users\Metabodiru\AppData\Roaming\PrismLauncher\instances\TheOptimizer\gestion\datos\servidor\forge-instalado\libraries\net\minecraft\server\1.20.1-20230612.114412\server-1.20.1-20230612.114412-srg.jar"

RAIZ = Path(__file__).resolve().parents[1]
DATOS = RAIZ / "datos"
DOCS = RAIZ / "docs"

REFERENCIAS = {
    "m_36399_": "Player.causeFoodExhaustion (agotamiento del jugador)",
    "m_38703_": "FoodData.addExhaustion (agotamiento del sistema de comida)",
}

# fconst_x equivale a constantes float
FCONST = {"fconst_0": 0.0, "fconst_1": 1.0, "fconst_2": 2.0}


def clases_candidatas() -> list[str]:
    candidatas = []
    with zipfile.ZipFile(JAR) as z:
        for nombre in z.namelist():
            if not nombre.endswith(".class") or "$" in nombre:
                continue
            datos = z.read(nombre)
            if all(ref.encode() not in datos for ref in REFERENCIAS):
                continue
            candidatas.append(nombre[:-6].replace("/", "."))
    return sorted(candidatas)


def javap(clase: str) -> list[str]:
    resultado = subprocess.run(
        [JAVAP, "-p", "-c", "-classpath", JAR, clase],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    return resultado.stdout.splitlines() if resultado.returncode == 0 else []


def extraer() -> list[dict]:
    filas: list[dict] = []
    for clase in clases_candidatas():
        lineas = javap(clase)
        metodo = "?"
        pendiente: float | None = None
        for linea in lineas:
            if re.match(r"^  [A-Za-z].*\(.*\).*;$", linea):
                metodo = linea.strip()
                pendiente = None
                continue
            m = re.search(r"ldc\s+#\d+\s+// float ([\-0-9.E]+)f", linea)
            if m:
                pendiente = float(m.group(1))
                continue
            m = re.search(r"(fconst_[012])\b", linea)
            if m:
                pendiente = FCONST[m.group(1)]
                continue
            for ref, descripcion in REFERENCIAS.items():
                if ref in linea and "invoke" in linea:
                    filas.append({
                        "clase": clase.split(".")[-1],
                        "metodo": metodo,
                        "via": descripcion,
                        "valor": pendiente,
                    })
                    pendiente = None
                    break
    return filas


def _escribir(ruta: Path, contenido: str) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(contenido)


def main() -> None:
    filas = extraer()
    DATOS.mkdir(parents=True, exist_ok=True)
    _escribir(DATOS / "hambre_vanilla.json", 
        json.dumps({"version": "1.20.1", "fuente": "bytecode SRG", "llamadas": filas},
                   ensure_ascii=False, indent=2) + "\n",
    )
    _escribir(DOCS / "HAMBRE_VANILLA_EXTRACCION.md", 
        "\n".join([
            "# Fuentes vanilla de agotamiento (1.20.1)",
            "",
            "Extraído del bytecode con `javap`: cada llamada a `Player.causeFoodExhaustion(float)` o",
            "`FoodData.addExhaustion(float)` con la constante que pasa.",
            "",
            "| Clase | Método | Vía | Valor |",
            "|---|---|---|---:|",
            *[f"| {f['clase']} | {f['metodo'][:60]} | {f['via']} | {'-' if f['valor'] is None else f['valor']} |" for f in filas],
            "",
        ]) + "\n",
    )
    print(f"llamadas extraidas: {len(filas)}")


if __name__ == "__main__":
    main()
