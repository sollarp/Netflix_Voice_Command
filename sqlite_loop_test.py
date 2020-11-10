from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sqlite3


conn = sqlite3.connect('neflix_data_store.db')
c = conn.cursor()

#def create_table():
c.execute("CREATE TABLE IF NOT EXISTS netflix_data_sql(nameofshow TEXT, url TEXT)")

def data_entry(movie_name, url_link):
    #num = input('Salesman ID:')
    #movie_name = input('Name:')
    #url_link = input('City:')
    c.execute("""INSERT INTO netflix_data_sql(nameofshow, url)VALUES(?,?)""",(movie_name, url_link))
    print("searching...")
    
    conn.commit()
    #c.close()
    #conn.close()
#create_table()
#data_entry()
chrome_options = Options()
chrome_options.add_argument("--user-agent=Mozilla/5.0 (X11; CrOS armv7l 11895.95.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.125 Safari/537.36"
)
chrome_options.add_argument("start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--user-data-dir=chrome-data")
        

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',
                                       options=chrome_options)

driver.get('https://www.netflix.com/SwitchProfile?tkn=J3LTSQQC2NDQHLYPD6UGZN76TI')


    

ids = driver.find_elements_by_xpath('//a[@href]' and '//a[@aria-label]')
index = 0
n = 4

for ii in ids[:n]:

    if index == 3:
        movie_name = (ii.get_attribute('aria-label'))
        url_link = (ii.get_attribute('href'))
        data_entry(movie_name, url_link)
        break
    print("plus")
    index += 1
        
    



