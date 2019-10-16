from urllib import request
#依然是从urllib里导入的request 包

req = request.Request('https://translate.google.cn/')#request函数先写下了URL


req.add_header('User-Agent', "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36") #add_header部分为你的request包加上header 格式是（key，value）

with request.urlopen(req) as f:
    print("开始打印状态：")
    print('Status:', f.status, f.reason)
    print("开始打印头：")
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print("开始打印数据：")
    print('Data:', f.read().decode('utf-8'))
