from pages.base_page import BasePage
from locators.locators import ProfilePageLocators


class ProfilePage(BasePage):
    def is_my_ads_section_visible(self):
        return self.is_visible(ProfilePageLocators.SECTION_MY_ADS)

    def is_ad_with_title_visible(self, title):
        return self.is_visible(ProfilePageLocators.ad_card_by_title(title))