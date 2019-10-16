#encoding=utf-8
import sys
reload(sys) 
sys.setdefaultencoding('utf8') 

import os
import re
import numpy as np
import pandas as pd
import pickle


#来吧pandas！

data=pd.read_csv("ed_de.csv", encoding="utf-8",header=None)
print(data.shape[0])#求得dataframe的大小
print(data[1][5])

dict_length=data.shape[0]

dictaa={}
def make_utf8(str):
	return str.encode('utf-8')

for i in range(0,dict_length):


	str_en=str(data[0][i]).encode('utf-8').strip()
	str_de=str(data[1][i]).encode('utf-8').strip()

	print str_en
#	print str_de

	list_de=(str_de.split(";"))

#	print list_de

#	list_de_utf8 = list(map(make_utf8,list_de))

#	print list_de_utf8
	dictaa[str_en] = list_de

#	print dictaa


with open('dict_ed4de_py27.pkl','wb') as fr:
    pickle.dump(dictaa,fr,protocol=2)

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