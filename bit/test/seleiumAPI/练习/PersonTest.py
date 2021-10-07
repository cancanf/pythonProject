import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# 获得操作浏览器的遥控驱动
driver = webdriver.Chrome()

driver.get("https://baidu.com/")

# 百度搜索框的元素
# <input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">

# 1.使用name对元素进行定位并使用send_keys输入字段
# driver.find_element_by_name("wd").send_keys("selenium")

# 2.使用tag_name标签名来进行元素定位  注意input标签通常不止一个
# driver.find_element_by_tag_name("input").send_keys("selenium")

# 3.通过元素的class name进行定位
# driver.find_element_by_class_name("s_ipt").send_keys("selenium")

# css定位 直接复制selector
driver.find_element_by_css_selector("#kw").send_keys("selenium")
# xpath定位 直接复制xpath
# driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")

# 点击按钮的元素
# <input type="submit" value="百度一下" id="su" class="btn self-btn bg s_btn">
# 使用id进行定位并进行点击事件
driver.find_element_by_id("su").click()

# link text 定位
# 咨询元素
#<a href="https://www.baidu.com/s?rtt=1&amp;bsst=1&amp;cl=2&amp;tn=news&amp;ie=utf-8&amp;word=seleium" wdfield="word" onmousedown="return c({'fm':'tab','tab':'news'})" sync="true" class="s-tab-item s-tab-news">资讯</a>
time.sleep(3)
driver.find_element_by_link_text("资讯").click()

time.sleep(3)
# Partial link text定位
driver.find_element_by_partial_link_text("视").click()

time.sleep(6)  #
# 智能等待，隐式的等待一个元素被发现或者一个命令完成
# driver.implicitly_wait()


driver.quit()  # 会进行资源的关闭
# driver.close()  # 只会将浏览器进行关闭
