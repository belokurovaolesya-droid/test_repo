from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_first_name(self, first_name):
        field = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "first-name")
            )
        )
        field.send_keys(first_name)

    def enter_last_name(self, last_name):
        field = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "last-name")
            )
        )
        field.send_keys(last_name)

    def enter_postal_code(self, postal_code):
        field = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "postal-code")
            )
        )
        field.send_keys(postal_code)

    def click_continue(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "continue")
            )
        )
        button.click()

    def get_total(self):
        total = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        return total.text
