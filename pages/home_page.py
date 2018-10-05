from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config.config_parser import config_gui


class HomePage(BasePage):

    login_button = (By.CSS_SELECTOR, "button.btn-lg.btn-primary.button-login")

    def load_page(self):
        url = config_gui.get('DEFAULT', 'test_app_url')
        self.load_website(url)

    def go_to_login_page(self):
        self.click(self.login_button)
