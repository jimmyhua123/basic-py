import selenium,time,os,wget,json
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH =  'C:\\Users\\User\\Desktop\\工具\\chromedriver_win32 (1)\\chromedriver.exe'
driver =webdriver.Chrome(PATH)
#ctrl+/ 快樹註解

driver.get("https://www.instagram.com/")
username=WebDriverWait(driver, 20).until(#網頁跳轉需要時間 等20秒或 (By.CLASS_NAME, "sc-3yr054-1")出現
    EC.presence_of_element_located((By.NAME, "username"))
)
password=WebDriverWait(driver, 20).until(#網頁跳轉需要時間 等20秒或 (By.CLASS_NAME, "sc-3yr054-1")出現
    EC.presence_of_element_located((By.NAME, "password"))
)
username.clear()
password.clear()

Your_account='0912341074'
Your_password='madhead345'
username.send_keys(str(Your_account))
password.send_keys(str(Your_password))

login =driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
login.click()
WebDriverWait(driver, 20).until(#網頁跳轉需要時間 等20秒或 (By.CLASS_NAME, "sc-3yr054-1")出現
    EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
)

driver.get('https://www.instagram.com/mochamom_et/')
time.sleep(2)
eles = driver.find_elements_by_class_name('v1Nh3')
for ele in eles:
    ele.click()
    time.sleep(1)
    driver.find_element_by_class_name('fr66n').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[6]/div[3]/button').click()
    time.sleep(1)