# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 15:57:12 2021

@author: 1821086



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

#現在の評価の取り出し
cur.execute("select now_speed_score from response81 where rowid = last_insert_rowid();")
list4 = cur.fetchone()
cur.execute("select now_speed_score from response82 where rowid = last_insert_rowid();")
list5 = cur.fetchone()
cur.execute("select now_speed_score from response83 where rowid = last_insert_rowid();")
list6 = cur.fetchone()

print("=====================")
print("                    ")
print("  ロードバランサ診断中")
print("                    ")
print("=====================")


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

f = open('/etc/nginx/nginx.conf', 'w', encoding='UTF-8')

#既に決まっているところはそのまま書くよ。
datalist1 = ['user www-data;\n','worker_processes auto;\n','pid /run/nginx.pid;\n','include /etc/nginx/modules-enabled/*.conf;\n','events {\n','	worker_connections 768;\n','}\n','http {\n','	include /etc/nginx/mime.types;\n','gzip on;\n','gzip_vary on;\n','upstream backend1{\n']
f.writelines(datalist1)


if minmam == list1[0]:#81が平均最速なら
    print('\n過去24時間で「サーバ81」が一番応答速度が速いので優先接続されます。')
    datalist2 = ['server 192.168.1.81 weight=10;\n server 192.168.1.82 weight=1;\n server 192.168.1.83 weight=1;\n']
    f.writelines(datalist2)
    allocation='192.168.1.81'
    
    
elif minmam == list2[0]:#82が平均最速なら
    print('\n過去24時間で「サーバ82」が一番応答速度が速いので優先接続されます。')
    datalist2 = ['server 192.168.1.81 weight=1;\n server 192.168.1.82 weight=10;\n server 192.168.1.83 weight=1;\n']
    f.writelines(datalist2)
    allocation='192.168.1.82'
    
elif minmam == list3[0]:#83が平均最速なら
    print('\n過去24時間で「サーバ83」が一番応答速度が速いので優先接続されます。')
    datalist2 = ['server 192.168.1.81 weight=1;\n server 192.168.1.82 weight=1;\n server 192.168.1.83 weight=10;\n']
    f.writelines(datalist2)
    allocation='192.168.1.83'


#現在速度がD評価だったら書き直し（割り振らないようにする）
if 10<=list4[0]:
    datalist2 = ['server 192.168.1.81 weight=0;\n server 192.168.1.82 weight=1;\n server 192.168.1.83 weight=1;\n']

if 10<=list5[0]:
    datalist2 = ['server 192.168.1.81 weight=1;\n server 192.168.1.82 weight=0;\n server 192.168.1.83 weight=1;\n']
   
if 10<=list6[0]:
    datalist2 = ['server 192.168.1.81 weight=1;\n server 192.168.1.82 weight=1;\n server 192.168.1.83 weight=0;\n']

    
datalist5 = ['}\n','server{\n','listen 80;\n','server_name localhost;\n','location /{\n','proxy_pass http://backend1;\n','}\n','}\n','}\n']

#コンフィグファイルへ保存
f.writelines(datalist5)
f.close()


#--------------NGINX適応処理----------------

#そのまま適応させると割り振り先カウントがリセットされる。前回と違った時だけ更新する。

#前回の割り振りを呼び出し
f2 = open('allocation.txt', 'r', encoding='UTF-8')
data = f2.read()

if allocation==data:
    print('最速サーバは前回と同じ：設定変更ありません')


#前回と違う→ロードバランサに処理を適用させる。（reload実行の為シェルを呼び出す）
else:
    print('最速サーバが変わりました：設定変更します')
    subprocess.run(['/home/pi/tools/nginxrestart.sh'])
    print('設定を変更しました')
    
    
#--------------今回の割り振り先を記録----------------

f2 = open('allocation.txt', 'w', encoding='UTF-8')

if minmam == list1[0]:#81が平均最速なら
    f2.write('192.168.1.81')
    
elif minmam == list2[0]:#82が平均最速なら
    f2.write('192.168.1.82')
    
elif minmam == list3[0]:#83が平均最速なら
    f2.write('192.168.1.83')

f2.close()
