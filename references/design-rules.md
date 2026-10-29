# Circuit design and safety rules

- Start with an I/O allocation table: I1.., Q1.., AI/AQ when relevant; descriptions, active level, voltage and terminals.
- Build a truth table/state-transition table before drawing when manual and automatic commands overlap.
- Show every connection as `SOURCE.output -> DESTINATION.input` with B identifiers and exact pin labels. No implied wiring.
- Keep logical diagram separate from field wiring and mains-voltage power circuits.
- Define behavior at power-up, power loss, brownout, reboot, missing sensor, stuck button and simultaneous inputs.
- For bidirectional motors: interlock opposite directions logically **and** use suitable electrical/mechanical protection as required by the application. Add changeover/dead time if necessary. Stop-first behavior must be explicitly modeled.
- For manual overrides: specify if button presses are edge- or level-sensitive, whether a second press stops, and how automatic triggers resume.
- For time-based events: define exact timezone, DST, astronomical coordinates, fallback clock time, event collision and date transitions.
- For maximum run duration: verify timer begins at actual output activation and cannot be bypassed by retriggering; specify restart conditions.
- Fail-safe operation requires appropriate hardware design and risk assessment; LOGO! is not automatically a safety PLC.
- Minimize block count only after meeting functional, safety and clarity requirements.
- Explain each functional chain in Dutch using examples a novice can reproduce.