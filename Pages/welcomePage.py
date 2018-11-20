from TestforUS1.locators import Locator
from TestforUS1.methods import Methods

class Welcome(object):

    def __init__(self, driver):
        self.driver = driver
        self.methods = Methods(self.driver)

    def signIn(self):
        self.methods.clickElement(Locator.signIn, 'id')

    def signUp(self):
        self.methods.clickElement(Locator.signUp, 'id')