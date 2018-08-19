import unittest
import sys, os
path = os.path.join(os.path.dirname(__file__), '../scrape')
sys.path.append(path)

from core import scraping
from core import writeData

import datetime

class TestCore(unittest.TestCase):
    def setUp(self):
        print("setup")
    def test__scraping(self):
        url="https://r.nikkei.com/search?keyword=%E3%83%AC%E3%82%B7%E3%83%BC%E3%83%88&volume=2"
        result = scraping(url)
        self.assertEqual('foo', 'foo')

    def test_writeData(self):
        
        now = datetime.datetime.today().strftime("%Y%m%d%H")

        hoge = [
            {
                "title": "ご飯",
                "link": "https://url1",
                "excerpt": "昨今の"
            },
            {
                "title": "ご飯",
                "link": "https://url1",
                "excerpt": "昨今の"
            }

        ]
        result = writeData(hoge, now)
        self.assertEqual('foo', 'foo')

if __name__ == '__main__':
    unittest.main()