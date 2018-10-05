from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config.config_parser import config_gui


class MyNotePage(BasePage):

    open_add_note_button    = (By.CSS_SELECTOR, "div#my-notes-page > button.btn.btn-lg.btn-primary")
    note_content            = (By.CSS_SELECTOR, "div#my-notes-page > div.list-group")

    note_title          = (By.CSS_SELECTOR, "div#ad-note-page > p > input[name='note.title']")
    note_description    = (By.CSS_SELECTOR, "div#ad-note-page > p > textarea[name='note.description']")
    add_note_button     = (By.CSS_SELECTOR, "div#ad-note-page > p > button.btn.btn-lg.btn-primary")


    def is_my_note_page(self):
        return self.is_element_visible(self.open_add_note_button)

    def add_note(self):
        title = config_gui.get('DEFAULT', 'title')
        description = config_gui.get('DEFAULT', 'description')

        self.click(self.open_add_note_button)
        self.send_key(self.note_title, title)
        self.send_key(self.note_description, description)
        self.click(self.add_note_button)

    def verify_note(self):
        node_content = self.get_text(self.note_content)
        title = config_gui.get('DEFAULT', 'title')

        assert title in node_content, "{0} note is not found".format(title)
