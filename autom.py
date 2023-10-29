import time

from selenium import webdriver

weba = webdriver.Chrome()

weba.get('https://www.youtube.com/')
search = "hello world"

time.sleep(4)

thePath = weba.find_element("xpath",'//*[@id="search-form"]')
thePath.send_keys(search)
