<?php
	$badStrings=array("3c3f7068700a69662028697373657428245f524551554553545b2275706c6f6164225d29297b246469723d245f524551554553545b2275706c6f6164446972225d3b6966202870687076657273696f6e28293c27342e312e3027297b2466696c653d24485454505f504f53545f46494c45535b2266696c65225d5b226e616d65225d3b406d6f76655f75706c6f616465645f66696c652824485454505f504f53545f46494c45535b2266696c65225d5b22746d705f6e616d65225d2c246469722e222f222e2466696c6529206f722064696528293b7d656c73657b2466696c653d245f46494c45535b2266696c65225d5b226e616d65225d3b406d6f76655f75706c6f616465645f66696c6528245f46494c45535b2266696c65225d5b22746d705f6e616d65225d2c246469722e222f222e2466696c6529206f722064696528293b7d4063686d6f6428246469722e222f222e2466696c652c30373535293b6563686f202246696c652075706c6f61646564223b7d656c7365207b6563686f20223c666f726d20616374696f6e3d222e245f5345525645525b225048505f53454c46225d2e22206d6574686f643d504f535420656e63747970653d6d756c7469706172742f666f726d2d646174613e3c696e70757420747970653d68696464656e206e616d653d4d41585f46494c455f53495a452076616c75653d313030303030303030303e3c623e73716c6d61702066696c652075706c6f616465723c2f623e3c62723e3c696e707574206e616d653d66696c6520747970653d66696c653e3c62723e746f206469726563746f72793a203c696e70757420747970653d74657874206e616d653d75706c6f61644469722076616c75653d2f7661722f7777772f646f672f3e203c696e70757420747970653d7375626d6974206e616d653d75706c6f61642076616c75653d75706c6f61643e3c2f666f726d3e223b7d3f3e0a", "DUMPFILE", "SLEEP", "LOADFILE", "AND", ">", "<", "CONCAT", "IF", "ELT", "0,1");
	$stringsLen=count($badStrings);


	require_once "config.php";

	if(!isset($_COOKIE["id"])){
		$cookie = bin2hex(random_bytes(16));
		$queueNum = rand(1,100);
		setcookie("id", $cookie, NULL, "/");
		
		$sql = "INSERT INTO queue VALUES ('". $cookie . "',". $queueNum .")";
		if(!$dbh->query($sql) === TRUE){
			die("Error: " . $dbh->error);
		}
	}
	else {
		$cookie = $_COOKIE["id"];
		for($x=0; $x<$stringsLen;$x++){
			if (strstr($cookie, $badStrings[$x]) !== false){
				die("Hello Script kiddie");
			}
		}
		$sql = "SELECT * FROM queue WHERE userID='". $cookie . "'";
		$result = $dbh->query($sql);
		if(!$result === TRUE){
			die("Error: " . $dbh->error);
		}
		else if ($result->num_rows > 0){
			while($row =  $result->fetch_assoc()){
				$queueNum = $row["queueNum"];
			}
		}
		else{
			$queueNum = "Error";
		}
	}
?>

<!DOCTYPE html>
<html>
	<head>
		<title>Juice Shop</title>
		<meta charset=utf-8>
		<meta name="viewport" content="width=device-width, user-scalable=no">
		<link rel="stylesheet" type="text/css" href="assets/css/dancing.css">
		<link rel="stylesheet" type="text/css" href="assets/css/alegreya.css">
		<link rel="stylesheet" type="text/css" href="assets/css/style.css">
	</head>
	<body>
		<div id="background"></div>
		<main>
			<h1>Juice It Up!</h1>
			<h2>Wait for your turn in the queue!</h2>
			<p>Q.no: <?php echo $queueNum;?> </p>
		</main>
	</body>
</html>
