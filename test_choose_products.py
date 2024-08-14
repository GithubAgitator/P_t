import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.address_page import Address_page
from pages.chescout_page import Chescout_page
from pages.home_info_page import Home_info_page
from pages.main_page import Login_page
from pages.pizza_gyrme_page import Pizza_gyrme_page
from pages.telephone_page import Telephone_page
from pages.total_page import Total_page
from pages.zakaz_page import Zakaz_page


# Опции браузера


def test_buy_product():
    options = webdriver.ChromeOptions()
    driver = (webdriver.Chrome(options=options))

    print("Старт тест 1")

    p_m = Login_page(driver)
    p_m.choose_kat_products()

    a_p = Address_page(driver)
    a_p.address_city()

    h_p = Home_info_page(driver)
    h_p.info_home()

    p_z_p = Pizza_gyrme_page(driver)
    p_z_p.pizza_m()

    c_p = Chescout_page(driver)
    c_p.checkout()

    t_p = Total_page(driver)
    t_p.click_pl()

    z_p = Zakaz_page(driver)
    z_p.zakaz_с()

    tel_p = Telephone_page(driver)
    tel_p.telep()

