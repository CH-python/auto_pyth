from selenium import webdriver
import time, allure, unittest
from TestforUS1.Pages.welcomePage import Welcome
from TestforUS1.Pages.signInPage import SignIn
from TestforUS1.Pages.mainUserPage import MainUserPage
from TestforUS1.Pages.paymentsPage import PaymentsPage,PopupItemPayment,\
    SelectPaymentSum,PopupEasyPay,AdditionalFields,AdditionalClose

class TestTC15(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:8080/")

    def testCheckBalanceAfterPay(self):
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
        balanceValue1 = float(paymentPage.balance.text)
        popupDetails = PopupItemPayment(self.driver)
        time.sleep(1)
        popupDetails.btnPay.click()

        self.driver.implicitly_wait(10)
        selectPaymentSum = SelectPaymentSum(self.driver)
        selectPaymentSum.inputPaymentSum.send_keys("10")
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
        fields.phoneInput.send_keys("55555555")

        popEasyPay.btnPopupPay.click()

        self.driver.implicitly_wait(10)
        back = AdditionalClose(self.driver)
        back.btnBack.click()
        popEasyPay.btnPopupPay.click()

        self.driver.switch_to.default_content()

        time.sleep(10)
        self.driver.get("http://localhost:8080/user/paymentsPage")
        time.sleep(1)
        paymentPage = PaymentsPage(self.driver)
        balanceValue2 = float(paymentPage.balance.text)
        result = balanceValue2 - balanceValue1
        print(balanceValue2,balanceValue1,result)
        self.assertEquals(result, 10.0);

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()