import time

from selenium import webdriver
import os

driver = webdriver.Chrome()
file = "file:///" + os.path.abspath("../../../selenium2html/frame.html")
driver.get(file)
time.sleep(2)
driver.switch_to_frame("f1")
driver.switch_to_frame("f2")
driver.find_element_by_id("kw").send_keys("sadfasdf")
driver.find_element_by_id("su").click()
time.sleep(5)
#跳转到默认页面
driver.switch_to.default_content()
driver.switch_to.frame("f1")
#driver.switch_to_frame()
driver.find_element_by_link_text("click").click()
time.sleep(6)

driver.quit()

