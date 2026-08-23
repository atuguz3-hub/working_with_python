from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainShopPage:

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует главную страницу магазина.

        Args:
            driver: Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver

    def add_backpack(self) -> None:
        """Добавляет рюкзак в корзину."""
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        ).click()

    def add_bolt_t_shirt(self) -> None:
        """Добавляет футболку Bolt в корзину."""
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()

    def add_onesie(self) -> None:
        """Добавляет комбинезон Onesie в корзину."""
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        ).click()

    def open_cart(self) -> None:
        """Открывает корзину."""
        self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        ).click()
