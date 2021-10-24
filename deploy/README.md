
<h2 align="center">デプロイについて</h2>

提案システムを再現するにはこのdeployをラズベリーパイ上にクローンします。<br>
git cloneでプログラムを配備する手順を下記にて説明します。<br>
「mkdir{ディレクトリ名}」でプログラムを配置する場所を作成<br>
「cd {作成したディレクトリ名}」で移動<br>
「 git clone https://github.com/kait-takanolab/1821086_matsuo_thesis.git」を実行し、クローンする<br>


deploy<br>
 ├ LoadBalancer<br>
 ｜  ├ LoadBalancer.py<br>
 ｜  ├ measure_evaluation_InsertDB.py<br>
 ｜  ├ nginxrestart.sh<br>
 ｜  ├ response<br>
 ｜  └ roop_LoadBalancer.sh<br>
 ├ Webserver<br>
 ｜  └ var<br>
 ｜      └ www<br>
 ｜          └ html<br>
 ｜              ├ pdo_search.php<br>
 ｜              └ pdo_search_form.html<br>
 ├ method2動作の様子.wmv<br>
 └ README.md<br>


ディレクトリ：Webserver<br>
本提案システムのWebサーバ側で動かす「検索システム」のプログラムです。<br>
Apache、PHPをインストールした後「var/www/html」にファイルを配備すると再現できます。<br>
<br>

ディレクトリ:LoadBalancer<br>
提案システムとして設計開発した動的ロードバランサのプロトタイプを動かすPythonプログラムやシェルがあります。<br>
実装方法の詳細は卒論の4章にあります。<br>
<br>
LoadBalancer.py<br>
提案システムのプロトタイプ。応答速度DBから過去24時間の平均を算出し、どのサーバが平均して良い結果を出しているのか判断。一番良い結果(平均応答速度が最速)のサーバに多く割り振るように動的なロードバランサ。<br>
<br>
measure_evaluation_InsertDB.py(提案システム)<br>
各サーバの速度を計測、評価を行いデータベース(response.db)へ挿入する。<br>
<br>
nginxrestart.sh<br>
Nginxを再読み込みしてコンフィグを適用させる。当プログラムはLB内で呼び出して実行<br>
<br>
roop_LoadBalancer.sh<br>
２つのプログラムを同時に実行しループするようにしたシェル。60秒ごとに実行される。<br>

