# -*- codeing = utf-8 -*-
# @Author:TRISA QQ:1628791325 trisanima.cn
# @Time : 2021/1/22 16:51
# @File : demo1.py
# @Software: PyCharm


# 函数的定义
'''
def printinfo():
    print("----------------------------")
    print("       人生苦短，我用py       ")
    print("----------------------------")


# 函数的调用

printinfo()

'''

# 带参数的函数
'''
def add2Num(a,b):
    c = a + b
    print(c)

add2Num(11,22)

'''

# 带返回值的函数
'''
def add2num(a,b):
    return a + b    #通过return来返回运算结果

result = add2num(11,22)
print(result)
#print(add2num(11,22))

'''

# 返回多个值的函数
'''
def divid(a,b):
    shang = a//b
    yushu = a%b
    return shang,yushu      # 多个返回值用逗号分隔

sh,yu = divid(5,2)      # 需要使用多个值来保持返回的内容

print("商：%d，余数：%d"%(sh,yu))

'''


# 全局变量和局部变量
'''
def test1():
    a = 300     # 局部变量
    print("test1---------修改前：a = %d" % a)
    a = 100
    print("test1---------修改后：a = %d" % a)


def test2():
    a = 500    
    print("test2---------：a = %d" % a)


test1()
test2()
'''
'''
a = 100     # 全局变量


def test1():

    print(a)


def test2():
    print(a)


test1()
test2()
'''


# 全局变量和局部变量相同名字
'''

a = 100

def test1():
    a = 300     # 局部变量优先使用
    print("test1---------修改前：a = %d" % a)
    a = 200
    print("test1---------修改后：a = %d" % a)


def test2():
    print("test2---------：a = %d" % a)  # 无局部变量，默认使用全局变量


test1()
test2()

'''

# 在函数中修改全局变量

a = 100

def test1():
    global a       # 声明全局变量在函数中的标识符
    print("test1---------修改前：a = %d" % a)
    a = 200
    print("test1---------修改后：a = %d" % a)


def test2():
    print("test2---------：a = %d" % a)  # 无局部变量，默认使用全局变量

test1()
test2()










