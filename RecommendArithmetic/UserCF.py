# %%
import pandas as pd
import time
import numpy as np
import math
df = pd.read_csv("D:\\code\\Python\\traindata.csv")
# %%
# 每个用户的借阅记录|user-item矩阵
user_item = df.groupby(['userid'])
item_user = df.groupby(['bookid'], sort=False)
# %%
# %%
user_same_count = pd.DataFrame(0, index=user_item.groups.keys(), columns=user_item.groups.keys(), dtype=np.int)
# %%
user_book_count = user_item.count()
# %%
for name, group in item_user['userid']:
    for x, y in group.items():
        for m, n in group.items():
            if not y == n:
                user_same_count.at[y, n] += 1
# %%
for i in range(0, user_same_count.columns.size-1):
    user_same_count.iat[i, i] = 0
#%%
user_similarity=user_same_count.div(user_book_count.dot(user_book_count.T).apply(lambda x:np.sqrt(x)))
# %%
for i in range(0,user_similarity.columns.size-1):
    for userid in user_similarity.iloc[1].nlargest(n=3).index:
        print(user_item.get_group(userid))