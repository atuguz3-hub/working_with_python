from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу оформления заказа.

        Args:
            driver: Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver

    def enter_first_name(self, first_name: str) -> None:
        """Вводит имя покупателя.

        Args:
            first_name: Имя покупателя.
        """
        self.driver.find_element(
            By.ID, "first-name"
        ).send_keys(first_name)

    def enter_last_name(self, last_name: str) -> None:
        """Вводит фамилию покупателя.

        Args:
            last_name: Фамилия покупателя.
        """
        self.driver.find_element(
            By.ID, "last-name"
        ).send_keys(last_name)

    def enter_postal_code(self, postal_code: str) -> None:
        """Вводит почтовый индекс.

        Args:
            postal_code: Почтовый индекс покупателя.
        """
        self.driver.find_element(
            By.ID, "postal-code"
        ).send_keys(postal_code)

    def click_continue(self) -> None:
        """Переходит к следующему этапу оформления заказа."""
        self.driver.find_element(
            By.ID, "continue"
        ).click()

    def get_total(self) -> str:
        """Возвращает итоговую сумму заказа.

        Returns:
            Итоговая сумма заказа в виде строки.
        """
        return self.driver.find_element(
            By.CLASS_NAME, "summary_total_label"
        ).text
