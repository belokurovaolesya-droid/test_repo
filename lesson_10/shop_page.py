"""Page Object страницы каталога магазина."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ShopPage:
    """Страница каталога товаров."""

    def __init__(self, driver: WebDriver) -> None:
        """Создаёт объект страницы каталога.

        Args:
            driver (WebDriver): веб-драйвер браузера.

        Returns:
            None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product(self, product_name: str) -> None:
        """Добавляет товар в корзину.

        Args:
            product_name (str): название товара в каталоге.

        Returns:
            None
        """
        product = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    f"//div[text()='{product_name}']"
                )
            )
        )

        product_container = product.find_element(
            By.XPATH,
            "./ancestor::div[@class='inventory_item']"
        )

        button = product_container.find_element(
            By.TAG_NAME,
            "button"
        )

        button.click()

    def open_cart(self) -> None:
        """Открывает корзину.

        Returns:
            None
        """
        cart = self.wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        )
        cart.click()
