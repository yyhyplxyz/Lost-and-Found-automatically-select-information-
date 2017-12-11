# -*- coding: utf-8 -*-
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')
today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
print today
#print today
import xlrd
def gettext():
    workbook =  xlrd.open_workbook('失物招领信息.xlsx')
    workbook = workbook.sheets()[0]
    row_num = workbook.nrows
    list = []
    for i in range(1,row_num):
        row = workbook.row_values(i)
        time = xlrd.xldate.xldate_as_datetime(workbook.cell(i,13).value, 0)
        time = str(time)
        if today in time:
            #print str(row[13])
            app = []
            for j in range(7):
                app.append(row[j])
            app.append(row[10])
            app.append(row[0])
            list.append(app)
    print(list)
    for i in list:
        path = 'text_pics/'+str(i[-1])+'.txt'
        file_object = open(path, 'w')
        #file_object.write(' ')
        for j in range(1,7):
            if(i[j] == ''):
                i[j] = '未知'
        file_object.write('检获物品种类：'+i[4]+'\n')
        file_object.write(i[7]+'\n')
        file_object.write('检获者姓名：'+i[1]+'\n')
        file_object.write('手机：'+i[2]+'\n')
        file_object.write('微信：'+i[3]+'\n')
        file_object.write('检获地点：'+i[5]+'\n')
        file_object.write('\n')
        file_object.write('\n')
        file_object.close( )
    return list

if __name__ == "__main__":
    gettext()
