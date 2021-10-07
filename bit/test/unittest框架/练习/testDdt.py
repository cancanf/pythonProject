# -*- coding: utf-8 -*-

import csv
import sys
import time
import unittest

from ddt import ddt, unpack, data
from selenium import webdriver


def getCsv(file_name):
    rows = []
    path = sys.path[0]

    with open(path + '/data/' + file_name, 'rt') as f:
        readers = csv.reader(f, delimiter=',', quotechar='|')
        next(readers, None)
        for row in readers:
            temprows = []
            for i in row:
                temprows.append(i)
            rows.append(temprows)
        return rows

@ddt
class Baidu1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    # @file_data('test_baidu_data.json')
    # @unpack
    @data("王凯", "Lisa", "特朗普", "蒋欣")
    @unittest.skip("skipping")
    def test_baidu1(self, value):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(value)
        driver.find_element_by_id("su").click()
        time.sleep(3)


    # json格式读取
    # @unittest.skip("skipping")
    # @file_data('D:\\pythonProject1\\pythonProject\\bit\\test\\unittest框架\\练习\\data\\test_baidu_data.json')
    # def test_baidu2(self, value):
    #     print(value)
    #     testdata, execptdata = tuple(value.strip().split(":"))
    #     driver = self.driver
    #     driver.get(self.base_url + "/")
    #     driver.find_element_by_id("kw").clear()
    #     driver.find_element_by_id("kw").send_keys(testdata)
    #     driver.find_element_by_id("su").click()
    #     time.sleep(2)
    #     # 判断搜索网页的title和我们期望的是否一致
    #     self.assertEqual(execptdata, driver.title, msg="和预期搜索结果不一致！")
    #     print(execptdata)
    #     print(driver.title)
    #     time.sleep(2)



    # @data(['Lisa', u"Lisa_百度搜索"], [u"双笙", u"7798双笙_百度搜索"], [u"双笙2", u"双笙2_百度搜索"])
    @data(*getCsv('test_baidu_data.txt'))
    # ([周迅, 周迅_百度搜索], [张国荣, 张国荣111_百度搜索], [张一山，张一三_百度搜索])
    @unpack
    def test_baidu2(self, value, execptdata):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(value)
        driver.find_element_by_id("su").click()
        time.sleep(2)
        # 判断搜索网页的title和我们期望的是否一致
        self.assertEqual(execptdata, driver.title, msg="和预期搜索结果不一致！")
        print(execptdata)
        print(driver.title)
        time.sleep(2)


if __name__ == '__main__':
    unittest.main(verbosity=1)
    # getpy("test_baidu_data.json")
