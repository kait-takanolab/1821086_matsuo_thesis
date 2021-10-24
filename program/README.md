
<h2 align="center">プログラムの説明</h2>

LoadBalancer_method1.py(試作)<br>
現在の応答速度がD評価のサーバが現れたら直ちに接続が制限されれる。(1/10に制限)

LoadBalancer_method2.py(試作)<br>
応答速度DBから過去24時間の平均を算出し、どのサーバが平均して良い結果を出しているのか判断。一番良い結果(平均応答速度が最速)のサーバに多く割り振るように動的なロードバランサを作った。<br>

LoadBalancer.py(提案システム)<br>
卒論で使うのはこれ。設計開発したロードバランサのプロトタイプ。内容は割り振り方法はmethod2と同じ。出力結果を観やすいように改良してある。<br>

measure_evaluation_InsertDB.py(提案システム)<br>
各サーバの速度を計測、評価を行いデータベース(response.db)へ挿入する。<br>

nginxrestart.sh<br>
Nginxを再読み込みしてコンフィグを適用させる。当プログラムはLB内で呼び出して実行<br>

roop_LoadBalancer.sh<br>
２つのプログラムを同時に実行しループするようにしたシェル。60秒ごとに実行される。<br>




