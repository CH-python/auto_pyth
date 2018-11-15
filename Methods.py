from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementNotVisibleException
import logging
logging.basicConfig(level=logging.INFO, filename='sample.log')
logger = logging.getLogger()

class Methods(object):

    def __init__(self, driver):
        self.driver = driver

    def getLocatorType(self, locatorType):
        locatorType = locatorType.lower()
        locatorTypes = {
            'id': By.ID,
            'name': By.NAME,
            'xpath': By.XPATH,
            'css': By.CSS_SELECTOR,
            'class': By.CLASS_NAME,
            'link': By.LINK_TEXT
        }
        if locatorType in locatorTypes:
            return locatorTypes[locatorType]
        self.logging.info("Locator type: %s not supported!" % locatorType)
        raise NoSuchElementException

    def getElement(self, locator, locatorType='css'):
        try:
            element = self.driver.find_element(self.getLocatorType(locatorType), locator)
            self.logging.info("Element with locator: %s By type: %s  Found!" % (locator, locatorType))
            return element
        except NoSuchElementException:
            self.logging.error("Element with locator: %s By type:%s  Not Found!" % (locator, locatorType))
            raise NoSuchElementException

    def clickElement(self, locator, locatorType='css'):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.logging.info("Click on element with locator: %s and locator type: %s" % (locator, locatorType))
        except ElementNotInteractableException:
            self.logging.error("Can not click on element with locator: %s and locator/"
                                 " type: %s" % (locator, locatorType))
            raise ElementNotInteractableException
        return self

    def sendKeys(self, data, locator, locatorType="css"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.logging.info(" Data %s successfully send to element with locator:/"
                              " %s and locator type: %s" % (data, locator, locatorType))
        except ElementNotInteractableException:
            self.logging.error(" Failed to send: %s to the element with/"
                                 " locator:%s and locator type: %s" % (data, locator, locatorType))
            raise ElementNotInteractableException
        return self

