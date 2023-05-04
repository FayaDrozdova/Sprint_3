from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Locators


class TestLogin:

    def test_login_by_enter_account_button_success(self, driver, data):
        driver.get(data.URL)
        driver.find_element(By.XPATH, Locators.CREATE_ORDER_BUTTON).click()
        driver.find_element(By.XPATH, Locators.LOGIN_EMAIL_INPUT).send_keys(data.EMAIL)
        driver.find_element(By.XPATH, Locators.LOGIN_PASSWORD_INPUT).send_keys(data.PASSWORD)
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()

        element = WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.CREATE_ORDER_BUTTON)),
            'Не найдена кнопка создания заказа'
        )

        assert element.text == 'Оформить заказ', \
            'После логина через кнопку "Войти в аккаунт" нет кнопки "Оформить заказ", ' \
            'доступной зарегистрированным пользователям'

        driver.quit()

    def test_login_by_personal_cabinet_button_success(self, driver, data):
        driver.get(data.URL)
        driver.find_element(By.XPATH, Locators.PERSONAL_CABINET_LINK).click()
        driver.find_element(By.XPATH, Locators.LOGIN_EMAIL_INPUT).send_keys(data.EMAIL)
        driver.find_element(By.XPATH, Locators.LOGIN_PASSWORD_INPUT).send_keys(data.PASSWORD)
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()

        element = WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.CREATE_ORDER_BUTTON)),
            'Не найдена кнопка создания заказа'
        )

        assert element.text == 'Оформить заказ', \
            'После логина через кнопку "Личный кабинет" нет кнопки "Оформить заказ", ' \
            'доступной зарегистрированным пользователям'

        driver.quit()

    def test_login_in_registration_form_success(self, driver, data):
        driver.get(data.REGISTER_URL)
        driver.find_element(By.XPATH, Locators.LOGIN_LINK).click()
        driver.find_element(By.XPATH, Locators.LOGIN_EMAIL_INPUT).send_keys(data.EMAIL)
        driver.find_element(By.XPATH, Locators.LOGIN_PASSWORD_INPUT).send_keys(data.PASSWORD)
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()

        element = WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.CREATE_ORDER_BUTTON))
        )

        assert element.text == 'Оформить заказ', \
            'После логина через кнопку регистрации нет кнопки "Оформить заказ", ' \
            'доступной зарегистрированным пользователям'

        driver.quit()

    def test_login_by_forgot_password_form_success(self, driver, data):
        driver.get(data.FORGOT_PASSWORD_URL)
        driver.find_element(By.XPATH, Locators.LOGIN_LINK).click()
        driver.find_element(By.XPATH, Locators.LOGIN_EMAIL_INPUT).send_keys(data.EMAIL)
        driver.find_element(By.XPATH, Locators.LOGIN_PASSWORD_INPUT).send_keys(data.PASSWORD)
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()

        element = WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.CREATE_ORDER_BUTTON))
        )

        assert element.text == 'Оформить заказ', \
            'После логина через кнопку регистрации нет кнопки "Оформить заказ", ' \
            'доступной зарегистрированным пользователям'

        driver.quit()
