from TestforUS1.locators import Locator
from selenium.webdriver.common.by import By

class Page(object):

    def __init__(self, driver):
        self.driver = driver