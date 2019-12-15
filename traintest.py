import pandas as pd
import math

def UserSimilatrity(train): 
    # build inverse table for item_users
    # 建立用户-物品的倒排表

    # 声明一个字典
    item_users=dict()
    # 遍历列表中的元素
    for book,user in train:
        # 如果物品没在里面
        if book not in item_users:
            # 以该物品为键，一个set为值，该set存放所有操作过物品的人
             item_users[book]=set()
        # 找到了，把人加进去
        item_users[book].add(user)


    # 上面的这一段完成后，item_user是一个以物品为键，包含操作过该物品的人的set为值的一个字典
    # ===============================================================================

    # calculate co-rated items between users
    C=dict()
    N=dict()
    # 遍历所有物品，i代表物品，users代表操作过该物品的人的集合
    for i,users in item_users.items():
        # 遍历操作过该物品的用户
        for u in users:
            # 用户每操作一个物品这个值就会加一，这个值记录了用户操作的物品总数
            if u not in N.keys():
                N[u]=0
            N[u] += 1
            # 再次遍历对该物品操作过的用户
            for v in users:
                # 同一个用户，忽略不计
                if u==v:
                    continue
                if (u,v) not in C.keys():
                    C[(u,v)]=0
                #为这两个用户+1，表示操作过同一个物品
                C[(u,v)]+=1
    # 这一步结束后得到两个字典，字典N记录每个用户操作的物品数，字典C记录每两个用户操作同一个物品的数量

    #calculate finial similarity matrix W
    W=dict()
    # 遍历C，键为两个关联用户的元组，值为操作过同一个物品
    for related_users,cuv in C.items():
            W[related_users]=cuv/math.sqrt(N[related_users[0]]*N[related_users[1]])
    return W

data = pd.read_csv("traindata.csv")
data2 = data.to_dict()
data_bookid=data2['bookid']
data_userid=data2['userid']
Z=[]
for i in data_bookid:
    t=(data_bookid[i],data_userid[i])
    Z.append(t)

W=UserSimilatrity(Z)
print('共有'+str(len(W))+'组成员有关联')
dict1={'a':2,'e':3,'f':8,'d':4}
list1=sorted(W.items(), key=lambda d:d[1], reverse=True)
print(list1[0:100])
