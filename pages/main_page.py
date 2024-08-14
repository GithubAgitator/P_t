import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Login_page(Base):
    url = 'https://dominopizza.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    #Locators
    choose_product = "//*[@id='pizza']/div/div[2]/a/div/div[3]/div[3]/div[2]/div"
    choose_product_meni = "//*[@id='__nuxt']/div/div[2]/div[2]/div[6]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div[2]"
    choose_ingridient = "//*[@id='__nuxt']/div/div[2]/div[2]/div[6]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div[4]/div/div[2]/div[2]/div"
    products_1 = "//*[@id='__nuxt']/div/div[2]/div[2]/div[6]/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div[2]/div/span"

    name_pizza = "//h1[text()='Пицца Капрезе']"




    #Getters
    def get_choose_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.choose_product)))

    def get_choose_product_meni(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.choose_product_meni)))

    def get_choose_ingridient(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.choose_ingridient)))
    def get_products_1(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(("xpath", self.products_1)))

    def get_word_value(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.name_pizza)))

    # Actions
    def input_choose_product(self):
        self.get_choose_product().click()
        print(f"Пицца выбрана")

    def click_choose_size(self):
        self.get_choose_product_meni().click()
        print(f"Размер пиццы выбран")

    def click_choose_ingridient(self):
        self.get_choose_ingridient().click()
        print("Ингридиент выбран")

    def click_products_1(self):
        self.get_products_1().click()
        print("Добвлено в карзину")



    #Methods
    def choose_kat_products(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_choose_product()
        self.click_choose_size()
        self.click_choose_ingridient()
        self.assert_word(self.get_word_value(), 'Пицца Капрезе')
        self.click_products_1()
        self.get_screenshot()

