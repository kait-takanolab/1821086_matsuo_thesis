
import sqlite3
import requests
import datetime

#応答速度計測
url = 'https://dot-blog.jp/'
res = requests.get(url)
time_elapsed = res.elapsed.total_seconds()

#現在時刻取得
dt_now = datetime.datetime.now()


#データベースＳＱＬＩＴＥに接続
dbname = 'response'
conn = sqlite3.connect(dbname)

# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()


#応答速度DBへ挿入
setdb1 = (None,time_elapsed,dt_now)
cur.execute("insert into response81 (id,speed,datetime) values (?,?,?)", setdb1)

#応答速度DBから過去24時間の平均を取り出す
cur.execute("select avg(speed) from response81 where datetime > datetime(datetime(), '+0 days', '-1 hours');")
list1 = cur.fetchone()
print (list1) 

"""
#select結果取り出し1行
cur.execute("select avg(speed) from response81 where datetime > '2021-07-05 14:00';")
list1 = cur.fetchone()
print (list1)
"""




# データベースへコミット。これで変更が反映される。
conn.commit()
conn.close()