from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

file = "file:///" + os.path.abspath("../../../selenium2html/level_locate.html")
driver.get(file)
time.sleep(5)
# 定位思路：
# 具体思路是：先点击显示出1个下拉菜单，然后再定位到该下拉菜单所在的ul，再定位这个ul 下的某个具体的link。
# 在这里，我们定位第1个下拉菜单中的Action 这个选项。
driver.find_element_by_link_text('Link1').click()
time.sleep(1)
mm = driver.find_element_by_link_text("Another action")
ActionChains(driver).move_to_element(mm).perform()
time.sleep(5)
driver.quit()



