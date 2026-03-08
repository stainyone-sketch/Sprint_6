import allure
import pytest
from pages.order_page import OrderPage
from data import OrderData

@pytest.mark.order
@allure.epic("Заказ самоката")
class TestOrder:

    @allure.title("Позитивный сценарий заказа самоката (старт с верхней кнопки)")
    def test_positive_order_flow_from_top(self, driver, home_page):
        order_data = OrderData.ORDER_SETS[0]
        home_page.click_order_top()
        order = OrderPage(driver)
        order.fill_first_step(order_data)
        order.fill_second_step(order_data)
        order.click_order_button()
        order.is_confirmation_modal_visible()
        order.click_confirm()
        assert order.is_success_modal_visible(), "Сообщение об успехе не появилось"

    @allure.title("Позитивный сценарий заказа самоката (старт с нижней кнопки)")
    def test_positive_order_flow_from_bottom(self, driver, home_page):
        order_data = OrderData.ORDER_SETS[1]
        home_page.click_order_bottom()
        order = OrderPage(driver)
        order.fill_first_step(order_data)
        order.fill_second_step(order_data)
        order.click_order_button()
        order.is_confirmation_modal_visible()
        order.click_confirm()
        assert order.is_success_modal_visible(), "Сообщение об успехе не появилось"
