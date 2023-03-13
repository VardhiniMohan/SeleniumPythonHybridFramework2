import time
import pytest
from selenium.webdriver.common.by import By

from pageobjects.AccountPage import AccountPage
from pageobjects.HomePage import HomePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestHeroSection:
    def test_one(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        home_page.check_hero_section_image()

    def test_two(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        home_page.check_hero_section_ui()

    def test_three(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        home_page.check_resize_of_image_hero_section()

    def test_four(self):
        home_page = HomePage(self.driver)
        account_page = AccountPage(self.driver)
        account_page.successful_login()
        home_page.click_free_download_option()
        home_page.check_download_page()
        home_page.get_previous_page()
        home_page.click_view_demo_option()
        home_page.check_demo_page()

  

