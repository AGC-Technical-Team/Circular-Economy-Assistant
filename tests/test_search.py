import unittest

from src.search import search_resources


class TestSearch(unittest.TestCase):

    def test_matching_resource(self):
        resources = [
            {
                "verification_status": "verified",
                "next_review_date": "2099-01-01",
                "category": "furniture_household",
                "accepted_items": ["chair"],
                "excluded_items": [],
                "supported_intents": ["donate"],
                "condition_accepted": ["usable"],
                "locations_covered": ["zalka"],
            }
        ]

        user_request = {
            "item": "chair",
            "category": "furniture_household",
            "intent": "donate",
            "condition": "usable",
            "location": "zalka",
        }

        results = search_resources(resources, user_request)

        self.assertEqual(len(results), 1)

    def test_wrong_location_returns_no_match(self):
        resources = [
            {
                "verification_status": "verified",
                "next_review_date": "2099-01-01",
                "category": "furniture_household",
                "accepted_items": ["chair"],
                "excluded_items": [],
                "supported_intents": ["donate"],
                "condition_accepted": ["usable"],
                "locations_covered": ["zalka"],
            }
        ]

        user_request = {
            "item": "chair",
            "category": "furniture_household",
            "intent": "donate",
            "condition": "usable",
            "location": "tripoli",
        }

        results = search_resources(resources, user_request)

        self.assertEqual(len(results), 0)


if __name__ == "__main__":
    unittest.main()