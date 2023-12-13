from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from .base_page import BasePage
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self._login_button = driver.find_element((By.ID,'login'))
        self._username_textbox = driver.find_element((By.ID,'userName'))
        self._password_textbox = driver.find_element((By.ID, 'password'))
        self._error_message = driver.find_element((By.ID, 'name'))
    
    def navigateToSite(self):
        driver.get("https://demoqa.com/login")
        
    def login(self):
        self._username_textbox.send_keys("annguyen911")
        self._password_textbox.send_keys("Bench@123")
        self._login_button.click()