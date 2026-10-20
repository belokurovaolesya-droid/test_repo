"""Page Object страницы авторизации магазина."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    """Страница входа на saucedemo.com."""

    URL = "https://www.saucedemo.com/"

    def __init__(self, driver: WebDriver) -> None:
        """Создаёт объект страницы авторизации.

        Args:
            driver (WebDriver): веб-драйвер браузера.

        Returns:
            None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> None:
        """Открывает страницу авторизации.

        Returns:
            None
        """
        self.driver.get(self.URL)

    def enter_username(self, username: str) -> None:
        """Вводит имя пользователя.

        Args:
            username (str): логин пользователя.

        Returns:
            None
        """
        field = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "user-name")
            )
        )
        field.send_keys(username)

    def enter_password(self, password: str) -> None:
        """Вводит пароль.

        Args:
            password (str): пароль пользователя.

        Returns:
            None
        """
        field = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "password")
            )
        )
        field.send_keys(password)

    def click_login(self) -> None:
        """Нажимает кнопку входа.

        Returns:
            None
        """
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "login-button")
            )
        )
        button.click()

    def login(self, username: str, password: str) -> None:
        """Выполняет вход в магазин.

        Args:
            username (str): логин пользователя.
            password (str): пароль пользователя.

        Returns:
            None
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
