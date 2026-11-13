import json
import urllib.request
import urllib.parse
import hashlib
import os

mods_dir = r"C:\Users\Metabodiru\Desktop\AmpereRepo\mods"

# List of the 25 unmatched third-party mods
unmatched_files = [
    "FastLeafDecay-32.jar",
    "JustEnoughResources-1.20.1-1.4.0.247.jar",
    "KaleidoscopeCavescookery-1.0.3-1.20.1Forge.jar",
    "Kiwi-1.20.1-Forge-11.10.3.jar",
    "PresenceFootsteps-1.20.1-1.9.1-beta.1.jar",
    "alexs_caves_spellbooks-1.2.0.jar",
    "alltheleaks-1.1.4+1.20.1-forge.jar",
    "alshanex_familiars-1.20.1_v4.1.0.jar",
    "alternate_current-mc1.20-1.7.0.jar",
    "balm-forge-1.20.1-7.3.44.jar",
    "buildinggadgets2-1.0.8.jar",
    "cleanswing-1.20-1.8.jar",
    "familiarslib-1.20.1-1.9.jar",
    "framework-forge-1.20.1-0.8.0.jar",
    "geckolib-forge-1.20.1-4.8.4.jar",
    "goblintraders-forge-1.20.1-1.11.5.jar",
    "irons_spellbooks-1.20.1-3.16.3.jar",
    "kaleidoscope_flora-0.3.5.1-all.jar",
    "kaleidoscope_nether-1.1.8-forge+mc1.20.1.jar",
    "kaleidoscopecookery-1.6.0-forge+mc1.20.1.jar",
    "laserio-1.6.8.jar",
    "notrample-1.20.1-1.0.1.jar",
    "simpletomb-1.20.1-1.3.0.jar",
    "sound-physics-remastered-forge-1.20.1-1.5.1.jar",
    "structure_layout_optimizer-forge-1.0.11.jar"
]

results = []

for filename in unmatched_files:
    path = os.path.join(mods_dir, filename)
    size_mb = round(os.path.getsize(path) / (1024 * 1024), 2)
    # Extract sensible search terms
    term = filename.lower()
    term = term.replace(".jar", "")
    for stop in ["-forge", "_forge", "-mc1.20.1", "-1.20.1", "-1.20", ".forge"]:
        term = term.replace(stop, "")
    term = term.split("-")[0].split("_")[0]
    
    url = f"https://api.modrinth.com/v2/search?query={urllib.parse.quote(term)}&limit=3"
    req = urllib.request.Request(url, headers={"User-Agent": "TheOptimizer-Auditor/1.0"})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            hits = data.get("hits", [])
    except Exception as e:
        hits = []

    results.append({
        "file": filename,
        "size_mb": size_mb,
        "term": term,
        "hits": [{"title": h["title"], "slug": h["slug"], "loaders": h.get("loaders", []), "versions": h.get("versions", [])} for h in hits]
    })

with open(r"gestion\datos\unmatched_search_detailed.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("Detailed search finished.")
