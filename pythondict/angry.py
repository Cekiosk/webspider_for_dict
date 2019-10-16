#encoding=utf-8

aaa=["海大","对面"]
bbb=["sl","nm"]

print(aaa)

dictydt = {}
for i in range(0,len(aaa)):
    print(aaa[i])
    dictydt[aaa[i]] = bbb[i]
    print("rückwärts")

print( dictydt )
