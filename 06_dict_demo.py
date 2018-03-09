#!/usr/bin/python
#-*-coding:utf-8-*-

# 简单数据库-字典示例
# author : dh

people = {
	'Alice': {
		'phone': '2341',
		'addr': 'Foo drive 23'
	}
	'Beth': {
		'phone': '9102',
		'addr': 'Bar street 42'
	}
	'Cecil': {
		'phone': '3158',
		'addr': 'Baz avenue 90'
	}

}

labels = {
	'phone': "phone number",
	'addr': "address"
}

name = raw_input('Name:')

if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

if name in people: print "%s's %s is %s." % (name, lables[key],people[name][key])
