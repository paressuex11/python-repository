import requests
url=input('Please input the url: ')
kv={'useragent':'Mozilla/5.0'}
try:
    r=requests.get(url,timeout=30,headers=kv)
    r.raise_for_status()
    r.encoding=r.apprent_encoding
    print(r.text[:200])
except:
    print('出错啦!!!!!!!!!')
