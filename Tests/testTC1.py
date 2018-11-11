import unittest
from selenium import webdriver
from TestforUS1.Pages.welcomePage import Welcome
from TestforUS1.Pages.signInPage import SignIn
from TestforUS1.Pages.mainUserPage import MainUserPage
from TestforUS1.Pages.paymentsPage import PaymentsPage,PopupItemPayment
from TestforUS1.screenShot import SS


class TestTC1(unittest.TestCase):

    def setUp(self):

        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:8080/")

    def testGetToSignIn(self):
        ss = SS(self.driver)
        welcome = Welcome(self.driver)
        ss.ScreenShot('/testTC1/screen1.png')
        welcome.signIn.click()
        ss.ScreenShot('/testTC1/screen2.png')

        signIn = SignIn(self.driver)
        signIn.email.send_keys("user1@gmail.com")
        signIn.password.send_keys("Qwerty12345")
        signIn.submit.click()

        self.driver.implicitly_wait(10)
        userPage = MainUserPage(self.driver)
        ss.ScreenShot('/testTC1/screen3.png')
        userPage.itemPayments.click()

        ss.ScreenShot('/testTC1/screen4.png')
        paymentPage = PaymentsPage(self.driver)
        paymentPage.btnDetails.click()

        ss.ScreenShot('/testTC1/screen5.png')
        popupDetails = PopupItemPayment(self.driver)
        actual = popupDetails.titleDetails.text
        self.assertEquals(actual, "Utility details");

    def TearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()