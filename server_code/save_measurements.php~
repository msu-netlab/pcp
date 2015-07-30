<?php
include 'constants.php';
$con = mysql_connect($dbhostname, $dbusername, $dbpassword);
if (!$con)
{
	die('Website down for maintenance. We will be live soon.');
}
mysql_select_db($dbschemaname, $con);

$user_ip = $_GET['user_ip'];
$cdn_ip = $_GET['cdn_ip'];
$rtt = $_GET['rtt'];


$sql = "insert into pcp_measurements (id, user_ip, cdn_ip, rtt) values(NULL, '$user_ip', '$cdn_ip', '$rtt')";
//echo $sql;
if (!mysql_query ($sql,$con)) {
	die('Website down for maintenance. We will be live soon.');
}
else {
	echo "Recorded in DB.";
}

$command = "python /var/www/html/pcp/python/store_measurements.py ".$user_ip." ".$cdn_ip." ".$rtt;
echo exec($command);

?>
