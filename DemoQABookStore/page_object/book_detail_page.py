from core.element.element import Element
from selenium.webdriver.common.by import By
from core.driver.driver_utils import DriverUtils
from .base_page import BasePage

class BookDetailPage(BasePage):
    def __init__(self):
        super().__init__()
        self._add_book_locator = Element((By.ID,'addNewRecordButton'))
        self._ok_button = Element((By.ID,'closeSmallModal-ok'))
    
    def add_book(self):
        self._add_book_locator.click()
        self._ok_button.click()
        DriverUtils.accept_alert()

    