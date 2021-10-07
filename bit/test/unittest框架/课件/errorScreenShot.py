# -*- coding: utf-8 -*-
import os
import time
import unittest

from selenium import webdriver


class Baidu1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors=[]
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

      # 忽略此测试用例
    @unittest.skip("skipping")
    def test_baidusearch(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(u"大虞海棠")
        driver.find_element_by_id("su").click()
        time.sleep(6)


    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        time.sleep(6)
        print(driver.title)
        try:
            self.assertEqual(u"dddd百度一下，你就知道", driver.title)
        except:
            self.saveScreenShot(driver, "hao.png")   # 出现异常就调用截图函数进行截图
        time.sleep(5)

    # 截图函数
    def saveScreenShot(self, driver, file_name):   # 参数：驱动，截图名字
        if not os.path.exists("./image"):
            os.makedirs("./image")
        now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
        driver.get_screenshot_as_file("./image/"+now+"-"+file_name)
        time.sleep(3)
    if __name__ == "__main__":
        unittest.main()