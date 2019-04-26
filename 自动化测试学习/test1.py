from selenium import webdriver

driver=webdriver.Firefox()
# get方法 打开指定网址
driver.get('http://www.baidu.com')
print(driver.get_cookies())
# 查找元素
element_keyword=driver.find_element_by_id("kw")

# 输入字符
element_keyword.send_keys('松勤')

# 找到搜索按钮
element_search_button=driver.find_element_by_id("su")
# 点击该元素
element_search_button.click()
# 退出进程
driver.quit()



