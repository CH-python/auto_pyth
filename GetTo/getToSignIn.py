from TestforUS1.Pages.welcomePage import Welcome

class getToSignInPage(object):

    def __init__(self, driver):
        self.driver = driver

        welcome = Welcome(self.driver)
        welcome.signIn.click()
