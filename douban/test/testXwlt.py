# -*- codeing = utf-8 -*-
# @Author:TRISA QQ:1628791325 trisanima.cn
# @Time : 2021/4/7 22:39
# @File : testXwlt.py
# @Software: PyCharm


import xlwt
'''
workbook = xlwt.Workbook(encoding="utf-8")  # 创建workbook
worksheet = workbook.add_sheet('sh1')       # 创建工作表
worksheet.write(0,0,"hello")                # 写入数据，第一行参数“行”，第二列 第三参数内容
workbook.save('student.xls')
'''

workbook = xlwt.Workbook(encoding="utf-8")  # 创建workbook
worksheet = workbook.add_sheet('sh1')       # 创建工作表
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d *%d = %d"%(i+1,j+1,(i+1)*(j+1)))

workbook.save('student.xls')


