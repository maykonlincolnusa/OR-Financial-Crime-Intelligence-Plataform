# Roadmap

Each repository should remain independently useful while sharing versioned contracts.

## Delivery order

1. Stabilize common entity, account, transaction, alert, evidence, and case schemas.
2. Use OR AML Simulator for reproducible contract and regression fixtures.
3. Benchmark SplitShield, MuleGraph, and AML Graph on labelled synthetic scenarios.
4. Connect OR Trace evidence to Case Intelligence without losing provenance.
5. Add reviewed decisions as feedback, never as unqualified ground truth.
6. Integrate SAR drafting and Regula control evidence behind explicit approvals.
7. Demonstrate the full flow with an outbox/inbox event pattern and observability.

## Production gaps

- Durable databases, migrations, encryption, key management, retention, and recovery.
- Enterprise identity, RBAC/ABAC, segregation of duties, and tenant isolation.
- Schema registry, signed releases, backward compatibility, and data lineage.
- Streaming state, retries, dead-letter queues, idempotent consumers, and replay tools.
- Model/rule governance, validation, drift monitoring, fairness review, and quality metrics.
- Privacy impact assessment, security testing, operational runbooks, and regulatory review.

## Definition of a strong portfolio release

- English documentation with clear problem, run instructions, assumptions, and limitations.
- Executable example, meaningful tests, CI, and no secrets or personal data.
- Evidence-linked output and explicit human-review boundaries.
- Measured performance and detection quality using governed datasets.
- Architecture diagram or short demo showing how the independent service integrates.
