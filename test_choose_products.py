import time

from pages.chescout_page import Chescout_page
from pages.main_page import Login_page
from pages.address_page import Address_page
from pages.home_info_page import Home_info_page
from selenium import webdriver
from pages.pizza_gyrme_page import Pizza_gyrme_page
from pages.total_page import Total_page
from pages.zakaz_page import Zakaz_page
from pages.telephone_page import Telephone_page


def test_buy_product_1():
    options = webdriver.ChromeOptions()
    driver = (webdriver.Chrome(options=options))

    print("Старт тест")

    pizza = Login_page(driver)
    pizza.choose_kat_products()
    time.sleep(10)

    address_city = Address_page(driver)
    address_city.address_city()

    info_h = Home_info_page(driver)
    info_h.info_home()
    time.sleep(5)

    pizza = Pizza_gyrme_page(driver)
    pizza.pizza_m()

    total_price = Chescout_page(driver)
    total_price.checkout()

    t_p = Total_page(driver)
    t_p.total_pz()

    z_p = Zakaz_page(driver)
    z_p.zakaz_с()

    t_p = Telephone_page(driver)
    t_p.telep()



