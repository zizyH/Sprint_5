import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config import BASE_URL
from helpers.generators import generate_unique_user
from pages.main_page import MainPage
from pages.auth_modal import AuthModal


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def registered_user(driver):
    """Предусловие: регистрирует нового пользователя и возвращает его данные."""
    user = generate_unique_user()

    driver.get(BASE_URL)
    main_page = MainPage(driver)
    auth_modal = AuthModal(driver)

    main_page.click_login_registration()
    auth_modal.click_no_account()
    auth_modal.fill_registration_form(user["email"], user["password"])
    auth_modal.click_create_account()

    # Ждём, пока в шапке появится имя пользователя — значит регистрация прошла
    assert main_page.is_user_logged_in(), "Регистрация в фикстуре не удалась"

    return user