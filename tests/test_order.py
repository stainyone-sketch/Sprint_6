import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.header import Header
from locators.main import MainPage
from locators.order import OrderPage
from data import OrderData
from constants import BASE_URL


@allure.epic("Заказ самоката")
@pytest.mark.order
class TestOrder:

    @allure.title("Позитивный сценарий заказа самоката (старт с {start_point})")
    @pytest.mark.parametrize(
        "order_data, start_from_bottom, start_point",
        [
            (OrderData.ORDER_SETS[0], False, "верхней кнопки"),
            (OrderData.ORDER_SETS[1], True, "нижней кнопки"),
        ],
        ids=["top", "bottom"]
    )
    def test_positive_order_flow(self, driver, wait, open_main_page, order_data, start_from_bottom, start_point):
        # 1. Нажатие кнопки заказа
        if start_from_bottom:
            order_button = wait.until(EC.element_to_be_clickable(MainPage.ORDER_BUTTON_BOTTOM))
        else:
            order_button = wait.until(EC.element_to_be_clickable(Header.ORDER_BUTTON_HEADER))
        order_button.click()

        # 2. Заполнение первого блока данных
        wait.until(EC.visibility_of_element_located(OrderPage.FIRST_NAME)).send_keys(order_data["name"])
        driver.find_element(*OrderPage.LAST_NAME).send_keys(order_data["surname"])
        driver.find_element(*OrderPage.ADDRESS).send_keys(order_data["address"])

        # Метро
        metro_input = driver.find_element(*OrderPage.METRO_INPUT)
        metro_input.click()
        metro_option = wait.until(EC.element_to_be_clickable(OrderPage.metro_option(order_data["metro"])))
        metro_option.click()

        driver.find_element(*OrderPage.PHONE).send_keys(order_data["phone"])
        driver.find_element(*OrderPage.NEXT_BUTTON).click()

        # 3. Заполнение второго блока данных
        # Дата
        wait.until(EC.visibility_of_element_located(OrderPage.DATE_INPUT))
        date_input = driver.find_element(*OrderPage.DATE_INPUT)
        date_input.clear()
        date_input.send_keys(order_data["date"])
        date_input.send_keys(Keys.ENTER)

        # Клик на body, чтобы закрыть календарь
        body = driver.find_element(By.TAG_NAME, "body")
        body.click()

        # Срок аренды
        rental_dropdown = wait.until(EC.element_to_be_clickable(OrderPage.RENTAL_DROPDOWN))
        rental_dropdown.click()
        rental_option = wait.until(EC.element_to_be_clickable(OrderPage.rental_option(order_data["rental_period"])))
        rental_option.click()

        # Цвет самоката
        if order_data["color"] == "black":
            driver.find_element(*OrderPage.COLOR_BLACK).click()
        else:
            driver.find_element(*OrderPage.COLOR_GREY).click()

        # Комментарий
        comment_field = driver.find_element(*OrderPage.COMMENT)
        comment_field.clear()
        comment_field.send_keys(order_data["comment"])

        # Клик по кнопке "Заказать"
        order_btn = wait.until(EC.element_to_be_clickable(OrderPage.ORDER_BUTTON))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order_btn)
        try:
            order_btn.click()
        except Exception:
            driver.execute_script("arguments[0].click();", order_btn)

        # Ожидание модального окна с вопросом и клик "Да"
        long_wait = WebDriverWait(driver, 15)
        confirm_modal = long_wait.until(EC.visibility_of_element_located(OrderPage.CONFIRM_MODAL))
        confirm_button = long_wait.until(EC.element_to_be_clickable(OrderPage.CONFIRM_BUTTON))
        confirm_button.click()

        # Проверка финального окна успеха
        success_modal = long_wait.until(EC.visibility_of_element_located(OrderPage.SUCCESS_MODAL))
        success_text = success_modal.find_element(*OrderPage.SUCCESS_MESSAGE)
        assert success_text.is_displayed(), "Сообщение об успешном заказе не появилось"
        