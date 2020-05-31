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
        bot.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        # password
        bot.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        # submit username and password
        bot.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]').click()
        sleep(3)
        # Click on 'Not Now'
        try:
            bot.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        except:
            bot.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
            
        bot.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        sleep(3)

    def getFollowers(bot):
        bot.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img").click()
        sleep(3)
        follower_box = bot.driver.find_element_by_xpath("//a[contains(@href, '/{}/{}/')]".format(bot.username,"followers"))
        follower_box.click()
        sleep(3)
        print("You have " + follower_box.text)

    
    def getFollowing(bot):
        bot.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img").click()
        sleep(3)
        following_box = bot.driver.find_element_by_xpath("//a[contains(@href, '/{}/{}/')]".format(bot.username,"following"))
        following_box.click()
        sleep(3)
        print("You have " + following_box.text + " you")

    def ViewFeed(bot):
        bot.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def ViewPosts(bot):
        bot.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img").click()
        sleep(3)
        bot.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

username = input("Enter your username: ")
pw = input("Enter your password: ")
bot = Instabot(username, pw)
command = input("What do you want to do - get followers, get following, view feed, view posts?: " + "\n")

if (command == "get followers"):
    bot.getFollowers()

elif (command == "get following"):
    bot.getFollowing()

elif (command == "view feed"):
    bot.ViewFeed()

elif (command == "view posts"):
    bot.ViewPosts()

