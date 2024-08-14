import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Home_info_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    kvartira = "//input[@id='input-flat']"
    etaz = "//input[@id='input-floor']"
    podezd = "//input[@id='input-entrance']"
    domofon = "//input[@id='input-doorphone']"
    komment = "//input[@id='input-comment']"
    btn = "//button[text()='Сохранить']"

    #Getters
    def get_kvartira(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.kvartira)))

    def get_etaz(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.etaz)))

    def get_podezd(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.podezd)))

    def get_domofon(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.domofon)))

    def get_komment(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.komment)))

    def get_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.btn)))

    # Actons

    def input_kvartira(self, kv):
        self.get_kvartira().send_keys(kv)
        print(f"Номер квартиры {kv}")

    def input_etaz(self, et):
        self.get_etaz().send_keys(et)
        print(f"Этаж {et}")

    def input_podezd(self, podz):
        self.get_podezd().send_keys(podz)
        print(f"Ваш подъезд {podz}")

    def input_domofon(self, domof):
        self.get_domofon().send_keys(domof)
        print(f"Домофон {domof}")

    def input_komment(self, km):
        self.get_komment().send_keys(km)
        print(f"Спасибо за ваш комментрарий")

    def click_btn(self):
        self.get_btn().click()
        print(f"Сохранить")

    # Methods
    def info_home(self):
        self.get_current_url()
        self.input_kvartira('55')
        self.input_etaz('7')
        self.input_podezd("6")
        self.input_domofon('55')
        self.input_komment('Hello')
        self.click_btn()
        self.get_screenshot()



