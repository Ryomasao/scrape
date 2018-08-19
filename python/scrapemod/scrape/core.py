# coding: UTF-8
import urllib.request, urllib.error
from bs4 import BeautifulSoup

from firebase import firebase
firebase = firebase.FirebaseApplication("https://scrape-b2b08.firebaseio.com/", None)

def scraping(test):
    #アクセスするURL
    url = 'https://r.nikkei.com/search?keyword=%E3%83%AC%E3%82%B7%E3%83%BC%E3%83%88&volume=20'
    html = urllib.request.urlopen(url=url)
    soup = BeautifulSoup(html, "html.parser")
    title_tag = soup.title
    title = title_tag.string
    class_ = "nui-card__content"

    contents = soup.find_all("div", class_=class_)

    list = [];

    for content in contents:
        titleBlock = content.find("h3", class_="nui-card__title")
        titleLink = titleBlock.find("a")
        link = titleLink.get('href')
        title = titleLink.string

        excerptBlock = content.find("a", class_="nui-card__excerpt")
        exceprt = excerptBlock.get("href")
        exceprtString = ''
        for item in excerptBlock.contents:
            exceprtString += item.string

        list.append(
            {
                "title": title.replace(' ', ''),
                "link": link,
                "excerpt": exceprtString.replace(' ','')
            }
        )

    return list

def writeData(data, execDate):
    result = firebase.post('/data', data={execDate: data})


if __name__ == '__main__':
    scraping()
    
