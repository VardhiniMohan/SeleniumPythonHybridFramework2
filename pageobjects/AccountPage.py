from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobjects.HomePage import HomePage
from pageobjects.LoginPage import LoginPage


class AccountPage:
    def __init__(self,driver):
        self.driver=driver

    def check_account_page_title(self):
        return self.driver.title.__eq__("OpenCart - Your Account")

    def get_main_logo(self):
        return self.driver.find_element(By.XPATH,"//img[@title='OpenCart - Your Account']")

    def click_main_logo(self):
        self.get_main_logo().click()

    def successful_login(self):
        home_page = HomePage(self.driver)
        home_page.get_website()
        home_page.click_login_button()
        login_page = LoginPage(self.driver)
        login_page.enter_login_fields("vardhinivm11@gmail.com", "12345", "2491")
        self.click_main_logo()
        home_page.check_main_page_title()

