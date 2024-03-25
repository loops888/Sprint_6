import allure

from constants import Constants
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Заполняем поля с персональной информацией по заказу.')
    def fill_personal_info_for_order(self, name, surname, address, metro_station, phone):
        self.agree_to_cookies()
        self.click_on_element(OrderPageLocators.ORDER_BUTTON_UP)
        self.insert_text_in_field(OrderPageLocators.NAME_FIELD, name)
        self.insert_text_in_field(OrderPageLocators.SURNAME_FIELD, surname)
        self.insert_text_in_field(OrderPageLocators.ADDRESS_FIELD, address)
        self.choose_metro_station(metro_station)
        self.insert_text_in_field(OrderPageLocators.PHONE_NUMBER_FIELD, phone)
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполняем поля с дополнительной информацией по заказу.')
    def fill_additional_order_info(self, delivery_date, rental_period):
        self.choose_delivery_date(delivery_date)
        self.choose_rental_period(rental_period)
        self.click_on_element(OrderPageLocators.GREY_COLOR_CHECKBOX)
        self.insert_text_in_field(OrderPageLocators.COMMENTARY, Constants.COMMENTARY)

    @allure.step('Проверяем успешность создания заказа.')
    def check_successful_order(self):
        self.click_on_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)
        self.click_on_element(OrderPageLocators.YES_BUTTON)
        order_result = self.get_text_from_element(OrderPageLocators.SUCCESSFUL_ORDER_FORM)
        return order_result

    @allure.step('Выбираем станцию метро.')
    def choose_metro_station(self, metro):
        method, locator = OrderPageLocators.METRO_STATION_CHOSEN
        metro_locator = locator.format(metro)
        self.click_on_element(OrderPageLocators.METRO_STATION_FIELD)
        self.scroll_to_element((method, metro_locator))
        self.click_on_element((method, metro_locator))

    @allure.step('Выбираем дату доставки.')
    def choose_delivery_date(self, delivery_date):
        method, locator = OrderPageLocators.DELIVERY_TIME_CHOSEN
        date = locator.format(delivery_date)
        self.click_on_element(OrderPageLocators.DELIVERY_TIME_FIELD)
        self.click_on_element((method, date))

    @allure.step('Выбираем срок аренды.')
    def choose_rental_period(self, rental_period):
        method, locator = OrderPageLocators.RENTAL_PERIOD_CHOSEN
        period = locator.format(rental_period)
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        self.scroll_to_element((method, period))
        self.click_on_element((method, period))

    @allure.step('Нажимаем на логотип Яндекса.')
    def click_on_yandex_logo(self):
        self.scroll_to_element(OrderPageLocators.ORDER_BUTTON_DOWN)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON_DOWN)
        self.click_on_element(OrderPageLocators.YANDEX_LOGO)
        url = self.check_url_after_redirect(Constants.DZEN_URL)
        return url

    @allure.step('Нажимаем на логотип Самоката.')
    def click_on_scooter_logo(self):
        self.scroll_to_element(OrderPageLocators.ORDER_BUTTON_DOWN)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON_DOWN)
        self.click_on_element(OrderPageLocators.SCOOTER_LOGO)
        url = self.check_url_after_redirect(Constants.URL)
        return url
