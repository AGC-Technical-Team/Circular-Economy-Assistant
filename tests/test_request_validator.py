import unittest

from src.request_validator import validate_request_data


class TestRequestValidator(unittest.TestCase):

    def test_valid_request(self):
        request_data = {
            "category": "electronics",
            "intent": "recycle",
            "condition": "non_working",
        }

        result = validate_request_data(request_data)

        self.assertTrue(result)

    def test_invalid_request(self):
        request_data = {
            "category": "random_category",
            "intent": "throw_away",
            "condition": "kind_of_broken",
        }

        result = validate_request_data(request_data)

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()