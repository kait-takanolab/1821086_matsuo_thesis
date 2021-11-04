# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 00:31:47 2021

@author: 1821086


実験用：ロードバランサ計測プログラム
requests.get()はHTTPのGETメソッドに相当する。
応答以外にもページのスクレイピングも可能
→どのWEBサーバへロードバランサが割り振ったのか確認できるので実験に最適。
"""

import requests
from bs4 import BeautifulSoup
import datetime
import time


i = 0

while i < 100000:
    #ロードバランサの応答速度を計測
    url = 'http://192.168.1.80/'
    res = requests.get(url)
    time_elapsed = res.elapsed.total_seconds()
    print('time_elapsed:', time_elapsed)

    # Webスクレイピング
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    
    # titleで判別（.textを指定することでタグの中を抽出できるらしい）
    assign=soup.find("h1").text
    print(assign)
    
    #時刻を取得
    dt_now = datetime.datetime.now()
    print(dt_now)
    
    #ファイルへ出力
    f = open('LB_data_output.txt', 'a')
    
    #後でCSVで整理するとき便利だから区切り符を入れておく。
    f.write(str(dt_now) + "/" + str(time_elapsed) + "/" + assign+"\n")
    f.close()
    i += 1
    time.sleep(1)











