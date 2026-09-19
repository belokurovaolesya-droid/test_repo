from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    URL = (
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "slow-calculator.html"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, delay):
        field = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#delay")
            )
        )
        field.clear()
        field.send_keys(str(delay))

    def click_button(self, value):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//span[text()='{value}']")
            )
        )
        button.click()

    def get_result(self, expected_result):
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"),
                expected_result
            )
        )

        return self.driver.find_element(
            By.CSS_SELECTOR, ".screen"
        ).text
