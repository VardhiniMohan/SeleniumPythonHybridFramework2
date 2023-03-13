import datetime
import time

import pytest

from pageobjects.AccountPage import AccountPage
from pageobjects.HomePage import HomePage
from pageobjects.LoginPage import LoginPage
from pageobjects.RegisterPage import RegisterPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestingTwo:
    def test_one(self):
        home_page = HomePage(self.driver)
        home_page.get_website()
        home_page.click_register_button()
        register_page = RegisterPage(self.driver)
        register_page.enter_username()
        register_page.enter_first_name()
        register_page.enter_last_name()
        register_page.enter_random_mail()
        register_page.enter_country("India")
        time.sleep(10)
        register_page.get_password_field().send_keys("12345")
        register_page.get_register_button().click()
        register_page.check_account_register_success()

    def test_two(self):
        home_page = HomePage(self.driver)
        home_page.get_website()
        home_page.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.enter_login_fields("vardhinivm11@gmail.com", "12345", "2491")
        account_page = AccountPage(self.driver)
        account_page.click_main_logo()
        home_page.check_main_page_title()

    def test_three(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        home_page.click_feature_option()
        home_page.get_opencart_logo_from_feature_page().click()
        home_page.click_demo_option()
        home_page.get_opencart_logo_from_demo_page().click()
        home_page.click_marketplace_option()
        home_page.get_opencart_logo_from_marketplace_page().click()
        home_page.click_blog_option()
        home_page.get_opencart_logo_from_blog_page().click()
        home_page.click_download_option()
        home_page.get_opencart_logo_from_download_page().click()

    def test_four(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        home_page.check_main_page_title()
        home_page.check_main_page_url()

    def test_five(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        home_page.check_main_page_title()
        home_page.get_opencart_logo().click()
        home_page.check_main_page_title()










