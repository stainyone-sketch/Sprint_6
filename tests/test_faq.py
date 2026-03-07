import allure
import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators.faq import FAQ
from data import FAQ_ITEMS
from constants import BASE_URL

@allure.epic("FAQ")
@allure.feature("Аккордеон")
@pytest.mark.faq
class TestFaq:

    @pytest.fixture(autouse=True)
    def open_main_page_and_close_cookie(self, driver, wait):
        driver.get(BASE_URL)
        from locators.cookie_banner import CookieBanner
        try:
            banner = wait.until(EC.element_to_be_clickable(CookieBanner.ACCEPT_BUTTON))
            banner.click()
        except:
            pass

    @allure.title("Проверка вопроса: {question}")
    @pytest.mark.parametrize("question, expected_answer", FAQ_ITEMS, ids=[q[0][:20] for q in FAQ_ITEMS])
    def test_faq_question(self, driver, wait, question, expected_answer):
        answer_locator = FAQ.answer_panel(question)
        answer_element = driver.find_element(*answer_locator)
        assert not answer_element.is_displayed(), "Ответ уже виден до клика"

        question_element = wait.until(EC.element_to_be_clickable(FAQ.question_button(question)))
        driver.execute_script("arguments[0].scrollIntoView();", question_element)
        driver.execute_script("arguments[0].click();", question_element)

        wait.until(EC.visibility_of(answer_element))
        assert answer_element.text == expected_answer
        