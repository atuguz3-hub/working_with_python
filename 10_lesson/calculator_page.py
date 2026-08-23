from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу калькулятора.

        Args:
            driver: Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver

    def open(self) -> None:
        """Открывает страницу медленного калькулятора."""
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def set_delay(self, delay: str) -> None:
        """Устанавливает задержку вычисления.

        Args:
            delay: Значение задержки в секундах.
        """
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(delay)

    def click_button(self, value: str) -> None:
        """Нажимает кнопку калькулятора.

        Args:
            value: Текст кнопки, которую необходимо нажать.
        """
        self.driver.find_element(
            By.XPATH, f"//span[text()='{value}']"
        ).click()

    def get_result(self) -> str:
        """Ожидает результат вычисления и возвращает его.

        Returns:
            Результат вычисления в виде строки.
        """
        WebDriverWait(self.driver, 50).until(
            lambda driver: driver.find_element(
                By.CSS_SELECTOR, ".screen"
            ).text == "15"
        )
        return self.driver.find_element(
            By.CSS_SELECTOR, ".screen"
        ).text
