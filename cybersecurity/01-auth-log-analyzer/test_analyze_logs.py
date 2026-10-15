import tempfile, unittest
from pathlib import Path
from analyze_logs import analyze
class Tests(unittest.TestCase):
    def test_threshold_alert(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"log.txt"; p.write_text("t,1.2.3.4,admin,FAIL\nt,1.2.3.4,admin,FAIL\n")
            self.assertIn("1.2.3.4", analyze(p,2)["alerts"])
if __name__ == "__main__": unittest.main()
