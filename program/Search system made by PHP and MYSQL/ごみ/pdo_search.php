<?php
header("Content-type: text/html; charset=utf-8");

if(empty($_POST)) {
	header("Location: pdo_search_form.html");
	exit();
}else{
	//名前入力判定
	if (!isset($_POST['yourname'])  || $_POST['yourname'] === "" ){
		$errors['name'] = "名前が入力されていません。";
	}
}

if(!empty($errors)){
	
$dsn = 'mysql:host=localhost;dbname=search;charset=utf8';
$user = 'root';
$password = 'root';

	try{
		$dbh = new PDO($dsn, $user, $password);
		$statement = $dbh->prepare("SELECT * FROM name WHERE name LIKE (:name) ");
	
		if($statement){
			$yourname = $_POST['yourname'];
			$like_yourname = "%".$yourname."%";
			//プレースホルダへ実際の値を設定する
			$statement->bindValue(':name', $like_yourname, PDO::PARAM_STR);
			
			if($statement->execute()){
				//レコード件数取得
				$row_count = $statement->rowCount();
				
				while($row = $statement->fetch()){
					$rows[] = $row;
				}
				
			}else{
				$errors['error'] = "検索失敗しました。";
			}
			
			//データベース接続切断
			$dbh = null;	
		}
	
	}catch (PDOException $e){
		print('Error:'.$e->getMessage());
		$errors['error'] = "データベース接続失敗しました。";
	}
}

?>

<!DOCTYPE html>
<html>
<head>
<title>検索結果</title>
<meta charset="utf-8">
</head>
<body>

<table border='1'>
<tr><td>id</td><td>name</td></tr>

<?php 
foreach($rows as $row){
?> 
<tr> 
	<td><?=$row['id']?></td> 
	<td><?=htmlspecialchars($row['name'],ENT_QUOTES,'UTF-8')?></td> 
</tr> 
<?php 
}
?>


foreach($errors as $value){
	echo "<p>".$value."</p>";
}




</body>
</html>