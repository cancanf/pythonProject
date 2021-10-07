from selenium import webdriver
import time
import os
file = "file:\\" + os.path.abspath("../../../selenium2html/drop_down.html")
driver = webdriver.Chrome()
driver.get(file)
time.sleep(3)
dd = driver.find_element_by_id("ShippingMethod")
dd.click()
dd.find_element_by_xpath("//*[@id='ShippingMethod']/option[1]").click()

time.sleep(3)
driver.quit()