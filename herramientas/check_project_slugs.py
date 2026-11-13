import urllib.request
import json
import urllib.parse

mods_to_test = {
    "irons_spellbooks": "irons-spells-n-spellbooks",
    "goblintraders": "goblin-traders",
    "framework": "framework",
    "buildinggadgets2": "building-gadgets-2",
    "laserio": "laserio",
    "alternate_current": "alternate-current",
    "alltheleaks": "all-the-leaks",
    "simpletomb": "simple-tomb",
    "cleanswing": "clean-swing-through-grass",
    "jer": "just-enough-resources-jer",
    "presencefootsteps": "presence-footsteps",
    "structure_layout_optimizer": "structure-layout-optimizer",
    "alexs_caves_spellbooks": "alexs-caves-spells-n-spellbooks",
    "kaleidoscope": "kaleidoscope-cookery"
}

results = {}

for name, slug in mods_to_test.items():
    url = f"https://api.modrinth.com/v2/project/{slug}"
    req = urllib.request.Request(url, headers={"User-Agent": "TheOptimizer-Auditor/1.0"})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            results[name] = {
                "found": True,
                "title": data.get("title"),
                "slug": data.get("slug"),
                "game_versions": data.get("game_versions", [])[:5],
                "loaders": data.get("loaders", [])
            }
    except urllib.error.HTTPError as e:
        results[name] = {"found": False, "status": e.code}
    except Exception as e:
        results[name] = {"found": False, "error": str(e)}

for name, info in results.items():
    if info.get("found"):
        print(f"[FOUND] {name:25} -> {info['title']} ({info['slug']}) - Loaders: {info['loaders']}")
    else:
        print(f"[NOT FOUND] {name:25} -> Status: {info.get('status', info.get('error'))}")
