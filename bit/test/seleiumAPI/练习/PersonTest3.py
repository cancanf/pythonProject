from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://baidu.com/")
# print("浏览器最大化")
# browser.maximize_window()
# time.sleep(4)
# browser.set_window_size(1500, 500)
# time.sleep(4)

print(browser.current_url)
browser.find_element_by_id("kw").send_keys("没啥")
browser.find_element_by_id("su").click()
print(browser.current_url)

time.sleep(3)
# js语句执行，将滚动条拖到10000，大多数情况也就是到了底部
js = "var q=document.documentElement.scrollTop=10000"
browser.execute_script(js)
time.sleep(3)
# 0为顶部
js = "var q=document.documentElement.scrollTop=0"
browser.execute_script(js)

time.sleep(6)
browser.back()
# 后退
print(browser.current_url)
time.sleep(3)
# 前进
browser.forward()
time.sleep(3)
browser.quit()
