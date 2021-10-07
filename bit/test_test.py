# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestTest:
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_test(self):
        self.driver.get("http://127.0.0.1:88/zentao/testreport-view-1.html")
        self.driver.set_window_size(1550, 830)
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.LINK_TEXT, "套件").click()
        self.driver.find_element(By.LINK_TEXT, "测试单").click()
        self.driver.find_element(By.LINK_TEXT, "测试报告").click()
        self.driver.find_element(By.LINK_TEXT, "用例库").click()
        self.driver.find_element(By.LINK_TEXT, "自动化").click()
        self.driver.close()

    @classmethod
    def main(cls):
        pass


if __name__ == '__main__':

  pytest.main()