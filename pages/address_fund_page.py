import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class AddressFundPage(Base):

    #Locators

    address_residents = "//a[@data-test-id='Адреса проживающих']"


    #Getters

    def get_address_residents(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address_residents)))

    #Action

    def click_address_residents(self):
        self.get_address_residents().click()
        print('Click Address Residents')


    #Methods

    def go_to_address_residents(self):
        with allure.step('Go To Address Residents'):
            self.get_current_url()
            self.click_address_residents()
            self.save_screenshot()



