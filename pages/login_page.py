from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilites.logger import Logger
import allure

class LoginPage(Base):

    url = 'https://demo.app.stack-it.ru/fl'

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    #Locators

    login_field = '//input[@id="VInput71"]'
    password_field = '//input[@id="VInput75"]'
    enter_button = '//button[@data-cy="submit-btn"]'
    message_ok = "//button[@data-cy='btn-yes']"

    #Getters

    def get_login_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_field)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_field)))

    def get_enter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_message_ok(self):
        return WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.XPATH, self.message_ok)))


    #Action

    def input_login(self, login):
        self.get_login_field().send_keys(login)
        print('Input Login')

    def input_password(self, password):
        self.get_password_field().send_keys(password)
        print('Input Password')

    def click_enter_button(self):
        self.get_enter_button().click()
        print('Click Login Button')

    def click_message_ok(self):
        self.get_message_ok().click()
        print('Click Login Button')


    #Methods

    def authorization(self):
        with allure.step('Authorization'):
            Logger.add_start_step(method='authorization')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_login('DEMOWEB')
            self.input_password('awdrgy')
            self.click_enter_button()
            try:
                self.click_message_ok()
            except TimeoutException:
                Logger.add_end_step(url=self.driver.current_url, method='authorization')
            self.save_screenshot()
