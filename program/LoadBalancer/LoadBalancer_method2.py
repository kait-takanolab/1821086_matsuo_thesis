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


#応答速度テーブルから過去24時間の平均を取り出すDATETIMEで判断してる。
cur.execute("select avg(speed) from response81 where datetime > datetime(datetime(), '-1 days', '+0 hours');")
list1 = cur.fetchone()

cur.execute("select avg(speed) from response82 where datetime > datetime(datetime(), '-1 days', '+0 hours');")
list2 = cur.fetchone()

cur.execute("select avg(speed) from response83 where datetime > datetime(datetime(), '-1 days', '+0 hours');")
list3 = cur.fetchone()


#一応表示させる
print("----192.168.1.81の平均----")
print("ave_speed:",list1[0])

print("----192.168.1.82の平均----")
print("ave_speed:",list2[0])

print("----192.168.1.83の平均----")
print("ave_speed:",list3[0])


#過去２４時間の平均で最もレスポンスが良い(値が小さい)サーバを選ぶ。
minmam = min(list1[0],list2[0],list3[0])  



#--------------コンフィグ書き換え----------------

#既に決まっているところはそのまま書くよ。
f = open('/etc/nginx/nginx.conf', 'w', encoding='UTF-8')
datalist1 = ['user www-data;\n','worker_processes auto;\n','pid /run/nginx.pid;\n','include /etc/nginx/modules-enabled/*.conf;\n','events {\n','	worker_connections 768;\n','}\n','http {\n','	include /etc/nginx/mime.types;\n','gzip on;\n','gzip_vary on;\n','upstream backend1{\n']
f.writelines(datalist1)


if minmam == list1[0]:#81が平均最速なら
    print('\n過去24時間で「サーバ81」が一番応答速度が速い')
    datalist2 = ['server 192.168.1.81 weight=1;\n']
    f.writelines(datalist2)
else:
    datalist2 = ['server 192.168.1.81 weight=10;\n']
    f.writelines(datalist2)
    
if minmam == list2[0]:#82が平均最速なら
    print('\n過去24時間で「サーバ82」が一番応答速度が速い')
    datalist3 = ['server 192.168.1.82 weight=1;\n']
    f.writelines(datalist3)
else:
    datalist3 = ['server 192.168.1.82 weight=10;\n']
    f.writelines(datalist3)

if minmam == list3[0]:#83が平均最速なら
    print('\n過去24時間で「サーバ83」が一番応答速度が速い')
    datalist4 = ['server 192.168.1.83 weight=1;\n']
    f.writelines(datalist4)
else:
    datalist4 = ['server 192.168.1.83 weight=10;\n']
    f.writelines(datalist4)

datalist5 = ['}\n','server{\n','listen 80;\n','server_name localhost;\n','location /{\n','proxy_pass http://backend1;\n','}\n','}\n','}\n']

#コンフィグファイルへ保存
f.writelines(datalist5)
f.close()


#ロードバランサに処理を適用させる。（reload実行の為シェルを呼び出す）
subprocess.run(['/home/pi/tools/nginxrestart.sh'])

print("good")


