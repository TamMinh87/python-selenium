from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config.config_parser import config_gui


class LoginForm(BasePage):

    FORM_HEADER = (By.CLASS_NAME, "segment_header")
    PASSWORD_FIELD = (By.ID, "Password")


    def bypass_login_form(self):
        if self.is_element_visible(self.FORM_HEADER):
            self.input_password()

    def input_password(self):
        protected_password = config_gui.get('DEFAULT', 'protected_password')
        self.send_key(self.PASSWORD_FIELD, protected_password + "\n")
