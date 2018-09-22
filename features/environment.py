import allure
from allure_commons.types import AttachmentType
from behave import fixture, use_fixture
from selenium import webdriver
from config.config_parser import config_gui


# TODO: singleton

@fixture
def selenium_browser(context):
    if context.browser_name == 'chrome':
        context.browser = webdriver.Chrome()
    elif context.browser_name == 'firefox':
        context.browser = webdriver.Firefox()

    yield context.browser

    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


def before_all(context):
    context.browser_name = config_gui.get('DEFAULT', 'browser') \
        if 'browser' not in context.config.userdata.keys() \
        else context.config.userdata['browser']

    # You’ll have noticed the “context” variable that’s passed around.
    # It’s a clever place where you and behave can store information to share around.
    # It runs at three levels, automatically managed by behave.

    use_fixture(selenium_browser, context)

    # -- HINT: CLEANUP-FIXTURE is performed after after_all() hook is called.


def after_step(context, step):
    #if step.status == "failed":
    try:
        screen_path = 'screenshots/{}.png'.format(step.name)
        context.browser.save_screenshot(screen_path)
        allure.attach(context.browser.get_screenshot_as_png(), name=screen_path, attachment_type=AttachmentType.PNG)
    except Exception:
        raise Exception("error when taking screenshot")
