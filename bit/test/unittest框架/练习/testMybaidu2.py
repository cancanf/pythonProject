import time
import unittest

from selenium import webdriver


class MyBaidu(unittest.TestCase):
    def setUp(self):
        print("开始测试setUp()： ")
        self.driver = webdriver.Chrome()
        self.url = "https://www.baidu.com/"
        self.driver.implicitly_wait(2)

    def tearDown(self):
        print("结束测试tearDown()： ")
        self.driver.quit()

    def test_new(self):
        driver = self.driver
        driver.get(self.url)
        driver.implicitly_wait(3)
        driver.find_element_by_link_text("直播").click()
        print(driver.title)
        time.sleep(3)

    def test_baidusearch(self):
        driver = self.driver
        driver.get(self.url)
        time.sleep(3)
        title = driver.title
        driver.find_element_by_id("kw").send_keys("南辕北辙")
        driver.find_element_by_id("su").click()
        self.assertTrue(title == "百度一下，你就知道", msg="百度一下 is not equal！")
        time.sleep(6)

    if __name__ == "__main__":
        unittest.main(verbosity=2)
