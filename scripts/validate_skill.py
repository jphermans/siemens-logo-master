#!/usr/bin/env python3
"""Validate portable skill structure without third-party dependencies."""
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
s=root/'SKILL.md'
t=s.read_text(encoding='utf-8')
assert t.startswith('---\n'), 'Missing YAML frontmatter'
head=t.split('---',2)[1]
assert re.search(r'^name: siemens-logo-master$',head,re.M)
assert re.search(r'^description: .+',head,re.M)
for p in ['references/sources.md','references/block-verification.md','references/design-rules.md','references/test-matrix.md','references/pdf-style.md','references/versioning.md','scripts/render_report.py','assets/example_circuit.json']:
    assert (root/p).is_file(),p
print('OK: valid portable SKILL.md layout and bundled references')