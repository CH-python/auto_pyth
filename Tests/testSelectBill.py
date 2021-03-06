import unittest
from TestforUS1.webdriverFactory import WebdriverFactory
from TestforUS1.dataTests import DataTest
from TestforUS1.Pages.welcomePage import Welcome
from TestforUS1.Pages.loginPage import Login
from TestforUS1.Pages.mainUserPage import MainUserPage
from TestforUS1.Pages.paymentsPage import PaymentsPage, PopupUtilityDetails

class TestTC1(unittest.TestCase):

    def setUp(self):
        self.driver = WebdriverFactory.getWebdriver(DataTest.browser)
        self.driver.get(DataTest.url['home'])

    def testSelectBill(self):
        welcomePage = Welcome(self.driver)
        loginPage = Login(self.driver)
        mainUserPage = MainUserPage(self.driver)
        paymentPage = PaymentsPage(self.driver)
        utilityDetailsPopup = PopupUtilityDetails(self.driver)

        welcomePage.signIn()
        loginPage.login(DataTest.popupEasyPay['email'],
                        DataTest.popupEasyPay['password'])
        mainUserPage.getToPaymentPage()
        paymentPage.getPaymentDetails()
        utilityTitle = utilityDetailsPopup.getTitleDetails()
        self.assertEquals(utilityTitle, "Utility details")

    def tearDown(self):
        self.driver.close()
