from selenium.webdriver.common.by import By
from datetime import datetime
from helper import getRidOfSpaceAndSpecialChar
from helper import downloadImg as dlImg
from userData import userData
from tweetTextInfo import tweetTextInfo
from tweetPicture import tweetPicture
from myLog import funcLogger

class tweetDetailPageNotReply:
    """
    Introduction:
    Gather All Info of the tweet :Text Info , User Info , MultiMedia Download Info
    In the page of a Specific tweet

    Init Method:
    twitter webpage element <article ... \article >

    """
    def __init__(self,articleSession):
        self.tweet = articleSession

        # separate the tweet into several parts
        sectionMap = self.separateTweet()

        # Collect basic information (must before everything)
        self.userData = self.getUserInfo(sectionMap["userSection"])

        # Collect Comment and Reply
        self.textInfo = self.getTextInfo(sectionMap["timeSection"],sectionMap["commentSection"],sectionMap["replySection"],sectionMap["multiMediaSection"])

        # Collect the image information
        self.getPicInfo(sectionMap["imgSections"])
        self.pics = [ tweetPicture(url=self.imgNameToUrls[fileName],
            fileName=fileName,
            filePath=self.imgNameToFilePath[fileName]) 
            for fileName in self.imgNameToFilePath ]

    @funcLogger
    def separateTweet(self):
        sectionMap = {}
        mainInfoSection = self.tweet.find_element(by=By.XPATH,value="./div[1]/div[1]/div[1]")
        sectionMap["userSection"]= mainInfoSection.find_element(by=By.XPATH,value="./div[2]")
        blogSection = mainInfoSection.find_element(by=By.XPATH,value="./div[3]")
        blogSubSections = blogSection.find_elements(by = By.XPATH,value = "./div") # four/three sections: reply comment reference and status
        sectionMap["blogSubSections"] = blogSubSections
        # self.actionSection = self.blogSubSections[len(self.blogSubSections)-1]
        if self.hasStatusSection(blogSubSections):
            sectionMap["statusSection"] = blogSubSections[len(blogSubSections)-2]
            sectionMap["timeSection"] = blogSubSections[len(blogSubSections)-3]
            sectionMap["multiMediaSection"] = blogSubSections[len(blogSubSections)-4]
            sectionMap["commentSection"] = blogSubSections[len(blogSubSections)-5]
            if len(blogSubSections) == 6:
                sectionMap["replySection"] = blogSubSections[len(blogSubSections)-6]
                self.hasReplySection = True
            else:
                self.hasReplySection = False
                sectionMap["replySection"] = None
        else:
            sectionMap["statusSection"] = None
            sectionMap["timeSection"] = blogSubSections[len(blogSubSections)-2]
            sectionMap["multiMediaSection"] = blogSubSections[len(blogSubSections)-3]
            sectionMap["commentSection"] = blogSubSections[len(blogSubSections)-4]
            if len(blogSubSections) == 5:
                sectionMap["replySection"] = blogSubSections[len(blogSubSections)-5]
                self.hasReplySection = True
            else:
                self.hasReplySection = False
                sectionMap["replySection"] = None
        sectionMap["imgSections"] = sectionMap["multiMediaSection"].find_elements(by = By.XPATH , value = ".//img")
        return sectionMap


    def hasStatusSection(self,blogSubSections):
        try:
            statusSection = blogSubSections[len(blogSubSections)-2]
            if self.hasLikes(statusSection) or self.hasRetweets(statusSection) or self.hasQuoteTweets(statusSection):
                return True
        except:
            return False

    def hasLikes(self,statusSection):
        try:
            statusSection.find_element(by=By.XPATH,value = ".//span[text()='Likes']")
            return True
        except:
            return False


    def hasRetweets(self,statusSection):
        try:
            statusSection.find_element(by=By.XPATH,value = ".//span[text()='Retweets']")
            return True
        except:
            return False


    def hasQuoteTweets(self,statusSection):
        try:
            statusSection.find_element(by=By.XPATH,value = ".//span[text()='Quote Tweets']")
            return True
        except:
            return False

    def getPicInfo(self,imgSections):
        imgUrls = self.getPicUrls(imgSections)
        self.picInfoMap(imgUrls)
    
    def getPicUrls(self,imgSections):
        imgUrls = []
        if not len(imgSections) == 0:
            for entry in imgSections:
                if not entry.get_attribute("src")[-4:] == ".svg":
                    imgUrls.append(entry.get_attribute("src"))
        return imgUrls

    def picInfoMap(self,imgUrls):
        self.imgNameToFilePath = {}
        self.imgNameToUrls = {}
        seq = 0
        for url in imgUrls:
            fileName = self.userData.userHandle + "_" + self.textInfo.timeFull + "seq-" + str(seq)
            # if dlImg(url,fileName,self.userData.userImgDir):
            self.imgNameToUrls[fileName] = url
            self.imgNameToFilePath[fileName] = self.userData.userImgDir
            seq = seq + 1

    def getUserInfo(self,userSection):
        userName = getRidOfSpaceAndSpecialChar(userSection.find_element(by=By.XPATH,value=".//span").text)
        userHandle = userSection.find_element(by=By.XPATH,value=".//span[contains(text(),'@')]").text
        return userData(userName,userHandle)

    def getTextInfo(self,timeSection,commentSection,replySection,multiMediaSection):
        tweetTime = timeSection.find_element(by=By.XPATH,value=".//span").text
        timeObj = datetime.strptime(tweetTime,'%H:%M %p · %b %d, %Y')
        comment,reply = self.getReplyAndMajorComment(commentSection,replySection)
        refText = self.getQuoteTweetText(multiMediaSection)
        return tweetTextInfo(comment,reply,timeObj,refText)

    def getReplyAndMajorComment(self,commentSection,replySection):
        comment = commentSection.text
        if self.hasReplySection:
            reply = replySection.text
        else:
            reply = ""
        return comment,reply

    def getQuoteTweetText(self,multiMediaSection):
        return multiMediaSection.text

    def isContainSubQuote(self,multiMediaSection):
        try:
            multiMediaSection.find_element(by=By.XPATH,value=".//time")
            return True
        except:
            return False

