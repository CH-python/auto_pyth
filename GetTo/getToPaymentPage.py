from TestforUS1.Pages.mainUserPage import MainUserPage

class getToPaymentPage(object):

    def __init__(self, driver):
        self.driver = driver
        userPage = MainUserPage(self.driver)
        userPage.itemPayments.click()