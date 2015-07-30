<?php
  $ip1 = $_GET['ip1'];
  $ip2 = $_GET['ip2'];

  $command = "python python/get_distance.py ".$ip1." ".$ip2;
  echo exec($command);
?>
