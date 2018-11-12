import unittest
from selenium import webdriver
from TestforUS1.Pages.welcomePage import Welcome
from TestforUS1.Pages.signInPage import SignIn
from TestforUS1.Pages.mainUserPage import MainUserPage
from TestforUS1.Pages.paymentsPage import PaymentsPage,PopupItemPayment,SelectPaymentSum,PopupEasyPay

class TestTC4(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:8080/")

    def testGetToPaymentPopup(self):
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
        selectPaymentSum.inputPaymentSum.send_keys("3")
        selectPaymentSum.btnDownloadCheck.click()
        selectPaymentSum.btnProceed.click()

        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        self.driver.implicitly_wait(10)
        popupEasyPay = PopupEasyPay(self.driver)
        actual = popupEasyPay.titlePopupEasyPay.text
        self.assertEqual(actual, 'EasyPay')



    def TearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()