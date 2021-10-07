from ddt import ddt, unpack, data
import time
from selenium import webdriver
import unittest


class Articlelist(unittest.TestCase):

    def setUp(self):
        self.drive = webdriver.Chrome()


    def tearDown(self):
        self.drive.quit()

    def test_login(self):
        driver = self.drive
        driver.implicitly_wait(10)
        driver.get("http://localhost:8081/login.html")
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//*[@id='app']/input[1]").send_keys("test")
        driver.find_element_by_xpath("//*[@id='app']/input[2]").send_keys("test")
        driver.find_element_by_css_selector("#app > button:nth-child(8)").click()
        # driver.find_element_by_name("注册")

    def test_addArticlet(self):
        driver = self.drive
        driver.implicitly_wait(10)
        driver.get("http://localhost:8081/jsp/articleList.jsp")
        driver.implicitly_wait(10)
        driver.find_element_by_id("article_add_btn").click()
        



if __name__ == '__main__':
    unittest.main(verbosity=1)
