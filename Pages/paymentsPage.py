from TestforUS1.locators import Locator
from TestforUS1.Methods import Methods

class PaymentsPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.methods = Methods(self.driver)

    def getPaymentDetails(self):
        self.methods.waitForElement(Locator.details, 'css').clickElement(Locator.details, 'css')

    def getBalanceValue(self):
        self.methods.clickElement(Locator.balance, 'css')

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

    def fillPopupEasyPayFields(self, mail, cardNumberm, dateCard, cvNumber):

        self.driver.find_element(By.CSS_SELECTOR, Locator.mailInput).send_keys(mail)
        self.driver.find_element(By.CSS_SELECTOR, Locator.cardNumberInput).send_keys(cardNumberm)
        self.driver.find_element(By.CSS_SELECTOR, Locator.dateCardInput).send_keys(dateCard)
        self.driver.find_element(By.CSS_SELECTOR, Locator.cvNumberInput).send_keys(cvNumber)
        self.driver.find_element(By.CSS_SELECTOR, Locator.btnRememberMe).click()
        self.driver.find_element(By.CLASS_NAME, Locator.btnPopupPay).click()
        self.driver.find_element(By.CSS_SELECTOR, Locator.titlePopupEasyPay).text


    def fillAdditionalFieldsPopupEasy(self,zipCode,phone):

        self.driver.find_element(By.CSS_SELECTOR, Locator.zipCodeInput).send_keys(zipCode)
        self.driver.find_element(By.CSS_SELECTOR, Locator.phoneInput).send_keys(phone)

    def clickBackPopupEasy(self):

        self.driver.find_element(By.CLASS_NAME, Locator.btnBack).click()