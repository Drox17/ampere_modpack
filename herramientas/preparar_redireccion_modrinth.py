import json
import urllib.request
import urllib.parse
import os
import time

repo_mods_dir = r"C:\Users\Metabodiru\Desktop\AmpereRepo\mods"

# 1. Load exact 92 matches
with open(r"gestion\datos\modrinth_audit.json", "r", encoding="utf-8") as f:
    audit_data = json.load(f)

# 2. Load extra 10 matches
with open(r"gestion\datos\extra_10_matched.json", "r", encoding="utf-8") as f:
    extra_10 = json.load(f)

# Re-read version files for the 92 matches to have full version object (with sha512 and id)
jar_to_sha1 = {}
for j in audit_data["exact_matches"].keys():
    p = os.path.join(repo_mods_dir, j)
    if os.path.exists(p):
        import hashlib
        jar_to_sha1[j] = hashlib.sha1(open(p, "rb").read()).hexdigest()

sha1_to_jar = {v: k for k, v in jar_to_sha1.items()}
all_sha1s = list(jar_to_sha1.values())

exact_full_versions = {}
for i in range(0, len(all_sha1s), 50):
    batch = all_sha1s[i:i+50]
    body = json.dumps({"hashes": batch, "algorithm": "sha1"}).encode("utf-8")
    req = urllib.request.Request(
        "https://api.modrinth.com/v2/version_files",
        data=body,
        headers={"User-Agent": "TheOptimizer-Auditor/1.0", "Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        for h, v in res.items():
            jar_name = sha1_to_jar[h]
            exact_full_versions[jar_name] = v
    time.sleep(0.5)

print(f"Fetched full version data for {len(exact_full_versions)} exact matches.")

# Combine all 102 target mods
mods_to_redirect = {}

for jar, v in exact_full_versions.items():
    primary_file = v["files"][0]
    mods_to_redirect[jar] = {
        "project_id": v["project_id"],
        "version_id": v["id"],
        "version_name": v["name"],
        "filename": primary_file["filename"],
        "url": primary_file["url"],
        "sha512": primary_file["hashes"]["sha512"]
    }

for jar, d in extra_10.items():
    mods_to_redirect[jar] = {
        "project_id": d["project_id"],
        "version_id": d["version_id"],
        "version_name": d["name"],
        "filename": d["filename"],
        "url": d["url"],
        "sha512": d["hashes"]["sha512"]
    }

print(f"Total mods to redirect: {len(mods_to_redirect)}")

# Fetch project metadata (slug, title, client_side, server_side) in batches
project_ids = list(set(m["project_id"] for m in mods_to_redirect.values()))
print(f"Unique projects: {len(project_ids)}")

projects_metadata = {}
for i in range(0, len(project_ids), 50):
    batch = project_ids[i:i+50]
    encoded_ids = urllib.parse.quote(json.dumps(batch))
    url = f"https://api.modrinth.com/v2/projects?ids={encoded_ids}"
    req = urllib.request.Request(url, headers={"User-Agent": "TheOptimizer-Auditor/1.0"})
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        for p in res:
            projects_metadata[p["id"]] = p
    time.sleep(0.5)

print(f"Fetched metadata for {len(projects_metadata)} projects.")

# Build plan
plan = []
for jar, m in sorted(mods_to_redirect.items()):
    p_meta = projects_metadata.get(m["project_id"], {})
    slug = p_meta.get("slug", m["project_id"])
    title = p_meta.get("title", m["version_name"])
    
    # side
    cs = p_meta.get("client_side", "required")
    ss = p_meta.get("server_side", "required")
    if cs == "unsupported":
        side = "server"
    elif ss == "unsupported":
        side = "client"
    else:
        side = "both"
        
    pw_toml_content = f'''name = "{title}"
filename = "{m['filename']}"
side = "{side}"

[download]
url = "{m['url']}"
hash-format = "sha512"
hash = "{m['sha512']}"

[update]
[update.modrinth]
mod-id = "{m['project_id']}"
version = "{m['version_id']}"
'''
    plan.append({
        "jar": jar,
        "slug": slug,
        "pw_toml_filename": f"{slug}.pw.toml",
        "pw_toml_content": pw_toml_content
    })

with open(r"gestion\datos\modrinth_redirect_plan.json", "w", encoding="utf-8") as f:
    json.dump(plan, f, indent=2, ensure_ascii=False)

print(f"Generated redirect plan for {len(plan)} mods in gestion/datos/modrinth_redirect_plan.json")
