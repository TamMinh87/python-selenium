from behave import given, when, then
from ui.pages.lead_capture_form import LeadCaptureForm
from ui.pages.login_form import LoginForm


@given(u'I load "{url}"')
def load_page(context, url):
    if url == "Lead Capture Form":
        LeadCaptureForm(context.browser).load_page()
        LoginForm(context.browser).bypass_login_form()


@when(u'I fill all valid information')
def submit_valid_information(context):
    params = {
        "first_name": "Tamaaaaaaabc",
        "last_name": "Test",
        "street_address": "Test",
        "city": "Test",
        "state": "Alaska",
        "zip_code": "70000",
        "email_address": "Test@gmail.com",
        "date_of_demo": "21/09/2018",
    }

    LeadCaptureForm(context.browser).submit_form(**params)


@then(u'I should see correct information on database level')
def verify_lead_capture_data(context):
    params = {
        "first_name": "Tamaaaaaaabc",
        "last_name": "Test",
        "street_address": "Test",
        "city": "Test",
        "state": "Alaska",
        "zip_code": "70000",
        "email_address": "Test@gmail.com",
        "date_of_demo": "21/09/2018",
    }

    #LeadCaptureForm(context.browser).verify_total_records()
    LeadCaptureForm(context.browser).verify_input_data(**params)







