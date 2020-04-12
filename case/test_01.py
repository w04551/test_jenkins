from selenium import webdriver

url = "https://www.baidu.com/"

r = webdriver.Firefox()
r.get(url)