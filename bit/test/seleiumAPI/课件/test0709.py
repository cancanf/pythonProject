from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
# driver.find_element_by_id("kw").send_keys("东京奥运会")
# driver.find_element_by_id("su").click()
# time.sleep(6)
# # clear
# driver.find_element_by_id("kw").clear()
# time.sleep(3)
driver.find_element_by_id("kw").send_keys("福原爱")
driver.find_element_by_id("su").submit()
# text=driver.find_element_by_id("bottom_layer").text
# print(text)
time.sleep(6)
driver.quit()
#driver.close()