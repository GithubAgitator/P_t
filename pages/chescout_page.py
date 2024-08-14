import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Chescout_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    but_card = "//button[@class='cart-button']"

    # Getters
    def get_but_card(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.but_card)))

    # Actons

    def click_but_card(self):
        self.get_but_card().click()
        print(f"Корзина")


    # Methods
    def checkout(self):
        self.get_current_url()
        self.click_but_card()
        self.get_screenshot()