
import pandas as pd
#这个文件用于手动设置count值
counter=pd.read_pickle("counter.pkl")

counter.loc[0, 0] = 40000#当前存储成功的词的序号 一个也没有就是-1
counter.to_pickle('counter.pkl')#保存成功变量
print(counter.loc[0, 0])
