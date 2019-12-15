# coding=utf-8

import xlrd
import datetime
import init
import copy
import json
import json_handledatetime

# class DateEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, datetime.datetime):
#             return obj.strftime('%Y-%m-%d %H:%M:%S')
#         elif isinstance(obj, datetime.date):
#             return obj.strftime("%Y-%m-%d")
#         else:
#             return json.JSONEncoder.default(self, obj)
file = 'allrecords.xls'  # 文件自行建立

records_book = []
recordItem = init.Record()
records_reader = []

wb = xlrd.open_workbook(file)  # 打开文件
table = wb.sheet_by_name('book')

for index in range(table.nrows):  # 按行遍历表格
    if index < 5:
        continue
    mid = {'bookName': init.subs(str(table.row(index)[3])), 'reader': init.subs(str(table.row(index)[0])),
           'college': init.subs(str(table.row(index)[1])), 'time': init.subs(str(table.row(index)[7])),
           'status': init.subs(str(table.row(index)[6])), 'place': init.subs(str(table.row(index)[5]))}
    records_book.append(mid)

dataFile = 'records_book.json'

with open(dataFile, 'w+') as f:
    json.dump(records_book, f)

table = wb.sheet_by_name('reader')

for index in range(table.nrows):  # 按行遍历表格
    if index < 5:
        continue
    mid = {'bookName': init.subs(str(table.row(index)[3])), 'reader': init.subs(str(table.row(index)[0])),
           'time': init.subs(str(table.row(index)[7])),
           'status': init.subs(str(table.row(index)[6])), 'place': init.subs(str(table.row(index)[5]))}
    records_reader.append(mid)

dataFile = 'records_reader.json'

with open(dataFile, 'w+') as f:
    json.dump(records_reader, f)
# for i in range(len(records)):
#     json.dump(records[i], f)
