from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def get_login_page_title(self):
        return self.driver.title

    def get_email_field(self):
        return self.driver.find_element(By.ID,"input-email")

    def get_password_field(self):
        return self.driver.find_element(By.ID,"input-password")

    def get_login_button(self):
        return self.driver.find_element(By.XPATH,"//button[text()='Login']")

    def get_send_keys_field(self):
        return self.driver.find_element(By.ID,"input-pin")

    def get_continue_button(self):
        return self.driver.find_element(By.XPATH,"//button[text()='Continue']")

    def enter_login_fields(self,email,password,keys):
        self.get_email_field().send_keys(email)
        self.get_password_field().send_keys(password)
        self.get_login_button().click()
        self.get_send_keys_field().send_keys(keys)
        self.get_continue_button().click()


