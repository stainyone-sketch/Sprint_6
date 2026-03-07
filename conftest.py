import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from constants import BASE_URL
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    firefox_options = Options()
    firefox_options.add_argument("--width=1920")
    firefox_options.add_argument("--height=1080")
    
    service = Service()
    
    driver = webdriver.Firefox(service=service, options=firefox_options)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)

@pytest.fixture
def open_main_page(driver, wait):
    driver.get(BASE_URL)
    try:
        from locators.cookie_banner import CookieBanner
        banner = wait.until(EC.element_to_be_clickable(CookieBanner.ACCEPT_BUTTON))
        banner.click()
    except:
        pass
    return driver
