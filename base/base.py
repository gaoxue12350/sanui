#!/usr/bin/env python 
#-*-coding:utf-8-*-

from selenium import  webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec
import  time as t

class WebDriver(object):
	def __init__(self,driver):
		self.driver=driver

	def findElement(self,*loc):
		try:
			return WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*loc))
		except  NoSuchElementException,e:
			print 'Error details :%s' % (e.args[0])

	def wait(self):
		t.sleep(2)

	def refersh(self):
		self.driver.refresh()





