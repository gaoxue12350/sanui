#!/usr/bin/env python 
#-*-coding:utf-8-*-


import  unittest
from selenium import  webdriver

class Init(unittest.TestCase):
	def setUp(self, value='url'):
		self.driver = webdriver.Firefox()
		self.driver.maximize_window()
		self.driver.implicitly_wait(30)
		self.driver.get('http://eco.parkingwang.com/#/')

	def tearDown(self):
		self.driver.quit()
