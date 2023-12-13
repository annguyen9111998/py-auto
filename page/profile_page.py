from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from .base_page import BasePage
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

class ProfilePage(BasePage):
    def __init__(self):
        super().__init__()
        self.ok_button = driver.find_element((By.ID,'closeSmallModal-ok'))