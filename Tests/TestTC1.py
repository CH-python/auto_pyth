import unittest
from selenium import webdriver
from TestforUS1.Pages.WelcomePage import Welcome
from TestforUS1.Pages.SignInPage import SignIn
from TestforUS1.Pages.MainUserPage import MainUserPage
from TestforUS1.Pages.PaymentsPage import PaymentsPage,PopupItemPayment

class TestTC1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:8080/")

    def test_getToSignIn(self):
        welcome = Welcome(self.driver)
        welcome.signIn.click()

        signIn = SignIn(self.driver)
        signIn.email.send_keys("user1@gmail.com")
        signIn.password.send_keys("Qwerty12345")
        signIn.submit.click()

        self.driver.implicitly_wait(10)
        userPage = MainUserPage(self.driver)
        userPage.itemPayments.click()

        paymentPage = PaymentsPage(self.driver)
        paymentPage.btnDetails.click()
        popupDetails = PopupItemPayment(self.driver)
        actual = popupDetails.titleDetails.text
        # self.assertEquals(actual, "Utility details");

    def TearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()