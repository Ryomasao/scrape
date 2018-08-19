from scrapemod.scrape.core import scraping
from scrapemod.scrape.core import writeData

import datetime

def main():
    url = 'https://r.nikkei.com/search?keyword=%E3%83%AC%E3%82%B7%E3%83%BC%E3%83%88&volume=5'
    result = scraping(url)
    now = datetime.datetime.today().strftime("%Y%m%d%H%M%S")
    writeData(result, now)

if __name__ == '__main__':
    main()