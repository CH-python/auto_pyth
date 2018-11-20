import unittest, time
from TestforUS1.webdriverFactory import WebdriverFactory
from TestforUS1.dataTests import DataTest
from TestforUS1.Pages.welcomePage import Welcome
from TestforUS1.Pages.loginPage import Login
from TestforUS1.Pages.mainUserPage import MainUserPage
from TestforUS1.Pages.paymentsPage import PaymentsPage, PopupUtilityDetails, PopupSelectPaymentSum, PopupEasyPay

class TestTC15(unittest.TestCase):

    def setUp(self):
        self.driver = WebdriverFactory.getWebdriver(DataTest.browser)
        self.driver.get(DataTest.url['home'])

    def testCheckBalanceAfterPay(self):
        driver = self.driver
        # wait = WebDriverWait(driver, 10)

        welcomePage = Welcome(driver)
        loginPage = Login(driver)
        mainUserPage = MainUserPage(driver)
        paymentPage = PaymentsPage(driver)
        utilityDetailsPopup = PopupUtilityDetails(driver)
        selectSumPopup = PopupSelectPaymentSum(driver)
        easyPayPopup = PopupEasyPay(driver)

        welcomePage.signIn()
        loginPage.login(DataTest.popupEasyPay['email'],
                        DataTest.popupEasyPay['password'])
        mainUserPage.getToPaymentPage()
        paymentPage.getPaymentDetails()
        balanceValue1 = paymentPage.getBalanceValue()
        utilityDetailsPopup.clickButtonPay()

        selectSumPopup.enterInputSum(DataTest.sumValue)
        selectSumPopup.clickBtnDownload()
        selectSumPopup.clickBtnProceed()

        easyPayPopup.getToIframe()
        easyPayPopup.fillPopupEasyPayFields(DataTest.popupEasyPay['cardNumber'],
                                            DataTest.popupEasyPay['dateCard'],
                                            DataTest.popupEasyPay['cvNumber'])
        easyPayPopup.clickRememberMe()
        easyPayPopup.fillAdditionalFieldsPopupEasy(DataTest.popupEasyPay['zipCode'],
                                                   DataTest.popupEasyPay['phone'],
                                                   DataTest.popupEasyPay['mail'])
        easyPayPopup.clickBackPopupEasy()

        driver.switch_to.default_content()
        time.sleep(10)
        driver.get(DataTest.url['paymentsPage'])
        balanceValue2 = paymentPage.getBalanceValue()
        result = balanceValue2 - balanceValue1
        self.assertEquals(float(result), float(DataTest.sumValue))

    def tearDown(self):
        self.driver.close()