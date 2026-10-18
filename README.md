# OR Financial Crime Intelligence Platform

A lightweight integration boundary for independent OR financial-crime modules. It demonstrates safe alert aggregation while each detector remains deployable and testable on its own.

## Why it matters

Financial institutions rarely replace every monitoring component at once. A modular architecture needs stable identifiers, versioned contracts, replay safety, traceable origins, and a clear path from alert to investigation.

## Current capabilities

- Aggregate alerts from independent modules.
- Scope alert identity by source module.
- Ignore identical replays and reject conflicting replays.
- Preserve source module and transaction evidence references.
- Produce deterministic, versioned output for case triage.
- Strict validation, CLI, optional authenticated API, Docker image, and CI.

## Run

```sh
python -m pip install -e '.[dev,api]'
python -m or_financial_crime_platform --demo
pytest -q && ruff check src tests
```

API: set `OR_API_KEY` to at least 16 characters, run `uvicorn or_financial_crime_platform.api:create_app --factory`, then POST `examples/request.json` to `/v1/analyze`.

## Architecture direction

Simulator creates governed synthetic fixtures; CrossLedger normalizes and reconciles; SplitShield, MuleGraph, and AML Graph detect patterns; Trace reconstructs temporal paths; Case Intelligence manages investigation; SAR Intelligence drafts evidence-grounded reports; Regula maps controls; this Platform coordinates contracts without absorbing each product's domain logic.

See [portfolio](docs/portfolio.md) and [roadmap](docs/roadmap.md).

## Limitations and roadmap

This prototype is not a workflow engine or production event bus. It has no durable storage, service discovery, schema registry, tenant isolation, distributed tracing, RBAC, retry queue, or end-to-end deployment. Next steps are signed JSON Schemas, correlation IDs, an outbox/inbox pattern, contract tests, OpenTelemetry, policy enforcement, and a reference integration using synthetic data.
