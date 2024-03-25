from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTION_LOCATOR = (By.XPATH, "//div[@id='accordion__heading-{}']")
    ANSWER_LOCATOR = (By.XPATH, "//div[@id='accordion__panel-{}']")
    COOKIES = (By.ID, 'rcc-confirm-button')