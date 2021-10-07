from selenium import webdriver
import time
import os

driver = webdriver.Chrome()
file_path = "file:///" + os.path.abspath("../../../selenium2html/checkbox.html")

driver.get(file_path)
# driver.find_element_by_id("c2").click()
inputs = driver.find_elements_by_tag_name("input")
for input in inputs:
    if input.get_attribute('type') == 'checkbox':
        input.click()

time.sleep(8)
driver.quit()
