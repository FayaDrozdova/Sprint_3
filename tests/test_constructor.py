from selenium.webdriver.common.by import By
from locators import Locators


class TestConstructor:

    def test_transition_to_bread_success(self, driver, data):
        driver.get(data.URL)
        sauce_section = driver.find_element(By.XPATH, Locators.CONSTRUCTOR_SAUCE_SECTION)
        driver.execute_script("arguments[0].scrollIntoView();", sauce_section)
        bread_section = driver.find_element(By.XPATH, Locators.CONSTRUCTOR_BREAD_SECTION)
        driver.execute_script("arguments[0].scrollIntoView();", bread_section)
        bread_tab = driver.find_element(By.XPATH, Locators.CONSTRUCTOR_BREAD_TAB)

        assert 'tab_tab_type_current__2BEPc' in bread_tab.get_attribute('class')

        driver.quit()

    def test_transition_to_sauce_success(self, driver, data):
        driver.get(data.URL)
        sauce_section = driver.find_element(By.XPATH, Locators.CONSTRUCTOR_SAUCE_SECTION)
        driver.execute_script("arguments[0].scrollIntoView();", sauce_section)
        sauce_tab = driver.find_element(By.XPATH, Locators.CONSTRUCTOR_SAUCE_TAB)

        assert 'tab_tab_type_current__2BEPc' in sauce_tab.get_attribute('class')

        driver.quit()

    def test_transition_to_topping_success(self, driver, data):
        driver.get(data.URL)
        topping_section = driver.find_element(By.XPATH, Locators.CONSTRUCTOR_TOPPING_SECTION)
        driver.execute_script("arguments[0].scrollIntoView();", topping_section)
        topping_tab = driver.find_element(By.XPATH, Locators.CONSTRUCTOR_TOPPING_TAB)

        assert 'tab_tab_type_current__2BEPc' in topping_tab.get_attribute('class')

        driver.quit()
