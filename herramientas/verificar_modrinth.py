import os
import hashlib
import json
import urllib.request
import time

mods_dir = r"C:\Users\Metabodiru\Desktop\AmpereRepo\mods"
jars = sorted([f for f in os.listdir(mods_dir) if f.endswith(".jar")])
print(f"Total JAR files: {len(jars)}")

file_hashes = {}
file_sizes = {}
for j in jars:
    path = os.path.join(mods_dir, j)
    data = open(path, "rb").read()
    file_hashes[j] = hashlib.sha1(data).hexdigest()
    file_sizes[j] = len(data)

total_bytes = sum(file_sizes.values())
print(f"Total size: {total_bytes / (1024*1024):.2f} MB")

# Query Modrinth version_files by SHA1 in batches of 50
hash_to_jar = {v: k for k, v in file_hashes.items()}
all_hashes = list(file_hashes.values())

exact_matches = {}
for i in range(0, len(all_hashes), 50):
    batch = all_hashes[i:i+50]
    body = json.dumps({"hashes": batch, "algorithm": "sha1"}).encode("utf-8")
    req = urllib.request.Request(
        "https://api.modrinth.com/v2/version_files",
        data=body,
        headers={"User-Agent": "TheOptimizer-Auditor/1.0", "Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as response:
        res = json.loads(response.read().decode("utf-8"))
        for h, v_data in res.items():
            jar_name = hash_to_jar[h]
            exact_matches[jar_name] = v_data
    time.sleep(0.5)

matched_bytes = sum(file_sizes[j] for j in exact_matches)
print(f"Exact hash matches on Modrinth: {len(exact_matches)} / {len(jars)} ({matched_bytes / (1024*1024):.2f} MB)")

unmatched = [j for j in jars if j not in exact_matches]
print(f"Unmatched count: {len(unmatched)}")

out_data = {
    "exact_matches": {},
    "unmatched": unmatched
}

for j, v_data in exact_matches.items():
    primary_file = v_data["files"][0]
    out_data["exact_matches"][j] = {
        "project_id": v_data.get("project_id"),
        "version_number": v_data.get("version_number"),
        "name": v_data.get("name"),
        "url": primary_file.get("url"),
        "filename": primary_file.get("filename"),
        "size_mb": round(file_sizes[j] / (1024 * 1024), 2)
    }

with open(r"gestion\datos\modrinth_audit.json", "w", encoding="utf-8") as f:
    json.dump(out_data, f, indent=2, ensure_ascii=False)

print("Saved report to gestion/datos/modrinth_audit.json")
