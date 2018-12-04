#selenium函数操作浏览器
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

broswer=webdriver.Chrome()
try:
    broswer.get("https://www.baidu.com")
    inputs=broswer.find_element_by_id("kw")
    inputs.send_keys("python")
    inputs.send_keys(Keys.ENTER)
    wait=WebDriverWait(broswer,10)
    wait.until(EC.presence_of_element_located((By.ID,"content_left")))
    print(broswer.current_url)
    print(broswer.get_cookies())
    #print(broswer.page_source)
finally:
    time.sleep(10)
    broswer.close()