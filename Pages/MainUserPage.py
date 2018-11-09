from TestforUS1.locators import Locator
from selenium.webdriver.common.by import By


class MainUserPage(object):

    def __init__(self, driver):
        self.driver = driver

        # Main user page locators defining
        self.itemPayments = driver.find_element(By.XPATH, Locator.payments)

class popupItemPayment(object):

    def __init__(self, driver):
        self.driver = driver

        self.titleDetails = driver.find_element(By.XPATH, Locator.titlePopup)
        self.btnDetails = driver.find_element(By.XPATH, Locator.details)




