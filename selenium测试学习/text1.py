from selenium import webdriver
b=webdriver.Firefox()
b.get('http://www.maiziedu.com/')
b.maximize_window()     # 全屏
ele=b.find_element_by_link_text('企业直通班')
ele.click()
b.back()
# b.back()
# b.back()
print(ele.id)
ele1=b.find_element_by_partial_link_text('直通班')  # 模糊定义
print(ele1.id)
ele=b.find_element_by_link_text('企业直通班')     # 准确定义
ele1.click()
b.back()     # 跳转
ele_css=b.find_element_by_css_selector("div.ui-container:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)#text")
type(ele_css)
ele_css=b.find_element_by_css_selector("html body.YaHei.index div.main div.main-container div.slide div.slide-box ul li a")
ele_css.click()
b.back()

ele_css=b.find_element_by_css_selector("html body.YaHei.index div.main div.main-container div.slide div.slide-box ul li a")
ele_css.click()     # 点击
ele_css.send_keys('python')
ele_css=b.find_element_by_css_selector('input[\'id=search\']') # 输入错误；未匹配到

b.back()
ele=b.find_element_by_css_selector('input[id=\'search\']')
ele.clear()      # 清除
ele.send_keys('')

ele=b.find_element_by_css_selector('input[type="text"]')
print(ele.id)

ele.clear()
ele=b.find_element_by_css_selector('img["麦子学院三周年"]')






