from selenium import webdriver
import time
import os



driver=webdriver.Chrome()
file = "file:///"+os.path.abspath("C:/课件/我的课件/测试/selenium2/locateElement/selenium2html/alert.html")
driver.get(file)
driver.maximize_window()
time.sleep(6)

driver.find_element_by_id("tooltip").click()
time.sleep(5)
#
alert = driver.switch_to.alert
text=alert.text
print(text)
# 关掉弹框
alert.accept()

time.sleep(5)
driver.quit()