from TestforUS1.locators import Locator
from selenium.webdriver.common.by import By

class Welcome(object):
    def __init__(self, driver):
        self.driver = driver

        #welcome page locators defining

        self.signIn = self.driver.find_element(By.ID, Locator.signIn)
        self.signUp = self.driver.find_element(By.ID, Locator.signUp)


