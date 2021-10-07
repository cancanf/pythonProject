# coding=utf-8

# 操作测试对象
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")

time.sleep(3)

# xpath定位 直接复制xpath 找到搜索框
find = driver.find_element_by_xpath("//*[@id='kw']")
time.sleep(3)
var = driver.find_element_by_xpath("//*[@id='bottom_layer']/div/p[1]/a").text
print("title = " + driver.title)
print("rul = " + driver.current_url)
print("text = " + var)
find.send_keys("selenium")

find.submit()
time.sleep(3)

driver.quit()

