from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os



driver=webdriver.Chrome()
file = "file:///"+os.path.abspath("C:/课件/我的课件/测试/selenium2/locateElement/selenium2html/drop_down.html")
driver.get(file)
driver.maximize_window()
time.sleep(6)
# xpath定位
# driver.find_element_by_xpath("//*[@id='ShippingMethod']/option[4]").click()
options = driver.find_elements_by_tag_name("option")
# for option in options:
#     if option.get_attribute('value') == '9.03':
#         option.click()
#用数组的方式定位，注意下标
options[3].click()

time.sleep(6)
driver.quit()