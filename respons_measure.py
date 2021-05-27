# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

要求を送信してから応答が到着するまでに経過した時間を計測

"""  

import requests
import time
import datetime

for i in range(100):
    url = 'https://kait.jp'
    res = requests.get(url)
    time_elapsed = res.elapsed.total_seconds()
    date = datetime.datetime.now()    
    print(date,':', time_elapsed)
    #ファイルに書き込み
    with open('responselog.txt', 'a') as f:
        print(date, file=f)
        print(time_elapsed, file=f)
        time.sleep(1800)#30分ごとに計測