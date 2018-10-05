from behave import when, then
from pages.my_note_page import MyNotePage


@when(u'I add note')
def add_note(context):
    MyNotePage(context.browser).add_note()


@then(u'I should see a note')
def verify_note(context):
    MyNotePage(context.browser).verify_note()
