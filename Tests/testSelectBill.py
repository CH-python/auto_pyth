import unittest
from selenium import webdriver
from TestforUS1.Pages.welcomePage import Welcome
from TestforUS1.Pages.loginPage import Login
from TestforUS1.Pages.mainUserPage import MainUserPage
from TestforUS1.Pages.paymentsPage import PaymentsPage, PopupUtilityDetails



class TestTC1(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:8080/")

    def testSelectBill(self):

        welcomePage = Welcome(self.driver)
        loginPage = Login(self.driver)
        mainUserPage = MainUserPage(self.driver)
        paymentPage = PaymentsPage(self.driver)
        utilityDetailsPopup = PopupUtilityDetails(self.driver)

        welcomePage.signIn()
        loginPage.login('user1@gmail.com', 'Qwerty12345')
        mainUserPage.getToPaymentPage()
        paymentPage.getPaymentDetails()
        actual = utilityDetailsPopup.getTitleDetails()
        print(actual)
        self.assertEquals(actual, "Utility details")

    def tearDown(self):
        self.driver.close()

# if __name__ == "__main__":
#     unittest.main()