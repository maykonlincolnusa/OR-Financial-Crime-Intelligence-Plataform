"""Aggregate independently produced findings without coupling modules."""

from __future__ import annotations


def aggregate_module_results(results: list[dict[str, object]]) -> dict[str, object]:
    modules = []
    alerts_by_id: dict[str, dict[str, object]] = {}
    for result in results:
        module = str(result["module"])
        modules.append(module)
        for alert in result.get("alerts", []):
            alert_id = str(alert["id"])
            normalized = dict(alert)
            normalized["source_module"] = module
            alerts_by_id.setdefault(alert_id, normalized)
    alerts = sorted(alerts_by_id.values(), key=lambda alert: str(alert["id"]))
    return {
        "modules": sorted(set(modules)),
        "alerts": alerts,
        "alert_count": len(alerts),
        "status": "READY_FOR_CASE_TRIAGE" if alerts else "NO_ALERTS",
    }

