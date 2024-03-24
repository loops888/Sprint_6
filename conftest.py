import pytest
from selenium import webdriver
from faker import Faker
from phone_gen import PhoneNumber
import datetime

from constants import Constants

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Constants.URL)
    yield driver
    driver.quit()


@pytest.fixture
def contact_information():
    faker_ru = Faker('ru_RU')
    name = faker_ru.first_name()
    surname = faker_ru.last_name()
    address = faker_ru.street_name()
    phone = PhoneNumber('RU')
    number = phone.get_number()
    return name, surname, address, number

@pytest.fixture
def today_date():
    date = datetime.date.today().day
    return date




