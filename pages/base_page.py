import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скроллим к элементу')
    def scroll_to_element(self, locator):
        element = self.find_element_with_waiting(locator)
        self.driver.execute_script("return arguments[0].scrollIntoView();", element)

    @allure.step('Кликаем по элементу')
    def click_on_element(self, locator):
        element = self.find_element_with_waiting(locator)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        element.click()

    @allure.step('Ищем элемент с ожиданием.')
    def find_element_with_waiting(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Получаем текст из элемента.')
    def get_text_from_element(self, locator):
        return self.find_element_with_waiting(locator).text

    @allure.step('Форматируем элемент.')
    def format_locator(self, locator, num):
        method, locator_final = locator
        locator_final = locator_final.format(num)
        return method, locator_final

    @allure.step('Заполняем элемент текстом.')
    def insert_text_in_field(self, locator, value):
        element = WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        element.send_keys(value)

    @allure.step('Принимаем куки.')
    def agree_to_cookies(self):
        cookies = (By.ID, 'rcc-confirm-button')
        element = WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(cookies))
        element.click()

    @allure.step('Проверяем url после редиректа.')
    def check_url_after_redirect(self, link):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 5).until(expected_conditions.url_contains(link))
        return self.driver.current_url
