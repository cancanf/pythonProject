from selenium import webdriver
import time
import os

driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/')

# driver.find_element_by_id("kw").send_keys("吴亦凡")
# driver.find_element_by_id("su").click()
file_path = "file:///" + os.path.abspath("../../../selenium2html/checkbox.html")
driver.get(file_path)

inputs = driver.find_elements_by_tag_name("input")
for input in inputs:
    if input.get_attribute('type') == 'checkbox':
        input.click()

time.sleep(8)
driver.quit()
