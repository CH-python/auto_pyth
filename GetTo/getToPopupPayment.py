from TestforUS1.Pages.paymentsPage import SelectPaymentSum

class getToPopupPayment(object):

    def __init__(self, driver):
        self.driver = driver

        selectPaymentSum = SelectPaymentSum(self.driver)
        selectPaymentSum.inputPaymentSum.send_keys("3")
        selectPaymentSum.btnDownloadCheck.click()
        selectPaymentSum.btnProceed.click()