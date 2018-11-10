import unittest
from selenium import webdriver
from TestforUS1.Pages.welcomePage import Welcome
from TestforUS1.Pages.signInPage import SignIn
from TestforUS1.Pages.mainUserPage import MainUserPage
from TestforUS1.Pages.paymentsPage import PaymentsPage,PopupItemPayment,SelectPaymentSum

class TestTC3(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
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
        popupDetails.btnPay.click()

        selectPaymentSum = SelectPaymentSum(self.driver)


        selectPaymentSum.btnDownloadCheck.click()
        active = selectPaymentSum.btnDownloadCheck.get_attribute("class")
        self.assertEqual(active, 'btn btn-default active')

        selectPaymentSum.btnSendCheck.click()
        self.driver.implicitly_wait(10)
        active = selectPaymentSum.btnSendCheck.get_attribute("class")
        self.assertEqual(active, 'btn btn-default active')



    def TearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()