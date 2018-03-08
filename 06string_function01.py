# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 09:16:21 2018

@author: Dnt1024
"""
# 字符串方法
filename = 'span.txt'
filename.endswith('txt') # 检测字符串是否以txt结尾
# True
filename.startswith('span') # 检测字符串是否以span开始
# True

url = "https://www.baidu.com"
url.startswith('http') # True

choices = ('http', 'https')
url.startswith(choices) # True

# 查找字符串
string = 'I am dh'
string.find('am')
