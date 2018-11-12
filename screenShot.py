from selenium import webdriver

class SS(object):

    def __init__(self, driver):
        self.driver = driver

    def ScreenShot(self, path):
        directory = 'C:/Users/Катя/Test_US1_payment/ScreenShots'
        self.driver.save_screenshot(directory + path)




