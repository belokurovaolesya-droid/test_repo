from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    try:
        driver.get(
            "https://the-internet.herokuapp.com/dynamic_loading/2"
        )

        start_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
        )
        start_button.click()

        hello_world = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
        )

        driver.save_screenshot(
            r"C:\Users\pc\Desktop\dz\lesson_06\test_lesson06_task1.png"
        )

        assert hello_world.text == "Hello World!"
    finally:
        driver.quit()