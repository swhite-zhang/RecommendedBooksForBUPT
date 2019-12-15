# coding=utf-8

import copy
import xlrd
import init
import datetime
import json
import json_handledatetime
import matplotlib.pyplot as plt

BOOKS = []
record_file = 'records_book.json'
with open(record_file, 'r')as f:
    records = json.load(f)

book_index = init.Book()
book_index.name = records[0]['bookName']
book_index.records.append(records[0])

for index in range(len(records)):
    if records[index]['bookName'] != book_index.name:
        book_mid = copy.deepcopy(book_index)
        BOOKS.append(book_mid)
        book_index.clear()
        book_index.name = records[index]['bookName']
    book_index.records.append(records[index])

'''
# 写入文件book.json

dat = 'book.json'

with open(dat, 'w+')as f:
    json.dump(BOOKS, f, cls=json_handledatetime.obj_to_json)
'''
'''
得到热度

'''

# for i in range(len(BOOKS)):
#     for j in range(len(BOOKS[i].records)):
#         if BOOKS[i].records[j]['time'][0:7] == "'":
#             print(BOOKS[i].to_str())

for i in range(len(BOOKS)):
    BOOKS[i].get_heat()
'''
得到学院借阅量
for i in range(len(BOOKS)):
    BOOKS[i].get_college()
'''

'''
画出每月借阅归还热度图

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


plt.figure(figsize=(16, 9), dpi=80)

mouth = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

borrow_heat = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
return_heat = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(BOOKS)):
    for j in range(12):
        borrow_heat[j] += BOOKS[i].heat_borrow['2017-' + mouth[j]]
        borrow_heat[j] += BOOKS[i].heat_borrow['2018-' + mouth[j]]
        return_heat[j] += BOOKS[i].heat_return['2017-' + mouth[j]]
        return_heat[j] += BOOKS[i].heat_return['2018-' + mouth[j]]

x = range(len(mouth))
plt.bar(x, borrow_heat, width=0.2)
plt.bar([i + 0.2 for i in x], return_heat, width=0.2)

plt.xticks([i + 0.1 for i in x], mouth)

plt.xlabel('月份')
plt.ylabel('借阅/归还')
plt.title('每月借阅量和归还量')

plt.show()

'''

# def subs(string):
#     s = string[6:-1]
#     return s
#
#
# def getreader(book, WSRow):
#     book.name = subs(str(WSRow[3]))  # 书名
#     book.isbn = subs(str(WSRow[2]))  # 书籍号
#     nowRecord = {'bookName': subs(str(WSRow[3])), 'reader': subs(str(WSRow[0])), \
#                  'time': datetime.datetime.strptime(subs(str(WSRow[7])), '%Y-%m-%d %H:%M:%S'), \
#                  'status': subs(str(WSRow[6])), 'place': subs(str(WSRow[5]))}
#     book.records.append(nowRecord)  # 记录
#
#
#
#
# file = 'Records.xls'  # 文件自行建立
#
# wb = xlrd.open_workbook(file)  # 打开文件
# table = wb.sheet_by_name("book")  # 通过索引顺序获取，返回xlrd.sheet.sheet()对象
#
# # print(str(table.row(0)))
#
# for index in range(table.nrows):  # 按行遍历表格
#     if index == 0:
#         continue
#     if str(table.row(index)[2])[6:-1] != bookIndex.isbn:
#         if index != 1:
#             bookMid = copy.deepcopy(bookIndex)
#             BOOKS.append(bookMid)
#         bookIndex.clear()
#         getreader(bookIndex, table.row(index))
#     else:
#         mid = {'bookName': subs(str(table.row(index)[3])), 'reader': subs(str(table.row(index)[0])), \
#                'time': datetime.datetime.strptime(subs(str(table.row(index)[7])), '%Y-%m-%d %H:%M:%S'), \
#                'status': subs(str(table.row(index)[6])), 'place': subs(str(table.row(index)[5]))}
#         bookIndex.records.append(mid)

# dat = 'book.dat'
#
# with open(dat, 'w+') as data_operation:
#     for i in range(len(BOOKS)):
#         data_operation.write(BOOKS[i].to_str() + '\n')

# dat = 'book.json'
# #
# # with open('Records.json', 'r')as f:
# #     BOOKS = json.load(f)
#
# with open(dat, 'w')as f:
#     json.dump(BOOKS, f)
