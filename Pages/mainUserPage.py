from TestforUS1.locators import Locator
from TestforUS1.Methods import Methods


class MainUserPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.methods = Methods(self.driver)

    def getToPaymentPage(self):
        self.methods.waitForElement(Locator.payments, 'css').clickElement(Locator.payments, 'css')

