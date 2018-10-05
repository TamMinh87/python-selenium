from behave import given, when, then
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_note_page import MyNotePage


@given(u'I load "{site_name}" page')
def load_page(context, site_name):
    if site_name == "Test App":
        HomePage(context.browser).load_page()
        HomePage(context.browser).go_to_login_page()
    #if url == "Another Page":
        #AnotherPage.load_page()


@then(u'I should see "{}" page')
def verify_page(context, page):
    if page == "My Note":
        assert MyNotePage(context.browser).is_my_note_page(), "it is not My Note page"
    #if page == "Another page":
        #assert AnotherPage(context.browser).is_another_page(), "it is not Another page"
    else:
        assert False, "{} page is not match any pre-define page".format(page)
