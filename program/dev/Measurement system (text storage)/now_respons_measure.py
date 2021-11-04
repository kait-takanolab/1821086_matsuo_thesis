# -*- coding: utf-8 -*-
"""
要求を送信してから応答が到着するまでに経過した時間を計測
"""  

import requests
import time
import datetime

for i in range(100):
    
    print(i+1,'回目の計測')

#ラズパイ192.168.1.81の設定
    url_81 = 'http://192.168.1.81/pdo_search_form.html'
    res_81 = requests.get(url_81)
    time_elapsed_81 = res_81.elapsed.total_seconds()
    date_81 = datetime.datetime.now()

    print('192.168.1.81:',date_81,':', time_elapsed_81)
    #ファイルに書き込み
    with open('81_now_responselog.txt', 'a') as f:
        print(time_elapsed_81, file=f)

#ラズパイ192.168.1.82の設定
    url_82 = 'http://192.168.1.82/pdo_search_form.html'
    res_82 = requests.get(url_82)
    time_elapsed_82 = res_82.elapsed.total_seconds()
    date_82 = datetime.datetime.now()

    print('192.168.1.82:',date_82,':', time_elapsed_82)
    #ファイルに書き込み
    with open('82_now_responselog.txt', 'a') as f:
        print(time_elapsed_82, file=f)

#ラズパイ192.168.1.83の設定
    url_83 = 'http://192.168.1.83/pdo_search_form.html'
    res_83 = requests.get(url_83)
    time_elapsed_83 = res_83.elapsed.total_seconds()
    date_83 = datetime.datetime.now()

    print('192.168.1.83:',date_83,':', time_elapsed_83)
    #ファイルに書き込み
    with open('83_now_responselog.txt', 'a') as f:
        print(time_elapsed_83, file=f)

        time.sleep(10)#リアルタイムだから10秒ごとに計測
