from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from locators import Locators


class TestRegistration:

    def test_registration_success(self, driver, data):
        email = data.generate_email()
        password = data.generate_correct_password()

        driver.get(data.REGISTER_URL)
        driver.find_element(By.XPATH, Locators.REGISTER_NAME_INPUT).send_keys(data.generate_name())
        driver.find_element(By.XPATH, Locators.REGISTER_EMAIL_INPUT).send_keys(email)
        driver.find_element(By.XPATH, Locators.REGISTER_PASSWORD_INPUT).send_keys(password)
        driver.find_element(By.XPATH, Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.LOGIN_BUTTON)),
            'Не найдена кнопка входа в аккаунт'
        )

        driver.find_element(By.XPATH, Locators.LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(By.XPATH, Locators.LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()

        element = WebDriverWait(driver, 5).until(
                expected_conditions.visibility_of_element_located((By.XPATH, Locators.CREATE_ORDER_BUTTON)),
                'Не найдена кнопка создания заказа'
        )

        assert element.text == 'Оформить заказ', 'После регистрации и логина нет кнопки "Оформить заказ", ' \
            'доступной зарегистрированным пользователям'

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

        assert driver.find_element(By.XPATH, Locators.REGISTER_ERROR_P).text in 'Некорректный пароль', \
            'Неверный текст ошибки'

        driver.quit()
