from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    start_url = driver.current_url

    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Данил")

    submit_button = driver.find_element(
        By.XPATH,
        "//button[contains(text(), 'Submit')]"
    )
    submit_button.click()

    WebDriverWait(driver, 5).until(
        lambda browser: browser.current_url != start_url
    )

    assert driver.current_url != start_url

    driver.quit()