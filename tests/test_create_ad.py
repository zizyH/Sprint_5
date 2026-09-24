from config import BASE_URL
from pages.main_page import MainPage
from pages.create_ad_modal import CreateAdModal
from pages.profile_page import ProfilePage


AD_TITLE = "Тестовое объявление"


class TestCreateAd:
    def test_create_ad_unauthorized(self, driver):
        driver.get(BASE_URL)
        main_page = MainPage(driver)
        create_ad_modal = CreateAdModal(driver)

        main_page.click_post_ad()

        assert create_ad_modal.is_auth_warning_displayed()

    def test_create_ad_authorized(self, driver, registered_user):
        driver.get(BASE_URL)
        main_page = MainPage(driver)
        create_ad_modal = CreateAdModal(driver)
        profile_page = ProfilePage(driver)

        main_page.click_post_ad()
        create_ad_modal.fill_ad_form(
            title=AD_TITLE,
            description="Описание тестового объявления",
            price="1000"
        )
        create_ad_modal.select_category("Технологии")
        create_ad_modal.select_city("Москва")
        create_ad_modal.select_condition_new()
        create_ad_modal.click_publish()

        driver.get(BASE_URL + "profile")

        assert profile_page.is_ad_with_title_visible(AD_TITLE)