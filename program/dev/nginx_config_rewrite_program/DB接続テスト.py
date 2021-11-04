# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 22:22:59 2021

@author: 1821086
"""
import sqlite3


#データベースＳＱＬＩＴＥに接続
dbname = 'response'
conn = sqlite3.connect(dbname)

# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()

#monitoringテーブルの最後の行から現在スピード評価の値を取り出す

#81現在評価の取り出し
cur.execute("SELECT now_speed_score FROM monitoring81 ORDER BY id DESC LIMIT 1;")
list1 = cur.fetchone()
print(list1[0])

#82現在評価の取り出し
cur.execute("SELECT now_speed_score FROM monitoring82 ORDER BY id DESC LIMIT 1;")
list2 = cur.fetchone()
print(list2[0])

#83現在評価の取り出し
cur.execute("SELECT now_speed_score FROM monitoring83 ORDER BY id DESC LIMIT 1;")
list3 = cur.fetchone()
print(list3[0])




"""
#応答速度テーブルへ計測結果を挿入
setdb1 = (None,time_elapsed,dt_now)
cur.execute("insert into response81 (id,speed,datetime) values (?,?,?)", setdb1)
"""