from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует страницу авторизации.

        Args:
            driver: Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver

    def open(self) -> None:
        """Открывает страницу авторизации."""
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username: str) -> None:
        """Вводит имя пользователя.

        Args:
            username: Имя пользователя.
        """
        self.driver.find_element(
            By.ID, "user-name"
        ).send_keys(username)

    def enter_password(self, password: str) -> None:
        """Вводит пароль.

        Args:
            password: Пароль пользователя.
        """
        self.driver.find_element(
            By.ID, "password"
        ).send_keys(password)

    def click_login(self) -> None:
        """Нажимает кнопку входа."""
        self.driver.find_element(By.ID, "login-button").click()
