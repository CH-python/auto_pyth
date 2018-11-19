from TestforUS1.locators import Locator
from TestforUS1.methods import Methods
import logging


class Welcome(object):


    def __init__(self, driver):
        self.driver = driver

    def signIn(self):
        logger = logging.getLogger()
        logger.info("New test")
        methods = Methods(self.driver)
        methods.clickElement(Locator.signIn, 'id')

    def signUp(self):
        methods = Methods(self.driver)
        methods.clickElement(Locator.signUp, 'id')


