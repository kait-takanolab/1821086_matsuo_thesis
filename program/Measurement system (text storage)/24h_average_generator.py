# -*- coding: utf-8 -*-
"""
取得したデータ（81，82，83responslog）は過去の応答速度も含まれる。
邪魔な日付データと古いデータを除外して、過去24時間の平均を出すようにするプログラム。
結果はファイルXX_1day_response_averageに書き込まれる。
"""

#192.168.1.81の平均をとる処理―――――――――――――――――――――――――
# ファイルの行数を調べる
gyou = 0
with open('responselog_192.168.1.81.txt') as f:
    for line in f:
        gyou += 1

#日付データをはじいて合計を求める
f = open('responselog_192.168.1.81.txt', 'r')
datalist = f.readlines()

sum=0
count=0

for num in range(gyou):
    if num < gyou-96:#古いデータ(最初の方)はスキップ30分ずつ測定しているので1440/30*2
        continue
    elif num % 2 == 0:#偶数は日付データなのでスキップ
        continue
    sum=sum+float(datalist[num])#レスポンス時間の合計
    count+=1
f.close()

#平均を出す
average=sum/count

print("対象：192.168.1.81")
print("平均：",average)

#ファイルに書き込み
with open('81_1day_response_average.txt', 'a') as f:
    print(average, file=f)
    
    
#192.168.1.82の平均をとる処理―――――――――――――――――――――――――
# ファイルの行数を調べる
gyou = 0
with open('responselog_192.168.1.82.txt') as f:
    for line in f:
        gyou += 1

#日付データをはじいて合計を求める
f = open('responselog_192.168.1.82.txt', 'r')
datalist = f.readlines()

sum=0
count=0

for num in range(gyou):
    if num < gyou-96:#古いデータ(最初の方)はスキップ30分ずつ測定しているので1440/30*2
        continue
    elif num % 2 == 0:#偶数は日付データなのでスキップ
        continue
    sum=sum+float(datalist[num])#レスポンス時間の合計
    count+=1
f.close()

#平均を出す
average=sum/count

print("対象：192.168.1.82")
print("平均：",average)

#ファイルに書き込み
with open('82_1day_response_average.txt', 'a') as f:
    print(average, file=f)
  
#192.168.1.83の平均をとる処理―――――――――――――――――――――――――
# ファイルの行数を調べる
gyou = 0
with open('responselog_192.168.1.83.txt') as f:
    for line in f:
        gyou += 1

#日付データをはじいて合計を求める
f = open('responselog_192.168.1.83.txt', 'r')
datalist = f.readlines()

sum=0
count=0

for num in range(gyou):
    if num < gyou-96:#古いデータ(最初の方)はスキップ30分ずつ測定しているので1440/30*2
        continue
    elif num % 2 == 0:#偶数は日付データなのでスキップ
        continue
    sum=sum+float(datalist[num])#レスポンス時間の合計
    count+=1
f.close()

#平均を出す
average=sum/count

print("対象：192.168.1.83")
print("平均：",average)

#ファイルに書き込み
with open('83_1day_response_average.txt', 'a') as f:
    print(average, file=f)
  


