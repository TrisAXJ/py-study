# -*- codeing = utf-8 -*-
# @Author:TRISA QQ:1628791325 trisanima.cn
# @Time : 2021/1/24 15:35
# @File : testre.py
# @Software: PyCharm

#

# 正则表达式：字符串模式（判断字符串是否符合一定的标准）

import re
# 创建模式对象

pat = re.compile("AA")      # 此处的AA，是正则表达式，用来去验证其他的字符串
# m = pat.search("CBA")      # search字符串被校验的内容

# m = pat.search("ABCAA")     # <re.Match object; span=(3, 5), match='AA'>
# m = pat.search("AABCAADDCCAA")      # search方法，进行比对查找

# 没有模式对象
# m = re.search("asd","Aasd")     # 前面的字符串是规则（模板），后面的字符串是被校验的对象
# print(m)


# print(re.findall("a","ASDaDFGAa"))      # 前面字符串是规则（正则表达式），后面字符串是被校验的字符串；re.findall()返回列表

# print(re.findall("[A-Z]","ASDaDFGAa"))      # ['A', 'S', 'D', 'D', 'F', 'G', 'A']

# print(re.findall("[A-Z]+","ASDaDFGAa"))     # ['ASD', 'DFGA']


# sub

# print(re.sub("a", "A", "abcdcasd"))       # 找到a 用A替换，在第三个字符串中查找； 输出：AbcdcAsd

# 建议在正则表达式中，被比较的字符串前面加上r，不用担心转义字符的问题
# a = r"\aabd-\'"
# print(a)


