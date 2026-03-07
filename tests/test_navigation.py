import allure
import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators.header import Header
from constants import BASE_URL, DZEN_URL

@allure.epic("Навигация")
@pytest.mark.navigation
class TestNavigation:

    @allure.title("Проверка перехода по логотипу Самоката")
    def test_scooter_logo_navigation(self, driver, wait, open_main_page):
        scooter_logo = wait.until(EC.element_to_be_clickable(Header.SCOOTER_LOGO))
        scooter_logo.click()
        wait.until(EC.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL

    @allure.title("Проверка перехода по логотипу Яндекса (открытие Дзена)")
    def test_yandex_logo_navigation(self, driver, wait, open_main_page):
        original_window = driver.current_window_handle
        yandex_logo = wait.until(EC.element_to_be_clickable(Header.YANDEX_LOGO))
        yandex_logo.click()
        wait.until(lambda d: len(d.window_handles) > 1)
        for handle in driver.window_handles:
            if handle != original_window:
                driver.switch_to.window(handle)
                break
        wait.until(EC.url_contains("dzen.ru"))
        assert "dzen.ru" in driver.current_url
        driver.close()
        driver.switch_to.window(original_window)
        