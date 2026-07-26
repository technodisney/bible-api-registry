import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load_json(name):
    with (ROOT / "data" / name).open(encoding="utf-8") as handle:
        return json.load(handle)


class CatalogTests(unittest.TestCase):
    def test_translation_catalog_has_machine_readable_required_fields(self):
        translations = load_json("translations.json")
        self.assertGreaterEqual(len(translations), 25)
        required = {"name", "abbreviations", "publisher_or_rights_holder", "access", "caveats", "sources"}
        for translation in translations:
            self.assertTrue(required <= translation.keys())
            self.assertTrue(translation["name"])
            self.assertIsInstance(translation["abbreviations"], list)
            self.assertIsInstance(translation["access"], list)
            self.assertIsInstance(translation["sources"], list)

    def test_provider_catalog_has_cost_and_restriction_fields(self):
        providers = load_json("providers.json")
        self.assertGreaterEqual(len(providers), 8)
        required = {"name", "operator", "signup", "free_tier", "premium_cost", "premium_required_when", "caveats", "sources"}
        for provider in providers:
            self.assertTrue(required <= provider.keys())
            self.assertTrue(provider["name"])
            self.assertTrue(provider["sources"])

    def test_readme_declares_machine_and_human_readable_sources(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("data/translations.json", readme)
        self.assertIn("data/providers.json", readme)


if __name__ == "__main__":
    unittest.main()
