from config import BASE_URL
from pages.main_page import MainPage


class TestLogout:
    def test_logout(self, driver, registered_user):
        driver.get(BASE_URL)
        main_page = MainPage(driver)

        main_page.click_logout()

        assert main_page.is_login_button_visible()