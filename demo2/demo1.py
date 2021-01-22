# -*- codeing = utf-8 -*-
# @Author:TRISA QQ:1628791325 trisanima.cn
# @Time : 1/12/2021 5:03 PM
# @File : demo1.py
# @Software: PyCharm

'''
word = '字符串'
sentence = "这是一个句子"
paragraph = """             # 保留输入的所有格式
        这是一个段落
        可以由多行组成
"""

print(word)
print(sentence)
print(paragraph)
'''
'''
#my_str = "I'm a student"
my_str = 'I\'m a student'       # \'转义 告诉解释器不是配对的单引号
print(my_str)
'''
'''
#my_str = "Jason said \"I like you\""
my_str = 'Jason said "I like you"'
print(my_str)
'''

'''
str = "chengdu"

print(str)
print(str[0])
print(str[0:5])     # [起始位置:结束位置:步进值]
print(str[1:7:2])   # [输出包含:输出不含: ]

print(str[:5])      # cheng [输出包含:输出不含: ]
print(str[5:])      # du

print(str + ",hello" + "." +"!")
print(str * 3 )     # 打印3次
print(str + "1"*3)  # chengdu111
'''
'''
print("hello\nchengdu")         # 使用反斜杠，实现转义字符的功能
print(r"hello\nchengdu")        # 在字符串前加r，表示直接显示原始字符串，不进行转义
'''

# 字符串常见操作
# bytes.decode(encoding="utf-8", errors="strict")
# Python3中没有decode方法，
# 但我们可以使用bytes对象的decode()方法来解码给定的 bytes对象，
# 这个bytes对象可以由str.encode()来编码返回。

# encode(encoding='UTF-8' ,errors='strict')
# 以encoding指定的编码格式编码字符串，
# 如果出错默认报一个ValueError的异常，
# 除非errors指定的是'ignore'或者'replace'

# isalnum()
# 如果字符串至少有一个字符并且所有字符都是字母或数字则返回True,否则返回False

# isalpha()
# 如果字符串至少有一个字符并且所有字符都是字母则返回True，否则返回False

# isdigit()
# 如果字符串只包含数字则返回True否则返回False.

# isnumeric()
# 如果字符串中只包含数字字符，则返回True，否则返回False
# 与isalnum的区别 百度

# join(seq)
# 以指定字符串作为分隔符，
# 将seq中所有的元素(的字符串表示)合并为一个新的字符串

# len(string)
# 返回字符串长度

# lstrip() rstrip()
# 截掉字符串左边/右边的空格或指定字符。

# split(str="",num=string.count(str))num=string.count(str))
# 以str为分隔符截取字符串，
# 如果num有指定值，则仅截取num+1个子字符串













