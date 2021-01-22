# -*- codeing = utf-8 -*-
# @Author:TRISA QQ:1628791325 trisanima.cn
# @Time : 2021/1/14 21:56
# @File : teacher2.py
# @Software: PyCharm

# BMI指数（即身体质量指数，简称体质指数又称体重，英文为Body Mass Index，简称BMI），
# 是用体重公斤数除以身高米数平方得出的数字，是目前国际上常用的衡量人体胖瘦程度以及是否健康的一个标准。
# BMI小于等于18.4，偏瘦；18.4-23.9，正常；23.9-27.9，过重；大于28，肥胖
# 请用python编写程序，输出结果

for i in range(200):
    highm = float(input("请输入你的身高(cm)："))
    if highm < 40 or highm > 300:
        print("你的输入有误：请从新输入！")
        continue
    else:
        high = highm / 100
        break

for i in range(200):
    kg: float = float(input("请输入你的体重(kg)："))
    if kg < 10 or kg > 300:
        print("你的输入有误：请从新输入！")
        continue
    else:
        break

num = kg/(high*high)
num = round(num, 1)
print("你的BMI指数值为：%.1f" % num)

if 18.4 > num > 0:
    print("你的BMI指数表明你偏瘦")
elif num <= 23.9:
    print("你的BMI指数表明你体重正常")
elif num <= 27.9:
    print("你的BMI指数表明你偏胖")
else:
    print("你的BMI指数表明你肥胖")
