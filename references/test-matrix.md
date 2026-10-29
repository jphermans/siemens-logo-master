# Verification and test matrix

For each case document: initial state, stimulus, expected I/Q states, elapsed time, actual result (only if measured), verdict, evidence.

Mandatory cases (adapt to project):
1. Cold start and restart while command is active.
2. Each automatic trigger independently.
3. Each manual control independently.
4. Opposite manual commands simultaneously.
5. Manual command during automatic movement.
6. Automatic trigger during manual movement.
7. Max-duration timeout, retrigger, repeated presses.
8. Power loss and recovery mid-cycle.
9. Sensor faults, invalid analog values, stuck input.
10. Timezone, DST, midnight and equal-time triggers when relevant.
11. Both output commands must never be true together for mutually exclusive actuators.

Verification status vocabulary:
- **Simulated:** real LOGO! Soft Comfort simulation was run and evidence recorded.
- **Bench-tested:** hardware test actually executed and recorded.
- **Theoretically reviewed:** logical walkthrough only; no simulation.
- **Unverified:** important logic or documentation remains unresolved.

Never turn an expected result into an observed result.