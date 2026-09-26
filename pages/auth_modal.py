from pages.base_page import BasePage
from locators.locators import AuthModalLocators


class AuthModal(BasePage):
    def click_no_account(self):
        self.click(AuthModalLocators.BTN_NO_ACCOUNT)

    def fill_registration_form(self, email, password):
        self.type(AuthModalLocators.INPUT_EMAIL, email)
        self.type(AuthModalLocators.INPUT_PASSWORD, password)
        self.type(AuthModalLocators.INPUT_SUBMIT_PASSWORD, password)

    def fill_login_form(self, email, password):
        self.type(AuthModalLocators.INPUT_EMAIL, email)
        self.type(AuthModalLocators.INPUT_PASSWORD, password)

    def click_create_account(self):
        self.click(AuthModalLocators.BTN_CREATE_ACCOUNT)

    def click_login(self):
        self.click(AuthModalLocators.BTN_LOGIN)

    def is_error_displayed(self):
        return self.is_visible(AuthModalLocators.TXT_ERROR)