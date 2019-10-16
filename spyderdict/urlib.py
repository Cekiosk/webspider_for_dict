from urllib import request
#-------------------------------------------------
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()#read是read data（就是包体部分）

    print("状态开始")
    print('Status:', f.status, f.reason)#这里有个参数叫f.status f.reason
    print("状态结束")

    print("头开始")

    for k in f.getheaders(): #用这个函数来获取头 #头里面每个元素是一个元祖，（key，value）
    #    print('%s: %s' % (k, v))

    #这个定位可以学一下
    #for k, v in f.getheaders():
        #print('%s: %s' % (k, v))

        print(type(k))
        print(k)

    print("头结束")

    print("数据开始")
    print('Data:', data.decode('utf-8')) #这里会输出所有的data
    print("数据结束")
    #全部打印出来差不多就是raw data了
#--------------------------------------------------------------