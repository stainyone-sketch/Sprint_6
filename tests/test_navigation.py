import allure
import pytest
<<<<<<< HEAD
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
=======
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
        
>>>>>>> e0c9b3b7d19f3b90a71204a558dce4f3c830449c
