"""Cross-module contract and evidence-lineage checks."""
from .validation import identifiers, records, text


def validate_pipeline(results, required_modules=None):
    required = set(identifiers(required_modules or [], "required_modules"))
    present, errors, evidence = set(), [], set()
    for index, result in enumerate(records(results, "results")):
        module = text(result.get("module"), "module")
        present.add(module)
        if result.get("schema_version") not in {"2.0", "3.0"}:
            errors.append({"index": index, "module": module, "code": "UNSUPPORTED_SCHEMA"})
        correlation = result.get("correlation_id")
        if correlation is not None:
            text(correlation, "correlation_id")
        for alert in records(result.get("alerts", []), "alerts"):
            alert_id = text(alert.get("id"), "alert id")
            refs = identifiers(alert.get("transaction_ids", []), "transaction_ids")
            if not refs:
                errors.append({"index": index, "module": module,
                               "alert_id": alert_id, "code": "MISSING_EVIDENCE"})
            evidence.update(refs)
    for module in sorted(required - present):
        errors.append({"module": module, "code": "REQUIRED_MODULE_MISSING"})
    return {"valid": not errors, "modules": sorted(present), "errors": errors,
            "unique_evidence_count": len(evidence), "schema_version": "3.0"}
