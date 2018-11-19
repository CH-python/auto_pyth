import unittest
from TestforUS1.webdriverFactory import WebdriverFactory
from TestforUS1.dataTests import DataTest
from TestforUS1.Pages.welcomePage import Welcome
from TestforUS1.Pages.loginPage import Login
from TestforUS1.Pages.mainUserPage import MainUserPage
from TestforUS1.Pages.paymentsPage import PaymentsPage, PopupUtilityDetails, PopupSelectPaymentSum, PopupEasyPay

class TestTC11(unittest.TestCase):

    def setUp(self):
        self.driver = WebdriverFactory.getWebdriver(DataTest.browser)
        self.driver.get(DataTest.url['home'])

    def testCheckNoSaveCardDataAfterRefresh(self):
        welcomePage = Welcome(self.driver)
        loginPage = Login(self.driver)
        mainUserPage = MainUserPage(self.driver)
        paymentPage = PaymentsPage(self.driver)
        utilityDetailsPopup = PopupUtilityDetails(self.driver)
        selectSumPopup = PopupSelectPaymentSum(self.driver)
        easyPayPopup = PopupEasyPay(self.driver)

        welcomePage.signIn()
        loginPage.login(DataTest.popupEasyPay['email'],
                        DataTest.popupEasyPay['password'])
        mainUserPage.getToPaymentPage()
        paymentPage.getPaymentDetails()
        utilityDetailsPopup.clickButtonPay()

        selectSumPopup.enterInputSum(DataTest.sumValue)
        selectSumPopup.clickBtnDownload()
        selectSumPopup.clickBtnProceed()

        easyPayPopup.getToIframe()
        easyPayPopup.fillPopupEasyPayFields(DataTest.popupEasyPay['cardNumber'],
                                            DataTest.popupEasyPay['dateCard'],
                                            DataTest.popupEasyPay['cvNumber'])

        self.driver.refresh()

        paymentPage.getPaymentDetails()
        utilityDetailsPopup.clickButtonPay()

        selectSumPopup.enterInputSum(DataTest.sumValue)
        selectSumPopup.clickBtnDownload()
        selectSumPopup.clickBtnProceed()

        easyPayPopup.getToIframe()

        cardNumber = easyPayPopup.getCardNumber()
        self.assertEqual(cardNumber, '')

    def tearDown(self):
        self.driver.close()