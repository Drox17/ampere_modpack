import urllib.request
import json

slugs = [
    "irons-spells-n-spellbooks",
    "alternate-current",
    "just-enough-resources-jer",
    "structure-layout-optimizer",
    "kaleidoscope-cookery",
    "kaleidoscope-nether"
]

for slug in slugs:
    url = f"https://api.modrinth.com/v2/project/{slug}/version?game_versions=%5B%221.20.1%22%5D&loaders=%5B%22forge%22%5D"
    req = urllib.request.Request(url, headers={"User-Agent": "TheOptimizer-Auditor/1.0"})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print(f"[{slug}] Found {len(data)} Forge 1.20.1 versions:")
            for v in data[:3]:
                files = [f["filename"] for f in v["files"]]
                print(f"   {v['version_number']}: {files}")
    except Exception as e:
        print(f"[{slug}] Error: {e}")
