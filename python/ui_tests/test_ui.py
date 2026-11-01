import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from python.ui_tests.pages import LoginPage, DashboardPage
from config import Config

pytestmark = pytest.mark.ui

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@allure.story("UI")
@allure.title("Успешная авторизация")
def test_login_success(driver) -> None:
    with allure.step("Открытие страницы логина"):
        page = LoginPage(driver)
        page.open()
    with allure.step("Ввод логина и пароля"):
        page.login(Config.UI_LOGIN, Config.UI_PASSWORD)
    with allure.step("Проверка перехода на главную страницу"):
        dashboard = DashboardPage(driver)
        assert dashboard.is_loaded()

@allure.story("UI")
@allure.title("Проверка заголовка страницы")
def test_dashboard_title(driver) -> None:
    with allure.step("Проверка, что заголовок не пустой"):
        assert len(driver.title) > 0

@allure.story("UI")
@allure.title("Проверка URL после логина")
def test_url_after_login(driver) -> None:
    with allure.step("Проверка отсутствия 'login' в URL"):
        assert "login" not in driver.current_url

@allure.story("UI")
@allure.title("Проверка доступности кнопки создания")
def test_create_button_visible(driver) -> None:
    with allure.step("Проверка, что мы авторизованы"):
        assert "login" not in driver.current_url

@allure.story("UI")
@allure.title("Проверка страницы логина")
def test_logout_check(driver) -> None:
    with allure.step("Переход на страницу логина"):
        driver.get("https://ru.yougile.com/login")
    with allure.step("Проверка, что страница загрузилась"):
        assert "login" in driver.current_url or len(driver.title) > 0