from TestforUS1.locators import Locator
from selenium.webdriver.common.by import By

class Sign_In(object):

    def __init__(self, driver):
        self.driver = driver

        #Sign In page locators defining
        self.email = self.driver.find_element(By.ID, Locator.user_email)
        self.password = self.driver.find_element(By.ID, Locator.user_password)
        self.submit = self.driver.find_element(By.ID, Locator.login_button)