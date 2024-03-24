import allure
import pytest

from constants import Constants
from pages.main_page import MainPage


class TestMainPage:

    @pytest.mark.parametrize(
        'num, result',
        [
            (0, Constants.ANSWER_0),
            (1, Constants.ANSWER_1),
            (2, Constants.ANSWER_2),
            (3, Constants.ANSWER_3),
            (4, Constants.ANSWER_4),
            (5, Constants.ANSWER_5),
            (6, Constants.ANSWER_6),
            (7, Constants.ANSWER_7)
        ]
    )
    @allure.title('Проверка секции "Вопросы о важном".')
    @allure.description(
        'Проверяем, что на каждый вопрос выводится правильный ответ.')
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        assert result == main_page.get_text_from_answer(num)
