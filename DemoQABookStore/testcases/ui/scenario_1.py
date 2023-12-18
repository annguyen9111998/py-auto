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
@allure.suite('Test Scenario 1')
class TestScenario1():
    @allure.title("Add book to your collection")
    @pytest.mark.parametrize("account", Account.get_list_account_from_json('resources/test_data/scenario_1.json','valid'))
    @pytest.mark.parametrize("book", Book.get_list_book_from_json('resources/test_data/book.json','valid'))
    def test_add_book_with_ui(self, account, book):    
        Report.report_step('Go to Log in page')
        book_store_page =  BookStorePage()
        book_store_page.go_to_login_page()
        
        Report.report_step('Log in to the application')
        login_page = LoginPage()
        login_page.login(account)
        
        Report.report_step('add book by name')
        book_detail_page = BookDetailPage()
        book_store_page.wait_for_page_load()
        book_store_page.click_book(book.book_name)
        book_detail_page.add_book()
        
        Report.report_step('Go to profile page')
        book_store_page.go_to_profile_page()
        
        Report.report_step('Verify book in page')
        profile_page = ProfilePage()
        assert profile_page.does_book_exist(book.book_name) == True

        Report.report_step('Delete a book to collection with API')
        BookHelper.delete_a_book_from_collection(AccountHelper.get_token(account, True),account.user_id,  book.isbn)