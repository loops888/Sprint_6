from selenium.webdriver.common.by import By


class OrderPageLocators:

    ORDER_BUTTON_UP = (By.XPATH, ".//button[(@class = 'Button_Button__ra12g' and @type='button') or (text()='Заказать')]")
    ORDER_BUTTON_DOWN = (By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    NAME_FIELD = (By.XPATH, ".//input[contains(@placeholder,'* Имя')]")
    SURNAME_FIELD = (By.XPATH, ".//input[contains(@placeholder,'* Фамилия')]")
    ADDRESS_FIELD = (By.XPATH, ".//input[contains(@placeholder,'* Адрес: куда привезти заказ')]")
    METRO_STATION_FIELD = [By.XPATH, ".//input[@placeholder = '* Станция метро']"]
    METRO_STATION_CHOSEN = [By.XPATH, ".//button/div[text()='{}']"]
    PHONE_NUMBER_FIELD = (By.XPATH, ".//input[contains(@placeholder,'* Телефон: на него позвонит курьер')]")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(),'Далее')]")
    DELIVERY_TIME_FIELD = (By.XPATH, ".//input[contains(@placeholder,'* Когда привезти самокат')]")
    DELIVERY_TIME_CHOSEN = (By.XPATH, ".//div[text()={}]")
    RENTAL_PERIOD_FIELD = (By.XPATH, ".//div[contains(@class,'Dropdown-placeholder')]")
    RENTAL_PERIOD_CHOSEN = (By.XPATH, ".//div[text()='{}']")
    GREY_COLOR_CHECKBOX = (By.XPATH, ".//input[@class = 'Checkbox_Input__14A2w' and @id='grey']")
    COMMENTARY = (By.XPATH, ".//input[@class = 'Input_Input__1iN_Z Input_Responsible__1jDKN' and @placeholder='Комментарий для курьера']")
    CONFIRM_ORDER_BUTTON = (By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    YES_BUTTON = (By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
    SUCCESSFUL_ORDER_FORM = (By.XPATH, ".//div[@class = 'Order_ModalHeader__3FDaJ' and text()='Заказ оформлен']")
    YANDEX_LOGO = (By.XPATH, ".//a[@class = 'Header_LogoYandex__3TSOI']")
    SCOOTER_LOGO = (By.XPATH, ".//a[@class = 'Header_LogoScooter__3lsAR']")
