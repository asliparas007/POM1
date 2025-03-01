from selenium.webdriver.common.by import By

from pageObjects.checkout_and_confirmation import checkOutandConfirmation


class ShopPage:
    def __init__(self,driver):
        self.driver = driver
        self.get_shop_button = (By.CSS_SELECTOR," a[href*='shop']")
        self.get_products = (By.XPATH, "//div[@class='card h-100']")
        self.getcartbutton = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def add_product(self, product_name):
        self.driver.find_element(*self.get_shop_button).click()
        products = self.driver.find_elements(*self.get_products)

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == product_name:
                product.find_element(By.XPATH, "div/button").click()

    def go_to_cart(self):
        self.driver.find_element(*self.getcartbutton).click()
        checkout_confirmation = checkOutandConfirmation(self.driver)
        return checkout_confirmation
