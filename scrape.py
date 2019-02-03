#env/bin/python3

from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys

dr = wd.Chrome("C:/Users/Xavier/Documents/chromedriver.exe")

dr.get("https://linkedin.com")

fname = dr.find_element_by_name('first')
fname.send_keys('Xavier')

lname = dr.find_element_by_name('last')
lname.send_keys('Collantes')

btn = dr.find_element_by_name('search')
btn.click()

print(dr.current_url)
