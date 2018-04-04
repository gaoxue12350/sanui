#!/usr/bin/env python
#-*-coding:utf-8-*-

from selenium import  webdriver
import  unittest
from utils.helper import DataHelper



class SingTest(unittest.TestCase,DataHelper):
	def setUp(self):
		self.driver=webdriver.Firefox()
		self.driver.maximize_window()
		self.driver.get('http://mail.sina.com.cn/#')
		self.driver.implicitly_wait(30)

	def tearDown(self):
		self.driver.quit()

	def test_usernameNull_password(self):
		'''验证：用户名为空,密码不为空,验证错误提示信息'''
		self.driver.find_element_by_id('freename').send_keys(self.getTxt()[0])
		self.driver.find_element_by_id('freepassword').send_keys(self.getTxt()[1])
		self.driver.find_element_by_link_text(u'登录').click()
		error_text = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]').text
		self.assertEqual(error_text,''.join(self.getTxt()[2].split('\n')).decode('utf-8'))

	def test_username_password_null(self):
		'''验证：用户名权为空，密码为空的错误提示信息'''
		self.driver.find_element_by_id('freename').send_keys(self.getTxt()[3])
		self.driver.find_element_by_id('freepassword').send_keys(self.getTxt()[4])
		self.driver.find_element_by_link_text(u'登录').click()
		error_text = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]').text
		self.assertEqual(error_text,self.getTxt()[5].decode('utf-8'))

if __name__ == '__main__':
	unittest.main(verbosity=2)
