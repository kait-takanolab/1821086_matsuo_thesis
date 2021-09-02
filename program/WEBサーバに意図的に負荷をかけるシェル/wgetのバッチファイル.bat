rem D評価サーバを作るため、意図的にサイトに負荷をかける。
rem Windowsでは標準でWGETに代わるbitsadmin /TRANSFERが用意されていた。
rem Dos攻撃みたいになるのでlocal以外で使わないでね。

rem bitsadmin.exe /TRANSFER <ジョブ名：任意でOK> <リモートURL> <ダウンロード先>


rem %HOMEPATH%は環境変数「\Users\ユーザー名」をコンピュータ毎に変えてくれる


:for /l %%n in (1,1,100000) do (
:bitsadmin /TRANSFER tes http://kumasakasoukou.com/index.html C:%HOMEPATH%\Downloads\index.html
:)


