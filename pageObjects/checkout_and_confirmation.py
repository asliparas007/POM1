from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class checkOutandConfirmation:
    def __init__(self,driver):
        self.driver = driver
        self.get_button = (By.XPATH, "//button[@class='btn btn-success']")
        self.get_country = (By.ID, "country")
        self.get_country_option = (By.LINK_TEXT,"India")
        self.get_checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.get_submit_button = (By.CSS_SELECTOR, "[type='submit']")
        self.get_success_message = (By.CLASS_NAME, "alert-success")

    def checkout(self):
        self.driver.find_element(*self.get_button).click()

    def enter_delivery_address(self,country):
        self.driver.find_element(*self.get_country).send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((self.get_country_option)))
        self.driver.find_element(*self.get_country_option).click()
        self.driver.find_element(*self.get_checkbox).click()
        self.driver.find_element(*self.get_submit_button).click()

    def validate_order(self):
        successText = self.driver.find_element(*self.get_success_message).text
        assert "Success! Thank you!" in successText













