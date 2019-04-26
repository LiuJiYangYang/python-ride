from selenium import webdriver
b=webdriver.Chrome()
help(b.get)

b.get('http://www.baidu.com')

a=b.title             # 標題
print(a)
a1='百度' in b.title    # 匹配，返回Ture或false
print(a1)
a2=b.current_url     # 顯示url
print(a2)

# b.get('http://www.baidui.com')
# b.current_url
#
# 'baidu' in b.current_url
#
# b.title
#
# '百度' in b.title

ele=b.find_element_by_id('kw')
id(ele)         #  輸入編號

type(ele)

ele.clear()      # 清除輸入

ele.send_keys('麥子學院')
b.back()       # 返回跳回
b.back()       # 返回跳回
b.back()

ele=b.find_element_by_name('wd')
ele.send_keys('麥子學院')

#####
from selenium import webdriver
b=webdriver.Firefox()
b.get('http://www.baidu.com')
ele=b.find_element_by_class_name('s_ipt')
ele
#
ele.send_keys('selenium')
ele1=b.find_element_by_tag_name('input')
ele1
#
ele.size
#
ele.id
#
ele1.id
#
ele1.size
# ele1.send_keys('11')      #  報錯
ele.id
#
ele2=b.find_element_by_id('kw')
ele2.id







