import unittest, time, logging
from TestforUS1.webdriverFactory import WebdriverFactory
from TestforUS1.Pages.welcomePage import Welcome
from TestforUS1.Pages.loginPage import Login
from TestforUS1.dataTests import DataTest
from TestforUS1.Pages.mainUserPage import MainUserPage
from TestforUS1.Pages.paymentsPage import PaymentsPage, PopupUtilityDetails, PopupSelectPaymentSum, PopupEasyPay

class Test(unittest.TestCase):

    def setUp(self):
        self.driver = WebdriverFactory.getWebdriver(DataTest.browser)
        self.driver.get(DataTest.url['home'])
        self.welcomePage = Welcome(self.driver)
        self.loginPage = Login(self.driver)
        self.mainUserPage = MainUserPage(self.driver)
        self.paymentPage = PaymentsPage(self.driver)
        self.utilityDetailsPopup = PopupUtilityDetails(self.driver)
        self.selectSumPopup = PopupSelectPaymentSum(self.driver)
        self.easyPayPopup = PopupEasyPay(self.driver)

    def getToPaymentDetailsPopup(self):
        self.welcomePage.signIn()
        self.loginPage.login(DataTest.popupEasyPay['email'],
                             DataTest.popupEasyPay['password'])
        self.mainUserPage.getToPaymentPage()
        self.paymentPage.getPaymentDetails()

    def loggerInfo(self,name):
        self.logger = logging.getLogger()
        self.logger.info("_" * 10 + name)

    def testCheckNoSaveCvcAfterRefresh(self):
        name = unittest.TestCase.id(self)
        self.loggerInfo(name)
        self.getToPaymentDetailsPopup()
        self.utilityDetailsPopup.clickButtonPay()

        self.selectSumPopup.enterInputSum(DataTest.sumValue)
        self.selectSumPopup.clickBtnDownload()
        self.selectSumPopup.clickBtnProceed()

        self.easyPayPopup.getToIframe()
        self.easyPayPopup.fillPopupEasyPayFields(DataTest.popupEasyPay['cardNumber'],
                                                 DataTest.popupEasyPay['dateCard'],
                                                 DataTest.popupEasyPay['cvNumber'])

        self.driver.refresh()

        self.paymentPage.getPaymentDetails()
        self.utilityDetailsPopup.clickButtonPay()

        self.selectSumPopup.enterInputSum(DataTest.sumValue)
        self.selectSumPopup.clickBtnDownload()
        self.selectSumPopup.clickBtnProceed()

        self.easyPayPopup.getToIframe()

        self.cvNumber = self.easyPayPopup.getCvNumber()
        self.assertEqual(self.cvNumber, '')

    def testCheckNoSaveCardDataAfterRefresh(self):
        name = unittest.TestCase.id(self)
        self.loggerInfo(name)
        self.getToPaymentDetailsPopup()
        self.utilityDetailsPopup.clickButtonPay()

        self.selectSumPopup.enterInputSum(DataTest.sumValue)
        self.selectSumPopup.clickBtnDownload()
        self.selectSumPopup.clickBtnProceed()

        self.easyPayPopup.getToIframe()
        self.easyPayPopup.fillPopupEasyPayFields(DataTest.popupEasyPay['cardNumber'],
                                                 DataTest.popupEasyPay['dateCard'],
                                                 DataTest.popupEasyPay['cvNumber'])

        self.driver.refresh()

        self.paymentPage.getPaymentDetails()
        self.utilityDetailsPopup.clickButtonPay()

        self.selectSumPopup.enterInputSum(DataTest.sumValue)
        self.selectSumPopup.clickBtnDownload()
        self.selectSumPopup.clickBtnProceed()

        self.easyPayPopup.getToIframe()

        cardNumber = self.easyPayPopup.getCardNumber()
        self.assertEqual(cardNumber, '')

    def testCheckBalanceAfterPay(self):
        name = unittest.TestCase.id(self)
        self.loggerInfo(name)
        self.getToPaymentDetailsPopup()

        balanceValue1 = self.paymentPage.getBalanceValue()
        self.utilityDetailsPopup.clickButtonPay()

        self.selectSumPopup.enterInputSum(DataTest.sumValue)
        self.selectSumPopup.clickBtnDownload()
        self.selectSumPopup.clickBtnProceed()

        self.easyPayPopup.getToIframe()
        self.easyPayPopup.fillPopupEasyPayFields(DataTest.popupEasyPay['cardNumber'],
                                                 DataTest.popupEasyPay['dateCard'],
                                                 DataTest.popupEasyPay['cvNumber'])
        self.easyPayPopup.clickRememberMe()
        self.easyPayPopup.fillAdditionalFieldsPopupEasy(DataTest.popupEasyPay['zipCode'],
                                                        DataTest.popupEasyPay['phone'],
                                                        DataTest.popupEasyPay['mail'])
        self.easyPayPopup.clickBackPopupEasy()

        self.driver.switch_to.default_content()
        time.sleep(10)
        self.driver.get(DataTest.url['paymentsPage'])
        balanceValue2 = self.paymentPage.getBalanceValue()
        result = balanceValue2 - balanceValue1
        self.assertEquals(result, float(DataTest.sumValue))

    def tearDown(self):
        self.driver.close()