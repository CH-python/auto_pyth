from TestforUS1.locators import Locator
from selenium.webdriver.common.by import By

class PaymentsPage(object):

    def __init__(self, driver):
        self.driver = driver

        # Sign In page locators defining

        self.btnDetails = driver.find_element(By.XPATH, Locator.details)
        self.balance = driver.find_element(By.XPATH, Locator.balance)

class PopupItemPayment(object):

    def __init__(self, driver):
        self.driver = driver

        self.titleDetails = driver.find_element(By.XPATH, Locator.titlePopup)
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

        self.titlePopupEasyPay = driver.find_element(By.XPATH, Locator.titlePopupEasyPay)
        self.mailInput = driver.find_element(By.XPATH, Locator.mailInput)
        self.cardNumberInput = driver.find_element(By.XPATH, Locator.cardNumberInput)
        self.dateCardInput = driver.find_element(By.XPATH, Locator.dateCardInput)
        self.cvNumberInput = driver.find_element(By.XPATH, Locator.cvNumberInput)
        self.btnRememberMe = driver.find_element(By.XPATH, Locator.btnRememberMe)
        self.btnPay = driver.find_element(By.CLASS_NAME, Locator.btnPay)

class AdditionalFields(object):

    def __init__(self, driver):
        self.driver = driver

        self.zipCodeInput = driver.find_element(By.XPATH, Locator.zipCodeInput)
        self.phoneInput = driver.find_element(By.XPATH, Locator.phoneInput)

class AdditionalClose(object):

    def __init__(self, driver):
        self.driver = driver

        self.btnBack = driver.find_element(By.CLASS_NAME, Locator.btnBack)


