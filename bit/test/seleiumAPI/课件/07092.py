from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:88/zentao/user-login.html")
driver.maximize_window()
driver.find_element_by_id("account").send_keys("admin")
driver.find_element_by_id("account").send_keys(Keys.TAB)
#
password=driver.find_element_by_name("password")
password.send_keys("Huiwen123456")
time.sleep(3)
password.send_keys(Keys.CONTROL, 'a')
time.sleep(3)
password.send_keys(Keys.CONTROL, 'x')
time.sleep(6)
password.send_keys("Huiwen890830")
time.sleep(3)
#river.find_element_by_id("submit").click()
driver.find_element_by_name("password").send_keys(Keys.ENTER)
time.sleep(6)
driver.quit()