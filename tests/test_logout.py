from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestLogout:

    def test_logout_success(self, driver, data):
        driver.get(data.LOGIN_URL)
        driver.find_element(By.XPATH, Locators.LOGIN_EMAIL_INPUT).send_keys(data.EMAIL)
        driver.find_element(By.XPATH, Locators.LOGIN_PASSWORD_INPUT).send_keys(data.PASSWORD)
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.CREATE_ORDER_BUTTON)),
            'Не найдена кнопка создания заказа'
        )

        driver.find_element(By.XPATH, Locators.PERSONAL_CABINET_LINK).click()

        WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOGOUT_BUTTON)),
            'Не найдена кнопка выхода из аккаунта'
        )

        driver.find_element(By.XPATH, Locators.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOGIN_BUTTON)),
            'Не найдена кнопка входа в аккаунт'
        )

        assert driver.current_url in data.LOGIN_URL, \
            'После выхода из аккаунта не произошло перенаправление на страницу входа'

        driver.quit()
