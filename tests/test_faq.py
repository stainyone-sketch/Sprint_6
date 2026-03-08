import allure
import pytest
from data import FAQ_ITEMS, FAQ_IDS

@pytest.mark.faq
@allure.epic("FAQ")
class TestFaq:
    @allure.title("Проверка вопроса: {question}")
    @pytest.mark.parametrize("question, expected_answer", FAQ_ITEMS, ids=FAQ_IDS)
    def test_faq_question(self, faq_page, question, expected_answer):
        faq_page.click_question(question)
        assert faq_page.get_answer_text(question) == expected_answer
