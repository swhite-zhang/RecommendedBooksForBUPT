# coding=utf-8

import xlrd
import init
import copy
import json
import matplotlib.pyplot as plt

# 读取记录
READERS = []

file = 'records_reader.json'

with open(file, 'r') as f:
    records = json.load(f)

reader_index = init.Reader()

reader_index.student_num = records[0]['reader']
reader_index.records.append(records[0])

for index in range(len(records)):
    if records[index]['reader'] != reader_index.student_num:
        reader_mid = copy.deepcopy(reader_index)
        reader_mid.grade = int(reader_index.records[0]['reader'][0:4])
        READERS.append(reader_mid)
        reader_index.clear()
        reader_index.student_num = records[index]['reader']
    reader_index.records.append(records[index])
reader_mid = copy.deepcopy(reader_index)
reader_mid.grade = int(reader_index.records[0]['reader'][0:4])
READERS.append(reader_mid)
print(READERS[len(READERS) - 1].student_num)

# 得到专业


file = 'allrecords.xls'
wb = xlrd.open_workbook(file)
table = wb.sheet_by_name('reader')

i = 0
READERS[i].majoy_in = init.subs(str(table.row(5)[1]))

for j in range(table.nrows):
    if j < 5:
        continue
    if READERS[i].student_num == init.subs(str(table.row(j)[0])):
        continue
    i += 1
    # print(READERS[i].student_num+'#'+str(table.row(j)[0]))
    READERS[i].majoy_in = init.subs(str(table.row(j)[1]))
    # mid = {'bookName': subs(str(table.row(index)[3])), 'reader': subs(str(table.row(index)[0])),
    #        'time': subs(str(table.row(index)[7])),
    #        'status': subs(str(table.row(index)[6])), 'place': subs(str(table.row(index)[5]))}
    # READERS[i].append(mid)
'''
得到label
for index in READERS:
    index.get_label()
'''

'''
得到热度
for index in READERS:
    index.get_heat()
'''

"""
画出柱状图

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(16, 9), dpi=80)

mouth = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

borrow_heat = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
return_heat = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

'''
大一
for i in range(len(READERS)):
    for j in range(12):
        if j > 7:
            borrow_heat[j] += READERS[i].heat_borrow[str(READERS[i].grade) + '-' + mouth[j]]
            return_heat[j] += READERS[i].heat_return[str(READERS[i].grade) + '-' + mouth[j]]
        else:
            if READERS[i].grade + 1 < 2019:
                borrow_heat[j] += READERS[i].heat_borrow[str(READERS[i].grade + 1) + '-' + mouth[j]]
                return_heat[j] += READERS[i].heat_return[str(READERS[i].grade + 1) + '-' + mouth[j]]
'''

'''
大二
for i in range(len(READERS)):
    for j in range(12):
        if READERS[i].grade + 1 < 2019:
            if j > 7:
                borrow_heat[j] += READERS[i].heat_borrow[str(READERS[i].grade+1) + '-' + mouth[j]]
                return_heat[j] += READERS[i].heat_return[str(READERS[i].grade+1) + '-' + mouth[j]]
            else:
                if READERS[i].grade + 2 < 2019:
                    borrow_heat[j] += READERS[i].heat_borrow[str(READERS[i].grade + 2) + '-' + mouth[j]]
                    return_heat[j] += READERS[i].heat_return[str(READERS[i].grade + 2) + '-' + mouth[j]]
'''

'''
2017级2017-2018学年每月借阅量和归还量
for i in range(len(READERS)):
    for j in range(12):
        if READERS[i].grade == 2017:
            if j > 8:
                borrow_heat[j] += READERS[i].heat_borrow[str(READERS[i].grade) + '-' + mouth[j]]
                return_heat[j] += READERS[i].heat_return[str(READERS[i].grade) + '-' + mouth[j]]
            else:
                if READERS[i].grade + 1 == 2018:
                    borrow_heat[j] += READERS[i].heat_borrow[str(READERS[i].grade + 1) + '-' + mouth[j]]
                    return_heat[j] += READERS[i].heat_return[str(READERS[i].grade + 1) + '-' + mouth[j]]
                                else:
                if READERS[i].grade + 1 == 2018:
                    borrow_heat[j] += READERS[i].heat_borrow[str(READERS[i].grade + 1) + '-' + mouth[j]]
                    return_heat[j] += READERS[i].heat_return[str(READERS[i].grade + 1) + '-' + mouth[j]]
'''

'''
2018级2018年每月借阅量和归还量

for i in range(len(READERS)):
    for j in range(12):
        if READERS[i].grade == 2018:
            if j > 7:
                borrow_heat[j] += READERS[i].heat_borrow[str(READERS[i].grade) + '-' + mouth[j]]
                return_heat[j] += READERS[i].heat_return[str(READERS[i].grade) + '-' + mouth[j]]


'''





x = range(len(mouth))
plt.bar(x, borrow_heat, width=0.2)
plt.bar([i + 0.2 for i in x], return_heat, width=0.2)

plt.xticks([i + 0.1 for i in x], mouth)

plt.xlabel('月份')
plt.ylabel('借阅/归还')
plt.title('')
plt.show()

"""

# for index in range(len(load))

# for index in range(len(READERS)):
#     print(READERS[index])
#     print(index)

# dataFile = 'reader.dat'
#
# with open(dataFile, 'w+') as f:
#     json.dump(READERS,f,cls=json_handledatetime.DateEncoder)

# for item in range(len(RECORDS)):
#     print(RECORDS[item])
#     print(item)

# def subs(string):
#     s = string[6:-1]
#     return s
#
#
# def getreader(reader, WSRow):
#     reader.studentNum = subs(str(WSRow[0]))
#     reader.grade = int(reader.studentNum[0: 4])
#     reader.majoyIn = subs(str(WSRow[1]))
#     nowRecord = {'bookName': subs(str(WSRow[3])), 'reader': subs(str(WSRow[0])),\
#                 'time': datetime.datetime.strptime(subs(str(WSRow[7])), '%Y-%m-%d %H:%M:%S'),\
#                 'status': subs(str(WSRow[6])), 'place': subs(str(WSRow[5]))}
#     reader.records.append(nowRecord)


#
# file = 'Records.xls' #文件自行建立
#
# wb = xlrd.open_workbook(file)  # 打开文件
# table = wb.sheets()[0]  # 通过索引顺序获取，返回xlrd.sheet.sheet()对象
#
# readerIndex = init.reader()
#
# i = 1
#
# for index in range(table.nrows):  # 按行遍历表格
#     if index == 0:
#         continue
#     if str(table.row(index)[0])[6:-1] != readerIndex.studentNum:
#         if index != 1:
#             readMid = copy.deepcopy(readerIndex)
#             READERS.append(readMid)
#         readerIndex.clear()
#         getreader(readerIndex, table.row(index))
#     else:
#         mid = {'bookName': subs(str(table.row(index)[3])), 'reader': subs(str(table.row(index)[0])),\
#                 'time': datetime.datetime.strptime(subs(str(table.row(index)[7])), '%Y-%m-%d %H:%M:%S'),\
#                 'status': subs(str(table.row(index)[6])), 'place': subs(str(table.row(index)[5]))}
#         readerIndex.records.append(mid)
