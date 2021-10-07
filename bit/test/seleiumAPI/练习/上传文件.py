from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

driver = webdriver.Chrome()
file = "file:///" + os.path.abspath("../../../selenium2html/upload.html")
driver.get(file)
driver.implicitly_wait(2)
driver.find_element_by_tag_name("input").send_keys("D:\\pythonProject1\\pythonProject\\bit\\selenium2html\\upload.html")
time.sleep(2)
driver.quit()
