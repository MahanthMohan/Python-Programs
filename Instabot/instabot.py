from selenium import webdriver # A package for web automation
from selenium.webdriver.common.keys import Keys
from time import sleep # to make sure the bot "sleeps" well after a process

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
        bot.driver.find_element_by_id("react-root").click()
        sleep(2)
        # Click on 'Not Now', try/except for managing sequence of events/dynamicity
        try: 
            bot.driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm').click()
        except:     
            bot.driver.find_element_by_id('react-root').click()
            
        bot.driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm').click()
        sleep(2)

    def followByUsername(bot,username_list):
        bot.username_list = username_list
        index = 0
        while (index < len(username_list)):
            bot.driver.get("https://www.instagram.com/{}/".format(username_list[index]))
            # click follow button
            sleep(2)
            follow_button = bot.driver.find_element_by_id("react-root")
            follow_button.click()
            index = index + 1


    def UnfollowByUsername(bot,username_list):
        bot.username_list = username_list
        index = 0
        while (index < len(username_list)):
            bot.driver.get("https://www.instagram.com/{}/".format(username_list[index]))
            sleep(2)
            # A try catch block to manage element not found exception for private/public accounts
            try:
                followed_button = bot.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button')
            except:
                followed_button = bot.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button')
            followed_button.click()
            Unfollow_button = bot.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.-Cab_")
            Unfollow_button.click()  
            index = index + 1 

    def getFollowers(bot, username, max):
            self.max = max
            bot.driver.get('https://www.instagram.com/' + username)
            # Find the follower box where we are going to do our scroll
            followersLink = bot.driver.find_element_by_css_selector('ul li a').click()
            sleep(1.5)
            # Locate the user links inside the follower box
            user_links = bot.driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
            user_links.click()

            # Instantiate ActionChains, a module of Selenium WebDriver that automates key actions
            actionChain = webdriver.ActionChains(bot.driver)
            leng = 0
            # While the leng < max, the space key is pressed down and only stops after reaching the end, which is max
            for i in range (leng, max):
                actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                # li attribute contains all the user data, however we only want the name & username
                usernamelist = user_links.find_elements_by_css_selector('li')
                username = usernamelist.find_element_by_css_selector('a').get_attribute('href')
            # Keep adding the usernames to the end of the list/list append
            followers = []
            followers.append(username)
            return followers

    # Everything needs a rest to work well :-)
    def closeSession(bot):
            bot.closeBrowser()
            print("***BOT TERMINATED***")

Instabot = Instabot("username", "pw")
Instabot.login()
Instabot.followByUsername(['microsoft','instagram'])
Instabot.UnfollowByUsername(['google','apple'])
Instabot.getFollowers('username','max')
Instabot.closeSession()