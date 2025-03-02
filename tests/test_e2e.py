import json
import os

import pytest
from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.ShopPage import ShopPage
from pageObjects.login import LoginPage
test_data_path = os.path.join(os.path.dirname(__file__), "../data/test_e2e.json")
test_data_path = os.path.abspath(test_data_path)  # Convert to absolute path
#test_data_path = '../data/test_e2e.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.parametrize("test_item_list",test_list)
def test_new_e2e(initialize_browser, test_item_list):
    driver = initialize_browser
    #  //a[contains(@href,'shop')]    a[href*='shop']
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login_page = LoginPage(driver)
    login_page.getTitile()
    shop_page = login_page.login(test_item_list["userEmail"],test_item_list["userPassword"])
    shop_page.add_product(test_item_list["productName"])
    checkout_confirmation = shop_page.go_to_cart ()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("India")
    checkout_confirmation.validate_order()






















