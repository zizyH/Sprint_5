from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.locators import CreateAdModalLocators


class CreateAdModal(BasePage):
    def is_auth_warning_displayed(self):
        return self.is_visible(CreateAdModalLocators.TXT_MODAL_TITLE)

    def fill_ad_form(self, title, description, price):
        self.type(CreateAdModalLocators.INPUT_TITLE, title)
        self.type(CreateAdModalLocators.INPUT_DESCRIPTION, description)
        self.type(CreateAdModalLocators.INPUT_PRICE, price)

    def select_category(self, category):
        self.click(CreateAdModalLocators.DROPDOWN_CATEGORY_ARROW)
        locator = (By.XPATH, f"//button[.//span[text()='{category}']]")
        self.click(locator)

    def select_city(self, city):
        self.click(CreateAdModalLocators.DROPDOWN_CITY_ARROW)
        locator = (By.XPATH, f"//button[.//span[text()='{city}']]")
        self.click(locator)

    def select_condition_new(self):
        self.js_click(CreateAdModalLocators.RADIO_NEW)

    def click_publish(self):
        self.click(CreateAdModalLocators.BTN_PUBLISH)