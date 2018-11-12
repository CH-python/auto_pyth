import unittest
from selenium import webdriver
from TestforUS1.GetTo.getToSignIn import getToSignInPage
from TestforUS1.GetTo.getToMainUserPage import getToMainUserPage
from TestforUS1.GetTo.getToPaymentPage import getToPaymentPage
from TestforUS1.GetTo.getToPopupDetails import getToPopupDetails
from TestforUS1.GetTo.getToPopupSelectSum import getToPopupSelectSum
from TestforUS1.GetTo.getToPopupPayment import getToPopupPayment
from TestforUS1.Pages.paymentsPage import PopupEasyPay

class TestTC4(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:8080/")

    def testGetToPaymentWindow(self):

        getToSignInPage(self.driver)
        getToMainUserPage(self.driver)
        self.driver.implicitly_wait(10)
        getToPaymentPage(self.driver)
        self.driver.implicitly_wait(10)
        getToPopupDetails(self.driver)
        self.driver.implicitly_wait(10)
        getToPopupSelectSum(self.driver)
        self.driver.implicitly_wait(10)
        getToPopupPayment(self.driver)


        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        self.driver.implicitly_wait(10)
        popupEasyPay = PopupEasyPay(self.driver)
        actual = popupEasyPay.titlePopupEasyPay.text
        self.assertEqual(actual, 'EasyPay')



    def TearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()