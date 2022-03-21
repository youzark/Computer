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
## download and save chapter in a give dir
helper.downloadChapterFromUrl(chapterList[2],"./")
##

















