from selenium.webdriver.common.by import By

class FAQ:
    @staticmethod
    def question_button(question_text: str):
        return (By.XPATH, f"//div[@role='button' and text()='{question_text}']")

    @staticmethod
    def answer_panel(question_text: str):
        return (By.XPATH,
                f"//div[@role='button' and text()='{question_text}']/"
                f"ancestor::div[@data-accordion-component='AccordionItem']//"
                f"div[@role='region']")
    