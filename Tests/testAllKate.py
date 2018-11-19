import unittest
from selenium import webdriver
from TestforUS1.Pages.welcomePage import Welcome
from TestforUS1.Pages.loginPage import Login
from TestforUS1.Pages.mainUserPage import MainUserPage
from TestforUS1.Pages.paymentsPage import PaymentsPage, PopupUtilityDetails, PopupSelectPaymentSum, PopupEasyPay

class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:8080/")

    def getToPaymentDetailsPopup(self):
        welcomePage = Welcome(self.driver)
        loginPage = Login(self.driver)
        mainUserPage = MainUserPage(self.driver)
        paymentPage = PaymentsPage(self.driver)

        welcomePage.signIn()
        loginPage.login('user1@gmail.com', 'Qwerty12345')
        mainUserPage.getToPaymentPage()
        paymentPage.getPaymentDetails()

    def testSelectBill(self):

        Test.getToPaymentDetailsPopup(self)
        utilityDetailsPopup = PopupUtilityDetails(self.driver)

        actual = utilityDetailsPopup.getTitleDetails()
        self.assertEquals(actual, "Utility details")

    def testButtonsDownloadAndSend(self):

        Test.getToPaymentDetailsPopup(self)
        utilityDetailsPopup = PopupUtilityDetails(self.driver)
        selectSumPopup = PopupSelectPaymentSum(self.driver)

        utilityDetailsPopup.clickButtonPay()
        selectSumPopup.clickBtnDownload()
        active = selectSumPopup.getAtributeDownload()
        self.assertEqual(active, 'btn btn-default active')

        selectSumPopup.clickBtnSendCheck()
        active = selectSumPopup.getAttributeSend()
        self.assertEqual(active, 'btn btn-default active')

    def testGetToPaymentWindow(self):

        Test.getToPaymentDetailsPopup(self)
        utilityDetailsPopup = PopupUtilityDetails(self.driver)
        selectSumPopup = PopupSelectPaymentSum(self.driver)
        easyPayPopup = PopupEasyPay(self.driver)

        utilityDetailsPopup.clickButtonPay()
        selectSumPopup.enterInputSum("3")
        selectSumPopup.clickBtnDownload()
        selectSumPopup.clickBtnProceed()
        easyPayPopup.getToIframe()

        title = easyPayPopup.getTitleEasypay()
        self.assertEqual(title, 'EasyPay')

    def tearDown(self):
        self.driver.close()