import datetime
from behave import when, then
from pages.lead_capture_form import LeadCaptureForm
from features.steps.utils import read_test_data


@when(u'I submit all valid information')
def submit_valid_information(context):
    data = read_test_data("lead_capture_data")
    params = data["lead_capture"]
    params["date_of_demo"] = datetime.datetime.now().strftime("%d/%m/%Y")

    before = LeadCaptureForm(context.browser).get_total_records()
    context.records_before_submit = before  # save total records to compare after adding new record

    LeadCaptureForm(context.browser).submit_form(**params)


@when(u'I submit all valid information with date from date picker')
def submit_valid_information_date_picker(context):
    data = read_test_data("lead_capture_data")
    params = data["lead_capture"]

    before = LeadCaptureForm(context.browser).get_total_records()
    context.records_before_submit = before  # save total records to compare after adding new record

    LeadCaptureForm(context.browser).submit_form_date_picker(**params)


@when(u'I submit empty form')
def submit_empty_information(context):
    LeadCaptureForm(context.browser).submit_empty_form()


@then(u'I should see correct information on database level')
def verify_lead_capture_data(context):
    data = read_test_data("lead_capture_data")
    params = data["lead_capture"]
    params["date_of_demo"] = datetime.datetime.now().strftime("%d/%m/%Y")

    records_after_submit = LeadCaptureForm(context.browser).get_total_records()

    LeadCaptureForm(context.browser).verify_total_records(context.records_before_submit, records_after_submit)
    LeadCaptureForm(context.browser).verify_input_data(**params)


@then(u'I should see correct error messages below each required field')
def verify_error_message_display(context):
    LeadCaptureForm(context.browser).verify_error_message_display()
