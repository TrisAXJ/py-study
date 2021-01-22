# -*- codeing = utf-8 -*-
# @Author:TRISA QQ:1628791325 trisanima.cn
# @Time : 1/12/2021 5:38 PM
# @File : demo2.py
# @Software: PyCharm


# namelist = ["小张", "小王", "小李"]

'''
#namelist = []       #定义一个空的列表
namelist = ["小张", "小王", "小李"]

testlist = [1, "测试"]         # 列表中可以存储混合类型
print(type(testlist[0]))
print(type(testlist[1]))

print(namelist[0])
print(namelist[1])
print(namelist[2])
'''

'''

for name in namelist:
    print(name)

#print(len(namelist))        # len()可以得到列表长度
length = len(namelist)
i = 0
while i<length:
    print(namelist[i])
    i += 1
'''

# print(namelist[0:2:1])





# 增：    【append】    # 在末尾追加一个元素作为整体
'''
print("----增加前名单列表数据----")
for name in namelist:
    print(name)

nametemp = input("请输入添加学生的姓名：")
namelist.append(nametemp)                   # 在末尾追加一个元素

print("----增加后名单列表数据----")
for name in namelist:
    print(name)
'''

# 增：    【extend】    # 逐一追加列表
'''
a = [1,2]
b = [3,4]
a.append(b)     # 当列表当作一个元素，加入到a列表中
print(a)        # [1,2,[3,4]] 列表嵌套

a.extend(b)     # 将b列表中的每个元素，逐一追加到a列表中
print(a)
'''


# 增：    【insert】    # 指定下标位置插入元素
'''
a = [0,1,2]
a.insert(1,3)   # 第一个变量表示下标，第二个表示元素（对象）
print(a)        # 【0，3，1，2】
'''









# 删：    【del】,【
'''
movieName = ["加勒比海盗","黑客帝国","第一滴血","指环王","速度与激情","指环王"]

print("----删除前电影列表数据----")
for name in movieName:
    print(name)

#del movieName[2]               # 在指定位置删除一个元素
#movieName.pop()                # 弹出末尾最后一个元素
#movieName.remove("指环王")      # 直接删除指定内容的元素(重复只会删除第一个)

print("----删除后电影列表数据----")
for name in movieName:
    print(name)
'''




# 改：    【
'''
print("----修改前名单列表数据----")
for name in namelist:
    print(name)

namelist[1] = "小红"         # 修改指定下标的元素内容

print("----修改后名单列表数据----")
for name in namelist:
    print(name)
'''




# 查： 【in, not in】
'''
findName = input("请输入你要查找的学生姓名:")

if findName in namelist:
    print("找到了相同名字")
else:
    print("没有找到")
'''





# index索引

mylist = ["a","b","c","a","b"]

'''
print(mylist.index("a",1,4))    # 可以查找指定下标范围的元素，并返回找到对应数据的下标

print(mylist.index("a",1,3))    # 范围区间，左闭右开 [1,3)
                                # 找不到会报错
'''

# count统计
'''
print(mylist.count("c"))        # 统计某个元素出现次数
'''


# 排序和反转
'''
a = [1,4,2,3]
print(a)
a.reverse()         # 将列表所有元素反转
print(a)

a.sort()            # 排序升序
print(a)

a.sort(reverse=True)# 排序降序
print(a)
'''





# 嵌套

#schoolNames = [[],[],[]]        # 有三个元素的空列表，每个元素都是一个空列表
'''
schoolName = [["北京大学","清华大学"],["南开大学","天津大学","天津大学"],["山东大学","中国海洋大学"]]

print(schoolName[0][0])
'''



###################################
# 综合练习：8个老师 3个办公室随机分配
'''
import random
offices = [[],[],[]]

names = ["a","b","c","d","e","f","g","h"]

for name in names:
    index = random.randint(0,2)
    offices[index].append(name)

i = 1
for office in offices:
    print("办公室%d 的人数为：%d"%(i,len(office)))
    i += 1
    for name in office:
        print("%s"%name,end="\t")
    print("\n")
    print("-"*20)
'''


######################################################
# 课后作业

products = [["iphone",6888],["MacPro",14800],["小米5",2499],["Coffee",31],["Book",60],["Nike",699]]
print("-"*6 + "  商品列表  " + "-"*6)

i = 0
for product in products:
    products[i].insert(0, i)
    for name in product:
        print("%s" % name, end="\t")
    i += 1
    print("\n", end="")

buy = []
for i in range(100):
    num = input("请输入要加入购物车的产品序号：")
    if num.isdigit():
        num = int(num)
        if num < 0 or num > len(products)-1:
            print("输入有误，请重新输入")
            continue
        else:
            buy.append(num)
    elif num.isalpha() and num == "q":
        break
    else:
        print("输入有误，请重新输入")
        continue

buy.sort()

print("-"*6 + "购物车中的商品" + "-"*6)
price = 0
i = 0
for thing in buy:
    i = 0
    for product in products:
        if product[0] == int(thing):
            for name in product:
                print("%s" % name,end="\t")
            print("\n",end="")
            price += products[i][2]
        i += 1

print("商品总价是：%d" % price)
