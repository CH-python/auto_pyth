import unittest
# import sys
# import os.path
# module_path = os.path.join('..', 'Pages')
# sys.path.append(module_path)
from selenium import webdriver
from TestforUS1.Pages.welcomePage import Welcome
from TestforUS1.Pages.loginPage import Login
from TestforUS1.Pages.mainUserPage import MainUserPage
from TestforUS1.Pages.paymentsPage import PaymentsPage, PopupUtilityDetails, PopupSelectPaymentSum, PopupEasyPay

class TestTC4(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:8080/")

    def testGetToEasyPayWindow(self):

        welcomePage = Welcome(self.driver)
        loginPage = Login(self.driver)
        mainUserPage = MainUserPage(self.driver)
        paymentPage = PaymentsPage(self.driver)
        utilityDetailsPopup = PopupUtilityDetails(self.driver)
        selectSumPopup = PopupSelectPaymentSum(self.driver)
        easyPayPopup = PopupEasyPay(self.driver)

        welcomePage.signIn()
        loginPage.login('user1@gmail.com', 'Qwerty12345')
        mainUserPage.getToPaymentPage()
        paymentPage.getPaymentDetails()
        utilityDetailsPopup.clickButtonPay()
        selectSumPopup.enterInputSum("25")
        selectSumPopup.clickBtnSendCheck()
        selectSumPopup.clickBtnProceed()
        easyPayPopup.getToIframe()
        actual = easyPayPopup.getTitleEasypay()
        self.assertEqual(actual, 'EasyPay')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()