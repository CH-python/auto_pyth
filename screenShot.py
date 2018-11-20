import os

class SS(object):

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, name):
        directory = 'E:/Django/Selenium/venv/TestforUS1/ScreenShots'
        folder = directory
        if not os.path.exists(folder):
            os.makedirs(folder)
        self.driver.save_screenshot(folder + name)