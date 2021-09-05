<?php
	$servername = "localhost";
	$username = "web";
	$password = "password";
	$dbname = "webapp";

	$dbh = new mysqli($servername, $username, $password, $dbname);
	if ($dbh->connect_error){
		die("Connection failed: ". $dbh->connect_error);
	}


?>
