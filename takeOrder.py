from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest
import time

class takeOrder(unittest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    #approves the topmost order not yet accepted, and the first accepted one if all orders have been accepted
    def order_approve(self, user_type):
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/header/div/nav/div/ul/li/a').click()
        self.driver.find_element_by_xpath('/html/body/header/div/nav/div/ul/li/ul/li[1]/a').click()
        try:
            self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[2]/table[2]/tbody/tr[2]/td[5]/form/input[4]').click()
            self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/form/div[1]/span[1]/input').click()
        except NoSuchElementException:
            self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[2]/table/tbody/tr[2]/td[5]/form/input[4]').click()
            self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/form/div[1]/span[1]/input').click()

    #rejects the topmost order not yet accepted, and the first accepted one if all orders have been accepted
    def order_reject(self, user_type):
        self.driver.find_element_by_xpath('/html/body/header/div/nav/div/ul/li/a').click()
        self.driver.find_element_by_xpath('/html/body/header/div/nav/div/ul/li/ul/li[1]/a').click()
        try:
            self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[2]/table[2]/tbody/tr[2]/td[5]/form/input[4]').click()
            self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/form/input[5]').click()
            self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/form/div[2]/span[1]/input').click()
            self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/form/textarea').send_keys('This is a test rejection.')
            self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/form/div/input[2]').click()
        except NoSuchElementException:
            self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[2]/table/tbody/tr[2]/td[5]/form/input[4]').click()
            self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/form/input[5]').click()
            self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/form/div[2]/span[1]/input').click()
            self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/form/textarea').send_keys('This is a test rejection.')
            self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/form/div/input[2]').click()

    #edits the metadata of the topmost order not yet accepted, and the first accepted one if all orders have been accepted
    def order_edit(self, user_type):
        self.driver.find_element_by_xpath('/html/body/header/div/nav/div/ul/li/a').click()
        self.driver.find_element_by_xpath('/html/body/header/div/nav/div/ul/li/ul/li[1]/a').click()
        
        try:
            self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[2]/table[2]/tbody/tr[2]/td[5]/form/input[4]').click()
            self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/form/input[5]').click()
            self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/form/div[3]/span[1]/input').click()
        except  NoSuchElementException:
            self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[2]/table/tbody/tr[2]/td[5]/form/input[4]').click()
            self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/form/div[3]/span[1]/input').click()
        
        time.sleep(1)
        self.driver.find_element_by_id('dc_title').clear()
        self.driver.find_element_by_id('dc_title').send_keys('Test Title EDITED')
        self.driver.find_element_by_id('dc_title_alternative_1').clear()
        self.driver.find_element_by_id('dc_title_alternative_1').send_keys('Test Sub-title 1 EDITED')
        try:
            self.driver.find_element_by_id('dc_title_alternative_2').clear()
            self.driver.find_element_by_id('dc_title_alternative_2').send_keys('Test Sub-title 2 EDITED')
        except NoSuchElementException:
            self.driver.find_element_by_xpath('//*[@id="edit_metadata"]/div[5]/div/div/button').click()
            time.sleep(.5)
            self.driver.find_element_by_id('dc_title_alternative_2').send_keys('Test-Subtitle 2 EDITED')
        select_agency = Select(self.driver.find_element_by_xpath('//*[@id="edit_metadata"]/div[7]/span/select'))
        select_agency.select_by_value('Records and Information Services, Department of (DORIS)')
        self.driver.find_element_by_id('dc_contributor_other_1').clear()
        self.driver.find_element_by_id('dc_contributor_other_1').send_keys('Test Contributor 1 EDITED')
        try:
            self.driver.find_element_by_id('dc_contributor_other_2').clear()
            self.driver.find_element_by_id('dc_contributor_other_2').send_keys('Test Contributor 2 EDITED')
        except NoSuchElementException:
            self.driver.find_element_by_xpath('//*[@id="edit_metadata"]/div[9]/div/div/button/span').click()
            time.sleep(.5)
            self.driver.find_element_by_id('dc_contributor_other_2').send_keys('Test Contributor 2 EDITED')
        select_category = Select(self.driver.find_element_by_xpath('//*[@id="subject-multiselect"]'))
        select_category.select_by_value('Accounting')
        select_category.select_by_value('Advertising')
        select_category.select_by_value('Alcohol')
        time.sleep(.25)
        self.driver.find_element_by_id('dc_description_abstract_id').clear()
        self.driver.find_element_by_id('dc_description_abstract_id').send_keys('EDITED DESCRIPTIONEDITED DESCRIPTIONEDITED DESCRIPTIONEDITED DESCRIPTIONEDITED DESCRIPTIONEDITED DESCRIPTIONEDITED DESCRIPTIONEDITED DESCRIPTIONEDITED DESCRIPTIONEDITED DESCRIPTION')
        select_month = Select(self.driver.find_element_by_xpath('//*[@id="submission-month"]'))
        select_month.select_by_value('11')
        self.driver.find_element_by_xpath('//*[@id="submission-day"]').clear()
        self.driver.find_element_by_xpath('//*[@id="submission-day"]').send_keys('11')
        self.driver.find_element_by_xpath('//*[@id="submission-year"]').clear()
        self.driver.find_element_by_xpath('//*[@id="submission-year"]').send_keys('1911')
        select_type = Select(self.driver.find_element_by_xpath('//*[@id="edit_metadata"]/div[17]/span/select'))
        select_type.select_by_value('Calendars')
        time.sleep(.25)
        self.driver.find_element_by_xpath('//*[@id="fiscal-year"]').clear()
        self.driver.find_element_by_xpath('//*[@id="fiscal-year"]').send_keys('1911')
        try:
            self.driver.find_element_by_xpath('(//*[@id="fiscal-year"])[2]').clear()
            self.driver.find_element_by_xpath('(//*[@id="fiscal-year"])[2]').send_keys('1912')
        except NoSuchElementException:
            self.driver.find_element_by_xpath('//*[@id="edit_metadata"]/div[21]/div/div/button').click()
            time.sleep(.25)
            self.driver.find_element_by_xpath('(//*[@id="fiscal-year"])[2]').send_keys('1912')
        self.driver.find_element_by_xpath('//*[@id="calendar-year"]').clear()
        self.driver.find_element_by_xpath('//*[@id="calendar-year"]').send_keys('1913')
        try:
            self.driver.find_element_by_xpath('(//*[@id="calendar-year"])[2]').clear()
            self.driver.find_element_by_xpath('(//*[@id="calendar-year"])[2]').send_keys('1914')
        except NoSuchElementException:
            self.driver.find_element_by_xpath('//*[@id="edit_metadata"]/div[23]/div/div/button').click()
            time.sleep(.25)
            self.driver.find_element_by_xpath('(//*[@id="calendar-year"])[2]').send_keys('1914')
        select_boro = Select(self.driver.find_element_by_xpath('//*[@id="edit_metadata"]/div[25]/span/select'))
        select_boro.select_by_value('bronx')
        select_boro.select_by_value('brooklyn')
        select_district = Select(self.driver.find_element_by_xpath('//*[@id="edit_metadata"]/div[27]/span/select'))
        select_district.select_by_value('District 1')
        select_district.select_by_value('District 3')
        select_district.select_by_value('District 7')
        select_board = Select(self.driver.find_element_by_xpath('//*[@id="edit_metadata"]/div[29]/span/select'))
        select_board.select_by_value('Bronx 5')
        select_board.select_by_value('Brooklyn 6')
        self.driver.find_element_by_xpath('//*[@id="dc_coverage_spatial-place_1"]').clear()
        self.driver.find_element_by_xpath('//*[@id="dc_coverage_spatial-place_1"]').send_keys('EDITVILLE')
        try:
            self.driver.find_element_by_xpath('//*[@id="dc_coverage_spatial-place_2"]').clear()
            self.driver.find_element_by_xpath('//*[@id="dc_coverage_spatial-place_2"]').send_keys('EDITVILLE 2')
        except NoSuchElementException:
            self.driver.find_element_by_xpath('//*[@id="edit_metadata"]/div[31]/div/div/button/span').click()
            self.driver.find_element_by_xpath('//*[@id="dc_coverage_spatial-place_2"]').send_keys('EDITVille 2')
        
        
        self.driver.find_element_by_xpath('//*[@id="submit-next"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="content"]/div/form/div[3]/input[3]').click()