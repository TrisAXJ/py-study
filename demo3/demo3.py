# -*- codeing = utf-8 -*-
# @Author:TRISA QQ:1628791325 trisanima.cn
# @Time : 2021/1/22 18:10
# @File : demo3.py
# @Software: PyCharm


'''
print("----text----1-----")

f = open("demo3.txt","r")       # 用只读模式打开了一个不存在的文件，报错

print("----text----2-----")     # 这句代码不会被执行
'''

# 捕获异常
'''
try:
    print("----text----1-----")

    f = open("demo3.txt","r")

    print("----text----2-----")

except IOError:         # 文件没找到属于IO异常（输入输出异常）
    pass                # 捕获异常后，执行的代码
'''

'''

try:
    print(num)
# except IOError:       # 异常类型想要被捕获，需要一致
except NameError:
    print("产生错误")
'''

'''
try:
    print("----text----1-----")
    f = open("demo3.txt","r")
    print("----text----2-----")
    print(num)
except (IOError,NameError):     # 将可能产生的所有异常类型，都放到下面的小括号中
    print("产生错误")
'''

# 获取错误描述
'''
try:
    print("----text----1-----")
    f = open("demo3.txt","r")
    print("----text----2-----")
    print(num)
except (IOError,NameError) as result:     # 将可能产生的所有异常类型，都放到下面的小括号中
    print("产生错误")
    print(result)
'''

# 捕获所有异常
'''
try:
    print("----text----1-----")
    f = open("demo3.txt","r")
    print("----text----2-----")
    
    print(num)
except Exception as result:     # Exception可以承接所有异常
    print("产生错误")
    print(result)
'''


# try.....finally 和嵌套

import time

try:
    f = open("text1.txt","r")

    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(1)
            print(content,end="")
    finally:
        f.close()
        print("\n文件关闭")

except Exception as result:
    print("发生异常。。")



















