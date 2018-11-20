from TestforUS1.locators import Locator
from TestforUS1.methods import Methods

class MainUserPage(object):

    def __init__(self, driver):
        self.driver = driver

    def getToPaymentPage(self):
        methods = Methods(self.driver)
        self.driver.implicitly_wait(10)
        methods.clickElement(Locator.payments, 'css')