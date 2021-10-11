
set target=https://www.yahoo.co.jp/

for /l %%n in (1,1,10) do (
wget -O /dev/null %target%

sleep 5

)

rem 結果が見れるように
pause

