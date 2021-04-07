# -*- codeing = utf-8 -*-
# @Author:TRISA QQ:1628791325 trisanima.cn
# @Time : 2021/1/22 21:31
# @File : spider.py
# @Software: PyCharm

from bs4 import BeautifulSoup   # 网页解析，获取数据
import re       # 正则表达式，进行文字匹配
import urllib.request,urllib.error      # 指定URL，获取网页数据
import xlwt     # 进行excel操作
import sqlite3  # 进行SQLite数据库操作



def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getData(baseurl)
    savepath = "豆瓣电影Top250.xls"

    # 3.保存数据
    saveData(datalist,savepath)

    # askURL("https://movie.douban.com/top250?start=")

# 影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')     # 创建正则表达式对象，表示规则（字符串的模式）
# 影片图片链接的规则
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)      # re.S 让换行符包含在字符中
# 影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')

findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')

findJudge = re.compile(r'<span>(\d*)人评价</span>')

findInq = re.compile(r'span class="inq">(.*)</span>')

findBd = re.compile(r'<p class="">(.*?)</p>',re.S)

# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10):        # 调用获取页面信息的函数，10次
        url = baseurl + str(i*25)
        html = askURL(url)      # 保存获取到的网页源码

        # 2.逐一解析数据
        soup = BeautifulSoup(html ,"html.parser")
        for item in soup.find_all('div',class_="item"):     # 查找符合要求的字符串，形成列表; class_加下划线表示类别
            #print(item)       # 测试：查看电影item全部信息
            data = []       # 保存一部电影的所有信息
            item = str(item)

            # 影片详情的链接
            link = re.findall(findLink,item)[0]     # re库用来通过正则表达式查找指定的字符串
            data.append(link)                       # 添加链接

            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc)

            titles = re.findall(findTitle,item)     # 片面可能只有一个中文名，没有外文名
            if(len(titles) == 2):
                ctitle = titles[0]                  # 添加中文名
                data.append(ctitle)
                otitle = titles[1].replace("/","")  # 去掉无关的符号 “/”
                data.append(otitle)                 #
            else:
                data.append(titles[0])
                data.append(' ')        # 外国名字留空

            rating = re.findall(findRating,item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)                       # 添加

            inq = re.findall(findInq,item)
            if len(inq) != 0 :
                inq = inq[0].replace("。","")
                data.append(inq)                            # 添加概述
            else:
                data.append(" ")

            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd)     # 去掉<br/>
            bd = re.sub('/'," ",bd)
            data.append(bd.strip())     # 去掉前后空格

            datalist.append(data)       # 把处理好的一部电影信息放入datalist
    # print(datalist)
    return datalist


# 得到指定一个URL的网页内容
def askURL(url):
    head = {            # 模拟浏览器头部信息，向豆瓣服务器发送信息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 87.0.4280.141Safari / 537.36"
    }
                        # 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（本质上是告诉服务器我们可以接受什么水平的文件内容）
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html





# 3.保存数据
def saveData(datalist,savepath):
    print("save....")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建workbook
    sheet = book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)       # 创建工作表
    col = ("电影详情链接","图片链接","影片中文名","影片外国名","评分","评价数","概况","相关信息")
    for i in range(0,7):
        sheet.write(0,i,col[i])  # 列名
    for i in range(0,250):
        print("第%d条" %i)
        data = datalist[i]
        for j in range(0,7):
            sheet.write(i+1,j,data[j])      # 数据

    book.save('student.xls')





if __name__ == "__main__":      # 当程序执行时
#调用函数
    main()