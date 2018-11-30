<?php

$pin = $_GET['pin'];
$mode = $_GET['mode'];
$command = "python gpio_write.py $mode $pin";

//echo($command);

$result = exec($command);


echo "pin:$pin mode:$result";



?>
