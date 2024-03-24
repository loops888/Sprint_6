import allure
import pytest

from constants import Constants
from pages.order_page import OrderPage


class TestOrderPage:

    @pytest.mark.parametrize(
        'metro_station, rental_period',
        [
            (Constants.METRO_STATION_1, Constants.RENTAL_PERIOD_1),
            (Constants.METRO_STATION_2, Constants.RENTAL_PERIOD_2),
            (Constants.METRO_STATION_3, Constants.RENTAL_PERIOD_3)
        ]
    )
    @allure.title('Проверка формы создания заказа.')
    @allure.description(
        'Переходим на страницу заказа, заполняем необходимые поля и подтверждаем заказ. Проверяем, что появилось сообщение "Заказ оформлен".')
    def test_fill_personal_info_for_order(self, driver, contact_information, metro_station, today_date, rental_period):
        order_page = OrderPage(driver)
        order_page.fill_personal_info_for_order(contact_information, metro_station)
        order_page.fill_additional_order_info(today_date, rental_period)
        assert 'Заказ оформлен' in order_page.check_successful_order()

    @allure.title('Проверка перехода на Дзен.')
    @allure.description(
        'Переходим на страницу заказа и оттуда нажимаем на логотип Яндекса. Проверяем, что в новом окне через редирект открывается главная страница Дзена.')
    def test_redirect_to_dzen(self, driver):
        order_page = OrderPage(driver)
        assert 'https://dzen.ru/?yredirect=true' in order_page.click_on_yandex_logo()

    @allure.title('Проверка перехода на главную страницу Самоката.')
    @allure.description(
        'Переходим на страницу заказа и оттуда нажимаем на логотип Самоката. Проверяем, что возвращаемся на главную страницу Самоката.')
    def test_redirect_to_main_page(self, driver):
        order_page = OrderPage(driver)
        assert 'https://qa-scooter.praktikum-services.ru/' in order_page.click_on_scooter_logo()
