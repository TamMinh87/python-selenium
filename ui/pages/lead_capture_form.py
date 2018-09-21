from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config.config_parser import config_gui
from api.formsite_api import get_result, get_results_count


class LeadCaptureForm(BasePage):

    FIRST_NAME      = (By.ID, "RESULT_TextField-1")
    LAST_NAME       = (By.ID, "RESULT_TextField-2")
    STREET_ADDRESS  = (By.ID, "RESULT_TextField-3")
    CITY            = (By.ID, "RESULT_TextField-5")
    STATE_DROPDOWN  = (By.ID, "RESULT_RadioButton-6")
    ZIP_CODE        = (By.ID, "RESULT_TextField-7")
    EMAIL_ADDRESS   = (By.ID, "RESULT_TextField-9")
    DATE_OF_DEMO    = (By.ID, "RESULT_TextField-10")
    SUBMIT_BUTTON   = (By.ID, "FSsubmit")

    def is_capture_lead_form(self):
        return self.is_element_visible(self.FIRST_NAME)

    def load_page(self):
        url = config_gui.get('DEFAULT', 'capture_lead_form_url')
        self.load_website(url)

    def submit_form(self, **kwargs):
        self.send_key(self.FIRST_NAME, kwargs.get("first_name"))
        self.send_key(self.LAST_NAME, kwargs.get("last_name"))
        self.send_key(self.STREET_ADDRESS, kwargs.get("street_address"))
        self.send_key(self.CITY, kwargs.get("city"))
        self.select_by_text(self.STATE_DROPDOWN, kwargs.get("state"))
        self.send_key(self.ZIP_CODE, kwargs.get("zip_code"))
        self.send_key(self.EMAIL_ADDRESS, kwargs.get("email_address"))
        self.send_key(self.DATE_OF_DEMO, kwargs.get("date_of_demo"))

        records_before = get_results_count()['fs_response']['count']['$']
        self.click(self.SUBMIT_BUTTON)
        records_after = get_results_count()['fs_response']['count']['$']
        assert records_before == records_after - 1, \
            "Total results before submitting is {} and after is {}".format(records_before, records_after)

    #def verify_total_records(self):


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
        if zip_code != kwargs.get("zip_code"):
            result = False
            error_messsage += "zip_code is not correct\t"
        if email_address != kwargs.get("email_address"):
            result = False
            error_messsage += "email_address is not correct\t"
        if date_of_demo != kwargs.get("date_of_demo"):
            result = False
            error_messsage += "date_of_demo is not correct\t"

        assert result == True, error_messsage
