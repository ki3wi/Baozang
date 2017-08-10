__author__ = 'shanqingmei'

# -*-coding=utf-8 -*-

from appium import webdriver
from time import sleep
import unittest
import os
import HTMLTestRunner

class take_screen_shot():
    def __init__(self, func):
        self.func = func
        self.name = func.__name__ + ' (__main__.AndroidTests).png'

    def __call__(self, *args):
        try:
            self.func(self, *args)
        finally:
            driver.get_screenshot_as_file(self.name)

class AndroidTests(unittest.TestCase):
    @classmethod
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['plataformVersion'] = '5.1.1'
        desired_caps['deviceName'] = '229b2948'
        desired_caps['appPackage'] = 'com.youxi.trove'
        desired_caps['appActivity'] = '.View.SplashActivity'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        global driver
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @classmethod
    def tearDown(self):
        #driver.close_app()
        driver.quit()
    '''
    @take_screen_shot
    def test_usr_login(self):
        print("Start landing")
        driver.implicitly_wait(3)
        driver.find_element_by_id("com.youxi.trove:id/toolbar_left_head").click()
        driver.find_element_by_id("com.youxi.trove:id/qaet_autoComplete").clear()
        driver.find_element_by_id("com.youxi.trove:id/qaet_autoComplete").send_keys("测试sqm")
        driver.implicitly_wait(1)
        driver.find_element_by_id("com.youxi.trove:id/login_password").clear()
        driver.find_element_by_id("com.youxi.trove:id/login_password").send_keys("ceshisqm")
        driver.implicitly_wait(1)
        driver.find_element_by_id("com.youxi.trove:id/login_click_1").click()
        driver.get_screenshot_as_file("loginsuccess.png")
    '''
##driver.switch_to.context("WEBVIEW")

    def test_mod(self):
        u'''遍历mod'''
        driver.implicitly_wait(2)
        driver.find_element_by_name("黑金龙").click()
        #driver.find_element_by_xpath("//android.widget.TextView[contains(@class,'android.view.View')and@index='2']").click()
        #driver.tap([52,705],10)
        #driver.find_element_by_xpath("//android.widget.TextView[contains(@name,'黑金龙')]").click()
        driver.implicitly_wait(2)
        driver.get_screenshot_as_file("modone.png")
        driver.find_element_by_id("com.youxi.trove:id/toolbar_left_head").click()

        driver.implicitly_wait(2)
        driver.find_element_by_name("阿特拉斯_数据毁灭者").click()
        driver.implicitly_wait(2)
        driver.get_screenshot_as_file("modtwo.png")
        driver.find_element_by_id("com.youxi.trove:id/toolbar_left_head").click()

        driver.implicitly_wait(2)
        driver.find_element_by_name("光辉行者").click()
        driver.implicitly_wait(2)
        driver.get_screenshot_as_file("modthree.png")
        driver.find_element_by_id("com.youxi.trove:id/toolbar_left_head").click()

        driver.implicitly_wait(2)
        driver.find_element_by_name("双管熔岩枪").click()
        driver.implicitly_wait(2)
        driver.get_screenshot_as_file("modfour.png")
        driver.find_element_by_id("com.youxi.trove:id/toolbar_left_head").click()

        driver.implicitly_wait(2)
        driver.swipe(start_x=575, start_y=1588, end_x=575, end_y=414, duration=1000)





    def test_fav(self):
        u'''订阅'''
        driver.implicitly_wait(3)
        driver.find_element_by_id("com.youxi.trove:id/favorite_btn").click()
        sleep(1)
        driver.get_screenshot_as_file("fav.png")
        driver.find_element_by_id("com.youxi.trove:id/toolbar_left_head").click()

if __name__ =='__main__':
#unittest.main()

    test = unittest.TestSuite()
    test.addTest(AndroidTests("test_mod"))
    test.addTest(AndroidTests("test_fav"))
    filename = 'C:\\Users\\ki3wi\\Desktop\\pic\\HTML\\baozangtest.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream = fp,title = u'宝藏世界测试报告',description = u'用例执行情况')
    runner.run(test)
    fp.close()

