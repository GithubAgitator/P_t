import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Pizza_gyrme_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    choose_pizza = "//*[@id='pizza']/div/div[3]/a/div/div[2]/div[3]/div[2]/div/span"
    choose = "//span[text()=' Добавить в корзину ']"

    # Getters
    def get_choose_pizza(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.choose_pizza)))

    def get_choose(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.choose)))

    # Actons

    def click_choose_pizza(self):
        self.get_choose_pizza().click()
        print(f"Пицца выбрана")

    def click_choose(self):
        self.get_choose().click()
        print("Пицца добавлена в карзину")

    # Methods
    def pizza_m(self):
        self.get_current_url()
        self.click_choose_pizza()
        self.click_choose()
        self.get_screenshot()
        time.sleep(5)