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

print type(data_de[0])

data_de1=data_de.copy()

#print data_de1.drop([0],axis=1)这个是正经的删除操作

list_t=data_de1.pop(1)
list_s=data_de1.pop(0)#这个pop是真实的删除 不能删除到一点都不剩(空dataframe用不了)
list_nan=data_de1.pop(2)

data_de1[0]=list_t#dataframe有一些东西需要初始化的
data_de1[1]=list_s

#print data_de1

data_add=pd.concat([data_de1,data_en])#是concat

data_add = data_add.reset_index(drop=True)

print data_add

data_add.to_pickle('en-de-all-rough.pkl')
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
