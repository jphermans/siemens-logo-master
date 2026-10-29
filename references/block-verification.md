# Block verification register

For **each** block, fill the following before approving a circuit:

| Field | Required |
|---|---|
| ID | B001, B002, ... |
| Exact display name | Transcribe from the selected LOGO! Soft Comfort version |
| Editor category/path | Verified menu location |
| Inputs | Exact pin labels, types and behavior |
| Outputs | Exact pin labels and behavior |
| Parameters | Names, units, ranges, initial state |
| Retentivity | State after power cycle, if applicable |
| Compatibility | Hardware/software restrictions |
| Source | Manual section or screenshot |
| Confidence | Verified / pending |

Typical concepts to research, **not a verified version-specific inventory**: AND, OR, NOT, edge evaluation, on-delay/off-delay, pulse relay, latching, weekly timer, astronomical timer, counters and comparators.

Do not infer a physical direct wire can connect two special function blocks merely because the UI shows related functionality. Check pin type and connection restrictions. If a block is missing, redesign with verified primitives; do not invent `rising edge` or `falling edge` blocks by name.

Distinguish logical inputs I1.. from physical sensor contact polarity, voltage and signal conditioning. Use exact Siemens UI naming in final tables; optional familiar aliases must be clearly labeled.