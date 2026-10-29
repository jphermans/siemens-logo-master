#!/usr/bin/env python3
"""Build an Agent Zero-compatible ZIP with SKILL.md at archive root."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parents[1]
destination = root / "Siemens_LOGO_Master_Skill_v1.1_A0.zip"
included = [root / "SKILL.md"]
for directory, suffixes in {
    "references": {".md"},
    "scripts": {".py"},
    "assets": {".json"}
}.items():
    included.extend(sorted(p for p in (root / directory).rglob("*") if p.is_file() and p.suffix in suffixes))
with ZipFile(destination, "w", ZIP_DEFLATED) as archive:
    for path in included:
        archive.write(path, path.relative_to(root).as_posix())
print(destination)
