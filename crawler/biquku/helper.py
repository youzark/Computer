## 
import urllib.request as req
import bs4 
##
def getUrls(indexUrl):
    request = req.Request(indexUrl ,
            headers = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0"
        })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data,"lxml")
    titleList = root.find_all("ul",class_="chapter")[1]
    return ChaptersUrl
##
