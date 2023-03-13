import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def get_username_field(self):
        return self.driver.find_element(By.ID, "input-username")

    def enter_username(self):
        self.get_username_field().send_keys("my" + datetime.datetime.now().strftime("%H_%M_%S"))

    def get_firstname_field(self):
        return self.driver.find_element(By.ID, "input-firstname")

    def enter_first_name(self):
        return self.get_firstname_field().send_keys("my")

    def get_lastname_field(self):
        return self.driver.find_element(By.ID, "input-lastname")

    def enter_last_name(self):
        return self.get_lastname_field().send_keys(datetime.datetime.now().strftime("name"))

    def get_email_field(self):
        return self.driver.find_element(By.ID, "input-email")

    def enter_random_mail(self):
        random_mail = "vardhinivm" + datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + "@gmail.com"
        return self.get_email_field().send_keys(random_mail)

    def get_country_dropdown(self):
        return self.driver.find_element(By.ID, "input-country")

    def enter_country(self, country):
        dropdown1 = self.get_country_dropdown()
        select = Select(dropdown1)
        select.select_by_visible_text(country)

    def get_password_field(self):
        return self.driver.find_element(By.ID, "input-password")

    def get_register_button(self):
        return self.driver.find_element(By.XPATH, "//button[text()='Register']")

    def get_register_page_title(self):
        return self.driver.title

    def check_account_register_success(self):
        assert self.driver.title.__eq__("OpenCart - Account Register Success")

    def get_continue_button(self):
        return self.driver.find_element(By.LINK_TEXT, "Continue")

    def click_continue_button(self):
        self.get_continue_button().click()


