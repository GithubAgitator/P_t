import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Telephone_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    telephone = "//input[@type='tel']"
    prog = "//span[text()='Продолжить']"

    # Getters

    def get_telephone(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.telephone)))

    def get_prog(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.prog)))


    # Actions
    def input_telephone(self, tel):
        self.get_telephone().send_keys(tel)
        print("Телефон добавлен")

    def clic_prod(self):
        self.get_prog().click()
        print("Ваш заказ оформлен")

    # Methods
    def telep(self):
        self.get_current_url()
        self.input_telephone('9051234545')
        self.clic_prod()
        time.sleep(5)
        self.assert_url('https://dominopizza.ru/auth/login')



