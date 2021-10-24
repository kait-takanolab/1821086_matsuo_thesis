


<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title></title>
</head>
<body>

<h1>DB挿入テスト</h1>


<?php


// データベースに接続するために必要なデータソースを変数に格納
  // mysql:host=ホスト名;dbname=データベース名;charset=文字エンコード
$dsn = 'mysql:host=localhost;dbname=monitoring;charset=utf8';
 
  // データベースのユーザー名
$user = 'root';
 
  // データベースのパスワード
$password = '';
 
// tryにPDOの処理を記述
try {
 
  // PDOインスタンスを生成
  $dbh = new PDO($dsn, $user, $password);
 
// エラー（例外）が発生した時の処理を記述
} catch (PDOException $e) {
 
  // エラーメッセージを表示させる
  echo 'データベースにアクセスできません！' . $e->getMessage();
 
  // 強制終了
  exit;
 
}


// INSERT文を変数に格納
$sql = "INSERT INTO log_81 (time,now,average) VALUES (now(),:now,:average)";
 
// 挿入する値は空のまま、SQL実行の準備をする
$stmt = $dbh->prepare($sql);
 
// 挿入する値を配列に格納する
$params = array(':now' => '98.456700', ':average' => '84.3432');
 
// 挿入する値が入った変数をexecuteにセットしてSQLを実行
$stmt->execute($params);
 
// 登録完了のメッセージ
echo '登録完了しました';


?>


</body>
</html>