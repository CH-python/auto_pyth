from TestforUS1.locators import Locator
from TestforUS1.methods import Methods

class PaymentsPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.methods = Methods(self.driver)

    def getPaymentDetails(self):
        self.methods.waitForElement(Locator.details, 'css').clickElement(Locator.details, 'css')

    def getBalanceValue(self):
        methods = Methods(self.driver)
        return float(methods.getText(Locator.balance, 'css'))


class PopupUtilityDetails(object):

    def __init__(self, driver):
        self.driver = driver
        self.methods = Methods(self.driver)

    def getTitleDetails(self):
        return self.methods.getText(Locator.titlePopupPayments, 'css')

    def clickButtonPay(self):
        self.methods.clickElement(Locator.pay, 'id')

class PopupSelectPaymentSum(object):

    def __init__(self, driver):
        self.driver = driver
        self.methods = Methods(self.driver)

    def enterInputSum(self, sum):
        self.methods.sendKeys(sum, Locator.paymentSum, 'id')

    def getAtributeDownload(self):
        return self.methods.getAttribute('class', Locator.downloadCheck, 'id')

    def getAttributeSend(self):
        return self.methods.getAttribute('class', Locator.sendCheck, 'id')

    def clickBtnDownload(self):
        self.methods.clickElement(Locator.downloadCheck, 'id')

    def clickBtnSendCheck(self):
        self.methods.clickElement(Locator.sendCheck, 'id')

    def clickBtnProceed(self):
        self.methods.clickElement(Locator.proceed, 'id')

class PopupEasyPay(object):

    def __init__(self, driver):
        self.driver = driver
        self.methods = Methods(self.driver)

    def getToIframe(self):
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))

    def getTitleEasypay(self):
        return self.methods.getText(Locator.titlePopupEasyPay, 'css')

    def fillPopupEasyPayFields(self, cardNumber, dateCard, cvNumber):
        methods = Methods(self.driver)
        methods.sendKeys(cardNumber, Locator.cardNumberInput, 'css')
        methods.sendKeys(dateCard, Locator.dateCardInput, 'css')
        methods.sendKeys(cvNumber, Locator.cvNumberInput, 'css')

    def clickRememberMe(self):
        methods = Methods(self.driver)
        methods.clickElement(Locator.btnRememberMe, 'css')

    def getCvNumber(self):
        methods = Methods(self.driver)
        return methods.getText(Locator.cvNumberInput, 'css')

    def getCardNumber(self):
        methods = Methods(self.driver)
        return methods.getText(Locator.cardNumberInput, 'css')

    def getTitlePopupEasyPay(self):
        methods = Methods(self.driver)
        return methods.getText(Locator.titlePopupEasyPay, 'css')

    def fillAdditionalFieldsPopupEasy(self, zipCode, phone, mail):
        methods = Methods(self.driver)
        methods.sendKeys(zipCode, Locator.zipCodeInput, 'css')
        methods.sendKeys(phone, Locator.phoneInput, 'css')
        methods.sendKeys(mail, Locator.mailInput, 'css')
        methods.clickElement(Locator.btnPopupPay, 'class')

    def clickBackPopupEasy(self):
        methods = Methods(self.driver)
        methods.clickElement(Locator.btnBack, 'class')