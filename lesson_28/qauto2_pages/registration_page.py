from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_28.qauto2_pages.base_page import BasePage
from lesson_28.qauto2_pages.ui_elements import UIElements


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super(RegistrationPage, self).__init__(driver)
        self.ui = UIElements()

    def open_registration_form(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.ui.signup_button)
        ).click()

    def fill_registration_form(self, name, last_name, email, password):
        self.input_text(self.ui.signup_name, name)
        self.input_text(self.ui.signup_last_name, last_name)
        self.input_text(self.ui.signup_email, email)
        self.input_text(self.ui.signup_password, password)
        self.input_text(self.ui.signup_repeat_password, password)
        return self

    def submit_registration(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.ui.register_button)
        ).click()

    def sign_in(self, name, last_name, email, password):
        self.fill_registration_form(name, last_name, email, password).submit_registration()

