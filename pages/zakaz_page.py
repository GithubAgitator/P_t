import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Zakaz_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    zakaz = "//span[text()='Перейти к оформлению']"


    #Getters
    def get_zakaz(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.zakaz)))

    #Actons

    def click_zakaz(self):
        self.get_zakaz().click()
        print("Продолжить")


    # Methods
    def zakaz_с(self):
        self.get_current_url()
        self.click_zakaz()
        self.get_screenshot()
        time.sleep(10)
