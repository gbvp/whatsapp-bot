import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Chrome('chromedriver.exe',options=chrome_options)
driver.get('https://web.whatsapp.com')  # Already authenticated
time.sleep(300)
driver.quit()