
from core.element.element import Element
from selenium.webdriver.common.by import By
from core.driver.driver_utils import DriverUtils
from .base_page import BasePage

class BookDetailPage(BasePage):
    def __init__(self):
        super().__init__()
        self._add_book_locator = Element((By.XPATH,'//button[@id="addNewRecordButton" and (text() = "Add To Your Collection")]'))
    
    def add_book(self):
        self._add_book_locator.click()
        DriverUtils.accept_alert()
    
    def verify_js_alert(self,alert_message):
        actual_message = DriverUtils.get_alert_text()
        assert alert_message == actual_message

    