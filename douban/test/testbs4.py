# -*- codeing = utf-8 -*-
# @Author:TRISA QQ:1628791325 trisanima.cn
# @Time : 2021/1/23 11:34
# @File : testbs4.py
# @Software: PyCharm

# BeautifulSoup4将复杂HTML文档转换成一个复杂的树形结杓,每个节点都湿Python对象，所有对象TL归纳为4种:
# Tag
# NavigableString
# BeautifulSoup
# Comment


from bs4 import BeautifulSoup

file = open("./baidu.html","rb")
html_1 = file.read()
bs = BeautifulSoup(html_1,"html.parser")          # 用""解析 html_1 文档

# print(bs.title)
# print(bs.a)
# print(bs.head)
# print(type(bs.head))        # Tag
# 1.Tag 标签及其内容：拿到它所找到的第一个内容


#print(bs.title.string)      # 内容
#print(type(bs.title.string))
# 2.NavigableString     标签里的内容(字符串)

#print(bs.a.attrs)


#print(type(bs))
# 3.BeautifulSoup   表示整个文档



#print(bs.name)      # [document]
#print(bs)



# print(bs.a.string)
# print(type(bs.a.string))
# 4. Comment    是一个特殊的NavigableString,输出的内容不包含注释符号


#----------------------------------------------------------------------------------

# 文档的遍历

# print(bs.head.contents)
# print(bs.head.contents[1])

# 更多内容，搜索BeautifulSoup文档


# 文档的搜索

# 1.find_all()
# 字符串过滤：会查找与字符串完全匹配的内容
# t_list = bs.find_all("a")

import re
# 正则表达式搜索：使用search（）方法来匹配内容
#t_list = bs.find_all(re.compile("a"))


# 方法：传入一个函数（方法），根据函数要求来搜索 （了解）
# def name_is_exist(tag):
#     return tag.has_attr("name")
#
# t_list = bs.find_all(name_is_exist)
#
# for item in t_list:
#     print(item)

# print(t_list)




# 2.kwargs  参数

# t_list = bs.find_all(id="head")
# t_list = bs.find_all(class_=True)
# t_list = bs.find_all(href="http://news.baidu.com")

# for item in t_list:
#     print(item)


# 3.text参数

# t_list = bs.find_all(text="hao123")
# t_list = bs.find_all(text=["hao123","地图","贴吧"])
# t_list = bs.find_all(text=re.compile("\d"))     # （\d表示数字数字） 应用正则表达式来查找包含特定文本的内容（标签里的字符串）


# 4.limit 参数

# t_list = bs.find_all("a",limit=3)   # 限制个数
#
# for item in t_list:
#     print(item)


# css选择器

# t_list = bs.select('title')     # 通过标签来查找

# t_list = bs.select(".mnav")     # 通过类名来查找

# t_list = bs.select("#u1")       #通过id来查找

# t_list = bs.select("a[class='bri']")    # 通过属性来查找

# t_list = bs.select("head > title")      # 通过子标签来查找

# t_list = bs.select(".mnav ~ .bri")      # 通过兄弟标签来查找

# print(t_list[0].get_text())





# for item in t_list:
#     print(item)






