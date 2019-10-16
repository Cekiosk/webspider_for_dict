import os
import re
import numpy as np
import pandas as pd
import pickle
import time
import random
from random import randint#使用randint需要加上这句

import os
import re
import numpy as np
import pandas as pd
import pickle
import time
import random
from random import randint#使用randint需要加上这句

datajson=pd.read_csv("dejson.csv", encoding="utf-8",header=None)

datadict=datajson[0]
dictlen=len(datajson)

print(datajson.index)
datajson[1]=datajson.index

datajson.to_csv("dejson_index.csv",index=0,header=0)