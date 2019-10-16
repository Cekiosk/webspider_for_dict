print("欢迎使用英汉词典")

print("输入⚆_⚆？退出")

print("----------------")

# 引入相关模块

import sys

import re

import bs4

import urllib.request

from bs4 import BeautifulSoup

import urllib.parse

# 规定外部输入

search = input("请输入英语单词：")

# 使用循环语句


url =  'http://dict.youdao.com/w/'+urllib.parse.quote(search)

# 读取网页

html = urllib.request.urlopen(url)

content = html.read().decode('utf-8')

html.close()

# 解析网页

soup = BeautifulSoup(content, "lxml")

text = soup.find('div', class_="trans-container")

print("汉语释义：")

# 使用正则表达式处理文本

for x in text:

    word = re.sub(re.compile(r""),'',str(x))

    words = re.sub(re.compile(r"\[(.+?)\]"),'',word)

    print(words)


search = input("请输入英语单词：")