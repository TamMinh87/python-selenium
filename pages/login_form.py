from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config.config_parser import config_gui


class LoginForm(BasePage):

    form_header = (By.CLASS_NAME, "segment_header")
    password_field = (By.ID, "Password")


    def bypass_login_form(self):
        if self.is_element_visible(self.form_header):
            self.input_password()

    def input_password(self):
        protected_password = config_gui.get('DEFAULT', 'protected_password')
        self.send_key(self.password_field, protected_password + "\n")
