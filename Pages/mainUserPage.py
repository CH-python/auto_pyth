from TestforUS1.locators import Locator
from selenium.webdriver.common.by import By

class MainUserPage(object):

    def __init__(self, driver):
        self.driver = driver

    def getToPaymentPage(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.CSS_SELECTOR, Locator.payments).click()
