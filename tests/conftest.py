

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: type1 or type2"
    )

@pytest.fixture(scope="function")
def initialize_browser(request):
    browser_name = request.config.getoption("--browser_name")
    service_obj = Service()
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(4)
    elif browser_name == "edge":
        driver = webdriver.Edge()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(4)
    driver.maximize_window()
    yield driver
    driver.quit()

