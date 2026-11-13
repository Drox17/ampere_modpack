import urllib.request
import json

slugs = [
    ("geckolib", "geckolib-forge-1.20.1-4.8.4.jar"),
    ("balm", "balm-forge-1.20.1-7.3.44.jar"),
    ("sound-physics-remastered", "sound-physics-remastered-forge-1.20.1-1.5.1.jar"),
    ("alshanexs-familiars", "alshanex_familiars-1.20.1_v4.1.0.jar"),
    ("familiarslib", "familiarslib-1.20.1-1.9.jar"),
    ("notrample", "notrample-1.20.1-1.0.1.jar"),
    ("kiwi", "Kiwi-1.20.1-Forge-11.10.3.jar"),
    ("fastleafdecay", "FastLeafDecay-32.jar")
]

for slug, local_file in slugs:
    url = f"https://api.modrinth.com/v2/project/{slug}/version?game_versions=%5B%221.20.1%22%5D&loaders=%5B%22forge%22%5D"
    req = urllib.request.Request(url, headers={"User-Agent": "TheOptimizer-Auditor/1.0"})
    try:
        with urllib.request.urlopen(req) as resp:
            versions = json.loads(resp.read().decode("utf-8"))
            filenames = []
            for v in versions:
                for f in v["files"]:
                    filenames.append(f["filename"])
            print(f"[{slug}] (local: {local_file})")
            print(f"  Available on Modrinth for Forge 1.20.1 ({len(versions)} versions): {filenames[:5]}")
    except Exception as e:
        print(f"[{slug}] Error: {e}")
