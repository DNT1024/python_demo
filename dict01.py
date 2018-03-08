# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 07:59:12 2018

@author: dnt1024
"""
dic = {}  #创建一个空的字典
tel = {'donghui': 123, 'Rosi': 243, 'zankivik': 567}

tel['Rosi'] # 查询
tel['yang'] = 021 # 添加一个键值对
tel
# {'Rosi': 243, 'donghui': 123, 'yang': 17, 'zankivik': 567}

list(tel.keys()) # 返回keys
#['donghui', 'zankivik', 'Rosi', 'yang']

sorted(tel.keys()) # 对key进行排序
#['Rosi', 'donghui', 'yang', 'zankivik']

'Tom' in tel # 成员测试
#False

'yang' in tel # 成员测试
# True

# dict的构造
dict([('wg', 89), ('zq', 100), ('dy', 12)])
# {'dy': 12, 'wg': 89, 'zq': 100}

