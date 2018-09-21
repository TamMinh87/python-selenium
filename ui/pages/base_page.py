import time

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, TimeoutException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
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
        #self.wait_for_element_visible(*locator)
        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        #self.wait_for_element_visible(*locator)
        return self.driver.find_elements(*locator)

    def get_select(self, locator):
        #self.wait_for_element_visible(*locator)
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

    def wait_for_element_visible(self, locator):
        """
        Waits for element will be visible for timings.default

        Args:
            locator: webdriver locator of the element
        """
        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator),
            message='Element %s %s either is not present or invisible' % locator)

    def wait_for_element_clickable(self, locator):
        """
        Waits for element will be clickable for timings.default

        Args:
            locator: webdriver locator of the element
        """
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator),
            message='Element %s %s is not clickable' % locator)

    def wait_ajax(self):
        """Awaiting ajax"""
        while self.driver.execute_script("return jQuery.active") != 0:
            time.sleep(0.5)

    def wait_load(self):
        """Wait for load ending"""
        wait = WebDriverWait(self.driver, self.PAGE_LOAD_TIMEOUT)
        if EC.visibility_of((By.XPATH, '//*[@class="i-loader"]')):
            wait.until(EC.invisibility_of_element_located((By.XPATH, '//*[@class="i-loader"]')))

    def wait_for_page_load_complete(self):
        WebDriverWait(self.driver, self.timeout).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete')

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
        """
        Send keys to the input

        Args:
            locator: webdriver locator of the element
            text: text to set
        """
        element = self.get_element(locator)
        element.send_keys(text)

    def select_by_index(self, locator, index):
        index = int(index)

        select = Select(self.driver.find_element(*locator))

        select.select_by_index(index)

        return select

    def select_by_text(self, locator, text):
        select = Select(self.driver.find_element(*locator))

        select.select_by_visible_text(text)

        return select

    def select_last_index(self, locator):
        select = Select(self.driver.find_element(*locator))

        select.select_by_index(len(select.options)-1)

        return select
