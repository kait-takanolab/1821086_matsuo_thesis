#!/usr/bin/bash
#echo "test"が10回実行される。
for i in `seq 10`
do
sudo python3 ResponseSpeed_InsertIntoDB.py
sleep 5
done
