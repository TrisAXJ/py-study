# -*- codeing = utf-8 -*-
# @Author:TRISA QQ:1628791325 trisanima.cn
# @Time : 1/11/2021 5:45 PM
# @File : demo3.py
# @Software: PyCharm
################################

'''
if 1:               #100 0 22
    print("True")
else:
    print("False")
print("end")

'''

###################################
# score = int(input("输入成绩"))
'''
if score>=90:
    print("A")
else:
    if score>=80:
        print("B")
    else:
        print("C")
'''

'''
if score>=90:
    print("A")
elif score>=80:
    print("B")
elif:
#else:
    print("C")
'''
####################################
'''
import random       # 导入相应模块 from.....import....

x = random.randint(0, 2)    # 随机生成0-2的随机数

print(x)
'''
####################################
# 课后作业
'''
a = int(input("请输入：剪刀0、石头1、布2："))
import random

x = random.randint(0,2)

if a > 2 and a < 0:
    print("输入错误")
else:
    if a == x:
        print("平局")
    elif a == 0 :
        if x == 1:
            print("你输了!")
        elif x == 2:
            print("你赢了!")
    elif a == 1:
        if x == 0:
            print("你输了!")
        elif x == 2:
            print("你赢了!")
    elif a == 2:
        if x == 0:
            print("你输了!")
        elif x == 1:
            print("你赢了!")
'''
###########
'''
import random

print()
print("*******欢迎来到猜拳滋戏********")
print("***********游戏规则************")
print( "*******0-剪刀 1-石头 2-布******")
print("***********开始PK************\n")
count1, count2 = 0, 0
f = 0
y = int(input("请输入你的数字:"))
r = random.randrange(0, 2)
print("玩家∶", y, "  电脑:", r)
c = y - r
if c == -2 or c == 1:
    count1 +=1
    print("呜呜你赢了!\n")
elif c == 0:
    print("平局! \n")
else:
    count2 += 1
    print("哈哈你输了! \n")
'''
##################################
