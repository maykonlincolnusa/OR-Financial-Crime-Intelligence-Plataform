import unittest

from or_financial_crime_platform import aggregate_module_results, project_info


class ProjectTest(unittest.TestCase):
    def test_aggregates_and_deduplicates_replays(self):
        item = {"module": "splitshield", "alerts": [{"id": "a1", "rule": "STRUCTURING"}]}
        result = aggregate_module_results([item, item])
        self.assertEqual(result["alert_count"], 1)
        self.assertEqual(result["duplicates_ignored"], 1)
        self.assertEqual(project_info()["status"], "reference-prototype")

    def test_rejects_conflicting_replay(self):
        with self.assertRaises(ValueError):
            aggregate_module_results([
                {"module": "mulegraph", "alerts": [{"id": "a1", "rule": "MULE"}]},
                {"module": "mulegraph", "alerts": [{"id": "a1", "rule": "OTHER"}]},
            ])

    def test_same_identifier_is_scoped_by_module(self):
        result = aggregate_module_results([
            {"module": "a", "alerts": [{"id": "same"}]},
            {"module": "b", "alerts": [{"id": "same"}]},
        ])
        self.assertEqual(result["alert_count"], 2)


if __name__ == "__main__":
    unittest.main()
