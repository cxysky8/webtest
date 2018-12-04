#爬去今日头条街拍关键字的搜索内容，并下载图片
import requests
import os
from hashlib import md5
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from multiprocessing.pool import Pool


def get_page(offset,searchWork,base_url):
    headers={
    "referer":"https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
    }
    urlParams={
        "offset":offset,
        "format":"json",
        "keyword":searchWork,
        "autoload":True,
        "count":20,
        "cur_tab":1,
        "from":"search_tab",
        "pd":"synthesis"
    }
    url=base_url+urlencode(urlParams)
    try:
        strRespone=requests.get(url,headers=headers)
        if strRespone.status_code==200:
            return strRespone.json()
    except requests.ConnectionError as e:
        print("error",e.args)

def get_page_titleUrl(json):
    if json.get("data"):
        items=json.get("data")
        for item in items:
            title=item.get("title")
            imageUrls=item.get("image_list")
            if imageUrls:
                for imageurl in imageUrls:
                    yield{
                        "title":title,
                        "imageUrl":imageurl.get("url")
                    }

def save_image(titleUrl):
    if not os.path.exists(titleUrl.get("title")):
        os.mkdir(titleUrl.get("title"))
    try:
        response=requests.get("https:"+titleUrl.get("imageUrl"))
        if response.status_code==200:
            file_path="{0}/{1}.{2}".format(titleUrl.get("title"),md5(response.content).hexdigest(),"jpg")
            print(file_path)
            if not os.path.exists(file_path):
                with open(file_path,"wb") as f:
                    f.write(response.content)
            else:
                print("Already Downloaded",file_path)
    except requests.ConnectionError:
        print("Failed to Save Image")


def main(offset):
    base_url="https://www.toutiao.com/search_content/?"
    json=get_page(offset,"街拍",base_url)
    titleUrl=get_page_titleUrl(json)
    for item in titleUrl:
        print(item)
        save_image(item)

GROUP_START=1
GROUP_END=3

if __name__ == "__main__":
    pool=Pool()
    groups=([x*20 for x in range(GROUP_START,GROUP_END+1)])
    pool.map(main,groups)
    pool.close()
    pool.join()