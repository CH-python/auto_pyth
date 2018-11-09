from TestforUS1.locators import Locator
from selenium.webdriver.common.by import By


class PaymentsPage(object):

    def __init__(self, driver):
        self.driver = driver

        # Sign In page locators defining
        self.first_utility_details = driver.find_element(By.XPATH, Locator.first_utility_details)
        self.second_utility_details= driver.find_element(By.XPATH, Locator.second_utility_details)



