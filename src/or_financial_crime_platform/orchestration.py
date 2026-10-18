"""Idempotent aggregation of independent module outputs."""
from __future__ import annotations

from copy import deepcopy

from .validation import identifiers, records, text


def aggregate_module_results(results):
    modules = set()
    alerts_by_key = {}
    duplicates = 0
    for result in records(results, "results"):
        module = text(result.get("module"), "module")
        modules.add(module)
        for alert in records(result.get("alerts"), "alerts"):
            alert_id = text(alert.get("id"), "alert id")
            key = (module, alert_id)
            normalized = deepcopy(alert)
            normalized["source_module"] = module
            if "transaction_ids" in normalized:
                identifiers(normalized["transaction_ids"], "transaction_ids")
            if key in alerts_by_key:
                if normalized != alerts_by_key[key]:
                    raise ValueError("conflicting alert replay within a module")
                duplicates += 1
            else:
                alerts_by_key[key] = normalized
    alerts = [alerts_by_key[key] for key in sorted(alerts_by_key)]
    return {
        "modules": sorted(modules), "alerts": alerts, "alert_count": len(alerts),
        "duplicates_ignored": duplicates, "schema_version": "2.0",
        "status": "READY_FOR_CASE_TRIAGE" if alerts else "NO_ALERTS",
    }

