#!env/bin/python3

from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options

PROXY = "172.83.138.45:53281"

options = Options()
options.headless = True
options.add_argument('--proxy-server=%s' % PROXY)

dr = wd.Chrome("C:/Users/Xavier/Documents/chromedriver.exe", chrome_options=options)

dr.get("https://whatismyip.com/")




#fname = dr.find_element_by_name('first')
#fname.send_keys('Xavier')

#lname = dr.find_element_by_name('last')
#lname.send_keys('Collantes')

#btn = dr.find_element_by_name('search')
#btn.click()

print(dr.current_url)
print(dr.get_window_size())
dr.set_window_size(2000, 1900)

#dr.maximize_window()

dr.get_screenshot_as_file('C:/Users/Xavier/Desktop/selenium.png')

dr.close()
