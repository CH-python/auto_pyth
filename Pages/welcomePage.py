from TestforUS1.locators import Locator
from selenium.webdriver.common.by import By

class Welcome(object):
    def __init__(self, driver):
        self.driver = driver

    def signIn(self):
        return self.driver.find_element(By.ID, Locator.signIn).click()

    def signUp(self):
        return self.driver.find_element(By.ID, Locator.signUp).click()


