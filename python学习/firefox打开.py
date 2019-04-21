from selenium import webdriver
driver = webdriver.Firefox()




driver.get("http://www.baidu.com")


ele = driver.find_element_by_id("kw")

ele.send_keys("geckodriver")
driver.find_element_by_id("su").click()