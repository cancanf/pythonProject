from selenium import webdriver
import time
import os



driver=webdriver.Chrome()
file = "file:///"+os.path.abspath("C:/课件/我的课件/测试/selenium2/locateElement/selenium2html/send.html")
driver.get(file)
driver.maximize_window()
time.sleep(6)

driver.find_element_by_tag_name("input").click()
time.sleep(3)
alert=driver.switch_to.alert

alert.send_keys("hello,summer!")
alert.accept()
time.sleep(6)
driver.quit()