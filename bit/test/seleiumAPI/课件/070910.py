from selenium import webdriver
import time
import os



driver=webdriver.Chrome()
file = "file:///"+os.path.abspath("C:/课件/我的课件/测试/selenium2/locateElement/selenium2html/modal.html")
driver.get(file)
driver.maximize_window()
time.sleep(3)

driver.find_element_by_id("show_modal").click()
time.sleep(3)

driver.find_element_by_id("click").click()
time.sleep(6)

div = driver.find_element_by_class_name("modal-footer")
buttons = div.find_elements_by_tag_name("button")
buttons[0].click()

time.sleep(6)
driver.quit()