from config import BASE_URL
from pages.main_page import MainPage
from pages.auth_modal import AuthModal


class TestLogin:
    def test_successful_login(self, driver, unique_user):
        driver.get(BASE_URL)
        main_page = MainPage(driver)
        auth_modal = AuthModal(driver)

        main_page.click_login_registration()
        auth_modal.click_no_account()
        auth_modal.fill_registration_form(unique_user["email"], unique_user["password"])
        auth_modal.click_create_account()

        main_page.click_logout()

        main_page.click_login_registration()
        auth_modal.fill_login_form(unique_user["email"], unique_user["password"])
        auth_modal.click_login()

        assert "User" in main_page.get_user_name()