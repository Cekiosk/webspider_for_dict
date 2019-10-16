import os
import re
import numpy as np
import pandas as pd
import pickle
import time
import random
from random import randint#使用randint需要加上这句
import querydict_spy

# counter=pd.DataFrame([
#     [1]
# ])#保存一个计数器
#sdata=pd.read_pickle("all-series.pkl")

#------------------------外部计数变量存储器-----------------------
counter=pd.read_pickle("counter.pkl")
cn_flag=counter.loc[0, 0]#即上次爬到了第几个
 #改变这个外部变量


datajson=pd.read_csv("dejson_index.csv", encoding="utf-8",header=None)

datadict=datajson[0]
dictlen=len(datajson)
limit=dictlen


for i in range(cn_flag+1,limit):#这个是对整个词表的循环
#---------------------------定时器
    a = randint(250, 780)  # 设置等待时间
    b = a / 100
    print(b)
    time.sleep(b)

#----------------------------追加到文件末尾
    fengge=" #f# "

    datatrans=querydict_spy.tans_spy(datadict[i])#在这一步查询 datadict是一个所有待查词的列表

    result_dict=str(datajson[1][i])+fengge+str(datadict[i])+fengge+str(datatrans)+fengge+"\n"#id+ 源词 +json结果
    print(result_dict)

    with open("final_resultIP96.txt", "a",encoding='utf-8') as fp:
        fp.write(result_dict)
    counter.loc[0, 0] = datajson[1][i]#当前存储成功的词的序号
    counter.to_pickle('counter.pkl')#保存成功变量



# a
# 打开一个文件用于追加（只写），写入内容为str
# 如果该文件已存在，文件指针将会放在文件的结尾，新的内容将会被写入到已有内容之后
# 如果该文件不存在，创建新文件进行写入
# file = open('test.txt', 'a')
# 创建一个空文件
# file = open('text.txt', 'a')
# file.write('aaa')
# file.close()
# file = open('text.txt')
# print(file.read())
# file.close()

# 关闭打开的文件
