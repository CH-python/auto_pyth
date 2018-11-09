from TestforUS1.locators import Locator
from selenium.webdriver.common.by import By

class Welcome(object):
    def __init__(self, driver):
        self.driver = driver

        #welcome page locators defining
        self.sign_in=self.driver.find_element(By.ID, Locator.sign_in)
        self.sign_up=self.driver.find_element(By.ID, Locator.sign_up)
