from core.element.element import Element
from selenium.webdriver.common.by import By
from .base_page import BasePage
import pytest
import time
import sys


class BookStorePage(BasePage):
    def __init__(self):
        super().__init__()
        self._login_button = Element((By.ID,'login'))
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
        
    def using_search_book_function(self,book_name):
        self._search_book_text_box.click()
        self._search_book_text_box.enter(book_name)
    
    def verify_book(self,book_name):
        # expected_book_link_xpath = '//a[contains(text(),\'%s\')]' % book_name
        # self.expected_book_locator= Element((By.XPATH, expected_book_link_xpath))
        # a = sys.getsizeof(self.expected_book_locator)
        # actual_book_link_xpath = '//span[contains(@id, "see-book")]'
        # self.actual_book_locator= Element((By.XPATH, actual_book_link_xpath))
        # b = sys.getsizeof(self.actual_book_locator)
        # assert a == b
        
        expected_book_link_xpath = '//a[contains(text(),\'%s\')]' % book_name
        self.expected_book_locator= Element.find_elements((By.XPATH, expected_book_link_xpath))
        a = len(self.expected_book_locator)
        actual_book_link_xpath = '//span[contains(@id, "see-book")]'
        self.actual_book_locator= Element.find_elements((By.XPATH, actual_book_link_xpath))
        b = len(self.actual_book_locator)
        assert a == b