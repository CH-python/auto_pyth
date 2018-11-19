from selenium import webdriver

class WebdriverFactory:
    @staticmethod
    def getWebdriver(browserName):
        if (browserName == 'firefox'):
            return webdriver.Firefox()
        elif (browserName == 'chrome'):
            return webdriver.Chrome()
        elif (browserName == 'opera'):
            return webdriver.Chrome()
        elif (browserName == 'ie'):
            return webdriver.ie()

        raise Exception("No such " + browserName + " browser exists")