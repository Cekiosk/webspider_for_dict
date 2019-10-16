#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import re
import numpy as np
import pandas as pd
import pickle


#运行 trans getstr后 运行这个
#来吧pandas！
#
#data=pd.read_csv("enplustest.csv", encoding="utf-8",header=None)

datajson=pd.read_csv("dejson.csv", encoding="utf-8",header=None)
# print(data.shape[0])#求得dataframe的大小
# print(datajson[0][5])
#
# dict_length=data.shape[0]
#
# dictaa={}
#
# listaa=[]
# def make_utf8(str):
# 	return str.encode('utf-8')
#
# for i in range(0,dict_length):
#
# #这个部分是两边去空格
# 	str_en=str(data[0][i]).encode('utf-8').strip()
# 	str_de=str(data[1][i]).encode('utf-8').strip()
#
# #	print str_en
# #	print str_de
# #这个部分是切割list
# 	list_derou=(str_de.split(";"))
# 	list_de= [s.strip() for s in list_derou]
# #	print(list_de.count(""))
# 	if "" in list_de:
# 		for i in range(list_de.count("")):
# 			list_de.remove("")
# 	print list_de

#	list_de_utf8 = list(map(make_utf8,list_de))

#	print list_de_utf8
#	dictaa[str_en] = list_de

#开始series

#print data[0]

####################
#sdata=pd.Series(data[0])
sdata=pd.read_pickle("all-series.pkl")
sjson=pd.Series(datajson[0])
#sjson=pd.read_pickle("all-series.pkl")
#sdata=sdata.map(str)#就是字符串化



listdict=sdata.tolist()
############################
#print listdict
#print sjson[sjson.isin(listdict)]

#################
list_result=list(sjson.isin(listdict))

print list_result.count(True)
print len(list_result)
##############
#打包数据
# with open('dict_ed4de_py27.pkl','wb') as fr:
#     pickle.dump(dictaa,fr,protocol=2)

# with open("instance.csv", "r") as csvFile:
#     dict_reader = csv.DictReader(csvFile)
# for i in dict_reader:
#     print(i)

# dictf=os.path.join("newdict2.txt")
# with open(dictf,encoding='utf-8') as f:
#     data= f.readline()
#
# print(data)

#data_splited=re.split('#fenggefu#', data)
#print(data_splited)
