from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.url = "https://ru.yougile.com"
        self.login_btn = (By.CSS_SELECTOR, "a.sign-in-button")
        self.email_input = (By.CSS_SELECTOR, "input[type='email']")
        self.password_input = (By.CSS_SELECTOR, "input[type='password']")
        self.submit_btn = (By.XPATH, "//*[contains(text(), 'Войти')]")

    def open(self) -> None:
        self.driver.get(self.url)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.login_btn)).click()

    def login(self, email: str, password: str) -> None:
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.email_input)).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        wait.until(EC.element_to_be_clickable(self.submit_btn)).click()

class DashboardPage:
    def __init__(self, driver) -> None:
        self.driver = driver

    def is_loaded(self) -> bool:
        return "login" not in self.driver.current_url