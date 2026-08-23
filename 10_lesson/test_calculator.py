import allure
from selenium import webdriver

from calculator_page import CalculatorPage


@allure.title("Проверка работы калькулятора")
@allure.description("Проверка сложения двух чисел в калькуляторе")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator():
    driver = webdriver.Chrome()

    calculator = CalculatorPage(driver)

    with allure.step("Открыть калькулятор"):
        calculator.open()

    with allure.step("Установить задержку 45 секунд"):
        calculator.set_delay("45")

    with allure.step("Ввести число 7"):
        calculator.click_button("7")

    with allure.step("Нажать кнопку +"):
        calculator.click_button("+")

    with allure.step("Ввести число 8"):
        calculator.click_button("8")

    with allure.step("Нажать кнопку ="):
        calculator.click_button("=")

    with allure.step("Получить результат"):
        result = calculator.get_result()

    with allure.step("Проверить, что результат равен 15"):
        assert result == "15"

    driver.quit()
