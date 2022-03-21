#!/usr/bin/env python
## 
import urllib.request as req
import bs4 
import helper
##
## grep all the chapters using helper function
chapterList = helper.getChapterUrls("http://www.biqugse.com/66293/")
##
## grep formatted chapter
content ,title = helper.getFormattedChapterFromUrl(chapterList[0])
##

## save chapter 
with open("./"+title,"w") as f:
    f.write(content)
##
## download Chapter from url
def downloadChapterFromUrl(chapUrl,pathDir):
    content ,title = helper.getFormattedChapterFromUrl(chapUrl)
    with open(pathDir+title,"w") as f:
        f.write(content)
##

## 
downloadChapterFromUrl(chapterList[1],"./")
print("finish")

##

















