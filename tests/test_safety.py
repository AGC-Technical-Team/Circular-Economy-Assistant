import unittest

from src.safety import check_safety


class TestSafety(unittest.TestCase):

    def test_unsafe_item_stops_search(self):
        user_request = {
            "condition": "unsafe_contaminated"
        }

        result = check_safety(user_request)

        self.assertFalse(result["safe_to_continue"])
        self.assertIsNotNone(result["message"])


if __name__ == "__main__":
    unittest.main()