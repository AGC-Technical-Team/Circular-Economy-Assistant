import unittest #testing framework that comes with Python, provides a way to write and run tests

from src.router import find_item


class TestRouter(unittest.TestCase): #class 

    def test_find_item_chair(self):
        result = find_item("I have an old chair")
        self.assertEqual(result, "chair")

    def test_unknown_item(self):
        result = find_item("I have a strange object")
        self.assertIsNone(result)


if __name__ == "__main__": #only run the tests if this file is executed directly, not when imported as a module
    unittest.main()

