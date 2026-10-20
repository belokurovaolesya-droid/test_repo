"""Page Object страницы оформления заказа."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage:
    """Страница оформления и итогов заказа."""

    def __init__(self, driver: WebDriver) -> None:
        """Создаёт объект страницы оформления заказа.

        Args:
            driver (WebDriver): веб-драйвер браузера.

        Returns:
            None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_first_name(self, first_name: str) -> None:
        """Вводит имя покупателя.

        Args:
            first_name (str): имя покупателя.

        Returns:
            None
        """
        field = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "first-name")
            )
        )
        field.send_keys(first_name)

    def enter_last_name(self, last_name: str) -> None:
        """Вводит фамилию покупателя.

        Args:
            last_name (str): фамилия покупателя.

        Returns:
            None
        """
        field = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "last-name")
            )
        )
        field.send_keys(last_name)

    def enter_postal_code(self, postal_code: str) -> None:
        """Вводит почтовый индекс.

        Args:
            postal_code (str): почтовый индекс.

        Returns:
            None
        """
        field = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "postal-code")
            )
        )
        field.send_keys(postal_code)

    def click_continue(self) -> None:
        """Нажимает кнопку продолжения оформления.

        Returns:
            None
        """
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "continue")
            )
        )
        button.click()

    def get_total(self) -> str:
        """Возвращает итоговую сумму заказа.

        Returns:
            str: текст итоговой суммы, например «Total: $58.29».
        """
        total = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        return total.text
