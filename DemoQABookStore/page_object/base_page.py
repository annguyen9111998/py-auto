from core.element.element import Element
from selenium.webdriver.common.by import By

class BasePage():
    def __init__(self):
        self._username_label = Element((By.ID,'userName-value'))
        self._profile_menu_item = Element((By.XPATH,"//span[.='Profile']"))
    
    def get_username_label_value(self):
        return self._username_label.get_text()
    
    def go_to_profile_page(self):
        self._profile_menu_item.click()
