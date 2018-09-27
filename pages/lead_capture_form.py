from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config.config_parser import config_gui
from api.formsite_api import get_result, get_results_count
from features.steps.utils import read_test_data


class LeadCaptureForm(BasePage):

    first_name              = (By.ID, "RESULT_TextField-1")
    last_name               = (By.ID, "RESULT_TextField-2")
    street_address          = (By.ID, "RESULT_TextField-3")
    city                    = (By.ID, "RESULT_TextField-5")
    state_dropdown          = (By.ID, "RESULT_RadioButton-6")
    zip_code                = (By.ID, "RESULT_TextField-7")
    email_address           = (By.ID, "RESULT_TextField-9")
    date_of_demo            = (By.ID, "RESULT_TextField-10")
    submit_button           = (By.ID, "FSsubmit")
    date_picker_button      = (By.CSS_SELECTOR, "img.svg.popup_button.inline_button")
    date_picker_today       = (By.CSS_SELECTOR, "a.ui-state-default.ui-state-highlight")

    first_name_error        = (By.CSS_SELECTOR, "#q17 > div.invalid_message")
    last_name_error         = (By.CSS_SELECTOR, "#q18 > div.invalid_message")
    street_address_error    = (By.CSS_SELECTOR, "#q19 > div.invalid_message")
    city_error              = (By.CSS_SELECTOR, "#q21 > div.invalid_message")
    state_dropdown_error    = (By.CSS_SELECTOR, "#q22 > div.invalid_message")
    zip_code_error          = (By.CSS_SELECTOR, "#q23 > div.invalid_message")
    email_address_error     = (By.CSS_SELECTOR, "#q25 > div.invalid_message")
    date_of_demo_error      = (By.CSS_SELECTOR, "#q27 > div.invalid_message")

    def is_lead_capture_form(self):
        return self.is_element_visible(self.first_name)

    def load_page(self):
        url = config_gui.get('DEFAULT', 'lead_capture_form_url')
        self.load_website(url)

    def select_date_from_date_picker(self):
        self.click(self.date_picker_button)
        self.click(self.date_picker_today)

    def submit_form(self, **kwargs):
        self.send_key(self.first_name, kwargs.get("first_name"))
        self.send_key(self.last_name, kwargs.get("last_name"))
        self.send_key(self.street_address, kwargs.get("street_address"))
        self.send_key(self.city, kwargs.get("city"))
        self.select_by_text(self.state_dropdown, kwargs.get("state"))
        self.send_key(self.zip_code, kwargs.get("zip_code"))
        self.send_key(self.email_address, kwargs.get("email_address"))
        self.send_key(self.date_of_demo, kwargs.get("date_of_demo"))
        self.click(self.submit_button)

    def submit_form_date_picker(self, **kwargs):
        self.send_key(self.first_name, kwargs.get("first_name"))
        self.send_key(self.last_name, kwargs.get("last_name"))
        self.send_key(self.street_address, kwargs.get("street_address"))
        self.send_key(self.city, kwargs.get("city"))
        self.select_by_text(self.state_dropdown, kwargs.get("state"))
        self.send_key(self.zip_code, kwargs.get("zip_code"))
        self.send_key(self.email_address, kwargs.get("email_address"))
        self.select_date_from_date_picker()
        self.click(self.submit_button)


    def submit_empty_form(self):
        self.click(self.submit_button)

    def get_total_records(self):
        return get_results_count()

    def verify_total_records(self, before, after):
        assert before == after - 1, "before: {} - after: {}".format(before, after)

    def verify_input_data(self, **kwargs):
        response = get_result()
        first_name      = response['fs_response']['results']['result']['items']['item'][0]['value']['$']
        last_name       = response['fs_response']['results']['result']['items']['item'][1]['value']['$']
        street_address  = response['fs_response']['results']['result']['items']['item'][2]['value']['$']
        city            = response['fs_response']['results']['result']['items']['item'][3]['value']['$']
        state           = response['fs_response']['results']['result']['items']['item'][4]['value']['$']
        zip_code        = response['fs_response']['results']['result']['items']['item'][5]['value']['$']
        email_address   = response['fs_response']['results']['result']['items']['item'][6]['value']['$']
        date_of_demo    = response['fs_response']['results']['result']['items']['item'][7]['value']['$']

        result = True
        error_messsage = ""

        # normal assertion
        assert first_name == kwargs.get("first_name"), "first_name is not correct"
        assert last_name == kwargs.get("last_name"), "last_name is not correct"
        assert street_address == kwargs.get("street_address"), "street_address is not correct"
        assert city == kwargs.get("city"), "city is not correct"
        assert state == kwargs.get("state"), "state is not correct"
        assert str(zip_code) == kwargs.get("zip_code"), "zip_code is not correct"
        assert email_address == kwargs.get("email_address"), "email_address is not correct"
        assert date_of_demo == kwargs.get("date_of_demo"), "date_of_demo is not correct"

        # or use soft-assertion as below
        if first_name != kwargs.get("first_name"):
            result = False
            error_messsage += "first_name is not correct\t"
        if last_name != kwargs.get("last_name"):
            result = False
            error_messsage += "last_name is not correct\t"
        if street_address != kwargs.get("street_address"):
            result = False
            error_messsage += "street_address is not correct\t"
        if city != kwargs.get("city"):
            result = False
            error_messsage += "city is not correct\t"
        if state != kwargs.get("state"):
            result = False
            error_messsage += "state is not correct\t"
        if str(zip_code) != kwargs.get("zip_code"):
            result = False
            error_messsage += "zip_code is not correct\t"
        if email_address != kwargs.get("email_address"):
            result = False
            error_messsage += "email_address is not correct\t"
        if date_of_demo != kwargs.get("date_of_demo"):
            result = False
            error_messsage += "date_of_demo is not correct\t"

        assert result is True, error_messsage

    def verify_error_message_display(self):
        assert self.is_element_visible(self.first_name_error)
        assert self.is_element_visible(self.last_name_error)
        assert self.is_element_visible(self.street_address_error)
        assert self.is_element_visible(self.city_error)
        assert self.is_element_visible(self.state_dropdown_error)
        assert self.is_element_visible(self.zip_code_error)
        assert self.is_element_visible(self.email_address_error)
        assert self.is_element_visible(self.date_of_demo_error)

    def verify_state_dropdown_options(self):
        actual_options = self.get_select_options(self.state_dropdown)
        expected_options = read_test_data("lead_capture_data")["state_options"]

        assert actual_options == expected_options, \
            "actual options {} \n expected option {}".format(actual_options, expected_options)
