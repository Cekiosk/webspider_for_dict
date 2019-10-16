# encoding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import os
import re
import numpy as np
import pandas as pd
import pickle

#data = pd.read_csv("enplustest.csv", encoding="utf-8", header=None)

data_en=pd.read_pickle("en-list-atom.pkl")
data_de=pd.read_pickle("de-list-atom.pkl")
data_all=pd.read_pickle("en-de-all-rough.pkl")
def joinstr(x):
    return "".join(x)

listtt=[['ddd','ssa'],['sassa']]
listt=map(lambda x: "".join(x),listtt)#返回对每个元素实施过f的list

sdata_all=pd.Series(data_all[1].map(lambda x: "".join(x)))

print sdata_all

sdata_all.to_pickle('all-series.pkl')



#print joinstr(listtt[0])



#data_add['']=data_en[1]
#print data_add
#datanew=data

#删除和添加操作
#
# datalist= datalist.drop(3)
#
# datalist = datalist.append(datalist.loc[2:2],ignore_index=False)
#
# print(datalist)
#
# print datalist[0][2]
#
# for i in range(0, len(datalist)):
#     if len(datause[1][i])>1:
#         #print datause[1][i]
#         #print len(datause[1][i])
#         pass;
# #         print data.iloc[i][0]


#datanew=datanew.drop(1)

# pat_space= re.compile(r'.*[ ].*')
#
#
# for i in range(0, len(data)):
#      if re.match(pat_space,data.iloc[i][0])!=None:
#          datanew = datanew.drop(i)
#
#
# #         print data.iloc[i][0]
#
# data[1][3]=['aaa','bbs']
#
# print(data)
# print(datanew)
