import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

def netflix_login_process():
    username = ("YOUR EMAIL ADDRESS")
    password = ("YOUR PASSWORD")
    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir=chrome-data")
    driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=chrome_options)
    chrome_options.add_argument("user-data-dir=chrome-data")
    driver.get('https://www.netflix.com/password')
    time.sleep(5)  # Time to enter credentials
    elem = driver.find_element_by_name("userLoginId")
    elem.send_keys(username)
    elem = driver.find_element_by_name("password")
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.quit()
    
netflix_login_process()
