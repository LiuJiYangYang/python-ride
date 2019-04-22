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

