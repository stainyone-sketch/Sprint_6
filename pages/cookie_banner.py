from .base_page import BasePage
from locators.cookie_banner import CookieBanner as CookieLocators


class CookieBanner(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CookieLocators

    def close(self):
        try:
            self.wait_clickable(self.locators.ACCEPT_BUTTON, timeout=5).click()
        except:
            pass
