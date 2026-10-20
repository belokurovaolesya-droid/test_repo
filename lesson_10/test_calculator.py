"""Тест медленного калькулятора с разметкой Allure."""

import allure
from selenium import webdriver

from calculator_page import CalculatorPage


@allure.title("Сложение на медленном калькуляторе")
@allure.description(
    "Открывает калькулятор, ставит задержку 45 секунд "
    "и проверяет, что 7 + 8 равно 15."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator():
    driver = webdriver.Chrome()

    try:
        calculator = CalculatorPage(driver)

        with allure.step("Открыть страницу калькулятора"):
            calculator.open()

        with allure.step("Установить задержку 45 секунд"):
            calculator.set_delay(45)

        with allure.step("Нажать кнопки 7, +, 8 и ="):
            calculator.click_button("7")
            calculator.click_button("+")
            calculator.click_button("8")
            calculator.click_button("=")

        with allure.step("Дождаться результата вычисления"):
            result = calculator.get_result("15")

    finally:
        driver.quit()

    with allure.step("Проверить, что результат равен 15"):
        assert result == "15"
