from behave import given, when, then
from pages.lead_capture_form import LeadCaptureForm
from pages.login_form import LoginForm
from pages.thank_you_page import ThankYouPage


@given(u'I load "{url}"')
def load_page(context, url):
    if url == "Lead Capture Form":
        LeadCaptureForm(context.browser).load_page()
        LoginForm(context.browser).bypass_login_form()
    #if url == "Another Page":
        #AnotherPage.load_page()


@then(u'I should see correct options under "{}"')
def verify_state_dropdown_options(context, dropdown):
    if dropdown == "State dropdown":
        LeadCaptureForm(context.browser).verify_state_dropdown_options()
    #if dropdown == "Another dropdown":
        #AnotherPage(context.browser).verify_state_dropdown_options()

@then(u'I should see "{}" page')
def verify_page(context, page):
    if page == "Thank you":
        assert ThankYouPage(context.browser).is_thank_you_page(), "it is not Thank you page"
    #if page == "Another page":
        #assert AnotherPage(context.browser).is_another_page(), "it is not Another page"
    else:
        assert False, "{} page is not match any pre-define page".format(page)