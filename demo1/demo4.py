# -*- codeing = utf-8 -*-
# @Author:TRISA QQ:1628791325 trisanima.cn
# @Time : 1/11/2021 10:24 PM
# @File : demo4.py
# @Software: PyCharm
'''
for i in range (5):
    print(i)
'''

'''
for i in range(0, 10, 2):
    print(i)       # 输出为 0 2 4 6 8 ；步进完判断 <10
'''

'''
for i in range(-10, -100, -20):
    print(i)
'''

'''
name = "chengdu"

for x in name:            # 对字符串里面遍历
    print(x,end="\t")
'''

'''
a = ["aa","bb","cc","dd"]
for i in range(len(a)):    # len(a)
    print(i,a[i])
'''

'''
i = 0
while i < 5 :
    print("当前是第%d次执行循环"%(i+1),end="\t")
    print("i=%d"%i)
    i += 1
'''
''' # 1~100 求和
i = 0
a = 0
n = 100
while i < n:
    i += 1
    a += i
print("结果：%d" % a)
'''

'''
count = 0
while count < 5:
    print(count,"小于5")
    count += 1                  # 最后一个循环结束 count = 5 不满足 while 条件
else:                           # 不满足whlie条件执行 else语句段
    print(count,"大于等于5")
'''

'''
i = 0
while i < 10:
    i = i + 1
    print("-"*30)    # -输出30次 一条横线
    if i == 5:
        break        # 结束整个（while）循环
    print(i)
'''

'''
i = 0
while i < 10:
    i = i + 1
    print("-"*30)   # -输出30次 一条横线
    if i == 5:
        continue    # 跳过本次（while）循环 continue 后面的所有语句
    print(i)
'''
##########################################################################
# 课后作业
'''
i = 1
j = 1
for i in range (1,10,1):
    print("",end="\n")
    for j in range(1,10,1):
        k = j * i
        if i < j:
            continue
        print("%d*%d=%d" % (i, j, k),end="\t")
'''

# 答案
'''
for i in range(1,10):
    for j in range(1,i+1):
   
        print("%d*%d=%d"%(i,j,i*j), end=" ")
    print("")
'''
