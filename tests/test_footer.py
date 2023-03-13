import pytest

from pageobjects.AccountPage import AccountPage
from pageobjects.HomePage import HomePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestFooter:
    def test_one(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        home_page.check_opencart_in_footer_options()
        home_page.click_feature_under_opencart()
        home_page.check_feature_page()
        home_page.click_showcase_under_opencart()
        home_page.check_resource_showcase_page()
        home_page.click_demo_under_opencart()
        home_page.check_demo_page()
        home_page.click_download_under_opencart()
        home_page.check_download_page()
        home_page.click_marketplace_under_opencart()
        home_page.check_marketplace_page()
        home_page.click_login_under_opencart()
        account_page.check_account_page_title()

    def test_two(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        assert home_page.get_company_in_footer_options().is_displayed()
        home_page.click_contact_us_under_company()
        home_page.check_contact_page()
        home_page.click_extension_advertising_under_company()
        home_page.check_advertising_page()
        home_page.click_marketplace_advertising_under_company()
        home_page.check_advertising_page()
        home_page.click_about_us_under_company()
        home_page.check_company_page()
        home_page.click_terms_and_conditions_under_company()
        home_page.check_policy_page()
        home_page.click_extension_developer_under_company()
        home_page.check_extension_developer_page()

    def test_three(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        assert home_page.get_support_in_footer_options().is_displayed()
        home_page.click_community_forum_under_support()
        home_page.check_community_forum_page()
        home_page.click_dedicated_support_under_support()
        home_page.check_support_page()
        home_page.click_opencart_partners_under_support()
        home_page.check_resources_partners_page()
        home_page.click_marketplace_support_under_support()
        home_page.check_support_page()
        home_page.click_migrate_to_opencart_under_support()
        home_page.check_migrate_to_opencart_page()

    def test_four(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        assert home_page.get_resources_in_footer_options().is_displayed()
        home_page.click_opencart_blog_under_resources()
        home_page.check_blog_page()
        home_page.click_opencart_documentation_under_resources()
        home_page.check_resource_documentation_page()
        home_page.click_opencart_books_under_resources()
        home_page.check_resource_books_page()
        home_page.click_github_bug_tracker_under_resources()
        home_page.check_resources_github_bug_tracker_page()
        home_page.click_developer_under_resources()
        home_page.check_resources_developer_page()

    def test_five(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        assert home_page.get_newsletter_in_footer_options().is_displayed()
        home_page.check_newsletter_under_newsletter()
        home_page.check_placeholder_under_newsletter()

    def test_six(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        assert home_page.get_social_section_under_newsletter().is_displayed()
        home_page.click_facebook_marketing_partner_logo()
        home_page.check_meta_partners_page()
        home_page.click_linkedin_logo()
        home_page.check_linkedin_page()
        home_page.click_facebook_logo()
        home_page.check_facebook_page()
        home_page.click_twitter_logo()
        home_page.check_twitter_page()

    def test_seven(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        home_page.enter_email_in_newsletter_field("vardhinivm11@gmail.com")
        home_page.click_on_arrow_after_email()
        assert home_page.get_sign_up_newsletter_form().is_displayed()

    def test_eight(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        home_page.check_footer_ui()






