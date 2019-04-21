from selenium import webdriver
driver = webdriver.Chrome()




driver.get("http://www.baidu.com")


ele = driver.find_element_by_id("kw")

ele.send_keys("chromedriver")
driver.find_element_by_id("su").click()