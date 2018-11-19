from selenium import webdriver

class SS(object):

    def __init__(self, driver):
        self.driver = driver

    def ScreenShot(self, path):
        directory = 'E:\Django\Selenium\\venv\TestforUS1'
        self.driver.save_screenshot(directory + path)




