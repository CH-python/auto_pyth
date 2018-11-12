from TestforUS1.locators import Locator
from selenium.webdriver.common.by import By

class PaymentsPage(object):

    def __init__(self, driver):
        self.driver = driver

        # Sign In page locators defining

        self.btnDetails = driver.find_element(By.CSS_SELECTOR, Locator.details)
        self.balance = driver.find_element(By.CSS_SELECTOR, Locator.balance)

class PopupItemPayment(object):

    def __init__(self, driver):
        self.driver = driver

        self.titleDetails = driver.find_element(By.CSS_SELECTOR, Locator.titlePopup)
        self.btnPay = driver.find_element(By.ID, Locator.pay)

class SelectPaymentSum(object):

    def __init__(self, driver):
        self.driver = driver

        self.inputPaymentSum = driver.find_element(By.ID, Locator.paymentSum)
        self.btnDownloadCheck = driver.find_element(By.ID, Locator.downloadCheck)
        self.btnSendCheck = driver.find_element(By.ID, Locator.sendCheck)
        self.btnProceed = driver.find_element(By.ID, Locator.proceed)

class PopupEasyPay(object):

    def __init__(self, driver):
        self.driver = driver

        self.titlePopupEasyPay = driver.find_element(By.CSS_SELECTOR, Locator.titlePopupEasyPay)
        self.mailInput = driver.find_element(By.CSS_SELECTOR, Locator.mailInput)
        self.cardNumberInput = driver.find_element(By.CSS_SELECTOR, Locator.cardNumberInput)
        self.dateCardInput = driver.find_element(By.CSS_SELECTOR, Locator.dateCardInput)
        self.cvNumberInput = driver.find_element(By.CSS_SELECTOR, Locator.cvNumberInput)
        self.btnRememberMe = driver.find_element(By.CSS_SELECTOR, Locator.btnRememberMe)
        self.btnPopupPay = driver.find_element(By.CLASS_NAME, Locator.btnPopupPay)

class AdditionalFields(object):

    def __init__(self, driver):
        self.driver = driver

        self.zipCodeInput = driver.find_element(By.CSS_SELECTOR, Locator.zipCodeInput)
        self.phoneInput = driver.find_element(By.CSS_SELECTOR, Locator.phoneInput)

class AdditionalClose(object):

    def __init__(self, driver):
        self.driver = driver

        self.btnBack = driver.find_element(By.CLASS_NAME, Locator.btnBack)