#!/usr/bin/env python
import requests
from concurrent.futures import ThreadPoolExecutor 
from myLog import funcLogger
import os
import logging

@funcLogger
def _downloadImg(url,fileName,filePath):
    if not os.path.exists(filePath+fileName):
        imageContent = requests.get(url).content
        fullPath = filePath + fileName
        with open(fullPath, "wb") as f:
            f.write(imageContent)

def picDownloader(workQueue,finishFlagQueue,threadNum=5):
    logging.info("Pic Downloader Ready To Download")
    with ThreadPoolExecutor(max_workers=threadNum) as ex:
        while True:
            if not workQueue.empty():
                pic = workQueue.get()
                ex.submit(_downloadImg,pic.url,pic.fileName,pic.filePath)
            else:
                finishFlag = finishFlagQueue.get()
                if finishFlag:
                    break
    logging.info("Pic Downloader Closed")
