from selenium import webdriver

from login_page import LoginPage
from shop_page import ShopPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_shop():
    driver = webdriver.Firefox()

    try:
        login_page = LoginPage(driver)
        shop_page = ShopPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        shop_page.add_product("Sauce Labs Backpack")
        shop_page.add_product("Sauce Labs Bolt T-Shirt")
        shop_page.add_product("Sauce Labs Onesie")

        shop_page.open_cart()

        cart_page.checkout()

        checkout_page.enter_first_name("Иван")
        checkout_page.enter_last_name("Петров")
        checkout_page.enter_postal_code("123456")
        checkout_page.click_continue()

        total = checkout_page.get_total()

    finally:
        driver.quit()

    assert total == "Total: $58.29"
