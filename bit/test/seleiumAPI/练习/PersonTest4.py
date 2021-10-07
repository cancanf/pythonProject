from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import HTMLTestRunner

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
# driver.find_element_by_id("kw").send_keys("横道世之介")
# 单击或者提交表单
# driver.find_element_by_id("su").submit()
# driver.find_element_by_id("su").click()
# su = driver.find_element_by_id("su")
# 双击
# ActionChains(driver).double_click(su).perform()
# 右击
# ActionChains(driver).context_click(su).perform()

#定位元素的原位置
time.sleep(3)
#定位元素的原位置
element = driver.find_element_by_id("s_btn_wr")
#定位元素要移动到的目标位置
target = driver.find_element_by_class_name("btn")
#执行元素的移动操作
ActionChains(driver).drag_and_drop(element, target).perform()
time.sleep(7)
driver.quit()
driver.close()
