from selenium import webdriver
from selenium.webdriver.support.ui import Select

# 启动浏览器驱动
driver=webdriver.Chrome()

driver.implicitly_wait(10)    # webdriver实例对象

# get 方法 打开指定网址
driver.get('https://kyfw.12306.cn/otn/leftTicket/init')

# 出发地输入内容，   #   webElement实例对象
fromEle=driver.find_element_by_id('fromStationText')
driver.find_element_by_class_name()

# 点击
fromEle.click()

fromEle.clear()

fromEle.send_keys('南京南')

selctOneEle = driver.find_element_by_xpath('//*[@id="citem_0"]')
# selctOneEles = driver.find_elements_by_xpath('//*[@id="citem_0"]')
selctOneEle.click()

# #    問題下拉框選擇ID
#
#
#
#
#
#
# # 目的地点是一样操作
# toEle=driver.find_element_by_id('toStationText')
# # 这里也要点击一下
# toEle.click()
# # toEle.clear()
# toEle.send_keys('杭州东')
# # 选择开始时间，F12看出来 是select
# timeSelect=Select(driver.find_element_by_id('cc_start_time'))
# timeSelect.select_by_visible_text('06:00-12:00')
#
# # 第三个tab就是第三天;css选择器
# tomorrow=driver.find_element_by_css_selector('#data_range li:nth-child(3)')
#
# # 點擊
# tomorrow.click()
# # 選擇2等座有票的車次
# xpath='//*[@id="queryLeftTable"]//td[4][@class]/../td[1]//a'
#
# theTrains=driver.find_element_by_xpath(xpath)
# for one in theTrains:
#     print(one.text)
#
# # 最後，driver.quit讓瀏覽器和驅動進程一起退出
# driver.quit()

