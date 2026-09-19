from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()

    try:
        driver.get("https://www.saucedemo.com/")

        wait = WebDriverWait(driver, 10)

        username = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "user-name")
            )
        )
        username.send_keys("standard_user")

        driver.find_element(
            By.ID, "password"
        ).send_keys("secret_sauce")

        driver.find_element(
            By.ID, "login-button"
        ).click()

        wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_list")
            )
        )

        products = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie",
        ]

        for product in products:
            item = driver.find_element(
                By.XPATH,
                f"//div[text()='{product}']"
            )

            item.find_element(
                By.XPATH,
                "./ancestor::div[@class='inventory_item']"
                "//button"
            ).click()

        driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        ).click()

        wait.until(
            EC.visibility_of_element_located(
                (By.ID, "checkout")
            )
        )

        driver.find_element(By.ID, "checkout").click()

        wait.until(
            EC.visibility_of_element_located(
                (By.ID, "first-name")
            )
        )

        driver.find_element(
            By.ID, "first-name"
        ).send_keys("Иван")

        driver.find_element(
            By.ID, "last-name"
        ).send_keys("Петров")

        driver.find_element(
            By.ID, "postal-code"
        ).send_keys("123456")

        driver.find_element(
            By.ID, "continue"
        ).click()

        total = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )

        total_text = total.text

    finally:
        driver.quit()
    assert total_text == "Total: $58.29"
