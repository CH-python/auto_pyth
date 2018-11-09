import unittest
from selenium import webdriver
from TestforUS1.Pages.WelcomePage import Welcome
from TestforUS1.Pages.SignInPage import SignIn
from TestforUS1.Pages.MainUserPage import MainUserPage
from TestforUS1.Pages.PaymentsPage import PaymentsPage,PopupItemPayment,SelectPaymentSum,PopupEasyPay,AdditionalFields,AdditionalClose

class TestTC2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
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

        self.driver.implicitly_wait(10)
        paymentPage = PaymentsPage(self.driver)
        paymentPage.btnDetails.click()
        popupDetails = PopupItemPayment(self.driver)
        popupDetails.btnPay.click()
        self.driver.implicitly_wait(10)
        selectPaymentSum = SelectPaymentSum(self.driver)
        selectPaymentSum.inputPaymentSum.send_keys("2")
        selectPaymentSum.btnDownloadCheck.click()
        selectPaymentSum.btnProceed.click()

        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        self.driver.implicitly_wait(10)
        popEasyPay = PopupEasyPay(self.driver)
        popEasyPay.cardNumberInput.send_keys("4242424242424242")
        popEasyPay.dateCardInput.send_keys("012019")
        popEasyPay.cvNumberInput.send_keys("333")
        popEasyPay.mailInput.send_keys("sviatuy93@gmail.com")
        popEasyPay.btnRememberMe.click()

        self.driver.implicitly_wait(10)
        fields = AdditionalFields(self.driver)
        fields.zipCodeInput.send_keys("58022")
        fields.phoneInput.send_keys("991214424")

        popEasyPay.btnPay.click()

        self.driver.implicitly_wait(10)
        close = AdditionalClose(self.driver)
        close.btnClose.click()
        self.driver.implicitly_wait(10)
        popEasyPay.btnPay.click()

        self.driver.switch_to.default_content()

        # self.driver.manage().timeouts().pageLoadTimeout(10, TimeUnit.SECONDS);
        # currentURL = self.driver.Url

    def TearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()