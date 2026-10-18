import unittest

from or_financial_crime_platform import aggregate_module_results, project_info


class ProjectSmokeTest(unittest.TestCase):
    def test_project_metadata(self) -> None:
        self.assertEqual(project_info()["status"], "starter")

    def test_aggregates_module_alerts(self) -> None:
        result = aggregate_module_results(
            [
                {"module": "splitshield", "alerts": [{"id": "a1", "rule": "STRUCTURING"}]},
                {"module": "mulegraph", "alerts": [{"id": "a2", "rule": "MULE"}]},
            ]
        )
        self.assertEqual(result["alert_count"], 2)
        self.assertEqual(result["status"], "READY_FOR_CASE_TRIAGE")



if __name__ == "__main__":
    unittest.main()

