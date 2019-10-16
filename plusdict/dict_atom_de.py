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

datalist=pd.read_pickle("de-list.pkl")
datause=pd.read_pickle("model.pkl")
#datanew=data
#
# print datalist[1][3]
# print type(datalist[1][3])

#datause=datalist.copy()
datanew=datalist.copy()
#
#print datalist
#删除和添加操作
#
# datalist= datalist.drop(3)
#


#datalist = datalist.append(datause.loc[2:2],ignore_index=False)
#
#print(datalist.loc[1,0])#行，列
#print datause[1][5]

#listt= datause[1][2]#这里的list大小必须对应
#datalist.loc[1,0]=listt #[列][行] 赋值就用这个
#
# print(datalist.loc[1,0])#行，列
# print(datalist)
#print datause
############################
#
# T_list=datause[1][5]
# for j in range(0,len(T_list)):
#     print type(T_list[j])
#     newlist = (T_list[j].split(";"))
#     print newlist
#     datause.loc[6,1]=newlist
#     datause.loc[6,0]=datalist.loc[7,0]
#
# datause = datause.append(datause.loc[6:6],ignore_index=False)
# #↑基本上做完了一次添加
#
# print datause
##############################################3
# print datalist[0][2]
#

##########
for i in range(0, len(datalist)):#这里遍历的长度是原来那个
    T_list=datalist[1][i]#用于判定use的后方情况如何
    if len(T_list)>1:
        #print T_list
        for j in range(0,len(T_list)):
           # print type(T_list[j])
            listatom = (T_list[j].split(";"))

            datause.loc[6, 0]=datalist.loc[i,0]#行，列，填充左边
            datause.loc[6, 1] = listatom
            #print datalist[0][6]
            #print datalist[1][6]
            datanew=datanew.append(datause.loc[6], ignore_index=False)
        datanew = datanew.drop(i)

datanew = datanew.reset_index(drop=True)
            #
            # datalist.loc[6, 1] = listatom #右边
            # datalist.loc[6, 0] = datause.loc[i,0]#左边
            # datause = datause.append(datalist.loc[6:6], ignore_index=False)

print datanew
datanew.to_pickle('de-list-atom.pkl')
#######################
        #print len(datause[1][i])
        #pass;
#         print data.iloc[i][0]

