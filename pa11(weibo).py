#爬取崔老师的前十页的微博
import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq

base_url="https://m.weibo.cn/api/container/getIndex?"
headers={
    "host":"m.weibo.cn",
    "referer":"https://m.weibo.cn/u/2830678474",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}

def get_page(pageIndex):
    urlParams={
        "type":"uid",
        "value":"2830678474",
        "containerid":"1076032830678474",
        "page":pageIndex,
    }
    url=base_url+urlencode(urlParams)
    try:
        strRespone=requests.get(url,headers=headers)
        if strRespone.status_code==200:
            return strRespone.json()
    except requests.ConnectionError as e:
        print("error",e.args)

def parse_page(pageJson):
    if pageJson:
        items=pageJson.get("data").get("cards")
        for item in items:
            item=item.get("mblog")
            if item:
                weibo={}
                weibo["id"]=item.get("id")
                weibo["text"]=pq(item.get("text")).text()
                weibo["attitudes"]=item.get("attitudes_count")
                weibo["comments"]=item.get("comments_count")
                weibo["reposts"]=item.get("reposts_count")
                yield weibo

if __name__ == "__main__":
    for page in range(1,11):
        json=get_page(page)
        results=parse_page(json)
        for result in results:
            print(result)