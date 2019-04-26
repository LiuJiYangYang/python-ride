# 要買票的車次
interested = [
    'G1379', 'G1377', 'D3295', 'G7393'
]

# 記錄循環次數
i = 0
# 循環不斷的搜索
while True:
    i += 1
    isGet = False  # 設置為沒有找到

    # 點擊這個，就會搜索車次了
    tomorrow.click()

    # 選擇2等座有票的車次
    xpath = '//*[@id="queryLeftTable"]//td[4][@class]/../td[1]//a'

    theTrains = driver.find_element_by_xpath(xpath)

    for one in theTrains:
        name=one.text
        if name in interested:
            isGet=True
            print('*** 有剩餘車票 ' + name)

    if isGet




####  登陸界面
driver=webdriver.Chrome(r"C:\Users\11839\AppData\Local\Programs\Python\Python36\chromedriver.exe")

driver.implicitly_wait(10)

# get 方法 打開指定網址
driver.get('https://kyfw.12306.cn/otn/login/init')
driver.find_element_by_id('username').send_keys('pppoe4444')

input('登錄界面，請輸入密碼登陸  后按回車')

driver.get('https://kyfw.12306.cn/otn/leftTicket/init')



# 點擊確認
driver.find_element_by_id('work_position_click_bottom_save').click

# “選擇”按鈕  .ush button
# 獲取文本信息


# 獲取div下面的div
jobs=driver.find_element_by_css_selector('#resultList div[ class=el]')

for job in jobs:
    fields=job.find_elements_by_tag_name('span')
    stringFilelds=[filed.text for field in fields]
    print('|',join(stringFilelds))


# 選擇杭州
driver.find_element_by_id(
    'work_position_click_center_right_list_category_000000_080200'
).click()

# 保存城市選擇
driver.find_element_by_id('work_position_click_botton_save').click()

# 點擊搜索
driver.find_element_by_css_selector('.ush  button').click()