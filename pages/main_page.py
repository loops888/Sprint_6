import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Получаем текст ответа на вопрос.')
    def get_text_from_answer(self, num):
        locator_q_formatted = self.format_locator(MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locator(MainPageLocators.ANSWER_LOCATOR, num)
        self.scroll_to_element(locator_q_formatted)
        self.click_on_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)
