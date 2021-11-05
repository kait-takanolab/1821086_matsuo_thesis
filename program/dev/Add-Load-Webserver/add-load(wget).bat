rem D評価サーバを作るため、意図的にサイトに負荷をかける。
rem Windowsでは標準でWGETに代わるbitsadmin /TRANSFERが用意されていた。
rem Dos攻撃みたいになるのでlocal以外で使わないでね。


rem どのサーバに負荷をかけるか選択↓
set target=http://192.168.1.81/index.php
:set target=http://192.168.1.82/index.php
:set target=http://192.168.1.83/index.php

rem 別のwinコンピュータで動くように環境変数を利用した。
rem 環境変数%HOMEPATH%は「\Users\ユーザー名」を自動で選んでくれる。
set forward=C:%HOMEPATH%\Downloads\


for /l %%n in (1,1,10) do (

rem bitsadmin.exe /TRANSFER <ジョブ名：任意でOK> <リモートURL> <ダウンロード先>
rem 同一ファイル名だと上書きになって分かりにくいのでloopに使う変数でファイル名を変えるようにした。1.html,2.html…
bitsadmin /TRANSFER tes %target% %forward%%%n.php

)

rem 結果が見れるように
pause

