import unittest
from hello import greet

class TestHello(unittest.TestCase):
    def test_default_greeting(self):
        self.assertEqual(greet(), "Hello, Bazel!")

    def test_custom_greeting(self):
        self.assertEqual(greet("DevOps"), "Hello, DevOps!")

if __name__ == "__main__":
    unittest.main()
