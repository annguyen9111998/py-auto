from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

class BasePage():
    def __init__(self):
        self._username_label = driver.find_element((By.ID,'userName-value'))
        self._profile_menu_item = driver.find_element((By.XPATH,"//span[.='Profile']"))
    
    def go_to_profile_page(self):
        self._profile_menu_item.click()
