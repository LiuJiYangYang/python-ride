from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.toutiao.com/')
driver.implicitly_wait(10)
driver.find_element_by_link_text('科技').click()
driver.implicitly_wait(10)
for x in range(3):
    js="var q=document.documentElement.scrollTop="+str(x*500)
    driver.execute_script(js)
    time.sleep(2)

time.sleep(5)
page = driver.page_source
doc = pq(page)
doc = etree.HTML(str(doc))
contents = doc.xpath('//div[@class="wcommonFeed"]/ul/li')
print(contents)
for x in contents:
    title = x.xpath('div/div[1]/div/div[1]/a/text()')
    if title:
        title = title[0]
        with open('toutiao.txt','a+',encoding='utf8')as f:
            f.write(title+'\n')
        print(title)
    else:
        pass