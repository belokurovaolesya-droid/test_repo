"""Тест покупки в интернет-магазине с разметкой Allure."""

import allure
from selenium import webdriver

from cart_page import CartPage
from checkout_page import CheckoutPage
from login_page import LoginPage
from shop_page import ShopPage


@allure.title("Оформление заказа в интернет-магазине")
@allure.description(
    "Авторизуется на сайте, добавляет три товара в корзину "
    "и проверяет, что итоговая сумма равна Total: $58.29."
)
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    driver = webdriver.Firefox()

    try:
        login_page = LoginPage(driver)
        shop_page = ShopPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        with allure.step("Открыть страницу магазина"):
            login_page.open()

        with allure.step("Авторизоваться под standard_user"):
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавить три товара в корзину"):
            shop_page.add_product("Sauce Labs Backpack")
            shop_page.add_product("Sauce Labs Bolt T-Shirt")
            shop_page.add_product("Sauce Labs Onesie")

        with allure.step("Открыть корзину"):
            shop_page.open_cart()

        with allure.step("Перейти к оформлению заказа"):
            cart_page.checkout()

        with allure.step("Заполнить данные покупателя"):
            checkout_page.enter_first_name("Иван")
            checkout_page.enter_last_name("Петров")
            checkout_page.enter_postal_code("123456")

        with allure.step("Нажать кнопку Continue"):
            checkout_page.click_continue()

        with allure.step("Получить итоговую сумму"):
            total = checkout_page.get_total()

    finally:
        driver.quit()

    with allure.step(
        "Проверить, что итог равен Total: $58.29"
    ):
        assert total == "Total: $58.29"
