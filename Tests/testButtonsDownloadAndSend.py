import unittest
from selenium import webdriver
from TestforUS1.GetTo.getToSignIn import getToSignInPage
from TestforUS1.GetTo.getToMainUserPage import getToMainUserPage
from TestforUS1.GetTo.getToPaymentPage import getToPaymentPage
from TestforUS1.GetTo.getToPopupDetails import getToPopupDetails
from TestforUS1.GetTo.getToPopupSelectSum import getToPopupSelectSum
from TestforUS1.Pages.paymentsPage import SelectPaymentSum

class TestTC3(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:8080/")

    def testButtonsDownloadAndSend(self):

        getToSignInPage(self.driver)
        getToMainUserPage(self.driver)
        self.driver.implicitly_wait(10)
        getToPaymentPage(self.driver)
        self.driver.implicitly_wait(10)
        getToPopupDetails(self.driver)
        self.driver.implicitly_wait(10)
        getToPopupSelectSum(self.driver)


        selectPaymentSum = SelectPaymentSum(self.driver)
        selectPaymentSum.btnDownloadCheck.click()
        active = selectPaymentSum.btnDownloadCheck.get_attribute("class")
        self.assertEqual(active, 'btn btn-default active')

        selectPaymentSum.btnSendCheck.click()
        self.driver.implicitly_wait(10)
        active = selectPaymentSum.btnSendCheck.get_attribute("class")
        self.assertEqual(active, 'btn btn-default active')



    def TearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()