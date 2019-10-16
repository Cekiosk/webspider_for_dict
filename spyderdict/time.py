import time

import random
from random import randint#使用randint需要加上这句

a=random.random()

for i in range(6):
    a = randint(200, 500) #就是两秒到5秒
    b=a/100
    print(b)
    time.sleep(b)