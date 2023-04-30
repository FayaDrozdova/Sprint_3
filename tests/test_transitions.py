from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestTransitions:

    def test_transition_to_personal_cabinet_by_personal_cabinet_button_success(self, driver, data):
        driver.get(data.URL)
        driver.find_element(By.XPATH, Locators.PERSONAL_CABINET_LINK).click()

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
            'Не найдена кнопка выхода'
        )

        assert driver.current_url in data.PERSONAL_CABINET_URL, 'Переход не на страницу Личного Кабинета'

    def test_transition_from_personal_cabinet_to_constructor_by_constructor_button_success(self, driver, data):
        driver.get(data.URL)
        driver.find_element(By.XPATH, Locators.PERSONAL_CABINET_LINK).click()

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
            'Не найдена кнопка выхода'
        )

        driver.find_element(By.XPATH, Locators.CONSTRUCTOR_BUTTON).click()

        WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.CREATE_ORDER_BUTTON)),
            'Не найдена кнопка создания заказа'
        )

        assert driver.current_url in data.URL, 'Переход не на страницу с конструктором'

    def test_transition_from_personal_cabinet_to_constructor_by_logo_success(self, driver, data):
        driver.get(data.URL)
        driver.find_element(By.XPATH, Locators.PERSONAL_CABINET_LINK).click()

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
            'Не найдена кнопка выхода'
        )

        driver.find_element(By.XPATH, Locators.CONSTRUCTOR_BUTTON).click()

        WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.CREATE_ORDER_BUTTON)),
            'Не найдена кнопка создания заказа'
        )

        assert driver.current_url in data.URL, 'Переход не на страницу с конструктором'
