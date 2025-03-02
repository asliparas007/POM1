import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None  # Global WebDriver instance


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Browser choice: chrome or edge")


@pytest.fixture(scope="function")
def initialize_browser(request):
    global driver
    if driver is None:
        browser_name = request.config.getoption("--browser_name")
        service_obj = Service()
        if browser_name == "chrome":
            driver = webdriver.Chrome(service=service_obj)
        elif browser_name == "edge":
            driver = webdriver.Edge()
        driver.implicitly_wait(4)
        driver.maximize_window()

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    yield driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Capture screenshot on test failure and embed in HTML report.
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when in ("call", "setup"):
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), 'Reports')
            os.makedirs(reports_dir, exist_ok=True)

            safe_test_name = report.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_")
            file_name = os.path.join(reports_dir, safe_test_name + ".png")

            print("Test failed! Capturing screenshot:", file_name)

            if driver is not None:  # Ensure driver is initialized
                _capture_screenshot(file_name)

                # Convert path for pytest-html
                rel_file_name = os.path.relpath(file_name, os.path.dirname(__file__))
                rel_file_name = rel_file_name.replace("\\", "/")  # Ensure correct format

                if os.path.exists(file_name):
                    html = f'<div><img src="{rel_file_name}" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>'
                    extra.append(pytest_html.extras.html(html))

        report.extra = extra


def _capture_screenshot(file_name):
    global driver
    if driver is not None:
        #print(f"Taking screenshot: {file_name}")
        driver.get_screenshot_as_file(file_name)
    else:
        print("Error: WebDriver is not initialized!")
