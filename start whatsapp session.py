import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Chrome('chromedriver.exe',options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data") 
driver.get('https://web.whatsapp.com')
time.sleep(30)  # Time to enter credentials
driver.quit()