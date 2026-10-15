import unittest
from check_url import inspect_url
class Tests(unittest.TestCase):
    def test_http_flag(self):
        self.assertTrue(any("HTTPS" in f for f in inspect_url("http://example.com")["flags"]))
    def test_parse_host(self):
        self.assertEqual(inspect_url("https://example.com/a")["host"],"example.com")
if __name__=="__main__": unittest.main()
