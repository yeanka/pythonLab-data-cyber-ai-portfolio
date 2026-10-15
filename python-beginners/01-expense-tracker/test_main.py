import unittest
from main import add_transaction, summary

class ExpenseTests(unittest.TestCase):
    def test_summary(self):
        items = [{"type":"income","amount":100}, {"type":"expense","amount":35.5}]
        self.assertEqual(summary(items), {"income":100, "expenses":35.5, "balance":64.5})
    def test_reject_nonpositive(self):
        with self.assertRaises(ValueError):
            add_transaction([], "expense", 0, "food")

if __name__ == "__main__":
    unittest.main()
