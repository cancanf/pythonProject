from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
urll=driver.current_url
print(urll)
driver.find_element_by_id("kw").send_keys("福原爱")
driver.find_element_by_id("su").submit()
#固定等待
#time.sleep(10)
#智能等待
# driver.implicitly_wait(10)
#driver.find_element_by_link_text("福原爱 - 百度百科").click()
#浏览器的最大化
driver.maximize_window()
#打印title
time.sleep(6)
title=driver.title
print(title)
url=driver.current_url
print(url)
#浏览器的后退
# driver.back()
time.sleep(6)
#浏览器的前进
# driver.forward()
#设置浏览器的宽和高
driver.set_window_size(400, 1000)
time.sleep(3)
#拖动滚动条到最底端
js1="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js1)
time.sleep(6)
#拖动滚动条到最顶端
js2="var q=document.documentElement.scrollTop=0"
driver.execute_script(js2)
time.sleep(6)
driver.quit()
