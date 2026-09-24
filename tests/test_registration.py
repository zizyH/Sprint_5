from config import BASE_URL
from pages.main_page import MainPage
from pages.auth_modal import AuthModal


class TestRegistration:
    def test_successful_registration(self, driver, unique_user):
        driver.get(BASE_URL)
        main_page = MainPage(driver)
        auth_modal = AuthModal(driver)

        main_page.click_login_registration()
        auth_modal.click_no_account()
        auth_modal.fill_registration_form(unique_user["email"], unique_user["password"])
        auth_modal.click_create_account()

        assert "User" in main_page.get_user_name()

    def test_registration_with_invalid_email(self, driver, unique_user):
        driver.get(BASE_URL)
        main_page = MainPage(driver)
        auth_modal = AuthModal(driver)

        main_page.click_login_registration()
        auth_modal.click_no_account()
        auth_modal.fill_registration_form("invalid-email", unique_user["password"])
        auth_modal.click_create_account()

        assert auth_modal.is_error_displayed()

    def test_registration_with_existing_email(self, driver, existing_user):
        driver.get(BASE_URL)
        main_page = MainPage(driver)
        auth_modal = AuthModal(driver)

        main_page.click_login_registration()
        auth_modal.click_no_account()
        auth_modal.fill_registration_form(existing_user["email"], existing_user["password"])
        auth_modal.click_create_account()

        assert auth_modal.is_error_displayed()