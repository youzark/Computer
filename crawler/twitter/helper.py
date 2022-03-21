import re
import requests
import os

# get rid of specific character in user name
def getRidOfSpaceAndSpecialChar(userName):
    return re.sub('\W+','',userName)

# download picture
def downloadImg(url,fileName,filePath="./img/"):
    # only Download If the picture does not exist
    if not os.path.exists(filePath+fileName):
        imageContent = requests.get(url).content
        fullPath = filePath + fileName
        if(len(imageContent) > 10000):
            with open(fullPath, "wb") as f:
                f.write(imageContent)
            return True
        else:
            return False
    else:
        return True
#
##
