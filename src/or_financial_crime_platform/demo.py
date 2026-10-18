"""Deterministic synthetic input; no customer data."""
DEMO = {
    "results": [
        {
            "module": "splitshield",
            "alerts": [
                {
                    "id": "shared-1",
                    "rule": "STRUCTURING",
                    "transaction_ids": [
                        "t1"
                    ]
                }
            ]
        },
        {
            "module": "mulegraph",
            "alerts": [
                {
                    "id": "shared-1",
                    "rule": "PASS_THROUGH",
                    "transaction_ids": [
                        "t3"
                    ]
                }
            ]
        }
    ]
}
