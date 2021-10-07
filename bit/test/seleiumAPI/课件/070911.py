from selenium import webdriver
import time
import os



driver=webdriver.Chrome()
file = "file:///"+os.path.abspath("C:/课件/我的课件/测试/selenium2/locateElement/selenium2html/upload.html")
driver.get(file)
driver.maximize_window()
time.sleep(3)

driver.find_element_by_tag_name("input").send_keys("C:/Users/18591/Pictures/test.jpg")
time.sleep(6)
driver.quit()