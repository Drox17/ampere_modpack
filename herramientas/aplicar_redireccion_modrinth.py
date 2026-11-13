import json
import os
import subprocess

repo_dir = r"C:\Users\Metabodiru\Desktop\AmpereRepo"
mods_dir = os.path.join(repo_dir, "mods")

with open(r"gestion\datos\modrinth_redirect_plan.json", "r", encoding="utf-8") as f:
    plan = json.load(f)

print(f"Applying redirect plan for {len(plan)} mods...")

written_pw = 0
deleted_jars = 0

for item in plan:
    pw_path = os.path.join(mods_dir, item["pw_toml_filename"])
    with open(pw_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(item["pw_toml_content"])
    written_pw += 1

    jar_path = os.path.join(mods_dir, item["jar"])
    if os.path.exists(jar_path):
        os.remove(jar_path)
        deleted_jars += 1

print(f"Written {written_pw} .pw.toml files.")
print(f"Removed {deleted_jars} raw .jar files from AmpereRepo/mods.")

# Verify remaining jars
remaining_jars = [f for f in os.listdir(mods_dir) if f.endswith(".jar")]
remaining_pws = [f for f in os.listdir(mods_dir) if f.endswith(".pw.toml")]

print(f"Remaining local .jar files in repo: {len(remaining_jars)}")
print(f"Total .pw.toml files in repo: {len(remaining_pws)}")

# Run packwiz refresh
res = subprocess.run(["packwiz", "refresh"], cwd=repo_dir, capture_output=True, text=True)
print("packwiz refresh output:")
print(res.stdout)
if res.stderr:
    print("packwiz refresh error:", res.stderr)

if res.returncode != 0:
    raise RuntimeError("packwiz refresh failed!")

print("packwiz refresh SUCCESS!")
