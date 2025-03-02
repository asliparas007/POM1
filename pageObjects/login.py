from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.ShopPage import ShopPage
from utlis.browserutils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

        self.get_username = (By.XPATH, '//input[@name="username"]')
        self.get_password = (By.XPATH, '//input[@name="password"]')
        self.get_submit = (By.XPATH, '//input[@type="submit"]')


    def login(self,username,password):
        self.driver.find_element(*self.get_username).send_keys(username)
        self.driver.find_element(*self.get_password).send_keys(password)
        self.driver.find_element(*self.get_submit).click()
        shop_page = ShopPage(self.driver)
        return shop_page
