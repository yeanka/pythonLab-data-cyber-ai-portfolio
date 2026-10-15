import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from main import category_for, organize
class Tests(unittest.TestCase):
    def test_category(self):
        self.assertEqual(category_for(Path("report.PDF")), "Documents")
    def test_preview_does_not_move(self):
        with TemporaryDirectory() as d:
            f = Path(d) / "photo.jpg"; f.write_text("x")
            organize(d)
            self.assertTrue(f.exists())
if __name__ == "__main__": unittest.main()
