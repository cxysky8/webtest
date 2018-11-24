import urllib.request

url="https://github.com/"
respone=urllib.request.urlopen(url)
StrRespone=respone.read().decode("utf-8")
with open("01.txt","w",encoding="utf-8") as f:
    f.write(StrRespone)
