#!/usr/bin/env python
## 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from engine import tweetEngine
from userData import getUserList
from userData import getUserCardFromName
import time
##

##
engine = tweetEngine()
engine.loginToTwitter()
driver = engine.driver
##

## 
# requests = driver.requests
##

## 
# print(type(requests))
# print(len(requests))
# for req in requests:
#     if str(req).find("m3u8") > 0:
#         print(req)
##

## 
engine.turnToSearchPageOf("python")
engine.find_element("//span[contains(text(),'Latest')]").click()
##

## test
# driver.refresh()
# jsScritpGetNetwork = "var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;"
# network = driver.execute_script(jsScritpGetNetwork)
# print(len(network))
# for item in network:
#     print(item["name"])
# fileNetwork = json.dumps()
##

## click profile
# driver.find_element(by=By.XPATH,value="//span[contains(text(),'Profile')]").click()
# wait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,"//span[contains(text(),'Likes')]")))
# driver.find_element(by=By.XPATH,value="//span[contains(text(),'Likes')]").click()
##


##
# for user in getUserList():
#     userCard = getUserCardFromName(user)
#     print(userCard)
#     userCard.printAllTweets()
##

## 
startTime = time.asctime()
print(startTime)
tweets = engine.downloadAllTheTweetsInThePage()
print(len(tweets))
for tweet in tweets:
    print("***********************************************")
    tweet.printTweet()
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("finish")
endTime = time.asctime()
print(endTime)
##

## 
driver.close()
##
