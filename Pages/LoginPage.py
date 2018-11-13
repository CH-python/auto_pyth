from TestforUS1.locators import Locator
from selenium.webdriver.common.by import By

class Login(object):

    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        self.driver.find_element(By.ID, Locator.userEmail).send_keys(email)
        self.driver.find_element(By.ID, Locator.userPassword).send_keys(password)
        self.driver.find_element(By.ID, Locator.loginButton).click()







