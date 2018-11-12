import unittest
from selenium import webdriver
from TestforUS1.GetTo.getToSignIn import getToSignInPage
from TestforUS1.GetTo.getToMainUserPage import getToMainUserPage
from TestforUS1.GetTo.getToPaymentPage import getToPaymentPage
from TestforUS1.GetTo.getToPopupDetails import getToPopupDetails
from TestforUS1.Pages.paymentsPage import PopupItemPayment
from TestforUS1.screenShot import SS


class TestTC1(unittest.TestCase):

    def setUp(self):

        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:8080/")

    def testSelectBill(self):

        getToSignInPage(self.driver)
        getToMainUserPage(self.driver)
        self.driver.implicitly_wait(10)
        getToPaymentPage(self.driver)
        self.driver.implicitly_wait(10)
        getToPopupDetails(self.driver)

        popupDetails = PopupItemPayment(self.driver)
        actual = popupDetails.titleDetails.text
        self.assertEquals(actual, "Utility details");

    def TearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()