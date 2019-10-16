# encoding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import os
import re
import numpy as np
import pandas as pd
import pickle

#data = pd.read_csv("enplustest.csv", encoding="utf-8", header=None)

data_en=pd.read_pickle("en-list-atom.pkl")
data_de=pd.read_pickle("de-list-atom.pkl")

data_all=pd.read_pickle("all-series.pkl")
print data_en

