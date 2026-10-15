import unittest
from main import assess_password
class Tests(unittest.TestCase):
    def test_long_mixed_password(self):
        self.assertEqual(assess_password("Zebra!River2026")["level"], "stronger")
    def test_short_password(self):
        self.assertEqual(assess_password("abc")["level"], "weak")
if __name__ == "__main__": unittest.main()
