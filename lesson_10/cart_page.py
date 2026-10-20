"""Page Object страницы корзины."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    """Страница корзины магазина."""

    def __init__(self, driver: WebDriver) -> None:
        """Создаёт объект страницы корзины.

        Args:
            driver (WebDriver): веб-драйвер браузера.

        Returns:
            None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def checkout(self) -> None:
        """Переходит к оформлению заказа.

        Returns:
            None
        """
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "checkout")
            )
        )
        button.click()
