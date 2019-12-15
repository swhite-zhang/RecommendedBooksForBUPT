import math
import init

#评分预测误差
#records[i]=[user,item,realUserMark,predictUserMark]

records = []
#均方根误差分析


def RMSE(records):
    return math.sqrt(
        sum([(rui-pui)*(rui-pui) for u, i, rui, pui in records])
        / float(len(records)))
#平均绝对误差


def MAE(records):
    return sum([abs(rui-pui)for u, i, rui, pui in records])\
        / float(len(records))


#推荐率
def Recall(recommend,reader):
    hit=0
    all=len(recommend)
    for item in reader.records:
        if item in recommend:
            hit+=1
    return hit/(all*1.0)

#召回率
def Precision(recommend,reader):
    hit = 0  
    all = len(recommend)
    for item in recommend:
        if item in reader.records:
                hit += 1 
    return hit / (all*1.0)
