# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

取得したデータ（responslog.txt）から平均を取る

"""


# ファイルの行数を調べる
gyou = 0
with open('responselog.txt') as f:
    for line in f:
        gyou += 1
print(gyou)


#日付データをはじいて合計を求める
f = open('responselog.txt', 'r')
datalist = f.readlines()

sum=0
count=0

for num in range(gyou):
    if num % 2 == 0:#偶数は日付データなのでスキップ
     continue
    sum=sum+float(datalist[num])#レスポンス時間の合計
    count+=1
f.close()

#平均を出す
average=sum/count

print("合計：",sum)
print("平均：",average)

