from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

option = Options()

option.add_experimental_option ("detach",True)

web = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
web.maximize_window()

web.get ("https://moal.sisk12.net/MOAL360x3/login")

time.sleep(4)
unam=web.find_element("xpath",'//*[@id="txtUserName"]')
# ############ username ##############
unam.send_keys("dbatale")

passn=web.find_element("xpath",'//*[@id="txtPassword"]')
# ############ password ##############
passn.send_keys("#Work2013")

login = web.find_element("xpath",'//*[@id="classicLoginButton"]')
login.click()

time.sleep(2)

nav = web.find_element("xpath", '//*[@id="594"]')
nav.click()
nav = web.find_element("xpath", '//*[@id="843"]')
nav.click()
nav = web.find_element("xpath", '//*[@id="928"]')
nav.click()

time.sleep(1)
nav = web.switch_to.frame(web.find_element("xpath", '//*[@id="contentFrame"]'))
nav = web.find_element("xpath", '//*[@name="ctl00$ctl02$txtFirstName"]')
# ############ Search ##############
nav.send_keys('roger')
j = web.find_element("xpath", '//*[@id="ctl00_ctl02_btnSearch"]')
j.click()
"""
nav.send_keys("some text")
value = "Randomblue"

actions = ActionChains()
actions.send_keys(value)
actions.perform()
"""



