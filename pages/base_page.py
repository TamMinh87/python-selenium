import time
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    PAGE_LOAD_TIMEOUT   = 10
    ELEMENT_TIMEOUT     = 30

    def __init__(self, driver, timeout=ELEMENT_TIMEOUT):
        self.driver = driver
        self.timeout = timeout

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    def get_select(self, locator):
        return Select(self.driver.find_element(*locator))

    def load_website(self, url):
        self.driver.get(url)

    def is_element_visible(self, locator):
        self.driver.implicitly_wait(0)
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except (NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException):
            return False
        finally:
            # set back to where you once belonged
            self.driver.implicitly_wait(self.timeout)

    def wait_for_element_clickable(self, locator):
        """
        Waits for element will be clickable for timings.default

        Args:
            locator: webdriver locator of the element
        """
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator),
            message='Element %s %s is not clickable' % locator)

    def click_on_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.click(element)
        action.perform()

    def click(self, locator):
        self.wait_for_element_clickable(locator)
        element = self.get_element(locator)
        self.click_on_element(element)

    def send_key(self, locator, text):
        element = self.get_element(locator)
        element.send_keys(text)

    def get_text(self, locator):
        return self.get_element(locator).text