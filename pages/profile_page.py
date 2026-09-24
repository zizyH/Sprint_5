from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.locators import ProfilePageLocators


class ProfilePage(BasePage):
    def is_my_ads_section_visible(self):
        return self.is_visible(ProfilePageLocators.SECTION_MY_ADS)

    def is_ad_with_title_visible(self, title):
        locator = (By.XPATH, ProfilePageLocators.AD_CARD_BY_TITLE.format(title=title))
        return self.is_visible(locator)