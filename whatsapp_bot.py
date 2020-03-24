from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json


class WhatsappBot:
	def __init__(self):
		self.bot = webdriver.Chrome('C:\\Users\\SPARTA\\Desktop\\Newfolder\\chromedriver.exe')
		# self.bot = webdriver.FireFox('F:\\bhavik\\whatsapp_bot\\geckodriver.exe')
# user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))

	def session(self):
		bot = self.bot
		bot.get('https://web.whatsapp.com/')
		input('Press any key to confirm session established')

	def message(self,phoneNumber):
		bot = self.bot
		bot.get('https://web.whatsapp.com/send?phone=91'+phoneNumber)
		time.sleep(20)
		# self.saveCookies(bot)
		try:

			text_message = bot.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
			text_message.send_keys('''Dear Cab Partner, To activate your registration in capital cab please update below document's''')
			text_message.send_keys(Keys.ENTER) 
			text_message.send_keys('''*Car Registration Document*''')
			text_message.send_keys(Keys.ENTER) 
			text_message.send_keys('''Car : RC book, fitness, insurance, permit''')
			text_message.send_keys(Keys.ENTER) 
			text_message.send_keys('''Driver : Driver Licence, photo, police verification''')
			text_message.send_keys(Keys.ENTER) 
			text_message.send_keys('''Owner : Aadhar card, Pan card, Bank details''')
			time.sleep(3)
			text_message.send_keys(Keys.ENTER) 
			# time.sleep(10)
			# button will be activated after message is set in input field
			# send_button = bot.find_element_by_class_name('_3M-N-')
			# send_button.send_keys(Keys.RETURN)
		except:
			print(phoneNumber+' is not a whatsapp number')
		time.sleep(5)

task = WhatsappBot()
task.session()
task.message('9960451879')
task.message('8766427276')