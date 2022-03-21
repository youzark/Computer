## 
import urllib.request as req
import bs4 
##

## given url of the index page return list of urls of all Chapters
def getChapterUrls(indexUrl):
    request = req.Request(indexUrl ,
            headers = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0"
        })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data,"lxml")
    titleList = root.find("div",id="list").contents[1].contents
    # get rid of the latest update part
    for index in range(1,len(titleList)):
        if(titleList[index].name == "dt"):
            break
    titleList = titleList[index:]
    # grep all the url of all the subsequent chapter url
    ChaptersUrl = ["http://www.biqugse.com" + title.contents[0]["href"] for title in titleList[2:] ]
    return ChaptersUrl
##

## get Chapter Name from url
def getChapterNameFromUrl(chapUrl):
    # request a chapter
    request = req.Request(chapUrl ,
            headers = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0"
        })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    # get all the tag with all informantion
    root = bs4.BeautifulSoup(data,"lxml")
    return root.head.title.string
##

## get a formatted chapter
def getFormattedChapterFromUrl(chapUrl):
    request = req.Request(chapUrl ,
            headers = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0"
        })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data,"lxml")
    content = root.find("div",id="content").contents
    title = root.head.title.getText()
    paragraphs = content[0::3]
    mainText = ''
    for paragraph in paragraphs:
        mainText = mainText + paragraph.getText() + "\n"
    return "\t\t\t" + title + "\n\n" + mainText, title
##

## download Chapter from url
def downloadChapterFromUrl(chapUrl,pathDir):
    content ,title = getFormattedChapterFromUrl(chapUrl)
    with open(pathDir+title,"w") as f:
        f.write(content)
##
