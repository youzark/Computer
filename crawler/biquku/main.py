#!/usr/bin/env python

## 
import urllib.request as req
import bs4 
##

## given url of the index page return list of urls of all Chapters
def getChapterUrls(indexUrl):
    print(indexUrl)
    request = req.Request(indexUrl ,
            headers = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0"
        })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    if data == None:
        raise Exception
    root = bs4.BeautifulSoup(data,"lxml")
    titleList = root.find_all("ul",class_="chapter")[1]
    nextPageButton = root.find("span",class_="right")
    hasNextPage = nextPageButton.a.attrs["class"][0] == "onclick"
    print(titleList)
    urls = [entry["href"] for entry in titleList.contents ]
    print(urls)
    return urls ,hasNextPage
##

## get all the chapter under a base url
def getAllChaptersUnderABaseUrls(Baseurl):
    index = 1
    chaptersList = []
    hasNextPage = True
    while hasNextPage:
        try:
            localChapters,hasNextPage = getChapterUrls(Baseurl + "page" + str(index) + ".html")
        except:
            break
        else:
            chaptersList = chaptersList + localChapters
            index = index + 1
    return chaptersList
##

## has next page
    

##

## get title

allurl = getAllChaptersUnderABaseUrls("http://m.beqiku.com/book/980/")

print(allurl)

##
