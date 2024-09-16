from selenium.webdriver.common.by import By


class UIElements:
    def __init__(self):
        self.signup_button = (By.XPATH, "//button[@class='hero-descriptor_btn btn btn-primary']")
        self.signup_name = (By.ID, "signupName")
        self.signup_last_name = (By.ID, "signupLastName")
        self.signup_email = (By.ID, "signupEmail")
        self.signup_password = (By.ID, "signupPassword")
        self.signup_repeat_password = (By.ID, "signupRepeatPassword")
        self.register_button = (By.XPATH, "//button[@class='btn btn-primary']")
        self.after_register_msg = (By.CLASS_NAME, "panel-empty_message")

