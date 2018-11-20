import os

class SS(object):

    def __init__(self, driver):
        self.driver = driver

    def ScreenShot(self, name):
        directory = 'C:/Users/Катя/Test_US1_payment/ScreenShots'
        folder = directory
        if not os.path.exists(folder):
            os.makedirs(folder)
        self.driver.save_screenshot(folder + name)





