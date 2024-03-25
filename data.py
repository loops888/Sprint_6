from faker import Faker
from phone_gen import PhoneNumber
import datetime

class Data:
    faker_ru = Faker('ru_RU')
    # name = переменная для генерации имени.
    name = faker_ru.first_name()
    # surname = переменная для генерации фамилии.
    surname = faker_ru.last_name()
    # address = переменная для генерации адреса.
    address = faker_ru.street_name()
    # number = переменная для генерации номера телефона.
    phone = PhoneNumber('RU')
    number = phone.get_number()
    # date = переменная для генерации текущей даты.
    date = datetime.date.today().day
