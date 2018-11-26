#爬取知乎提问及回答
import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq

url="https://www.zhihu.com/explore"
headers={
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
}
r=requests.get(url,headers=headers).text
doc=pq(r)
items=doc(".explore-tab .feed-item").items()
i=1
for item in items:
    question=item.find("h2").text()
    author=item.find(".author-link-line").text()
    answer=pq(item.find(".content").html()).text()
    with open("explore.txt","a",encoding="utf-8") as  f:
        f.write("\n".join(["第"+str(i)+"个问题："+question,author,"回答："+answer]))
        f.write("\n"+"="*100+"\n")
    i=i+1