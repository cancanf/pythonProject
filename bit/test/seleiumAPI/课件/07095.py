from selenium import webdriver
import time
import os


driver=webdriver.Chrome()
file = "file:///"+os.path.abspath("C:/课件/我的课件/测试/selenium2/locateElement/selenium2html/frame.html")
driver.get(file)
driver.maximize_window()
driver.switch_to.frame("f1")
driver.switch_to.frame("f2")
driver.find_element_by_id("kw").send_keys("布拉格")
driver.find_element_by_id("su").submit()
time.sleep(6)
#跳转到默认页面
driver.switch_to.default_content()
driver.switch_to.frame("f1")
#driver.switch_to_frame()
driver.find_element_by_link_text("click").click()
time.sleep(6)
driver.quit()