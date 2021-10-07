from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os



driver=webdriver.Chrome()
file = "file:///" + os.path.abspath("../../../selenium2html/level_locate.html")
driver.get(file)
driver.maximize_window()

driver.find_element_by_link_text("Link1").click()
time.sleep(6)
mm=driver.find_element_by_link_text("Another action")
ActionChains(driver).move_to_element(mm).perform()
time.sleep(6)
driver.quit()