from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from .base_page import BasePage
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

class BookStorePage(BasePage):
    def __init__(self):
        super().__init__()
        self._login_button = driver.find_element((By.ID,'login'))
        
    def go_to_login_page(self):
        self._login_button.click()