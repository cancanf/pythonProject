# coding:utf-8
import os
from selenium import webdriver
import datetime
import time
from os import path
from selenium.webdriver.common.action_chains import ActionChains

d = path.dirname(__file__)
abspath = path.abspath(d)

driver = webdriver.Firefox()
driver.maximize_window()


def login():
    # 打开淘宝登录页，并进行扫码登录
    driver.get("https://www.taobao.com")
    # 京东链接 https://www.jd.com/
    time.sleep(3)
    if driver.find_element_by_link_text("亲，请登录"):
        driver.find_element_by_link_text("亲，请登录").click()

    print("请在30秒内完成扫码")
    time.sleep(30)

    driver.get("https://cart.taobao.com/cart.htm")
    # 京东购物车链接 https://cart.jd.com/cart.action"

    time.sleep(3)
    # 点击购物车里全选按钮
    # if driver.find_element_by_id("J_CheckBox_939775250537"):
    #     driver.find_element_by_id("J_CheckBox_939775250537").click()
    # if driver.find_element_by_id("J_CheckBox_939558169627"):
    #     driver.find_element_by_id("J_CheckBox_939558169627").click()

    # 是对应商品的, 淘宝
    # "J_CheckBox_3006322588219"
    # <label for="J_CheckBox_3006322588219" data-spm-anchor-id="a1z0d.6639537.1997196601.i0.6e607484FJaMXq">勾选商品</label>
    # <label for="J_CheckBox_3006322588219"
    # <label for="J_CheckBox_3006323020107"

    # 京东
    # <input type="checkbox" name="checkItem" class="jdcheckbox" clstag="pageclick|keycount|Shopcart_CheckProd|0_100007773997">
    # <input type="checkbox" name="checkItem" class="jdcheckbox" clstag="pageclick|keycount|Shopcart_CheckProd|0_100004484897">
    # 全选<input type="checkbox" name="select-all" class="jdcheckbox" clstag="pageclick|keycount|Shopcart_CheckAll|0">
    # 店铺全选  <input type="checkbox" name="checkShop" class="jdcheckbox" clstag="pageclick|keycount|Shopcart_CheckShop|0_608176">
    # 店铺全选二<input type="checkbox" name="checkShop" class="jdcheckbox" clstag="pageclick|keycount|Shopcart_CheckShop|0_1000004123">

    # clstag="pageclick|keycount|Shopcart_CheckProd|0_100011088784">


def buy(buytime):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print("当前时间" + now)
        # 对比时间，时间到的话就点击结算
        if now > buytime:
            try:
                if driver.find_element_by_id("J_SelectAll1"):
                    driver.find_element_by_id("J_SelectAll1").click()
                now = datetime.datetime.now()
                print('login success:', now.strftime('%Y-%m-%d %H:%M:%S:%f'))
                # 点击结算按钮
                if driver.find_element_by_id("J_Go"):
                    driver.find_element_by_id("J_Go").click()
                driver.find_element_by_link_text('提交订单').click()
            except:
                time.sleep(0.1)
        print(now)
        time.sleep(0.1)


if __name__ == "__main__":
    # times = input("请输入抢购时间：")
    # 时间格式："2018-09-06 11:20:00.000000"
    login()
    buy("2021-10-22 10:00:00.000000")
