import unittest
from vowelapp.vowel import vowel

class VowelTest(unittest.TestCase):
    def test_vowel(self):
        self.assertEqual(vowel("dahdah"), (['a'], 3))

if __name__ == "__main__":
    unittest.main()