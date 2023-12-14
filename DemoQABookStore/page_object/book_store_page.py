from core.element.element import Element
from selenium.webdriver.common.by import By
from .base_page import BasePage

class BookStorePage(BasePage):
    def __init__(self):
        super().__init__()
        self._login_button = Element((By.ID,'login'))
        self._add_book_locator = Element((By.ID,'addNewRecordButton'))
        self._ok_button = Element((By.ID,'closeSmallModal-ok'))
        self._search_book_text_box = Element((By.ID,'searchBox'))
    
    def book_link(self, book_name):
        book_link_xpath = '//a[.=\'%s\']' % book_name
        return Element((By.XPATH, book_link_xpath))
    
    def click_book(self, book_name):
        book_link_xpath = '//a[.=\'%s\']' % book_name
        self.book_locator= Element((By.XPATH, book_link_xpath))
        self.book_locator.click()
    
    def go_to_login_page(self):
        self._login_button.click()
    
    def wait_for_page_load(self):
        self._username_label.wait_for_visibility()
    
    def add_book(self):
        self._add_book_locator.click()
        self._ok_button.click()
    
    def using_search_book_function(self,book_name):
        self._search_book_text_box.click()
        self._search_book_text_box.enter(book_name)
    
    def verify_book(self,book_name):
        book_link_xpath = '//a[.=\'%s\']' % book_name
        self.book_locator= Element((By.XPATH, book_link_xpath))
        a =self.book_locator.get_attribute('id')
        b =self.book_locator.wait_for_text_contains(book_name)
        assert a == b