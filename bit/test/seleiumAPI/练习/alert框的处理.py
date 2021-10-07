from selenium import webdriver
import time
import os


driver=webdriver.Chrome()
file = "file:///" + os.path.abspath("../../../selenium2html/alert.html")
driver.get(file)
time.sleep(2)
driver.maximize_window()
driver.find_element_by_id("tooltip").click()
time.sleep(2)
driver.switch_to_alert().accept()
time.sleep(5)
driver.quit()


