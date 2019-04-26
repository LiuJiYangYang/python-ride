import requests
payload={
    'p1':'v1',
    'p2':'v2',
}

r=requests.get('https://b2c.jihainet.com/wap/index.html#/index',
               payload)
print(r.text)




