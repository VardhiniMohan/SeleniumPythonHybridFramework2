import pytest

from pageobjects.AccountPage import AccountPage
from pageobjects.HomePage import HomePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestPageHeader:
    def test_one(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        assert home_page.get_opencart_logo().is_displayed()
        assert home_page.get_feature_option().is_displayed()
        assert home_page.get_demo_option().is_displayed()
        assert  home_page.get_blog_option().is_displayed()
        assert home_page.get_marketplace_option().is_displayed()
        assert home_page.get_download_option().is_displayed()
        assert home_page.get_resources_developer_option().is_displayed()

    def test_two(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        assert home_page.get_account_option().is_displayed()
        assert home_page.get_logout_option().is_displayed()

    def test_three(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        home_page.click_feature_option()
        home_page.check_feature_page()
        home_page.click_demo_option()
        home_page.check_demo_page()
        home_page.click_blog_option()
        home_page.check_blog_page()
        home_page.click_marketplace_option()
        home_page.check_marketplace_page()
        home_page.click_download_option()
        home_page.check_download_page()
        home_page.click_resources_developer_option()
        home_page.check_resources_developer_page()

    def test_four(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        home_page.click_account_option()
        account_page.check_account_page_title()
        home_page.click_logout_option()
        home_page.check_main_page_title()

    def test_five(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        home_page.check_logo_ui()
        home_page.check_header_ui()
