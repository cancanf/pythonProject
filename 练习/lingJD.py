#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2018/09/05
# 淘宝秒杀脚本，扫码登录版
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
    driver.get("https://www.jd.com/")
    # 京东链接 https://www.jd.com/
    time.sleep(3)

    # 淘宝<a href="https://login.taobao.com/member/login.jhtml?spm=a21bo.21814703.754894437.1.5af911d9B64hKF&amp;f=top&amp;redirectURL=https%3A%2F%2Fwww.taobao.com%2F" target="_top" class="h" data-spm-anchor-id="a21bo.21814703.754894437.1">亲，请登录</a>
    # 京东 <a href="javascript:login();" class="link-login">你好，请登录</a>
    if driver.find_element_by_link_text("你好，请登录"):
        driver.find_element_by_link_text("你好，请登录").click()

    print("请在30秒内完成扫码")
    time.sleep(20)
    driver.get("https://cart.jd.com/cart.action")
    # <a target="_blank" href="//cart.jd.com/cart.action">我的购物车</a>
    # 京东购物车链接 https://cart.jd.com/cart.action"

    time.sleep(10)
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
    # 全选<input type="checkbox" name="select-all" class="jdcheckbox" clstag="pageclick|keycount|Shopcart_CheckAll|0">
    # 店铺全选  <input type="checkbox" name="checkShop" class="jdcheckbox" clstag="pageclick|keycount|Shopcart_CheckShop|0_608176">
    # 店铺全选二<input type="checkbox" name="checkShop" class="jdcheckbox" clstag="pageclick|keycount|Shopcart_CheckShop|0_1000004123">
    # <input type="checkbox" name="checkItem" class="jdcheckbox" clstag="pageclick|keycount|Shopcart_CheckProd|0_100007773997">
    # <input type="checkbox" name="checkItem" class="jdcheckbox" clstag="pageclick|keycount|Shopcart_CheckProd|0_100004484897">
    # "//input[@]clstag='pageclick|keycount|Shopcart_CheckProd|0_100007773997'"
    if driver.find_element_by_xpath("//html/body/div[1]/div/ul[1]/li[2]/div[2]/div[2]/div/div/div[27]/a"):
        driver.find_element_by_xpath("//html/body/div[1]/div/ul[1]/li[2]/div[2]/div[2]/div/div/div[27]/a")
        time.sleep(3)
    if driver.find_element_by_xpath("//html/body/div[5]/div[1]/div[5]/div[2]/div[1]/div[2]/div[1]/div[1]/div/input"):
        driver.find_element_by_xpath(
            "//html/body/div[5]/div[1]/div[5]/div[2]/div[1]/div[2]/div[1]/div[1]/div/input").click()
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S:%f'))


def buy(buytime):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print("当前时间" + now)
        # 对比时间，时间到的话就点击结算
        if now > buytime:
            try:
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
    # buy("2021-05-14 11:29:00.000000")
