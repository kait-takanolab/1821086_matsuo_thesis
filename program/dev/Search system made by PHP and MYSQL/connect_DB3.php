<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>DB3</title>
</head>
<body>

<h2>DB3への接続</h2>

<?php

// 変数の初期化
$sql = null;
$res = null;
$dbh = null;

try {
	// DBへ接続
	$dbh = new PDO("mysql:host=127.0.0.1; dbname=DB3; charset=utf8", 'root', 'root');

	// SQL作成
	$sql = "SELECT * FROM service";

	// SQL実行
	$res = $dbh->query($sql);

	// 取得したデータを出力

echo"<table border=\"1\">";

	foreach( $res as $value ) {
		echo "</tr>";
		echo "<th>"."$value[id]"."</th>";
		echo "<th>"."$value[location]"."</th>";
		echo "<th>"."$value[name]"."</th>";
		echo "</tr>";
	}

echo"</table>";

} catch(PDOException $e) {
	echo $e->getMessage();
	die();
}

// 接続を閉じる
$dbh = null;

?>

</body>
</html>