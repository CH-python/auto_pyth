from TestforUS1.locators import Locator
from TestforUS1.Methods import Methods


class Login(object):

    def __init__(self, driver):
        self.driver = driver
        self.methods = Methods(self.driver)

    def login(self, email, password):
        self.methods.sendKeys(email,Locator.userEmail, 'id')
        self.methods.sendKeys(password, Locator.userPassword, 'id')
        self.methods.clickElement(Locator.loginButton, 'id')










