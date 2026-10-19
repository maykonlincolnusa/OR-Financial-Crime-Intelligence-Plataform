"""Validated boundary used by the CLI and HTTP adapter."""
from .orchestration import aggregate_module_results
from .pipeline import validate_pipeline


def run(payload):
    if not isinstance(payload, dict) or set(payload) - set(["results","action","required_modules"]):
        raise ValueError("request must be an object containing only documented fields")
    if payload.get("action") == "validate":
        return validate_pipeline(payload.get("results"), payload.get("required_modules"))
    if payload.get("action", "aggregate") != "aggregate" or "required_modules" in payload:
        raise ValueError("unknown action or unexpected validation option")
    return aggregate_module_results(payload.get('results'))
