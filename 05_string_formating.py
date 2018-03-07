#!/usr/bin/python
#coding:utf-8

width = input("please enter width:")

price_width = 10
item_width = width - price_width

header_format = '%-*s%*s'
format        = '%-*s%*.2f'

print '=' * width

print header_format % (item_width,'Item',price_width,'Price')

print '-' * width

print format % (item_width, 'Apples', price_width, 0.4)
print format % (item_width, 'Pears', price_width, 0.9)
print format % (item_width, 'Cantaloups', price_width, 1.4)
print format % (item_width, 'Banana', price_width, 2.5)
