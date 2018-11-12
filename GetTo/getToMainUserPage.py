from TestforUS1.Pages.signInPage import SignIn

class getToMainUserPage(object):

    def __init__(self, driver):
        self.driver = driver
        signIn = SignIn(self.driver)
        signIn.email.send_keys("user1@gmail.com")
        signIn.password.send_keys("Qwerty12345")
        signIn.submit.click()