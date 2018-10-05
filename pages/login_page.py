from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config.config_parser import config_gui


class LoginPage(BasePage):

    login_button    = (By.CSS_SELECTOR, "button.btn-lg.btn-primary.button-login")
    username        = (By.CSS_SELECTOR, "div#login-page > p > input[name='login.username']")
    password        = (By.CSS_SELECTOR, "div#login-page > p > input[name='login.password']")

    def login(self):
        username = config_gui.get('DEFAULT', 'username')
        password = config_gui.get('DEFAULT', 'password')

        self.send_key(self.username, username)
        self.send_key(self.password, password)
        self.click(self.login_button)
