import time

import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class AddressResidentsPage(Base):


    #Locators

    add_button = "//button[@data-cy='btn-add']"
    district_menu = "//div[@class='v-list-item__title font-weight-regular' and normalize-space(text())='Район']"
    save_button = '//button[@data-cy="btn-save"]'
    cancel_button = '//button[@data-cy="btn-cancel"]'
    delete_button = "//*[name()='svg']/*[name()='path' and starts-with(@d, 'M19,4H15.5')]"
    yes_delete_button = "button[data-cy='btn-yes']"
    name_district_field = "//input[@data-cy='stack-input']"

    checkbox_num = 5




    #Getters

    def get_add_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_button)))

    def get_district_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.district_menu)))

    def get_save_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.save_button)))

    def get_cancel_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cancel_button)))

    def get_delete_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delete_button)))

    def get_yes_delete_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.yes_delete_button)))

    def get_name_district_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_district_field)))

    #Action

    def click_add_button(self):
        self.get_add_button().click()
        print('Click Add Button')

    def select_district_menu(self):
        self.get_district_menu().click()
        print('Click District Menu')

    def click_save_button(self):
        self.get_save_button().click()
        print('Click Save Button')

    def click_cancel_button(self):
        self.get_cancel_button().click()
        print('Click Cancel Button')

    def click_delete_button(self):
        self.get_delete_button().click()
        print('Click Delete Button')

    def click_yes_delete_button(self):
        self.get_yes_delete_button().click()
        print('Click Yes Button')

    def select_checkbox(self, index):
        xpath = f"(//input[@data-cy='checkbox'])[ {index} ]"
        checkbox = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
        try:
            ActionChains(self.driver).move_to_element(checkbox).click().perform()
        except:
            self.driver.execute_script("arguments[0].click();", checkbox)
        print(f'Click Checkbox index {index}')

    def input_name_district(self, name_new_district):
        self.get_name_district_field().send_keys(name_new_district)
        print('Enter New District Name')

    def clear_name_district(self):
        field = self.get_name_district_field()
        self.driver.execute_script("arguments[0].value = '';", field)
        print('Clear District Name')


    def click_edit_button(self, number):

        xpath = f"(//button[@data-cy='btn-edit'])[{number}]"
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )

        # Скролл и клик
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        btn.click()
        print(f"✏️ Clicked edit button #{number}")



    #Methods

    def add_new_district(self):
        with allure.step('Add New District'):
            self.get_current_url()
            self.click_add_button()
            self.select_district_menu()
            self.input_name_district('test_district_1')
            self.click_save_button()
            self.save_screenshot()

    def add_new_empty_district(self):
        with allure.step('Add New Empty District'):
            self.get_current_url()
            self.click_add_button()
            self.select_district_menu()
            self.input_name_district('')
            self.click_save_button()
            self.save_screenshot()

    def check_double(self):
        with allure.step('Add New Empty District'):
            self.get_current_url()
            self.click_add_button()
            self.select_district_menu()
            self.input_name_district('test_district_1')
            self.click_save_button()
            self.input_name_district('test_district_1')
            self.click_save_button()
            self.save_screenshot()


    def edit_added_district(self):
        with allure.step('Delete Added District'):
            self.get_current_url()
            self.select_checkbox(self.checkbox_num)
            self.click_edit_button(self.checkbox_num)
            self.clear_name_district()
            self.input_name_district('test_district_2')
            self.get_name_district_field().send_keys(Keys.ENTER)
            self.save_screenshot()


    def delete_added_district(self):
        with allure.step('Delete Added District'):
            self.get_current_url()
            self.select_checkbox(self.checkbox_num)
            self.click_delete_button()
            self.click_yes_delete_button()
            self.save_screenshot()
