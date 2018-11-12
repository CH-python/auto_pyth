from TestforUS1.Pages.paymentsPage import PaymentsPage

class getToPopupDetails(object):

    def __init__(self, driver):
        self.driver = driver
        paymentPage = PaymentsPage(self.driver)
        paymentPage.btnDetails.click()