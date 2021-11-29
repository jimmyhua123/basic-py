# coding=utf-8
from platform import python_version
import os, time, json
import pandas as pd

import requests
import bs4
from bs4 import BeautifulSoup
import urllib
from selenium import webdriver
import selenium
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with open('data.json','r',encoding='utf8')as jFile: #r=read讀取as命名jfile
    jdata=json.load(jFile)#呼叫jdata=呼叫json

print("【現在時間】{}".format(time.strftime("%Y/%m/%d %H:%M:%S")))
print("【所在目錄】{}".format(os.getcwd()))
print("【Python】{}".format(python_version()))


# print("【requests】{}".format(requests.__version__))
# print("【BeautifulSoup】{}".format(bs4.__version__))

# data = [{"name":"Dale",  "age":18},
#         {"name":"candy", "age":20},
#         {"name":"andy",  "age": 2}]

# print(type(data))
# print(type(data[0]))

# NAME = [d.get("name") for d in data]
# print(NAME)
# ['Dale', 'candy', 'andy']

# AGE = [d.get("age") for d in data]
# print(AGE)
# [18, 20, 2]

# df = pd.DataFrame({"姓名":NAME, "年齡":AGE})
# print(df)
#       姓名  年齡
# 0   Dale  18
# 1  candy  20
# 2   andy   2

#https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python
PATH = 'C:\\Users\\User\\Desktop\\工具\\chromedriver_win32 (1)\\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=PATH, options=options)

#ctrl+/ 快樹註解

url="https://24h.pchome.com.tw/"
driver.get(url)
#search=driver.find_element_by_xpath('//*[@id="input"]')
search=driver.find_element_by_id('keyword')
search.clear()
search.send_keys(str('筆電'))

login=driver.find_element_by_xpath('//*[@id="doSearch"]')

login.click()

WebDriverWait(driver, 20).until(#網頁跳轉需要時間 等20秒或 (By.CLASS_NAME, "sc-3yr054-1")出現
    EC.presence_of_element_located((By.CLASS_NAME, "prod_name"))
)
titles=driver.find_elements_by_class_name("prod_name")
prices=driver.find_element_by_class_name("value")

for title in titles:
    print(title.text)#印標題
    prices=driver.find_element_by_id('price_DHAS4N-A900B7V2B')
    print(prices)#印標題


time.sleep(10)


