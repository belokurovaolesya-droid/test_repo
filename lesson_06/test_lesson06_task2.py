from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def test_session_storage_auth():
    driver = webdriver.Chrome()

    try:
        driver.get("https://gitflic.ru/")

        user_1_cookie = {
            "name": "SESSION",
            "value": "Y2UwZTZiOGQtYTMzZi00NGRlLTkyNzUtM2NmODM4MDJlODNl",
        }

        user_2_cookie = {
            "name": "SESSION",
            "value": "YTdhZjEyZmYtZjQ2OS00YWMwLWIyZWQtZjQzYjA5OGJlMDEw",
        }

        driver.add_cookie(user_1_cookie)
        driver.refresh()

        driver.get("https://gitflic.ru/user/belokurovaolesya")
        user_1_url = driver.current_url

        driver.delete_all_cookies()
        driver.refresh()

        driver.add_cookie(user_2_cookie)
        driver.refresh()

        driver.get("https://gitflic.ru/user/martygrimm6277")
        user_2_url = driver.current_url

        assert user_1_url != user_2_url
    finally:
        driver.quit()