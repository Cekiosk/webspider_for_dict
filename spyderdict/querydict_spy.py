import execjs
import requests
from random import randint#使用randint需要加上这句

class Py4Js():

    def __init__(self):
        self.ctx = execjs.compile("""
        function TL(a) {
        var k = "";
        var b = 406644;
        var b1 = 3293161072;

        var jd = ".";
        var $b = "+-a^+6";
        var Zb = "+-3^+b+-f";

        for (var e = [], f = 0, g = 0; g < a.length; g++) {
            var m = a.charCodeAt(g);
            128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023),
            e[f++] = m >> 18 | 240,
            e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224,
            e[f++] = m >> 6 & 63 | 128),
            e[f++] = m & 63 | 128)
        }
        a = b;
        for (f = 0; f < e.length; f++) a += e[f],
        a = RL(a, $b);
        a = RL(a, Zb);
        a ^= b1 || 0;
        0 > a && (a = (a & 2147483647) + 2147483648);
        a %= 1E6;
        return a.toString() + jd + (a ^ b)
    };

    function RL(a, b) {
        var t = "a";
        var Yb = "+";
        for (var c = 0; c < b.length - 2; c += 3) {
            var d = b.charAt(c + 2),
            d = d >= t ? d.charCodeAt(0) - 87 : Number(d),
            d = b.charAt(c + 1) == Yb ? a >>> d: a << d;
            a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d
        }
        return a
    }
    """)

    def getTk(self, text):
        return self.ctx.call("TL", text)


import urllib.request

ualist=["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0",
          "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
          "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
          "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
          "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
          "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",
          "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
          "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"
          ]

def open_url(url):#第二个参数是usragent

    usa=get_uagent()
    headers = {
        'User-Agent': usa,
        'Host': 'translate.google.cn',#服务器地址，请求报头域主要用于指定被请求资源的Internet主机和端口号，它通常从HTTP URL中提取出来的
        'Connection': 'keep - alive',#tcp链接保持链接
        'Referer': 'https: // translate.google.cn /',#从哪个网页来的
        'Accept': '* / *',#客户端可以接受的数据形式
        'X - Client - Data': 'CI62yQEIpLbJAQjEtskBCKmdygEIqKPKAQ ==',#谷歌浏览器特有的
        'Accept - Encoding': 'gzip, deflate, br',#可以接受的编码形式
        'Accept - Language':"zh - CN, zh;q = 0.9",#可以接受的语言
        'Cookie': '__guid=3261045.611701839150553300.1541641300911.0479; _ga=GA1.3.1450919447.1542343335; _gid=GA1.3.1896715690.1544689243; monitor_count=2; NID=150=Uerr1CQmMUaPmUbd4coufnqOuUY2d9MdBPyQy16FzKfE23iiKM2JXQFZRqHt1jmuZ4JPAFGlJ8_LRalFUujFLepcCc_CMPLayyA_3sVkR0-vKrRyC6S2kJilXOzkVQSNI-wQjsjitBbLXikYjMcw1tEaq0HzXl3yPEPCiX0KPks; 1P_JAR=2018-12-13-12'

        } #headers只是写了user-agent

    req = urllib.request.Request(url=url, headers=headers) #写了一个request请求的打包，因为是get所以没有内容
    response = urllib.request.urlopen(req)#可以填写一个url或者一个request

    data = response.read().decode('utf-8')
    return data


def translate(content, tk):


    content = urllib.parse.quote(content)

    url = "http://translate.google.cn/translate_a/single?client=t" \
          "&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
          "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
          "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, content)
    urlde="https://translate.google.cn/translate_a/single?client=webapp&sl=de&tl=en&hl=zh-CN" \
          "&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&otf=1&ssel=3&tsel=6&" \
          "kc=5&tk=%s&q=%s" % (tk, content)

    result = open_url(urlde)

    # 返回的结果为Json，解析为一个嵌套列表
    #print(result)
    return result

def tans_spy(word):
    js = Py4Js()  # 在这里申明了一个py4js对象
    content = word
    tk = js.getTk(content)  # 从对象里获取的这个就是计算tk的函数
    result=translate(content, tk)
    return result

def get_uagent():
    a = randint(0, len(ualist) - 1)  # random.randint(a,b)：用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n：a<=n<=b
    #print(ualist[a])
    return ualist[a]
    #print(a)



def main():
#    pass;
    print(tans_spy("an"))

    # js = Py4Js()#在这里申明了一个py4js对象
    #
    # # while 1:
    # #     content = input("输入待翻译内容：")
    # #
    # #     if content == 'q!':
    # #         break
    # content="an"
    # tk = js.getTk(content)#从对象里获取的这个就是计算tk的函数
    # translate(content, tk)


if __name__ == "__main__":
    main()
