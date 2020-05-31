from selenium import webdriver # A package for web automation
from time import sleep # to make sure the bot "sleeps" well after a process
from webdriver_manager.chrome import ChromeDriverManager # Manage exceptions from the Chrome Web Driver

# A class for Instagram Bot
class Instabot:
    def __init__(bot, username, pw): # Using bot to connect class elements to the class 
        bot.driver = webdriver.Chrome(ChromeDriverManager().install())
        bot.username = username
        # Opens a new chrome window with the website url
        bot.driver.get("https://instagram.com/accounts/login")
        sleep(2)
        # finds the username and password elements by full xpath
        # username
        bot.driver.find_element_by_name("username").send_keys(username)
        # password
        bot.driver.find_element_by_name("password").send_keys(pw)
        # submit username and password
        bot.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div").click()
        sleep(3)
        # Click on 'Not Now'
        try:
            bot.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        except:
            bot.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
            
        bot.driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm').click()
        sleep(3)

    def getFollowers(bot):
        bot.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img").click()
        sleep(3)
        follower_box = bot.driver.find_element_by_xpath("//a[contains(@href, '/{}/{}/')]".format(bot.username,"followers"))
        follower_box.click()
        sleep(3)
        print("You have " + follower_box.text)
        sugs = bot.driver.find_element_by_xpath()

    
    def getFollowing(bot):
        bot.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img").click()
        sleep(3)
        following_box = bot.driver.find_element_by_xpath("//a[contains(@href, '/{}/{}/')]".format(bot.username,"following"))
        following_box.click()
        sleep(3)
        print("You have " + following_box.text + " you")


bot = Instabot("momomahanth", "dov55789")
command = input("What do you want to do - get followers, get following?: " + "\n")

if (command == "get followers"):
    bot.getFollowers()

elif (command == "get following"):
    bot.getFollowing()


