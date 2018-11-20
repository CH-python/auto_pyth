import logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementNotVisibleException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from TestforUS1.screenShot import SS

class Methods(object):

    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', filename='sample.log', filemode='w')
    logger = logging.getLogger()


    def __init__(self, driver):
        self.driver = driver
        self.ss = SS(self.driver)
   
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
        self.logger.info("Locator type: %s not supported!" % locatorType)
        raise NoSuchElementException

    def getElement(self, locator, locatorType='css'):
        try:
            element = self.driver.find_element(self.getLocatorType(locatorType), locator)
            self.logger.info("Element with locator: %s By type: %s  Found!" % (locator, locatorType))
            return element
        except NoSuchElementException:
            self.ss.screenShot("/NotFound%sBy%s.png" % (locator, locatorType))
            self.logger.error("Element with locator: %s By type: %s  Not Found!" % (locator, locatorType))
            raise NoSuchElementException

    def clickElement(self, locator, locatorType='css'):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.logger.info("Click on element with locator: %s and locator type: %s" % (locator, locatorType))
        except ElementNotInteractableException:
            self.ss.screenShot("/NotСlick%sBy%s.png" % (locator, locatorType))
            self.logger.error("Can not click on element with locator: %s and locator"
                                 " type: %s" % (locator, locatorType))
            raise ElementNotInteractableException

    def sendKeys(self, data, locator, locatorType="css"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.logger.info("Data %s successfully send to element with locator: "
                             "%s and locator type: %s" % (data, locator, locatorType))
        except ElementNotInteractableException:
            self.ss.screenShot("/FailSend%sBy%s.png" % (locator, locatorType))
            self.logger.error("Failed to send: %s to the element with "
                                 "locator:%s and locator type: %s" % (data, locator, locatorType))
            raise ElementNotInteractableException

    def getText(self, locator, locatorType="css"):
        try:
            self.element = self.getElement(locator, locatorType).text
            self.logger.info("Text '%s' in element with locator: %s By type: %s  Found!" % (self.element, locator, locatorType))
        except NoSuchElementException:
            self.ss.screenShot("/TextNotFound%sBy%s.png" % (locator, locatorType))
            self.logger.error("Text '%s' in element with locator: %s By type:%s  Not Found!" % (locator, locatorType))
            raise NoSuchElementException
        return self.element

    def getAttribute(self, attr, locator, locatorType="css"):
        try:
            self.element = self.getElement(locator, locatorType).get_attribute(attr)
            self.logger.info("Attribute '%s' for element with locator:"
                             " %s By type: %s  Found!" % (attr, locator, locatorType))
        except NoSuchElementException:
            self.ss.screenShot("/NotFoundAttribute%sBy%s.png" % (locator, locatorType))
            self.logger.error("Attribute '%s' for element with locator:"
                                    " %s By type:%s  Not Found!" % (attr, locator, locatorType))
            raise NoSuchElementException
        return self.element

    def waitForElement(self, locator, locatorType='css', timeout=20):
        try:
            self.logger.info("Waiting for maximum: %d for element"
                          " to be visible on the page" % timeout)
            WebDriverWait(self.driver, timeout) \
                .until(expected_conditions.visibility_of_element_located((self.getLocatorType(locatorType), locator)))
            self.logger.info("Element with locator: %s appeared on the page" % locator)
        except NoSuchElementException:
            self.logger.error("Element with locator %s and locator type: "
                           "%s NOT FOUND!" % (locator, locatorType))
            raise NoSuchElementException
        except ElementNotVisibleException:
            self.logger.error("Element with locator: %s is not"
                           " visible on the page" % locator)
            raise ElementNotVisibleException
        return self
