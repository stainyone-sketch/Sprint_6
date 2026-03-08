from .base_page import BasePage
from locators.faq import FAQ


class FaqPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = FAQ

    def click_question(self, question_text):
        locator = self.locators.question_button(question_text)
        self.wait_clickable(locator).click()

    def get_answer_text(self, question_text):
        locator = self.locators.answer_panel(question_text)
        return self.wait_visible(locator).text

    def is_answer_visible(self, question_text):
        locator = self.locators.answer_panel(question_text)
        return self.is_element_visible(locator, timeout=2)
    