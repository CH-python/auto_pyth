from TestforUS1.locators import Locator
from selenium.webdriver.common.by import By

class SignIn(object):

    def __init__(self, driver):
        self.driver = driver

        #Sign In page locators defining

        self.email = self.driver.find_element(By.ID, Locator.userEmail)
        self.password = self.driver.find_element(By.ID, Locator.userPassword)
        self.submit = self.driver.find_element(By.ID, Locator.loginButton)







