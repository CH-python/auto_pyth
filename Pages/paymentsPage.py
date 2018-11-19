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

    def fillPopupEasyPayFields(self, cardNumberm, dateCard, cvNumber):
        self.driver.find_element(By.CSS_SELECTOR, Locator.cardNumberInput).send_keys(cardNumberm)
        self.driver.find_element(By.CSS_SELECTOR, Locator.dateCardInput).send_keys(dateCard)
        self.driver.find_element(By.CSS_SELECTOR, Locator.cvNumberInput).send_keys(cvNumber)

    def clickRememberMe(self):
        self.driver.find_element(By.CSS_SELECTOR, Locator.btnRememberMe).click()

    def getCvNumber(self):
        return self.driver.find_element(By.CSS_SELECTOR, Locator.cvNumberInput).text

    def getCardNumber(self):
        return self.driver.find_element(By.CSS_SELECTOR, Locator.cardNumberInput).text

    def getTitlePopupEasyPay(self):
        return self.driver.find_element(By.CSS_SELECTOR, Locator.titlePopupEasyPay).text

    def fillAdditionalFieldsPopupEasy(self, zipCode, phone, mail):
        self.driver.find_element(By.CSS_SELECTOR, Locator.zipCodeInput).send_keys(zipCode)
        self.driver.find_element(By.CSS_SELECTOR, Locator.phoneInput).send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, Locator.mailInput).send_keys(mail)
        self.driver.find_element(By.CLASS_NAME, Locator.btnPopupPay).click()

    def clickBackPopupEasy(self):
        self.driver.find_element(By.CLASS_NAME, Locator.btnBack).click()