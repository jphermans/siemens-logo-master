---
name: siemens-logo-master
description: Design, verify, explain and document Siemens LOGO! Soft Comfort FBD circuits in Dutch, including I/O tables, official block names, beginner instructions, landscape PDF diagrams and version control. Use for LOGO! PLC circuits, timers, shutters, motor control and troubleshooting.
---
# Siemens LOGO! Master

Version: 1.1.0. Communicate in Dutch and use official Siemens terminology for the **verified target software version**.

## Mandatory workflow

1. Determine actual LOGO! hardware, expansion modules, supply voltage, firmware and LOGO! Soft Comfort version. V8.3 is a reference target, not proof of hardware compatibility.
2. Write behavior requirements including automatic/manual modes, priority rules, simultaneous events, timer limits, power-on/restart behavior, sensor failures, and physical safety.
3. Consult `references/sources.md`, then check applicable official Siemens manuals and comparable examples. Record URLs and confidence. Never claim research you could not perform.
4. Verify every block name, editor category, terminal name and parameter against the relevant version following `references/block-verification.md`. Do not invent unavailable blocks or connections.
5. Design a readable left-to-right FBD with I/Q/AI/AQ mapping, B001... identifiers and unambiguous source-pin → destination-pin instructions. Follow `references/design-rules.md`.
6. Review normal and edge cases with `references/test-matrix.md`. Report status honestly as simulated (only if actually run), theoretically reviewed or unverified.
7. Explain each block, connection and parameter in simple Dutch so a beginner can recreate the FBD.
8. Produce A4 **landscape** PDF with diagram, legend, I/O table, block/parameter lists, detailed wiring instructions, test cases, sources, warnings and revisions. Follow `references/pdf-style.md`. Use `scripts/render_report.py` for illustrative output if the JSON contract fits.
9. Version project files `ProjectName_FBD_v1.0.pdf`, minor fixes v1.1, major design changes v2.0. Preserve previous versions. See `references/versioning.md`.
10. Summarize hardware, software, exact I/O and block count, verification level, assumptions and generated file links.

## Hard prohibitions

- Never call a generated PDF an authentic Soft Comfort printout unless exported by that software.
- Never claim an `.lsc` is native/importable without creating and verifying it using compatible tools.
- Never say a physical circuit is safe based only on a logic diagram.
- Never activate opposed motor directions simultaneously; require independent physical interlocks where needed.
- Never confuse generic IEC block names with verified Siemens GUI labels.
- Never present unexamined technical documents as verified sources.

## Bundled resources

- `references/sources.md`
- `references/block-verification.md`
- `references/design-rules.md`
- `references/test-matrix.md`
- `references/pdf-style.md`
- `references/versioning.md`
- `assets/example_circuit.json`
- `scripts/render_report.py`
- `scripts/validate_skill.py`

Example: “Maak een LOGO! 8.3 rolluikschakeling met zonsopgang of 07:00 omhoog, zonsondergang omlaag, handbediening, 35 seconden maximumlooptijd en onmiddellijke stop bij tegengestelde druk.”

Always distinguish **documented facts**, **assumptions**, **theoretical reviews**, and **actually executed tests**.