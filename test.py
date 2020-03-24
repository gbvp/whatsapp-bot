from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
input('Press any key to confirm session established')
cookies_list = driver.get_cookies()
cookies_dict = {}
for cookie in cookies_list:
    cookies_dict[cookie['name']] = cookie['value']

print(cookies_dict)