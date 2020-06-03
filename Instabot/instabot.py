from selenium import webdriver # A package for web automation
from selenium.webdriver.common.keys import Keys
from time import sleep # to make sure the bot "sleeps" well after a process
import json

# A class for Instagram Bot
class Instabot:
    def __init__(bot, username, pw): # Using bot to connect class elements to the class 
        bot.driver = webdriver.Chrome(executable_path= r'C:\Users\mohan\.wdm\drivers\chromedriver\83.0.4103.39\win32\chromedriver.exe')
        bot.username = username
        bot.pw = pw
    
    def login(bot):
        # Opens a new chrome window with the website url
        bot.driver.get("https://instagram.com/accounts/login")
        sleep(2)
        # finds the username and password elements by full xpath
        # username
        bot.driver.find_element_by_name("username").send_keys(bot.username)
        # password
        bot.driver.find_element_by_name("password").send_keys(bot.pw)
        # submit username and password
        bot.driver.find_element_by_css_selector("#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button").click()
        sleep(3)
        # Click on 'Not Now'
        try: 
            bot.driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm').click()
        except:     
            bot.driver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button').click()
            
        bot.driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm').click()
        sleep(2)

    def followByUsername(bot,username_list):
        bot.username_list = username_list
        index = 0
        while (index < len(username_list)):
            bot.driver.get("https://www.instagram.com/{}/".format(username_list[index]))
            # click follow button
            sleep(2)
            try:
                follow_button = bot.driver.find_element_by_css_selector("button")
            except:
                follow_button = bot.driver.find_element_by_css_selector("#react-root > section > main > div > header > section > div.nZSzR > button")
            follow_button.click()
            index = index + 1


    def UnfollowByUsername(bot,username_list):
        bot.username_list = username_list
        index = 0
        while (index < len(username_list)):
            bot.driver.get("https://www.instagram.com/{}/".format(username_list[index]))
            sleep(2)
            try:
                bot.driver.find_element_by_css_selector("#react-root > section > main > div > header > section > div.Y2E37 > div > span > span.vBF20._1OSdk > button")
                bot.driver.find_element_by_css_selector("#react-root > section > main > div > header > section > div.Y2E37 > button")
            except:
                try: 
                    followed_button = bot.driver.find_element_by_css_selector("#react-root > section > main > div > header > section > div.Y2E37 > div.Igw0E.IwRSH.eGOV_._4EzTm > span > span.vBF20._1OSdk > button")
                except:
                    followed_button = bot.driver.find_element_by_css_selector("#react-root > section > main > div > header > section > div.Y2E37 > button")
                followed_button.click()
                sleep(1)
                Unfollow_button = bot.driver.find_element_by_css("body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.-Cab_")
                Unfollow_button.click()  
            index = index + 1 

    def getFollowers(bot, username):
            bot.driver.get('https://www.instagram.com/' + username)
            followersLink = bot.driver.find_element_by_css_selector('ul li a')
            followersLink.click()
            sleep(2)
            user_links = bot.driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
            leng = len(user_links.find_elements_by_css_selector('li'))
        
            user_links.click()
            actionChain = webdriver.ActionChains(bot.driver)
            while (leng < max):
                actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                leng = len(user_links.find_elements_by_css_selector('li'))
            
            followers = []
            for user in user_links.find_elements_by_css_selector('li'):
                username = user.find_element_by_css_selector('a').get_attribute('href')
                followers.append(username)
            return followers

    def writeData(bot, follower_list, following_list):
        bot.follower_list = follower_list
        bot.following_list = following_list
        with open("IG_Data.json") as file:
            data = json.load(file)['IG_Data']
            followers = data[0]['data']
            following = data[1]['data']
            followers.append(follower_list)
            following.append(following_list)

    def closeSession(bot):
            bot.closeBrowser()
            print("***BOT TERMINATED***")

Instabot = Instabot("username", "pw")
Instabot.login()
Instabot.followByUsername(['google','xyz','microsoft'])
Instabot.closeSession()