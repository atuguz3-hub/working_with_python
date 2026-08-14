from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://gitflic.ru/")

    # Пользователь 1
    driver.add_cookie({
        "name": "SESSION",
        "value": "ZjFlNjBlYWUtZDY4Zi00Mzg2LTg5ZDYtN2E0M2Y0NzMzNGQ4",
        "domain": "gitflic.ru",
        "path": "/"
    })

    driver.refresh()

    driver.get("https://gitflic.ru/user/id620392600")

    wait.until(
        EC.url_to_be("https://gitflic.ru/user/id620392600")
    )

    user_1_url = driver.current_url

    # Выход из аккаунта
    driver.delete_all_cookies()

    # Пользователь 2
    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": "3:1786306149.5.0.1786306149978:HngYXw:8e7b.1.2:1|521326766.-1.20002.3:1786306149|3:12101759.194604.ObYvfUvYZabbQ90ZIWwsxEsRHwE",
        "domain": "gitflic.ru",
        "path": "/"
    })

    driver.refresh()

    driver.get("https://gitflic.ru/user/azaamat-tuguz")

    wait.until(
        EC.url_to_be("https://gitflic.ru/user/azaamat-tuguz")
    )

    user_2_url = driver.current_url

    assert user_1_url != user_2_url

    driver.quit()
