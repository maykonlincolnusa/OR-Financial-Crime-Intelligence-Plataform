# OR Financial Crime Portfolio

The OR portfolio contains independent, interoperable reference prototypes for AML, fraud operations, reconciliation, investigation, and control assurance.

| Project | Responsibility |
|---|---|
| OR Trace | Temporal multi-hop transaction lineage |
| OR AML Graph | Cycles and network-pattern analysis |
| OR MuleGraph | Explainable money-mule indicators |
| OR SplitShield | Rolling-window structuring indicators |
| OR CrossLedger | Conservative cross-ledger reconciliation |
| OR AML Simulator | Reproducible synthetic scenarios |
| OR Case Intelligence | Case priority and decision audit trail |
| OR SAR Intelligence | Evidence-grounded report drafting |
| OR Regula | Requirement, control, and evidence coverage |
| OR Financial Crime Intelligence Platform | Replay-safe alert integration |

## Shared design principles

- Independent repositories with a common transaction vocabulary.
- Decimal strings for money, explicit currency, time-zone-aware timestamps, and stable IDs.
- Explainable indicators linked to evidence; no score is proof of wrongdoing.
- Deterministic outputs, bounded workloads, strict validation, and replay safety.
- Synthetic, public, anonymized, or properly governed data only.
- Human review for investigative, regulatory, and customer-impacting decisions.

These projects demonstrate engineering judgment. They do not claim production readiness, regulatory certification, or knowledge of any institution's private controls.
