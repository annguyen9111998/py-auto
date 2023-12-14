import pytest
from data_object.account import Account
from data_object.book import Book
from page_object.book_store_page import BookStorePage
from page_object.login_page import LoginPage
from page_object.profile_page import ProfilePage
from page_object.book_detail_page import BookDetailPage
from helper.api.book_helper import BookHelper
from helper.api.account_helper import AccountHelper
from core.report.allure_report import Report
from core.driver.driver_utils import DriverUtils
import allure

@allure.parent_suite('UI Test')
@allure.suite('Test Scenario 2')
class TestScenario1():
    @allure.title("Search book with multiple result")
    @pytest.mark.parametrize("account", Account.get_list_account_from_json('resources/test_data/scenario_2.json','valid'))
    @pytest.mark.parametrize("book", Book.get_list_book_from_json('resources/test_data/book_scenario_2.json','valid'))
    def test_search_book_with_ui(self, account, book):    
        Report.report_step('Go to Log in page')
        book_store_page =  BookStorePage()
        # book_store_page.go_to_login_page()
        
        # Report.report_step('Log in to the application')
        # login_page = LoginPage()
        # login_page.login(account)
        
        # Report.report_step('using search function')
        # book_store_page.wait_for_page_load()
        book_store_page.using_search_book_function(book.book_name)
        book_store_page.verify_book(book.book_name)
