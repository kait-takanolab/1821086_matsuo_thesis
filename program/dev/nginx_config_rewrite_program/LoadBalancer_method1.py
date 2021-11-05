# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 15:57:12 2021

@author: 1821086

流れ：
測定した結果や評価が保存されているDBへアクセス。
D評価のサーバが現れたらコンフィグの重みづけを変更
（D評価サーバへの接続は1/10に制限される）
最後にコンフィグの内容を適用させる処理を実行

"""

import sqlite3
import subprocess


#DBから抽出処理------------------------------
#データベースＳＱＬＩＴＥに接続
dbname = 'response'
conn = sqlite3.connect(dbname)

# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()

#monitoringテーブルの最後の行から現在スピード評価の値を取り出す

#81現在評価の取り出し
cur.execute("SELECT now_speed_score FROM monitoring81 ORDER BY id DESC LIMIT 1;")
list1 = cur.fetchone()
server_81=list1[0];

#82現在評価の取り出し
cur.execute("SELECT now_speed_score FROM monitoring82 ORDER BY id DESC LIMIT 1;")
list2 = cur.fetchone()
server_82=list2[0];

#83現在評価の取り出し
cur.execute("SELECT now_speed_score FROM monitoring83 ORDER BY id DESC LIMIT 1;")
list3 = cur.fetchone()
server_83=list3[0];
#------------------------------

#既に決まっているところはそのまま書くよ。
f = open('/etc/nginx/nginx.conf', 'w', encoding='UTF-8')
datalist1 = ['user www-data;\n','worker_processes auto;\n','pid /run/nginx.pid;\n','include /etc/nginx/modules-enabled/*.conf;\n','events {\n','	worker_connections 768;\n','}\n','http {\n','	include /etc/nginx/mime.types;\n','gzip on;\n','gzip_vary on;\n','upstream backend1{\n']
f.writelines(datalist1)

#D評価サーバが現れたら重みを下げる処理
if server_81 == "D":
    datalist2 = ['server 192.168.1.81 weight=10;\n']
    f.writelines(datalist2)
else:
    datalist2 = ['server 192.168.1.81;\n']
    f.writelines(datalist2)
    
if server_82 == "D":
    datalist3 = ['server 192.168.1.82 weight=10;\n']
    f.writelines(datalist3)
else:
    datalist3 = ['server 192.168.1.82;\n']
    f.writelines(datalist3)

if server_83 == "D":
    datalist4 = ['server 192.168.1.83 weight=10;\n']
    f.writelines(datalist4)
else:
    datalist4 = ['server 192.168.1.83;\n']
    f.writelines(datalist4)

datalist5 = ['}\n','server{\n','listen 80;\n','server_name localhost;\n','location /{\n','proxy_pass http://backend1;\n','}\n','}\n','}\n']

#コンフィグファイルへ保存
f.writelines(datalist5)
f.close()

#ロードバランサに処理を適用させる。（reload実行の為シェルを呼び出す）
subprocess.run(['bash nginxrestart.sh'])

