from selenium.webdriver.common.by import By

class OrderPage:
    # Первый блок данных
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    @staticmethod
    def metro_option(metro_name):
        return (By.XPATH, f"//div[text()='{metro_name}']")

    # Второй блок данных
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_DROPDOWN = (By.XPATH, "//div[contains(text(), 'Срок аренды')]/ancestor::div[contains(@class, 'Dropdown-root')]//div[contains(@class, 'Dropdown-control')]")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button') and contains(@class, 'Button_Middle') and text()='Заказать']")

    @staticmethod
    def rental_option(period):
        return (By.XPATH, f"//div[@class='Dropdown-option' and text()='{period}']")

    COLOR_BLACK = (By.XPATH, "//label[contains(text(),'чёрный жемчуг')]")
    COLOR_GREY = (By.XPATH, "//label[contains(text(),'серая безысходность')]")

    # Окно подтверждения
    CONFIRM_MODAL = (By.XPATH, "//div[contains(text(), 'Хотите оформить заказ?')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")

    # Финальное сообщение об успехе
    SUCCESS_MODAL = (By.XPATH, "//div[contains(@class, 'Order_Modal')]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_Modal')]//div[contains(text(), 'Заказ оформлен')]")
    