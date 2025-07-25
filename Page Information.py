from datetime import datetime
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.drivers.edge import EdgeChromiumDriver
from webdriver_manager.drivers.firefox import GeckoDriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

#Variables
SUPPORTED_BROWSERS = {"chrome","firefox", "safari", "edge"}
DEFAULT_BROWSER = "chrome"
URL = "https://www.daraz.com.bd/#?"
PROJECT_ROOT = os.path.join(os.path.dirname(__file__),"..","..")
SCREENSHOT_DIR = os.path.join(PROJECT_ROOT, "Selenium Advance", "Screenshot Commands", "screenshots")

@pytest.fixture(scope="class")
def setup(request, browser=DEFAULT_BROWSER):
    if browser not in SUPPORTED_BROWSERS:
        raise ValueError(f"Browser {browser} is not supported.")
    else:
        driver = get_webdriver(browser)
        driver.maximize_window()
        driver.get(URL)

        request.cls.driver = driver
        yield
        driver.quit()

def get_webdriver(browser):
    if browser == 'chrome':
        return webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))
    elif browser == 'firefox':
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == 'edge':
        return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

@pytest.mark.usefixtures("setup")
class TestPageInfo:
    def test_page_info(self):
        try:
            print(f"Title: {self.driver.title}")
            print(f"Current_URL: {self.driver.current_url}")
            cookies = self.driver.get_cookies()
            print(f"Retrived Cookies {len(cookies)} are: {cookies}")
            # print(f"Page_Source: {self.driver.page_source}")
            time.sleep(2)

            time.sleep(5)
        except Exception as e:
            pytest.fail(f"Test failed due to exception: {e}")
