rem D評価サーバを作るため、意図的にサイトに負荷をかける。
rem Windowsでは標準でWGETに代わるbitsadmin /TRANSFERが用意されていた。
rem Dos攻撃みたいになるのでlocal以外で使わないでね。
rem bitsadmin.exe /TRANSFER <ジョブ名：任意でOK> <リモートURL> <ダウンロード先>
rem 別のwinコンピュータで動くように環境変数を利用した
rem 環境変数%HOMEPATH%は「\Users\ユーザー名」を自動で選んでくれる。
rem 同一ファイル名だと上書きになって分かりにくいのでloopに使う変数でファイル名を変えるようにした。1.html,2.html…




set forward=C:%HOMEPATH%\Downloads\
for /l %%n in (1,1,10) do (

bitsadmin /TRANSFER tes http://kumasakasoukou.com/index.html %forward%%%n.html

)

pause

