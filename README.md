
<h2 align="center">1821086_matsuo_thesis</h2>


### <img src="https://icooon-mono.com/i/icon_16004/icon_160041_64.png" height="30px;" /> 実験用プログラム

- https://github.com/kait-takanolab/1821086_matsuo_thesis/tree/main/program

### <img src="https://icooon-mono.com/i/icon_11129/icon_111291_64.png" height="30px;" /> 関連研究

- https://github.com/kait-takanolab/1821086_matsuo_thesis/tree/main/%E9%96%A2%E9%80%A3%E7%A0%94%E7%A9%B6

### <img src="https://icooon-mono.com/i/icon_12063/icon_120631_64.png" height="30px;" /> ゼミ発表用スライド

- https://github.com/kait-takanolab/1821086_matsuo_thesis/blob/main/meeting/1821086_matsuo_thesis.pptx

### <img src="https://icooon-mono.com/i/icon_12063/icon_120631_64.png" height="30px;" /> 中間発表用スライド

- https://github.com/kait-takanolab/1821086_matsuo_thesis/blob/main/%E7%99%BA%E8%A1%A8%E7%94%A8/1821086_%E4%B8%AD%E9%96%93%E7%99%BA%E8%A1%A8.pptx

### <img src="https://icooon-mono.com/i/icon_12063/icon_120631_64.png" height="30px;" /> 中間発表_発表前最終調整

- https://github.com/kait-takanolab/1821086_matsuo_thesis/blob/main/%E7%99%BA%E8%A1%A8%E7%94%A8/1821086_%E4%B8%AD%E9%96%93%E7%99%BA%E8%A1%A8.pptx

### <img src="https://icooon-mono.com/i/icon_15821/icon_158211_64.png" height="30px;" /> プログラムの説明
・workspace/LoadBalancer_methodX.py<br>
ロードバランサーの割り振りを変えるプログラム。<br>
<br>
<method1><br>
測定した結果や評価が保存されているDBへアクセス。<br>
D評価のサーバが現れたらコンフィグの重みづけを変更<br>
（D評価サーバへの接続は1/10に制限される）<br>
最後にコンフィグの内容をLBに適用させる処理(再起動不要なnginx-reload)を実行<br>
<method2><br>
作成中<br>
<method3><br>
作成中<br>
<br>
・workspace/measure_evaluation_InsertDB.py<br>
応答速度の計測、現在速と過去24時間の平均速を抽出し、評価。<br>
これをDB挿入している。<br>
