class BrowserUtils:
    def __init__(self,driver):
        driver.self = driver


    def getTitile(self):
        return self.driver.title