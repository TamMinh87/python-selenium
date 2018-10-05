from behave import when, then
from pages.login_page import LoginPage


@when(u'I submit valid credentials')
def submit_valid_credentials(context):
    LoginPage(context.browser).login()
