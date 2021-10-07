from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome()

driver.get("https://www.baidu.com/")
# id
# driver.find_element_by_id("kw").send_keys("张桐")
# driver.find_element_by_id("su").click()
# name
# driver.find_element_by_name("wd").send_keys("孙一宁")
# driver.find_element_by_id("su").click()
# class  name
# driver.find_element_by_class_name("s_ipt nobg_s_fm_hover").send_keys("王思聪")
# driver.find_element_by_id("su").click()
# link text
# driver.find_element_by_link_text("新闻").click()
# partial link text
# driver.find_element_by_partial_link_text("hao").click()
# tag name
# driver.find_element_by_tag_name("input").send_keys("孙一宁")
# driver.find_element_by_tag_name("input").click()
# xpath
# driver.find_element_by_xpath("//*[@name='wd']").send_keys("100周年")
# driver.find_element_by_xpath("//*[@id='su']").click()
# css selector
# driver.find_element_by_css_selector("#kw").send_keys("叛逆者")
# driver.find_element_by_css_selector("#su").submit()
# # text = driver.find_element_by_id("bottom_layer").text
# # print(text)
# time.sleep(6)
# title=driver.title
# print(title)
# print(driver.current_url)
# driver.set_window_size(400, 800)
# time.sleep(6)
# js = "var q=document.documentElement.scrollTop=10000"
# driver.execute_script(js)
# # driver.back()
# time.sleep(6)
# # driver.find_element_by_css_selector("#kw").clear()
# # driver.forward()
# js = "var q=document.documentElement.scrollTop=0"
# driver.execute_script(js)
# driver.get("http://127.0.0.1:88/zentao/user-login.html")
# driver.find_element_by_id("account").send_keys("admin")
# driver.find_element_by_id("account").send_keys(Keys.TAB)
driver.find_element_by_css_selector("#kw").send_keys("叛逆者")
su=driver.find_element_by_css_selector("#su")
time.sleep(6)
# driver.find_element_by_name("password").send_keys("Huiwen890830")
# driver.find_element_by_name("password").send_keys(Keys.ENTER)
# ssss=driver.find_element_by_partial_link_text("百度百科")
# ActionChains(driver).move_to_element(ssss)
ActionChains(driver).double_click(su).perform()
time.sleep(6)


driver.quit()
