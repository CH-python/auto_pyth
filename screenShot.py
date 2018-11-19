import os

class SS(object):

    def __init__(self, driver):
        self.driver = driver

    def GetFolder(self, path):
        directory = 'C:/Users/Катя/Test_US1_payment/ScreenShots'
        folder = directory + path
        if not os.path.exists(folder):
            os.makedirs(folder)
        return folder

    def ScreenShot(self, path, name):
        folder = self.GetFolder(path)
        self.driver.save_screenshot(folder + name)





