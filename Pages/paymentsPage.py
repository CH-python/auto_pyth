from TestforUS1.locators import Locator
from selenium.webdriver.common.by import By

class PaymentsPage(object):

    def __init__(self, driver):
        self.driver = driver

    def getPaymentDetails(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.CSS_SELECTOR, Locator.details).click()

    def getBalanceValue(self):
        self.driver.find_element(By.CSS_SELECTOR, Locator.balance)

class PopupUtilityDetails(object):

    def __init__(self, driver):
        self.driver = driver

    def getTitleDetails(self):
        return self.driver.find_element(By.CSS_SELECTOR, Locator.titlePopup).text

    def clickButtonPay(self):
        self.driver.find_element(By.ID, Locator.pay).click()

class PopupSelectPaymentSum(object):

    def __init__(self, driver):
        self.driver = driver

    def enterInputSum(self, sum):
        self.driver.find_element(By.ID, Locator.paymentSum).send_keys(sum)

    def getAtributeDownload(self):
        return self.driver.find_element(By.ID, Locator.downloadCheck).get_attribute("class")

    def getAttributeSend(self):
        return self.driver.find_element(By.ID, Locator.sendCheck).get_attribute("class")

    def clickBtnDownload(self):
        self.driver.find_element(By.ID, Locator.downloadCheck).click()

    def clickBtnSendCheck(self):
        self.driver.find_element(By.ID, Locator.sendCheck).click()

    def clickBtnProceed(self):
        self.driver.find_element(By.ID, Locator.proceed).click()

class PopupEasyPay(object):

    def __init__(self, driver):
        self.driver = driver

    def getToIframe(self):
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))

    def getTitleEasypay(self):
        return self.driver.find_element(By.CSS_SELECTOR, Locator.titlePopupEasyPay).text

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