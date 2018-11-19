import unittest
import logging
from TestforUS1.webdriverFactory import WebdriverFactory
from TestforUS1.dataTests import DataTest
from TestforUS1.Pages.welcomePage import Welcome
from TestforUS1.Pages.loginPage import Login
from TestforUS1.Pages.mainUserPage import MainUserPage
from TestforUS1.Pages.paymentsPage import PaymentsPage, PopupUtilityDetails, PopupSelectPaymentSum, PopupEasyPay


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = WebdriverFactory.getWebdriver(DataTest.browser)
        self.driver.get(DataTest.url['home'])
        self.logger = logging.getLogger()


        self.welcomePage = Welcome(self.driver)
        self.loginPage = Login(self.driver)
        self.mainUserPage = MainUserPage(self.driver)
        self.paymentPage = PaymentsPage(self.driver)
        self.utilityDetailsPopup = PopupUtilityDetails(self.driver)
        self.selectSumPopup = PopupSelectPaymentSum(self.driver)
        self.easyPayPopup = PopupEasyPay(self.driver)

    def getToPaymentDetailsPopup(self):

        self.welcomePage.signIn()
        self.loginPage.login(DataTest.popupEasyPay['email'], DataTest.popupEasyPay['password'])
        self.mainUserPage.getToPaymentPage()
        self.paymentPage.getPaymentDetails()

    def testSelectBill(self):
        self.logger.info("Test select bill")

        self.getToPaymentDetailsPopup()

        actual = self.utilityDetailsPopup.getTitleDetails()
        self.assertEquals(actual, "Utility details")

    def testButtonsDownloadAndSend(self):
        self.logger.info("Test button download and send")

        self.getToPaymentDetailsPopup()

        self.utilityDetailsPopup.clickButtonPay()
        self.selectSumPopup.clickBtnDownload()
        active = self.selectSumPopup.getAtributeDownload()
        print(active)
        self.assertEqual(active, 'btn btn-default active')

        self.selectSumPopup.clickBtnSendCheck()
        active = self.selectSumPopup.getAttributeSend()
        print(active)
        self.assertEqual(active, 'btn btn-default active')

    def testGetToPaymentWindow(self):
        self.logger.info("Test get to Payment window")

        self.getToPaymentDetailsPopup()

        self.utilityDetailsPopup.clickButtonPay()
        self.selectSumPopup.enterInputSum(DataTest.sumValue)
        self.selectSumPopup.clickBtnDownload()
        self.selectSumPopup.clickBtnProceed()
        self.easyPayPopup.getToIframe()

        title = self.easyPayPopup.getTitleEasypay()
        print(title)
        self.assertEqual(title, 'EasyPay')

    def tearDown(self):
        self.driver.close()