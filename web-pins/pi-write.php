<?php

$pin = $_POST['pin'];
$mode = $_POST['mode'];
$command = "sudo python GPIO_write.py $mode $pin";

//echo($command);

$result = shell_exec($command);

echo($result);



?>