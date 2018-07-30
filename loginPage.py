from selenium import webdriver
import unittest
import time

# logs into the website

class Login(unittest.TestCase):

    admin_username = 'testone@records.nyc.gov'
    admin_password = 'change4doris'

    user_username = 'testthree@records.nyc.gov'
    user_password = 'change4doris'

    
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def login(self, user_type):
        if user_type == 'admin':
            self.driver.find_element_by_link_text('Log In').click()
            time.sleep(.25)
            self.driver.find_element_by_id("employeeForm").submit()
            time.sleep(.25)
            self.driver.find_element_by_id("Ecom_User_ID").send_keys(self.admin_username)
            time.sleep(.25)
            self.driver.find_element_by_id("Ecom_Password").send_keys(self.admin_password)
            time.sleep(.25)
            form = self.driver.find_element_by_name("IDPLogin")
            time.sleep(.25)
            form.submit()
        
        elif user_type == 'user':
            self.driver.find_element_by_link_text('Log In').click()
            time.sleep(.25)
            self.driver.find_element_by_id("employeeForm").submit()
            time.sleep(.25)
            self.driver.find_element_by_id("Ecom_User_ID").send_keys(self.user_username)
            time.sleep(.25)
            self.driver.find_element_by_id("Ecom_Password").send_keys(self.user_password)
            time.sleep(.25)
            form = self.driver.find_element_by_name("IDPLogin")
            time.sleep(.25)
            form.submit()