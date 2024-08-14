import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Address_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    ad = "//*[@id='error-modal']/div/div/div/div[3]/div"
    address = "//*[@id='__nuxt']/div/div[2]/div[2]/div[6]/div/div/div[2]/div/div/div/div/div[3]/div[9]/a"
    input_address = "//input[@id='input-address']"
    input_choose = "//*[@id='__nuxt']/div/div[2]/div[2]/div[6]/div/div/div[2]/div/div/div/div/div[5]/div/div"
    a_d = "//div[text()='г Москва, 1-й Краснокурсантский проезд, д 3/5 к 11']"

    #Getters
    def get_ad(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.ad)))

    def get_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.address)))

    def get_input_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.input_address)))

    def get_input_choose(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.input_choose)))

    def get_a_d(self):
        return WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(("xpath", self.a_d)))
    #Actons

    def click_ad(self):
        self.get_ad().click()
        print("Адрес выбран")

    def click_address(self):
        self.get_address().click()
        print("выбран")

    def click_input_address(self, city):
        self.get_input_address().send_keys(city)
        print("Адрес введен")

    def click_a_d(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_a_d()).double_click().double_click().perform()
        print("Адрес выбран")


    def click_choose_address(self):
        self.get_input_choose().click()
        print("Click")
    # Methods
    def address_city(self):
        self.get_current_url()
        self.click_ad()
        self.click_address()
        self.click_input_address("1-й Краснокурсантский проезд, 3/5к1")
        time.sleep(2)
        self.click_a_d()
        self.click_choose_address()
        self.get_screenshot()
        time.sleep(10)