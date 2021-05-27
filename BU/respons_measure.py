# -*- coding: utf-8 -*-
"""
Created on Tue May 11 14:00:00 2021

@author: 1821086
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
import time
import datetime
import requests

#レスポンス速度を計測
url = 'https://kait.jp'
res = requests.get(url)
time_elapsed = res.elapsed.total_seconds()

#日付、時間と取得
date = datetime.datetime.now()

#ファイルに書き込み
with open('Aserver_1min_responselog.txt', 'a') as f:
  print(date, file=f)
  print(time_elapsed, file=f)
