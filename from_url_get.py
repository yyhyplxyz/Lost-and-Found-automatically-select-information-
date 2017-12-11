# -*- coding: utf-8 -*-
import urllib
import xlrd
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')
today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
f = open( "失物招领信息.txt", "r" )
urls = []
workbook =  xlrd.open_workbook('失物招领信息.xlsx')
workbook = workbook.sheets()[0]
row_num = workbook.nrows
index = []
for i in range(1, row_num):
    row = workbook.row_values(i)
    #print workbook.cell(i,13).value
    #print today
    time = xlrd.xldate.xldate_as_datetime(workbook.cell(i,13).value, 0)
    time = str(time)
    print time
    if row[6] != "" and today in time:
        index.append(row[0])
for line in f:
    urls.append(line)
num = 1
print index
for i in range(1,len(urls)):
    path = 'text_pics/'+(str(index[num - 1]))+'.png'
    num += 1
    f = open(path,'wb')
    f.write(urllib.urlopen(urls[len(urls) - i]).read())
    f.close()
f.close()
