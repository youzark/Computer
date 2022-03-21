import urllib.request as req

def downloadImg(url,fileName,filePath="."):
    fullPath = filePath + fileName
    req.urlretrieve(url,fullPath)
