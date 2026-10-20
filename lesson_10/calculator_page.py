"""Page Object страницы медленного калькулятора."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    """Страница медленного калькулятора."""

    URL = (
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "slow-calculator.html"
    )

    def __init__(self, driver: WebDriver) -> None:
        """Создаёт объект страницы калькулятора.

        Args:
            driver (WebDriver): веб-драйвер браузера.

        Returns:
            None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self) -> None:
        """Открывает страницу калькулятора.

        Returns:
            None
        """
        self.driver.get(self.URL)

    def set_delay(self, delay: int) -> None:
        """Устанавливает задержку вычисления.

        Args:
            delay (int): задержка в секундах.

        Returns:
            None
        """
        field = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#delay")
            )
        )
        field.clear()
        field.send_keys(str(delay))

    def click_button(self, value: str) -> None:
        """Нажимает кнопку калькулятора.

        Args:
            value (str): подпись кнопки, например «7» или «+».

        Returns:
            None
        """
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//span[text()='{value}']")
            )
        )
        button.click()

    def get_result(self, expected_result: str) -> str:
        """Ждёт появления результата и возвращает текст экрана.

        Args:
            expected_result (str): ожидаемый текст результата.

        Returns:
            str: текст на экране калькулятора.
        """
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"),
                expected_result
            )
        )

        return self.driver.find_element(
            By.CSS_SELECTOR, ".screen"
        ).text
