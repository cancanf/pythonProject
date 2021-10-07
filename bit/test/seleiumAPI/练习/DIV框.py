from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os



driver=webdriver.Chrome()
file = "file:///" + os.path.abspath("../../../selenium2html/modal.html")
driver.get(file)
time.sleep(2)

dr = driver.find_element_by_css_selector("#show_modal")
dr.click()
time.sleep(2)
dr.find_element_by_xpath("//*[@id='myModal']").find_element_by_id("click").click()
dr.find_element_by_xpath("//*[@id='myModal']/div[3]").click()
time.sleep(3)
driver.quit()




