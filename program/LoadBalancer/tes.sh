#!/usr/bin/bash
for i in `seq 100`
do
sudo python3 tes.py
sudo python3 measure_evaluation_InsertDB.py
sleep 20
done
