from behave import fixture, use_fixture, configuration
from selenium import webdriver
from config.config_parser import config_api, config_gui


@fixture
def selenium_browser(context):
    # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
    #if context.config.userdata['browser'].lower() == 'chrome':
    #    context.browser = webdriver.Chrome()

    if context.browser_name == 'chrome':
        context.browser = webdriver.Chrome()
    elif context.browser_name == 'firefox':
        context.browser = webdriver.Firefox()

    yield context.browser

    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


def before_all(context):

    context.browser_name = config_gui.get('DEFAULT', 'browser') if 'browser' not in context.config.userdata.keys() else context.config.userdata['browser']

    context.test = config_api.get('DEFAULT', 'test')

    # You’ll have noticed the “context” variable that’s passed around.
    # It’s a clever place where you and behave can store information to share around.
    # It runs at three levels, automatically managed by behave.

    use_fixture(selenium_browser, context)

    # -- HINT: CLEANUP-FIXTURE is performed after after_all() hook is called.
