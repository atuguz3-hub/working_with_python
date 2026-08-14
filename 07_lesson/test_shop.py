from selenium import webdriver

from login_page import LoginPage
from main_shop_page import MainShopPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_shop():
    driver = webdriver.Firefox()

    login_page = LoginPage(driver)
    main_shop_page = MainShopPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    main_shop_page.add_backpack()
    main_shop_page.add_bolt_t_shirt()
    main_shop_page.add_onesie()
    main_shop_page.open_cart()

    cart_page.click_checkout()

    checkout_page.enter_first_name("Иван")
    checkout_page.enter_last_name("Петров")
    checkout_page.enter_postal_code("123456")
    checkout_page.click_continue()

    total = checkout_page.get_total()

    driver.quit()

    assert total == "Total: $58.29"
