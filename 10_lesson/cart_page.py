from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class CartPage:

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу корзины.

        Args:
            driver: Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver

    def click_checkout(self) -> None:
        """Переходит к оформлению заказа."""
        self.driver.find_element(
            By.ID, "checkout"
        ).click()

    def get_items(self) -> list[WebElement]:
        """Возвращает список товаров в корзине.

        Returns:
            Список веб-элементов товаров.
        """
        return self.driver.find_elements(
            By.CLASS_NAME, "cart_item"
        )
