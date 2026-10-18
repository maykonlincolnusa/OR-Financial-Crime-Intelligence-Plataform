"""Public API for OR Financial Crime Intelligence Platform."""

from .orchestration import aggregate_module_results

__version__ = "0.2.0"


def project_info() -> dict[str, str]:
    return {
        "name": "OR Financial Crime Intelligence Platform",
        "focus": "Integration of financial-crime intelligence modules",
        "status": "reference-prototype",
    }


__all__ = ["aggregate_module_results", "project_info"]

