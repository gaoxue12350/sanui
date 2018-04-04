#!/usr/bin/env python 
#-*-coding:utf-8-*-

import  unittest
from page.login import *
from selenium import  webdriver

from page.init import Init

class LoginTest(Init,Login):

	def test_login(self,parent='login',value='nick'):
		'''验证：登录成功'''
		self.login()
		self.assertEqual(self.getNick(),self.getXmlUser(parent,value))

if __name__ == '__main__':
	unittest.main(verbosity=2)


