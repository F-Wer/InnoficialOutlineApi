import unittest

# import innoficialoutlineapi
from innoficialoutlineapi.main import *

class MyTestCase(unittest.TestCase):
    def test_positive_test(self):
        self.assertEqual(parse_url('https://www.tagesschau.de/ausland/papst-migration-appell-fluechtlinge-101.html'), 'pYYXKH' )

    def test_negative_test(self):
        with self.assertRaises(ExceptionOutline):
            parse_url('https://www.nytimes.com/live/2021/12/03/business/jobs-report-stock-market')  # add assertion here

if __name__ == '__main__':
    unittest.main()