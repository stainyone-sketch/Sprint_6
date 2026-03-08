import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import BASE_URL, DEFAULT_TIMEOUT
from pages.home_page import HomePage
from pages.order_page import OrderPage
from pages.faq_page import FaqPage

@pytest.fixture
def driver():
    firefox_options = Options()
    firefox_options.add_argument("--width=1920")
    firefox_options.add_argument("--height=1080")
    service = Service()  # или с указанием пути
    driver = webdriver.Firefox(service=service, options=firefox_options)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, DEFAULT_TIMEOUT)

@pytest.fixture
def home_page(driver):
    """Фикстура, открывающая главную страницу, закрывающая куки и возвращающая объект HomePage."""
    home = HomePage(driver)
    home.open(BASE_URL)
    home.close_cookie_banner()
    return home

@pytest.fixture
def order_page(driver):
    return OrderPage(driver)

@pytest.fixture
def faq_page(driver, home_page):
    """Фикстура, открывающая главную страницу, закрывающая куки и возвращающая объект FaqPage."""
    home_page.open(BASE_URL)
    home_page.close_cookie_banner()
    return FaqPage(driver)
