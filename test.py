from selenium import webdriver
import sys
import unittest
import loginPage
import newSubmission
import takeOrder

class Test(unittest.TestCase):
    def test(self):
        self.driver = webdriver.Chrome('/Users/bzhuang/Downloads/chromedriver')
        self.driver.get("https://gpp-test.appdev.records.nycnet//")

        login = loginPage.Login(self.driver)
        login.login(self.user_type)

        # submission = newSubmission.newSubmission(self.driver)
        # submission.new(self.user_type)
        
        order = takeOrder.takeOrder(self.driver)
        # order.order_approve(self.user_type)
        # order.order_reject(self.user_type)
        order.order_edit(self.user_type)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        Test.user_type = sys.argv.pop()
    unittest.main()
