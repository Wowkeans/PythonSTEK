import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class MainPage(Base):


    #Locators

    address_fund = "//a[@data-test-id='Адресный фонд']"



    #Getters

    def get_address_fund(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address_fund)))

    #Action

    def click_address_fund(self):
        self.get_address_fund().click()
        print('Click Address Fund')


    #Methods

    def go_to_address_fund(self):
        with allure.step('Go To Address Fund'):
            self.get_current_url()
            self.click_address_fund()
            self.save_screenshot()


