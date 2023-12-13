import pytest
import time 
from page.book_store_page import BookStorePage
from page.login_page import LoginPage
from page.profile_page import ProfilePage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

class Scenario1():
    def test_scenario_1(self):
        # book_store_page = BookStorePage()
        # login_page = LoginPage()
        # profile_page = ProfilePage()
        
        # login_page.navigateToSite()
        # login_page.login()
        driver.get("https://demoqa.com/login")