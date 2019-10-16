#encoding=utf-8
import os
import re

dictf=os.path.join("en_de.txt")
with open(dictf,encoding='utf-8') as f:
    data= f.read()
print(data)

pat_ende = re.compile(r'<font ([\s\S]*?)]\\n|\\n</font><br>')
pat_ende2= re.compile(r'\[([\s\S]*?)]|\\n|\S+\}')
pat_ende3= re.compile(r'/|\(|\)')

data_dealt=re.sub(pat_ende,r",",data)
data_dealt2=re.sub(pat_ende2,r" ",data_dealt)
data_dealt2=re.sub(pat_ende3,r";",data_dealt2)


#
#      result.append(line)
print(data_dealt2)
with open('newdict2.csv', 'w',encoding='utf-8') as fw:
    fw.write(data_dealt2)
