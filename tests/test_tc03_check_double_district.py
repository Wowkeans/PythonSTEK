import time
import allure

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.address_fund_page import AddressFundPage
from pages.address_residents_page import AddressResidentsPage

from pages.login_page import LoginPage
from pages.main_page import MainPage


# @pytest.mark.order(3)
@allure.description('Test Add District')
def test_add_district_cancel():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)

    lp = LoginPage(driver)
    lp.authorization()

    mp = MainPage(driver)
    mp.go_to_address_fund()

    afp = AddressFundPage(driver)
    afp.go_to_address_residents()

    arp = AddressResidentsPage(driver)
    arp.add_new_district()
    arp.add_new_district()

    driver.quit()
