"""Validated boundary used by the CLI and HTTP adapter."""
from .orchestration import aggregate_module_results


def run(payload):
    if not isinstance(payload, dict) or set(payload) - set(["results"]):
        raise ValueError("request must be an object containing only documented fields")
    return aggregate_module_results(payload.get('results'))
