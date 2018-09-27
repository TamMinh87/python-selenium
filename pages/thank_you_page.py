from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ThankYouPage(BasePage):

    success_title = (By.CLASS_NAME, "success-title")

    def is_thank_you_page(self):
        return self.is_element_visible(self.success_title)
