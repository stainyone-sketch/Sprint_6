from selenium.webdriver.common.by import By

class CookieBanner:
    BANNER = (By.XPATH, "//div[contains(@class, 'App_CookieConsent')]")
    ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")
    