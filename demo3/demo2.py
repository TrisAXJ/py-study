# -*- codeing = utf-8 -*-
# @Author:TRISA QQ:1628791325 trisanima.cn
# @Time : 2021/1/22 17:43
# @File : demo2.py
# @Software: PyCharm

'''
f = open("text.txt","w")    # 打开文件，w模式（写模式），文件不存在就新建

f.write("hello world, i am here!")

f.close()       # 关闭文件

'''

'''     # read方法，读取指定的字符，开始时定位在文件头部，每执行一次向后移动指定字符数

f = open("text.txt","r")

content = f.read(5)

print(content)          # (hello)

content = f.read(5)

print(content)          # ( worl)

f.close()
'''


'''
f = open("text.txt","r")

content = f.readlines()     #一次性读取全部文件为列表，每行为一个字符串元素

print(content)

i = 1
for temp in content:
    print("%d:%s"%(i,temp))
    i += 1


f.close()
'''


'''
f = open("text.txt","r")

content = f.readline()
print("1:%s"%content,end="")

content = f.readline()
print("2:%s"%content)

content = f.readline()
print("3:%s"%content)

f.close()
'''


import os

# 文件重命名
# os.rename("text.txt","text1.txt")

# 删除文件
# os.remove("x.*")

# 创建文件夹
# os.mkdir("wenjianjia")

# 获取当前目录
# os.getcwd()

# 改变默认目录
# os.chdir("../")

# 获取目录列表
# os.listdir("./")

# 删除文件夹
# os.rmdir("wenjianjia")






