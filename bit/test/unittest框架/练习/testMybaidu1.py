import unittest
from selenium import webdriver
import os
import time


class MyBaidu(unittest.TestCase):
    def setUp(self):
        print("开始测试setUp()： \n")
        self.driver = webdriver.Chrome()
        self.url = "https://www.baidu.com/"
        self.driver.implicitly_wait(2)

    def tearDown(self):
        print("结束测试tearDown()： \n")
        self.driver.quit()

    @unittest.skip("skipping")
    def test_new(self):
        driver = self.driver
        driver.get(self.url)
        driver.implicitly_wait(3)
        print(driver.title + "\n")
        driver.find_element_by_link_text("新闻").click()
        time.sleep(3)

    def test_baidusearch(self):
        driver = self.driver
        driver.get(self.url)
        time.sleep(3)
        title = driver.title
        driver.find_element_by_id("kw").send_keys("北辙南辕")
        driver.find_element_by_id("su").click()
        print("title" + title + "\n")
        self.assertTrue(title == "百度一下，你就知", msg="百度一下页面错误 is not equal！")
        time.sleep(6)

    if __name__ == "__main__":
        unittest.main(verbosity=1)
