from urllib import request
import urllib.request
import urllib.parse

url = 'http://www.baidu.com'

# response=urllib.request.urlopen(url=url)#参数=实参
#
# responseobj=response.read().decode('utf-8')#read方法
# responseobj1=response.geturl()
# responseobj2=dict(response.getheaders())#获取头部信息
# responseobj3=response.getcode()#获取头部信息
# responseobj4=response.readlines()#返回字节类型列表 一行一行读

image_url="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1544196773609&di=e36cbf0b8353d22d186a05de30d7d64b&imgtype=0&src=http%3A%2F%2Fmusicugc.qianqian.com%2Fugcdiy%2Fpic%2Fe10e5c64c4902a2ee4738c645bb73a79.jpg"
#url只允许简单字符
response2 = urllib.request.urlopen(image_url)
responseobj=response2.read()#read方法
#图片以字节形式（写入本地二进制格式）

#另一种保存图片方式
urllib.request.urlretrieve(image_url,'chen.jpg')

#url只接受有限的字符 其他要编码 就用到了parse
# with open("li.jpg" ,"wb") as fp:
#     fp.write(responseobj)
#字符串和二进制之间的转换
# encode 默认 utf8
# decode（为编码）

##print(responseobj3)#会获取一个对象
# with open('baidu.html','w',encoding='utf-8') as fp:
#     fp.write(responseobj)


# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))