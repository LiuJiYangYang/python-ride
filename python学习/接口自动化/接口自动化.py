# 现在流行的API接口都是http
# 接口通常是测试后端服务，后端是不是能正常处理。前端页面可以用UI
# 对被测系统输入信息  -检查输出信息
# 接口文档  - 接口消息的构成
# 测试工具  -  构造接口消息并发送接收
# 根据测试用例，构造出相应的HTTP请求，发送给服务器
# 内置库 httplib、urllib2
# 第三方库 urllib3、requests、pyCurl;接收并检查响应消息
import requests
r=requests.get('https://wanandroid.com/article/listproject/0/json')
print(r.status_code)

import requests

r=requests.get('http://jseckill.appjishu.com/seckill/list')
print(r.text)
r=requests.post('http://jseckill.appjishu.com/seckill/execution/1000/19923456783/c2097fe5d7ddf03207e4c3126b3d57b8')
print(r.text)
# 请求格式  application/x-www-from-urlencoded
#  就是单表形式的数据

# para1=value1&para2=value2&para3=value3
# {
#     'para1':value1,
#     'para2':value2,
#     'para3':value3
# }

import requests
payload={
    'action':'add_course',
    'data':'''{
    "name":"初中化学",
    "desc":"初中化学课程"，
    "display":"4"
    }'''
}
r=requests.post('http://localhost/api/mgr/sq_mgr',
                data=payload)
# print(r.text)             # recode:0
ret=r.json()
print(ret)

# assert r.text=='{"recode": 0}'
assert ret["reason"]==2          # 存在课程的返回值校验
assert ret["recode"]=='同名课程存在'

# application/json
# application/xml


