import allure
from selenium import webdriver

from login_page import LoginPage
from main_shop_page import MainShopPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@allure.title("Покупка товаров в интернет-магазине")
@allure.description("Проверка добавления товаров в корзину и оформления заказа")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    driver = webdriver.Firefox()

    login_page = LoginPage(driver)
    main_shop_page = MainShopPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    with allure.step("Открыть страницу авторизации"):
        login_page.open()

    with allure.step("Ввести имя пользователя"):
        login_page.enter_username("standard_user")

    with allure.step("Ввести пароль"):
        login_page.enter_password("secret_sauce")

    with allure.step("Нажать кнопку входа"):
        login_page.click_login()

    with allure.step("Добавить рюкзак в корзину"):
        main_shop_page.add_backpack()

    with allure.step("Добавить футболку Bolt в корзину"):
        main_shop_page.add_bolt_t_shirt()

    with allure.step("Добавить Onesie в корзину"):
        main_shop_page.add_onesie()

    with allure.step("Открыть корзину"):
        main_shop_page.open_cart()

    with allure.step("Перейти к оформлению заказа"):
        cart_page.click_checkout()

    with allure.step("Ввести имя"):
        checkout_page.enter_first_name("Иван")

    with allure.step("Ввести фамилию"):
        checkout_page.enter_last_name("Петров")

    with allure.step("Ввести почтовый индекс"):
        checkout_page.enter_postal_code("123456")

    with allure.step("Продолжить оформление заказа"):
        checkout_page.click_continue()

    with allure.step("Получить итоговую сумму"):
        total = checkout_page.get_total()

    with allure.step("Проверить итоговую сумму заказа"):
        assert total == "Total: $58.29"

    driver.quit()
