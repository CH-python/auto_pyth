import unittest
import TestforUS1.locators as Loc
from selenium import webdriver
from TestforUS1.Pages.welcomePage import Welcome
from TestforUS1.Pages.loginPage import Login
from TestforUS1.Pages.mainUserPage import MainUserPage
from selenium.webdriver.common.by import By
from TestforUS1.Pages.paymentsPage import PaymentsPage, PopupUtilityDetails, PopupSelectPaymentSum, PopupEasyPay

class TestTC7(unittest.TestCase):

    def setUp(self):

        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:8080/")

    def testGetRememberTelefone(self):

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
        easyPayPopup.fillPopupEasyPayFields("user1@gmail.com", "4242424242424242", "042019", "997")
        easyPayPopup.fillAdditionalFieldsPopupEasy("58000", "503381234")

        actual = easyPayPopup.driver.find_element(By.CSS_SELECTOR, Loc.Locator.phoneInputCSS)
        # print(str(actual))
        self.assertTrue(actual)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

