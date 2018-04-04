#!/usr/bin/env python
#-*-coding:utf-8-*-

import  unittest
from selenium import  webdriver
from page.shopHu import *
from page.login import *
from page.init import Init


class LoginTest(Init,ShopHu,Login):

	def test_addShop(self):
		'''验证：添加商户'''
		self.login()
		self.isAddShop()
		self.clickMnnage()
		shopName=self.getShopName()
		self.delShop()
		self.assertEqual(shopName, u'123456')

if __name__ == '__main__':
	unittest.main(verbosity=2)


