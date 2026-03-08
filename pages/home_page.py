from .base_page import BasePage
from locators.header import Header
from locators.home import MainPage
from locators.cookie_banner import CookieBanner


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.header = Header
        self.main = MainPage
        self.cookie = CookieBanner

    def open(self, url):
        self.driver.get(url)

    def close_cookie_banner(self):
        try:
            banner = self.wait_clickable(self.cookie.ACCEPT_BUTTON, timeout=5)
            banner.click()
        except:
            pass

    def click_order_top(self):
        self.wait_clickable(self.header.ORDER_BUTTON_HEADER).click()

    def click_order_bottom(self):
        self.wait_clickable(self.main.ORDER_BUTTON_BOTTOM).click()

    def click_yandex_logo(self):
        self.wait_clickable(self.header.YANDEX_LOGO).click()

    def click_scooter_logo(self):
        self.wait_clickable(self.header.SCOOTER_LOGO).click()
