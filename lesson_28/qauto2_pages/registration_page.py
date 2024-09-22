from lesson_28.qauto2_pages.base_page import BasePage
from lesson_28.qauto2_pages.ui_elements import UIElements
import allure


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super(RegistrationPage, self).__init__(driver)
        self.ui = UIElements()

    @allure.step('Opening registration page')
    def open_registration_form(self):
        self.click_element(self.ui.signup_button)

    @allure.step('Filling registration form')
    def fill_registration_form(self, name, last_name, email, password):
        self.input_text(self.ui.signup_name, name)
        self.input_text(self.ui.signup_last_name, last_name)
        self.input_text(self.ui.signup_email, email)
        self.input_text(self.ui.signup_password, password)
        self.input_text(self.ui.signup_repeat_password, password)
        return self

    @allure.step('Submit registration')
    def submit_registration(self):
        self.click_element(self.ui.register_button)

    @allure.step('Sign in with email {email}')
    def sign_in(self, name, last_name, email, password):
        self.fill_registration_form(name, last_name, email, password).submit_registration()

