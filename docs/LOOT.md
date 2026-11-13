# Botín activo — migración YUNG’s 1.24.4

Registro: **36 entradas SHA-256** en loot.json (27 anteriores y 9 nuevas: cuatro tablas, cuatro modifiers y su registro global). AdventureLoot 1.2.0 conserva byte por byte los overrides vanilla de cofres, mobs y cobre. Se añade al pack distribuido, al servidor y a las carpetas activas de PrismLauncher.

Los modifiers usan irons_spellbooks:append_loot, condiciones forge:loot_table_id y un registro replace=false. No reemplazan tablas de YUNG’s ni sus objetos ambientales. Los niveles son disjuntos; la esencia adicional se limita a Better Nether Fortresses.

| Nivel | Libro permitido, probabilidad | Recompensa arcana, probabilidad | Pesos de materiales |
|---|---:|---:|---|
| 1 | 35% | 65% | common_ink 6, uncommon_ink 3, arcane_essence 4, scroll 2 |
| 2 | 60% | 85% | uncommon_ink 6, rare_ink 3, blank_rune 3, scroll 4 |
| 3 | 80% | 100% | rare_ink 10, epic_ink 4, legendary_ink 1, blank_rune 5, scroll 4 |

Cada pool realiza una tirada; los tres libros tienen igual peso y siempre nivel I: Irrompibilidad, Botín, Eficiencia. Ninguna entrada nueva genera otros encantamientos o botellas de XP. Los pergaminos usan randomize_spell con calidad máxima 0.35/0.55/0.7. Las fortalezas tienen además 50% de una esencia cinder_essence. Legendary ink tiene peso 1 de 24, aproximadamente 4.17% por tirada del tercer nivel.

## Delegaciones y ausencias verificadas

Better Mineshafts no tiene tablas propias de cofres: SmallTunnel usa BuiltInLootTables.f_78759_, minecraft:chests/abandoned_mineshaft. Ya lo cubren el override y el modifier arcano existentes; no se duplica la inyección. YUNG’s Extras usa BuiltInLootTables.f_276662_, archaeology/desert_well; no es un cofre y no se altera. Cave Biomes no incluye tablas propias de cofres ni referencias a BuiltInLootTables en este JAR. La integración Cataclysm/fortalezas tampoco añade tablas propias. Better Strongholds conserva sus tablas y la integración previa.

No declarados ni instalados, por decisión del usuario: Better Jungle Temples, Better Caves, Bridges y Traveler’s Titles. No se simula cobertura para ellos. TerraBlender 3.0.1.11 ya estaba declarado y se sincroniza porque Cave Biomes lo necesita.

## Rutas exactas de los 29 cofres

### Nivel 1

- `betterdungeons:skeleton_dungeon/chests/common`
- `betterdungeons:small_dungeon/chests/loot_piles`
- `betterdungeons:small_nether_dungeon/chests/common`
- `betterdungeons:spider_dungeon/chests/egg_room`
- `betterdungeons:zombie_dungeon/chests/common`
- `betterwitchhuts:chests/hut_0`

### Nivel 2

- `betterdeserttemples:chests/food_storage`
- `betterdeserttemples:chests/lab`
- `betterdeserttemples:chests/library`
- `betterdeserttemples:chests/pharaoh_hidden`
- `betterdeserttemples:chests/pot`
- `betterdeserttemples:chests/statue`
- `betterdeserttemples:chests/storage`
- `betterdeserttemples:chests/tomb`
- `betterdeserttemples:chests/tomb_pharaoh`
- `betterdeserttemples:chests/wardrobe`
- `betterdungeons:skeleton_dungeon/chests/middle`
- `betterdungeons:zombie_dungeon/chests/special`
- `betterdungeons:zombie_dungeon/chests/tombstone`

### Nivel 3

- `betterfortresses:chests/beacon`
- `betterfortresses:chests/extra`
- `betterfortresses:chests/hall`
- `betterfortresses:chests/keep`
- `betterfortresses:chests/obsidian`
- `betterfortresses:chests/puzzle`
- `betterfortresses:chests/quarters`
- `betterfortresses:chests/storage`
- `betterfortresses:chests/worship`
- `betteroceanmonuments:chests/upper_side_chamber`

## Verificación

python -B -m botin_magia_aventura.probar valida preservación de overrides, separación de niveles y libros permitidos. verificar_estado.ps1 valida los hashes exactos del registro. Los IDs de tintas, runas, pergaminos y esencias se contrastaron con el registro real de Iron’s 3.16.3.

### Delegación adicional de fortaleza

`minecraft:chests/nether_bridge` recibe el nivel 3 y esencia igual que los cofres propios de Better Fortresses, sin reemplazar su tabla original. Son 29 tablas propias y una delegación vanilla (30 IDs en condiciones). El inventario de archivos y hashes de JAR está en [LOOT_SOURCE_AUDIT.md](LOOT_SOURCE_AUDIT.md). Se retiraron también cuatro definiciones inactivas de intercambios de Goblin Traders que aún conservaban botellas de XP; no se altera ningún override vanilla.
