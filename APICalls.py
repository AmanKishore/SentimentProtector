import requests
import json
import numpy as np
import pandas as pd
import sklearn
import matplotlib
import seaborn
import scipy
from pandas.io.json import json_normalize
import datetime
from pytrends.request import TrendReq
import TextAnalysisAPI
import ast

text = TextAnalysisAPI.ApiClient('1f67147b09804f90a1be856eaf11f89f')

r = text.get_sentiment('example.json')
# {"documents":[{"id":"1","score":0.92014169692993164},{"id":"2","score":0.05087512731552124},{"id":"3","score":0.80231726169586182},
# {"id":"4","score":0.21357250213623047},{"id":"5","score":0.94849288463592529}],"errors":[]

diction = (ast.literal_eval(r.text))['documents']
total = 0
elements = 0
for i in diction:
        total += i['score']
        elements += 1
print(total/elements)