
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep

class instabot():
    def __init__(self, username, password):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.username = username
        self.password = password

    def login(self):
        self.browser.get('https://www.instagram.com/accounts/login/')

        emailInput = self.browser.find_elements_by_css_selector('form input')[0]
        passwordInput = self.browser.find_elements_by_css_selector('form input')[1]

        emailInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        sleep(2)

    def followUser(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        sleep(2)
        followButton = self.browser.find_element_by_css_selector('button')
        if (followButton.text != 'Following'):
            followButton.click()
            sleep(2)
        else:
            print("You are already following this user")

    def UnfollowUser(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        sleep(2)
        followButton = self.browser.find_element_by_css_selector('button')
        if (followButton.text != 'Following'):
            followButton.click()
            sleep(2)
            confirmButton = self.browser.find_element_by_xpath('//button[text() = "Unfollow"]')
            confirmButton.click()
        else:
            print("You are not following this user")

instabot = instabot(str(input("username")), str(input("password")))
instabot.login()
instabot.followuser()
