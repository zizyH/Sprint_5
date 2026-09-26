from config import BASE_URL
from data.ads import EXPECTED_USER_NAME_PREFIX
from data.users import EXISTING_USER, INVALID_EMAIL
from helpers.generators import generate_unique_user
from pages.main_page import MainPage
from pages.auth_modal import AuthModal


class TestRegistration:
    def test_successful_registration(self, driver):
        user = generate_unique_user()

        driver.get(BASE_URL)
        main_page = MainPage(driver)
        auth_modal = AuthModal(driver)

        main_page.click_login_registration()
        auth_modal.click_no_account()
        auth_modal.fill_registration_form(user["email"], user["password"])
        auth_modal.click_create_account()

        assert EXPECTED_USER_NAME_PREFIX in main_page.get_user_name()

    def test_registration_with_invalid_email(self, driver):
        user = generate_unique_user()

        driver.get(BASE_URL)
        main_page = MainPage(driver)
        auth_modal = AuthModal(driver)

        main_page.click_login_registration()
        auth_modal.click_no_account()
        auth_modal.fill_registration_form(INVALID_EMAIL, user["password"])
        auth_modal.click_create_account()

        assert auth_modal.is_error_displayed()

    def test_registration_with_existing_email(self, driver, registered_user):
        main_page = MainPage(driver)
        auth_modal = AuthModal(driver)

        main_page.click_logout()

        main_page.click_login_registration()
        auth_modal.click_no_account()
        auth_modal.fill_registration_form(
            registered_user["email"], registered_user["password"]
    )
        auth_modal.click_create_account()

        assert auth_modal.is_error_displayed()