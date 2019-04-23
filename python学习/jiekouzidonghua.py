import requests

r = requests.post(url='https://wanandroid.com/article/listproject/0/json')
print(r.status_code)