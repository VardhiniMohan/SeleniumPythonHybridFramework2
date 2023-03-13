import pytest

from pageobjects.AccountPage import AccountPage
from pageobjects.HomePage import HomePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestContentSection:
    def test_one(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        home_page.check_content_section_ui()

    def test_two(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        home_page.check_resize_of_content_section()

    def test_three(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        assert home_page.get_section_two().is_displayed()
        home_page.click_british_red_cross_logo()
        home_page.check_british_red_cross_website()
        home_page.click_penn_logo()
        home_page.check_penn_website()
        home_page.click_concordia_college_logo()
        home_page.check_concordia_college_website()
        home_page.click_fx_creations_logo()
        home_page.check_fx_creations_website()
        home_page.click_hku_logo()
        home_page.check_hku_website()

    def test_four(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        assert home_page.get_section_three().is_displayed()
        home_page.click_visit_marketplace_option()
        home_page.check_marketplace_page()

    def test_five(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        assert home_page.get_section_four().is_displayed()
        home_page.click_visit_all_option()

    def test_six(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        assert home_page.get_section_five().is_displayed()
        home_page.check_section_five_ui()

    def test_seven(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        assert home_page.get_section_six().is_displayed()
        home_page.click_community_support_learn_more_option()
        home_page.check_community_forum_page()
        home_page.click_dedicated_support_learn_more_option()
        home_page.check_dedicated_support_page()

    def test_eight(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        assert home_page.get_section_seven().is_displayed()
        home_page.click_forbes_logo()
        home_page.check_forbes_page()
        home_page.click_paypal_logo()
        home_page.check_paypal_page()
        home_page.click_bbc_logo()
        home_page.check_bbc_page()
        home_page.click_south_china_morning_post_logo()
        home_page.check_south_china_morning_post_page()









