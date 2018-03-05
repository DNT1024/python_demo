#!/usr/bin/python
#-*-coding:utf-8-*-

#检查用户名和PIN

database = [
	['donghui','123'],
	['wangqiang','235'],
	['zsw','134'],
	['yangqiaoqiao','234']
]

username = raw_input("User Name:")
pin = raw_input("PIN code:")

if [username,pin] in database:
	print "Access granted"
