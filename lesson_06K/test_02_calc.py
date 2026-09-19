from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome()

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

        wait = WebDriverWait(driver, 50)

        delay = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#delay")
            )
        )
        delay.clear()
        delay.send_keys("45")

        driver.find_element(
            By.XPATH, "//span[text()='7']"
        ).click()

        driver.find_element(
            By.XPATH, "//span[text()='+']"
        ).click()

        driver.find_element(
            By.XPATH, "//span[text()='8']"
        ).click()

        driver.find_element(
            By.XPATH, "//span[text()='=']"
        ).click()

        result = wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"),
                "15"
            )
        )

        assert result
    finally:
        driver.quit()
