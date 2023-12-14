import pytest
import time 
from core.element.element import Element
from page_object.book_store_page import BookStorePage
from page_object.login_page import LoginPage
from data_object.account import Account
import allure

@allure.parent_suite('UI Test')
@allure.suite('Test Login')
class TestLogin():
    
    @allure.title("Test login with a valid account")
    @pytest.mark.smoke
    @pytest.mark.parametrize("account", Account.get_list_account_from_json('resources/test_data/account.json','valid'))
    def test_login_successfully_with_valid_account(self, account):
        book_store_page =  BookStorePage()
        book_store_page.go_to_login_page()

        login_page = LoginPage()
        login_page.login(account)
        
        header_text = book_store_page.get_username_label_value()
        assert header_text == account.username
    
    @allure.title("Test login with invalid accounts")
    @pytest.mark.parametrize("account",  Account.get_list_account_from_json('resources/test_data/account.json','invalid'))
    def test_login_unsuccessfully_with_valid_account(self, account):
        book_store_page =  BookStorePage()
        book_store_page.go_to_login_page()

        login_page = LoginPage()
        login_page.login(account)

        error_message = login_page.get_error_message()
        assert error_message == 'Invalid username or password!'
