from pages.base_page import BasePage
from locators.locators import MainPageLocators


class MainPage(BasePage):
    def click_login_registration(self):
        self.click(MainPageLocators.BTN_LOGIN_REGISTRATION)

    def click_post_ad(self):
        self.click(MainPageLocators.BTN_POST_AD)

    def click_logout(self):
        self.click(MainPageLocators.BTN_LOGOUT)

    def get_user_name(self):
        return self.get_text(MainPageLocators.TXT_USER_NAME)

    def is_user_logged_in(self):
        return self.is_visible(MainPageLocators.TXT_USER_NAME)

    def is_login_button_visible(self):
        return self.is_visible(MainPageLocators.BTN_LOGIN_REGISTRATION)