# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import time

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "192.168.108.101:5555"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
time.sleep(5)
el5 = driver.find_element_by_xpath("//*[@text='港股']")
el5.click()
time.sleep(10)
driver.quit()