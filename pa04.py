#爬取猫眼前100名电影榜单
import requests
import re
import json
import time

def get_one_page(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    respone=requests.get(url,headers=headers)
    if respone.status_code==200:
        return respone.text
    return None

def pares_one_page(content):
    StrPattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    return re.findall(StrPattern,content)

def main():
    url="http://maoyan.com/board/4?offset="
    for i in range(10):
        time.sleep(3)
        html=get_one_page(url+str(i))
        items=pares_one_page(html)
        print(items)
        with open('result.txt', 'a', encoding='utf-8') as f:
            f.write(json.dumps(items, ensure_ascii=False) + '\n')

if __name__ == '__main__':
    main()
