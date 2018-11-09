import unittest
from selenium import webdriver
from TestforUS1.Pages.WelcomePage import Welcome
from TestforUS1.Pages.SignInPage import Sign_In
from TestforUS1.Pages.MainUserPage import MainUserPage,popupItemPayment
from TestforUS1.Pages.PaymentsPage import PaymentsPage

class TestTC1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:8080/")

    def test_getToSignIn(self):
        welcome = Welcome(self.driver)
        welcome.sign_in.click()

        signIn = Sign_In(self.driver)
        signIn.email.send_keys("user1@gmail.com")
        signIn.password.send_keys("Qwerty13")
        signIn.submit.click()

        self.driver.implicitly_wait(10)
        userPage = MainUserPage(self.driver)
        userPage.itemPayments.click()

        self.driver.implicitly_wait(10)
        popupDetails = popupItemPayment(self.driver)
        popupDetails.btnDetails.click()

        self.driver.implicitly_wait(10)
        actual = popupDetails.titleDetails.text
        print(type(actual))
        print(actual)
        # self.assertEquals(actual, "Utility details")

    def TearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()