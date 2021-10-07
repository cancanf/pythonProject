import os
import time
import unittest

from selenium import webdriver


class Baidu1(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.url = "https://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self) -> None:
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_baidusearch(self):
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("大鱼海棠")
        driver.find_element_by_id("su").click()
        time.sleep(3)

    def test_baidu(self):
        driver = self.driver
        driver.get(self.url)
        driver.implicitly_wait(3)
        print(driver.title)
        try:
            self.assertEqual("dddd百度一下，你就知道", driver.title)
        except:
            self.saveScreenShot(driver, "hao.png")
        time.sleep(5)

    # 截图的函数
    def saveScreenShot(self, driver, filename):
        if not os.path.exists("./image"):
            os.makedirs("./image")
        now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
        driver.get_screenshot_as_file("./image/" + now + "-" + filename)
        time.sleep(2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
