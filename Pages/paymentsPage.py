from TestforUS1.locators import Locator
from TestforUS1.methods import Methods
from selenium.webdriver.common.by import By

class PaymentsPage(object):

    def __init__(self, driver):
        self.driver = driver

    def getPaymentDetails(self):
        self.driver.implicitly_wait(10)
        methods = Methods(self.driver)
        methods.clickElement(Locator.details, 'css')

    def getBalanceValue(self):
        methods = Methods(self.driver)
        return float(methods.getText(Locator.balance, 'css'))

class PopupUtilityDetails(object):

    def __init__(self, driver):
        self.driver = driver

    def getTitleDetails(self):
        methods = Methods(self.driver)
        return methods.getText(Locator.titlePopupPayments, 'css')

    def clickButtonPay(self):
        methods = Methods(self.driver)
        methods.clickElement(Locator.pay, 'id')

class PopupSelectPaymentSum(object):

    def __init__(self, driver):
        self.driver = driver

    def enterInputSum(self, sum):
        methods = Methods(self.driver)
        methods.sendKeys(sum, Locator.paymentSum, 'id')

    def getAtributeDownload(self):
        methods = Methods(self.driver)
        return methods.getAttribute('class', Locator.downloadCheck, 'id')

    def getAttributeSend(self):
        methods = Methods(self.driver)
        return methods.getAttribute('class', Locator.sendCheck, 'id')

    def clickBtnDownload(self):
        methods = Methods(self.driver)
        methods.clickElement(Locator.downloadCheck, 'id')

    def clickBtnSendCheck(self):
        methods = Methods(self.driver)
        methods.clickElement(Locator.sendCheck, 'id')

    def clickBtnProceed(self):
        methods = Methods(self.driver)
        methods.clickElement(Locator.proceed, 'id')

class PopupEasyPay(object):

    def __init__(self, driver):
        self.driver = driver

    def getToIframe(self):
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))

    def getTitleEasypay(self):
        methods = Methods(self.driver)
        return methods.getText(Locator.titlePopupEasyPay, 'css')

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