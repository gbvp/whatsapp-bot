from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
import os
import schedule
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
try:
    import autoit
#pip install -U https://github.com/jacexh/pyautoit/archive/master.zip 64 bit python and os
except:
    pass
import time
import datetime
import os

doc_filename = None

class WhatsappBot:
	def __init__(self):
		self.bot = webdriver.Chrome('C:\\Users\\SANJAY PATEL\\AppData\\Local\\Programs\\Python\\Python37-32\\chromedriver.exe')
# user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))

	def session(self):
		global doc_filename
		bot = self.bot
		bot.get('https://web.whatsapp.com/')
		input('Press any key to confirm session established')
		doc_filename = input('Enter the Document file name you want to send:')

	def message(self,phoneNumber,textMessage):
		bot = self.bot
		bot.get('https://web.whatsapp.com/send?phone=91'+phoneNumber)
		time.sleep(10)
		self.send_attachment()
		time.sleep(10)
		self.send_files()
		# self.saveCookies(bot)
		# try:
		# 	text_message = bot.find_element_by_class_name('_3u328')# copyable-text selectable-text')
		# 	text_message.send_keys(textMessage)
		# 	text_message.send_keys(Keys.ENTER) 
		# 	# time.sleep(10)
		# 	# button will be activated after message is set in input field
		# 	# send_button = bot.find_element_by_class_name('_3M-N-')
		# 	# send_button.send_keys(Keys.RETURN)
		# except:
		# 	print(phoneNumber+' is not a whatsapp number')
		# time.sleep(5)

	def send_attachment(self):
		bot = self.bot  # Attachment Drop Down Menu
		clipButton = bot.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span')
		clipButton.click()
		time.sleep(5)
		# To send Videos and Images.
		mediaButton = bot.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button')
		mediaButton.click()
		time.sleep(5)

		hour = datetime.datetime.now().hour
		# After 5am and before 11am scheduled this.
		if(hour >=5 and hour <=11):
			image_path = os.getcwd() +"\\Media\\" + 'goodmorning.jpg'
	    # After 9pm and before 11pm schedule this
		elif (hour>=21 and hour<=23):
			image_path = os.getcwd() +"\\Media\\" + 'goodnight.jpg'
		else: # At any other time schedule this.
			image_path = os.getcwd() +"\\Media\\" + 'howareyou.jpg'

		# print(image_path)
		autoit.control_focus("Open","Edit1")
		autoit.control_set_text("Open","Edit1",(image_path) )
		autoit.control_click("Open","Button1")

		time.sleep(5)
		whatsapp_send_button = bot.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div/span')
		whatsapp_send_button.click()
		time.sleep(5)

	#Function to send Documents(PDF, Word file, PPT, etc.)
	def send_files(self):
		bot = self.bot
		global doc_filename
		# Attachment Drop Down Menu
		clipButton = bot.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span')
		clipButton.click()
		time.sleep(5)

		# To send a Document(PDF, Word file, PPT)
		docButton = bot.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[3]/button')
		docButton.click()
		time.sleep(5)

		docPath = os.getcwd() + "\\Documents\\" + doc_filename

		autoit.control_focus("Open","Edit1")
		autoit.control_set_text("Open","Edit1",(docPath) )
		autoit.control_click("Open","Button1")

		time.sleep(5)
		whatsapp_send_button = bot.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div/span')
		whatsapp_send_button.click()
	
task = WhatsappBot()
task.session()
task.message('8156006800','hi')
