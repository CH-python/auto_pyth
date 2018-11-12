from TestforUS1.Pages.paymentsPage import PopupItemPayment

class getToPopupSelectSum(object):

    def __init__(self, driver):
        self.driver = driver
        popupDetails = PopupItemPayment(self.driver)
        popupDetails.btnPay.click()