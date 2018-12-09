#爬取淘宝网指定商品的信息
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


browser=webdriver.Chrome()
wait=WebDriverWait(browser,10)
KEYWORD="iPad"
MAX_PAGE=3

def save_file(product):
    fileName="taobao.txt"
    with open(fileName,"a",encoding="utf-8") as f:
        f.write(str(product)+"\n")

def get_products():
    html=browser.page_source
    doc=pq(html)
    items=doc("#mainsrp-itemlist .items .item").items()
    for item in items:
        product={
            "image":item.find(".pic .img").attr("data-src"),
            "price":item.find(".price").text(),
            "deal":item.find(".deal-cnt").text(),
            "title":item.find(".title").text(),
            "shop":item.find(".shop").text(),
            "location":item.find(".location").text(),
        }
        print(product)
        save_file(product)

def index_page(page):

    print("正在爬去第",page,"页")
    try:
        url="https://s.taobao.com/search?q="+quote(KEYWORD)
        
        browser.get(url)
        time.sleep(5)
        if page > 1:
            pageInput=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#mainsrp-pager div.form > input")))
            pageSubmit=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#mainsrp-pager div.form > span.btn.J_Submit")))
            pageInput.clear()
            pageInput.send_keys(page)
            pageSubmit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#mainsrp-pager li.item.active > span"),str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".m-itemlist .items .item")))
        get_products()
    except TimeoutError:
        index_page(page)

def main():
    for i in range(1,MAX_PAGE):
        index_page(i)
    browser.close()

if __name__ == "__main__":
    main()