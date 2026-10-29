# Versioning and deliverables

- Initial functional release: v1.0.
- Documentation correction, parameter tweak, minor change: v1.1, v1.2, ...
- Structural or behavior-breaking redesign: v2.0, v3.0, ...
- Never overwrite old releases silently.
- Naming: `<project-slug>_FBD_v<major>.<minor>.pdf`; include source JSON if used.
- Record version, date (dd-mm-yyyy), change summary, compatibility, verification status and known limitations.
- For a correction, show exactly which blocks/connections/parameters changed.
- Keep native `.lsc` as a separate optional artifact only when actually generated and verified in the supported Siemens software.