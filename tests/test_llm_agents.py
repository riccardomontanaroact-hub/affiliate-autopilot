import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock

from agent.llm_agents import build_payload, extract_output_text, run_reviews, validate_review


class LlmAgentTests(unittest.TestCase):
    def setUp(self):
        self.report = {
            "project": "VORLI",
            "summary": {"agents_run": 1},
            "agents": [{
                "agent": "Coordinatore e Stratega", "role": "Ordina i prossimi interventi.",
                "status": "OK", "summary": "Una pagina ha noindex.",
                "findings": ["noindex presente"], "next_step": "Verificare prima della promozione."
            }],
        }

    def test_payload_is_structured_and_has_no_tools(self):
        payload = build_payload(self.report["agents"][0], self.report, "gpt-test")
        self.assertFalse(payload["store"])
        self.assertEqual(payload["text"]["format"]["type"], "json_schema")
        self.assertNotIn("tools", payload)
        self.assertEqual(payload["text"]["format"]["schema"]["required"],
                         ["summary", "recommendations", "risks", "requires_human_approval"])

    def test_extract_text_from_responses_api_shape(self):
        self.assertEqual(extract_output_text({"output_text": '{"summary":"ok"}'}), '{"summary":"ok"}')
        response = {"output": [{"type": "message", "content": [
            {"type": "output_text", "text": '{"summary":"ok"}'}
        ]}]}
        self.assertEqual(extract_output_text(response), '{"summary":"ok"}')

    def test_validate_rejects_wrong_types_and_limits_recommendations(self):
        with self.assertRaises(ValueError):
            validate_review({"summary": 1})
        valid = validate_review({"summary": "ok", "recommendations": [str(i) for i in range(8)],
                                 "risks": [], "requires_human_approval": True})
        self.assertEqual(len(valid["recommendations"]), 5)

    def test_run_reviews_saves_ai_results_without_live_actions(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "report.json"
            path.write_text(json.dumps(self.report), encoding="utf-8")
            good = {"summary": "Priorità: verificare noindex.", "recommendations": ["Controllare meta robots."],
                    "risks": ["Non indicizzare pagine incomplete."], "requires_human_approval": True}
            response = Mock()
            response.read.return_value = json.dumps({"output_text": json.dumps(good)}).encode("utf-8")
            context = Mock()
            context.__enter__ = Mock(return_value=response)
            context.__exit__ = Mock(return_value=False)
            opener = Mock(return_value=context)
            result = run_reviews("fake-test-key", "gpt-test", report_path=path, opener=opener)
            saved = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(result["llm_failures"], 0)
            self.assertEqual(saved["agents"][0]["ai_review"]["status"], "completed")
            self.assertTrue(saved["agents"][0]["ai_review"]["requires_human_approval"])
            self.assertEqual(opener.call_count, 1)


if __name__ == "__main__":
    unittest.main()
