from TestforUS1.locators import Locator
from selenium.webdriver.common.by import By

class MainUserPage(object):

    def __init__(self, driver):
        self.driver = driver

        # Main user page locators defining
        self.itemPayments = driver.find_element(By.XPATH, Locator.payments)

class popupItemPayment(object):

    def __init__(self, driver):
        self.driver = driver

        self.titleDetails = driver.find_element(By.XPATH, Locator.titlePopup)
        self.btnDetails = driver.find_element(By.XPATH, Locator.details)
        self.btnPay = driver.find_element(By.ID, Locator.pay)
        self.inputPaymentSum = driver.find_element(By.ID, Locator.paymentSum)
        self.btnDownloadCheck = driver.find_element(By.ID, Locator.downloadCheck)
        self.btnProceed = driver.find_element(By.ID, Locator.proceed)

class popupEasyPay(object):

    def __init__(self, driver):
        self.driver = driver

        self.mailInput = driver.find_element(By.XPATH, Locator.mailInput)
        self.cardNumberInput = driver.find_element(By.XPATH, Locator.cardNumberInput)
        self.dateCardInput = driver.find_element(By.XPATH, Locator.dateCardInput)
        self.cvNumberInput = driver.find_element(By.XPATH, Locator.cvNumberInput)
        self.btnRememberMe = driver.find_element(By.XPATH, Locator.btnRememberMe)
        self.btnPay = driver.find_element(By.CLASS_NAME, Locator.btnPay)

class additionalFields(object):

    def __init__(self, driver):
        self.driver = driver

        self.zipCodeInput = driver.find_element(By.XPATH, Locator.zipCodeInput)
        self.PhoneInput = driver.find_element(By.XPATH, Locator.PhoneInput)

class additionalClose(object):

    def __init__(self, driver):
        self.driver = driver

        self.btnClose = driver.find_element(By.CLASS_NAME, Locator.btnClose)