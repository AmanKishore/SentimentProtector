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

# for sentiments in r.text:
#         print(sentiments)

# listval = []
# for i in range(180, 2, -1):
#     s = datetime.date.today() - datetime.timedelta(days=i)     # gets the date from 30 days ago
#     e = datetime.date.today() - datetime.timedelta(days=(i-1)) # gets date from 29 days ago need to make into a for loop
#     sdate = s.strftime('%Y-%m-%d')                             # converts to a string
#     edate = e.strftime('%Y-%m-%d')
#     val = news.get_news_past_six_months(sdate, edate, 'fortnite')
#     if val is not None:
#         totalCount = val['totalResults']
#         listval.append(totalCount)

# print(listval)

# # data = json.loads(re)
# # json_text = json.dumps(data)
# # df = json_normalize(json_text)

# # print('Results are {0}'.format(totalCount))

# # testing the google trends api
# pytrends = TrendReq()
# kw_list = ["Fortnite", "Minecraft", "Grand Theft Auto"]
# pytrends.build_payload(kw_list, cat=0, timeframe='all', geo='', gprop='')
# print(pytrends.get_historical_interest(kw_list, year_start=2017, month_start=9, day_start=1, hour_start=0, year_end=2018, month_end=8, day_end=1, hour_end=0, cat=0, geo='', gprop='', sleep=0))