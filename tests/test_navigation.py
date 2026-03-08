import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import BASE_URL

@pytest.mark.navigation
@allure.epic("Навигация")
class TestNavigation:

    @allure.title("Проверка перехода по логотипу Самоката")
    def test_scooter_logo_navigation(self, driver, home_page):
        home_page.click_scooter_logo()
        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL

    @allure.title("Проверка перехода по логотипу Яндекса (открытие Дзена)")
    def test_yandex_logo_navigation(self, driver, wait, home_page):
        original_window = driver.current_window_handle
        home_page.click_yandex_logo()
        wait.until(EC.number_of_windows_to_be(2))
        new_window = [handle for handle in driver.window_handles if handle != original_window][0]
        driver.switch_to.window(new_window)
        wait.until(EC.url_contains("dzen.ru"))
        assert "dzen.ru" in driver.current_url
