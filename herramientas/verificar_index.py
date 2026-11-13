import tomllib

data = tomllib.load(open(r"C:\Users\Metabodiru\Desktop\AmpereRepo\index.toml", "rb"))
mods = [f for f in data["files"] if f["file"].startswith("mods/")]
pws = [f for f in mods if f["file"].endswith(".pw.toml")]
jars = [f for f in mods if f["file"].endswith(".jar")]
print(f"Total mods in index: {len(mods)}")
print(f"Metadata files (.pw.toml): {len(pws)}")
print(f"Local JAR files (.jar): {len(jars)}")
print("Local JAR list:")
for j in jars:
    print("  -", j["file"])
