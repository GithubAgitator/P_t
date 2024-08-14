import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Total_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    click_plus = "//*[@id='cart-sidebar']/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div[2]/div[3]"
    name_pizza = "//div[text()='Маргарита Гурме 20 см']"


    # Getters

    def get_click_plus(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.click_plus)))
    def get_name_pizza(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(("xpath", self.name_pizza)))


    #Actions
    def click_pl(self):
        self.get_click_plus().click()
        print("Добавлена еще одна пицца")



    # Methods
    def total_pz(self):
        self.get_current_url()
        self.click_pl()
        self.assert_word(self.get_name_pizza(), 'Маргарита Гурме 20 см')