from config import BASE_URL
from data.ads import AD_TITLE, AD_DESCRIPTION, AD_PRICE, AD_CATEGORY, AD_CITY
from pages.main_page import MainPage
from pages.create_ad_modal import CreateAdModal
from pages.profile_page import ProfilePage


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
            description=AD_DESCRIPTION,
            price=AD_PRICE,
        )
        create_ad_modal.select_category(AD_CATEGORY)
        create_ad_modal.select_city(AD_CITY)
        create_ad_modal.select_condition_new()
        create_ad_modal.click_publish()

        driver.get(BASE_URL + "profile")

        assert profile_page.is_ad_with_title_visible(AD_TITLE)