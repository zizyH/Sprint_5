import uuid

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config import BASE_URL
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
def unique_email():
    return f"user_{uuid.uuid4().hex[:8]}@test.com"


@pytest.fixture
def unique_user(unique_email):
    return {
        "email": unique_email,
        "password": "Password123"
    }


@pytest.fixture
def existing_user():
    return {
        "email": "existing_user@test.com",
        "password": "Password123"
    }


@pytest.fixture
def registered_user(driver, unique_user):
    driver.get(BASE_URL)
    main_page = MainPage(driver)
    auth_modal = AuthModal(driver)

    main_page.click_login_registration()
    auth_modal.click_no_account()
    auth_modal.fill_registration_form(unique_user["email"], unique_user["password"])
    auth_modal.click_create_account()

    main_page.get_user_name()

    return unique_user