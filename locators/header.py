from selenium.webdriver.common.by import By

class Header:
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    ORDER_BUTTON_HEADER = (By.XPATH, "//button[text()='Заказать']")
    STATUS_BUTTON = (By.XPATH, "//button[text()='Статус заказа']")
    ORDER_INPUT = (By.XPATH, "//input[@placeholder='Введите номер заказа']")
    GO_BUTTON = (By.XPATH, "//button[text()='Go!']")
    INPUT_ERROR = (By.XPATH, "//div[contains(@class, 'Input_ErrorMessage')]")
    