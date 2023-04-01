from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from settings import *


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.base_url = Setting.BASE_URL
        self.driver.implicitly_wait(timeout)

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator),
                                                         message=f" Ахтунг пинг{locator}")

    def find_elements(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator),
                                                         message=f" Ахтунг пинг{locator}")
