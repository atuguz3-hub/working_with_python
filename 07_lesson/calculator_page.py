from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def set_delay(self, delay):
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(delay)

    def click_button(self, value):
        self.driver.find_element(
            By.XPATH, f"//span[text()='{value}']"
        ).click()

    def get_result(self):
        WebDriverWait(self.driver, 50).until(
            lambda driver: driver.find_element(
                By.CSS_SELECTOR, ".screen"
            ).text == "15"
        )
        return self.driver.find_element(
            By.CSS_SELECTOR, ".screen"
        ).text
