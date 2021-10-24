


<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title></title>
</head>
<body>

<h1>検索システムを搭載したラズパイの<br>自動評価機能付き監視システム</h1>


<?php

//現在のレスポンス速度の読み込み
 $file1 = file("81_now_responselog.txt");
 $file2 = file("82_now_responselog.txt");
 $file3 = file("83_now_responselog.txt");


//1日平均のレスポンス速度の読み込み
 $file4 = file("81_1day_response_average.txt");
 $file5 = file("82_1day_response_average.txt");
 $file6 = file("83_1day_response_average.txt");


//レスポンス速度を評価する自作関数
function evaluation($greeting){
if(0<=$greeting && $greeting<=0.016) {
$evaluation="S";
}
else if(0.017<=$greeting && $greeting<=0.099){
$evaluation="A";
}
else if(0.1<=$greeting && $greeting<=0.999){
$evaluation="B";
}
else if(1.0<=$greeting && $greeting<=9.999){
$evaluation="C";
}
else if(10.0<=$greeting){
$evaluation="D";
}
return $evaluation;
}

//レスポンス速度をコメントする自作関数
function comment($greeting){
if(0<=$greeting && $greeting<=0.016) {
$comment="とても良い";
}
else if(0.017<=$greeting && $greeting<=0.099){
$comment="良い";
}
else if(0.1<=$greeting && $greeting<=0.999){
$comment="普通";
}
else if(1000<=$greeting && $greeting<=9999){
$comment="悪い";
}
else if(10.0<=$greeting){
$comment="とても悪い";
}
return $comment;
}

//ファイルを読み込んで「評価」する関数へぶち込む
//現在の応答速度
$evaluation_file1=evaluation($file1[count($file1)-1]);
$evaluation_file2=evaluation($file2[count($file2)-1]);
$evaluation_file3=evaluation($file3[count($file3)-1]);
//1日の応答速度
$evaluation_file4=evaluation($file4[count($file4)-1]);
$evaluation_file5=evaluation($file5[count($file5)-1]);
$evaluation_file6=evaluation($file6[count($file6)-1]);

//ファイルを読み込んで「コメント」する関数へぶち込む
//現在の応答速度
$comment_file1=comment($file1[count($file1)-1]);
$comment_file2=comment($file2[count($file2)-1]);
$comment_file3=comment($file3[count($file3)-1]);
//1日の応答速度
$comment_file4=comment($file4[count($file4)-1]);
$comment_file5=comment($file5[count($file5)-1]);
$comment_file6=comment($file6[count($file6)-1]);


//-----------------------------------------192.168.1.81---------------------------------------------

echo"<b>サーバー192.168.1.81の監視</b>";
echo"<table border=\"1\">";
echo"<tr>";
echo" <th>計測名</th>";
echo" <th>計測値</th>";
echo" <th>評価</th>";
echo" <th>コメント</th>";
echo"</tr>";
echo"<tr>";
echo" <td>現在のレスポンス速度</td>";
echo" <td>".$file1[count($file1)-1]."</td>";
echo" <td>".$evaluation_file1."</td>";
echo" <td>".$comment_file1."</td>";
echo"</tr>";
echo"<tr>";
echo" <td>1日平均のレスポンス速度</td>";
echo" <td>".$file4[count($file4)-1]."</td>";
echo" <td>".$evaluation_file4."</td>";
echo" <td>".$comment_file4."</td>";
echo"</tr>";
echo"</table>";

echo "<br>";




//-----------------------------------------192.168.1.82---------------------------------------------
echo"<b>サーバー192.168.1.82の監視</b>";
echo"<table border=\"1\">";
echo"<tr>";
echo" <th>計測名</th>";
echo" <th>計測値</th>";
echo" <th>評価</th>";
echo" <th>コメント</th>";
echo"</tr>";
echo"<tr>";
echo" <td>現在のレスポンス速度</td>";
echo" <td>".$file2[count($file2)-1]."</td>";
echo" <td>".$evaluation_file2."</td>";
echo" <td>".$comment_file2."</td>";
echo"</tr>";
echo"<tr>";
echo" <td>1日平均のレスポンス速度</td>";
echo" <td>".$file5[count($file5)-1]."</td>";
echo" <td>".$evaluation_file5."</td>";
echo" <td>".$comment_file5."</td>";
echo"</tr>";
echo"</table>";

echo "<br>";
//-----------------------192.168.1.83---------------------------------
echo"<b>サーバー192.168.1.83の監視</b>";
echo"<table border=\"1\">";
echo"<tr>";
echo" <th>計測名</th>";
echo" <th>計測値</th>";
echo" <th>評価</th>";
echo" <th>コメント</th>";
echo"</tr>";
echo"<tr>";
echo" <td>現在のレスポンス速度</td>";
echo" <td>".$file3[count($file3)-1]."</td>";
echo" <td>".$evaluation_file3."</td>";
echo" <td>".$comment_file3."</td>";
echo"</tr>";
echo"<tr>";
echo" <td>1日平均のレスポンス速度</td>";
echo" <td>".$file6[count($file6)-1]."</td>";
echo" <td>".$evaluation_file6."</td>";
echo" <td>".$comment_file6."</td>";
echo"</tr>";
echo"</table>";

echo "<br>";


?>


※評価はGoogleの開発者向け学習サイト「web.dev」が収集したユーザエクスペリエンスを参考にしている。
https://web.dev/rail/


</body>
</html>