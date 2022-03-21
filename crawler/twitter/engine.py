from selenium.webdriver.common.by import By
# from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from tweetCard import tweetCard
from localPassword import getPasswd , getUserName
from time import sleep
from myLog import funcLogger
from threading import Thread
import logging
from downloader import picDownloader
import multiprocessing
from queue import Queue
"""
The only interface to users
Only high level action can be done.
high level action is defined to execute a specific task ( like download all the tweet in current site, add all the friends , display certain tweet , search for specific tweets for download )
high level action can be separate into {browserAction part} and {infomation part}
{infomation part} will control multiple threads responsible for separate tweet , download pic , download vid separately
"""
class tweetEngine:
    def __init__(self):
        logging.basicConfig(format="%(asctime)s-%(levelname)s:%(name)s:%(message)s",level=logging.ERROR)
        self.finishFlagQueue = Queue()
        self.picUrlQueue = Queue()

    # login 
    def loginToTwitter(self):
        # instance
        # options = Options()
        # options.headless = True
        # profile = webdriver.FirefoxProfile()
        # profile.set_preference("permissions.default.image",2)
        # profile.set_preference("media.autoplay.blocking_policy",2)
        # driver = webdriver.Firefox(firefox_profile=profile)
        options = {
                'proxy' : {
                    'http': "http://127.0.0.1:7890",
                    'https': "http://127.0.0.1:7890",
                    "no_proxy": "localhost,127.0.0.1"
                    }
                }
        driver = webdriver.Firefox(seleniumwire_options=options)
        self.driver = driver
        driver.get("http://www.twitter.com/login")
        sleep(4)

        # Login userName
        userNameElement = self.find_element("//input[@name='text']")
        userNameElement.clear()
        userNameElement.send_keys(getUserName())
        userNameElement.send_keys(Keys.RETURN)
        sleep(1)

        # Login password
        passWordElement = self.find_element("//input[@name='password']")
        passWordElement.clear()
        passWordElement.send_keys(getPasswd())
        passWordElement.send_keys(Keys.RETURN)
    #

    def openDownloader(self):
        self.picDownloaderThread = Thread(target=picDownloader.picDownloader,args=[self.picUrlQueue,self.finishFlagQueue],daemon=True)
        self.picDownloaderThread.start()

    def closeDownloader(self):
        self.finishFlagQueue.put(True)

    # search for info
    def turnToSearchPageOf(self,info):
        searchBar = self.find_element("//input[@aria-label='Search query']")
        searchBar.clear()
        searchBar.send_keys(info)
        searchBar.send_keys(Keys.RETURN)

        # come to latest tab
        self.find_element("//span[contains(text(),'Latest')]").click()

    def enterPersonalLikes(self):
        self.find_element("//span[contains(text(),'Profile')]").click()
        self.find_element("//span[contains(text(),'Likes')]").click()

    @funcLogger
    def scrollPageDown(self,lastPosition,tryTime = 2):
        while tryTime > 0:
            # self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            self.driver.execute_script("window.scrollBy(0,6 * window.innerHeight);")
            currentPosition = self.driver.execute_script("return window.pageYOffset;")
            sleep(1)
            success = not (lastPosition == currentPosition)
            if success:
                return True
            else:
                tryTime = tryTime - 1
        return False

    def getAllTheCurrentArticalSession(self):
        articleSessions = self.find_elements("//article[@data-testid='tweet']")
        return articleSessions

    def downloadMultiMediaPart(self,tweet):
        pics = tweet.pics
        for pic in pics:
            self.finishFlagQueue.put(False)
            self.picUrlQueue.put(pic)

    # def recordDownloadedCard(self,result):
    #     if self.tweetNotVisitYet(self.tweets,result):
    #         self.tweets.append(result)
    def downloadAllTheTweetsInThePage(self):
        pool = multiprocessing.Pool(4)
        tweets = []
        tweetQueue = multiprocessing.Queue()
        self.openDownloader()
        try:
            while True:
                lastPosition = self.driver.execute_script("return window.pageYOffset;")
                articleSessions = self.getAllTheCurrentArticalSession()
                print("get article success")
                for articleSession in articleSessions:
                    pool.apply_async(func=analyzeArticalSession,args=(articleSession,tweetQueue))
                # for articleSession in articleSessions:
                #     pool.apply_async(func=self.getTweetCard,args=[articleSession],callback=self.recordDownloadedCard)
                while not tweetQueue.empty():
                    tweet = tweetQueue.get()
                    if self.tweetNotVisitYet(tweets,tweet):
                        self.downloadMultiMediaPart(tweet)
                sleep(1)
                if not self.scrollPageDown(lastPosition):
                    pool.join()
                    pool.close()
                    while not tweetQueue.empty():
                        tweet = tweetQueue.get()
                        if self.tweetNotVisitYet(tweets,tweet):
                            self.downloadMultiMediaPart(tweet)
                    self.closeDownloader()
                    break
        except Exception as e:
            logging.exception(f"Catch exception In {__name__}")
            pool.join()
            pool.close()
            self.closeDownloader()
        return tweets

    # def downloadAllTheTweetsInThePage(self):
    #     pool = multiprocessing.Pool(4)
    #     self.tweets = []
    #     try:
    #         while True:
    #             lastPosition = self.driver.execute_script("return window.pageYOffset;")
    #             articleSessions = self.getAllTheCurrentArticalSession()
    #             for articleSession in articleSessions:
    #                 tweet = tweetCard(articleSession)
    #                 if self.tweetNotVisitYet(self.tweets,tweet):
    #                     self.tweets.append(tweet)
    #                 self.downloadMultiMediaPart(tweet)
    #                 sleep(1)
    #             if not self.scrollPageDown(lastPosition):
    #                 break
    #     except Exception as e:
    #         logging.exception(f"Catch exception In {__name__}")
    #     return self.tweets
    def tweetNotVisitYet(self,tweets,tweet):
        for tt in tweets:
            if tt.tweetDocument["fileName"] == tweet.tweetDocument["fileName"]:
                return False
        return True

    def find_element(self,xPathValue,baseElement=None):
        if not baseElement == None:
            return baseElement.find_element(by=By.XPATH,value=xPathValue)
        wait(self.driver,10).until(EC.presence_of_all_elements_located((By.XPATH,xPathValue)))
        return self.driver.find_element(by=By.XPATH,value=xPathValue)

    def find_elements(self,xPathValue,baseElement=None):
        if not baseElement == None:
            return baseElement.find_element(by=By.XPATH,value=xPathValue)
        wait(self.driver,10).until(EC.presence_of_all_elements_located((By.XPATH,xPathValue)))
        return self.driver.find_elements(by=By.XPATH,value=xPathValue)

@funcLogger
def analyzeArticalSession(articleSession,tweetQueue):
    print("here")
    tweet = tweetCard(articleSession)
    tweetQueue.put(tweet)
