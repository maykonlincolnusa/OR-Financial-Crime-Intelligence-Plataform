from or_financial_crime_platform import validate_pipeline


def test_validates_versions_required_modules_and_evidence():
    result = validate_pipeline([{"module": "mulegraph", "schema_version": "3.0",
                                 "alerts": [{"id": "a", "transaction_ids": ["t1"]}]}],
                               ["mulegraph", "splitshield"])
    assert result["valid"] is False
    assert {error["code"] for error in result["errors"]} == {"REQUIRED_MODULE_MISSING"}
    assert result["unique_evidence_count"] == 1


def test_rejects_alert_without_evidence():
    result = validate_pipeline([{"module": "mulegraph", "schema_version": "3.0",
                                 "alerts": [{"id": "a"}]}])
    assert result["errors"][0]["code"] == "MISSING_EVIDENCE"
