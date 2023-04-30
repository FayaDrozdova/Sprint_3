from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from locators import Locators


class TestRegistration:

    def test_registration_success(self, driver, data):
        driver.get(data.REGISTER_URL)
        driver.find_element(By.XPATH, Locators.REGISTER_NAME_INPUT).send_keys(data.generate_name())
        driver.find_element(By.XPATH, Locators.REGISTER_EMAIL_INPUT).send_keys(data.generate_email())
        driver.find_element(By.XPATH, Locators.REGISTER_PASSWORD_INPUT).send_keys(data.generate_correct_password())
        driver.find_element(By.XPATH, Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(
                expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOGIN_BUTTON)),
                'Не найдена кнопка входа в аккаунт'
        )

        assert driver.current_url in data.LOGIN_URL, 'Не происходит переход на страницу входа'

        driver.quit()

    def test_registration_error(self, driver, data):
        driver.get(data.REGISTER_URL)
        driver.find_element(By.XPATH, Locators.REGISTER_NAME_INPUT).send_keys(data.generate_name())
        driver.find_element(By.XPATH, Locators.REGISTER_EMAIL_INPUT).send_keys(data.generate_email())
        driver.find_element(By.XPATH, Locators.REGISTER_PASSWORD_INPUT).send_keys(data.generate_incorrect_password())
        driver.find_element(By.XPATH, Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.REGISTER_ERROR_P)),
            'Не найден тег с ошибкой'
        )

        assert driver.find_element(By.XPATH, Locators.REGISTER_ERROR_P).text in data.INCORRECT_PASSWORD_ERROR, \
            'Неверный текст ошибки'

        driver.quit()
