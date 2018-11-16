from TestforUS1.locators import Locator
from TestforUS1.Methods import Methods


class Login(object):

    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        methods = Methods(self.driver)
        methods.sendKeys(email,Locator.userEmail, 'id')
        methods.sendKeys(password, Locator.userPassword, 'id')
        methods.clickElement(Locator.loginButton, 'id')










