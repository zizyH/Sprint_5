from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы."""
    BTN_LOGIN_REGISTRATION = (By.XPATH, "//button[text()='Вход и регистрация']")
    BTN_POST_AD = (By.XPATH, "//button[text()='Разместить объявление']")
    BTN_LOGOUT = (By.XPATH, "//button[text()='Выйти']")
    TXT_USER_NAME = (By.XPATH, "//h3[contains(@class, 'name')]")


class AuthModalLocators:
    """Локаторы модального окна входа и регистрации."""
    BTN_NO_ACCOUNT = (By.XPATH, "//button[text()='Нет аккаунта']")
    BTN_LOGIN = (By.XPATH, "//button[text()='Войти']")
    BTN_CREATE_ACCOUNT = (By.XPATH, "//button[text()='Создать аккаунт']")

    INPUT_EMAIL = (By.XPATH, "//input[@name='email']")
    INPUT_PASSWORD = (By.XPATH, "//input[@name='password']")
    INPUT_SUBMIT_PASSWORD = (By.XPATH, "//input[@name='submitPassword']")

    TXT_ERROR = (By.XPATH, "//*[text()='Ошибка']")


class CreateAdModalLocators:
    """Локаторы формы создания объявления."""
    TXT_MODAL_TITLE = (By.XPATH, "//*[text()='Чтобы разместить объявление, авторизуйтесь']")

    INPUT_TITLE = (By.XPATH, "//input[@name='name']")
    INPUT_DESCRIPTION = (By.XPATH, "//textarea[@name='description']")
    INPUT_PRICE = (By.XPATH, "//input[@name='price']")

    DROPDOWN_CATEGORY_ARROW = (By.XPATH, "//input[@name='category']/following-sibling::button")
    DROPDOWN_CITY_ARROW = (By.XPATH, "//input[@name='city']/following-sibling::button")

    RADIO_NEW = (By.XPATH, "//input[@type='radio' and @value='Новый']")

    BTN_PUBLISH = (By.XPATH, "//button[text()='Опубликовать']")

    @staticmethod
    def option_category(category):
        """Локатор опции категории по её названию."""
        return By.XPATH, f"//button[.//span[text()='{category}']]"

    @staticmethod
    def option_city(city):
        """Локатор опции города по его названию."""
        return By.XPATH, f"//button[.//span[text()='{city}']]"


class ProfilePageLocators:
    """Локаторы страницы профиля."""
    SECTION_MY_ADS = (By.XPATH, "//*[text()='Мои объявления']")

    @staticmethod
    def ad_card_by_title(title):
        """Локатор карточки объявления по её заголовку."""
        return By.XPATH, f"//*[text()='{title}']"