<?php

$pin = $_GET['pin'];
$mode = $_GET['mode'];
//$command = "/usr/bin/python3 /var/www/html/remoteControlPi/web-pins/gpio_write.py $mode $pin";
//$command = "sudo /usr/bin/python3 /var/www/html/remoteControlPi/web-pins/gpio_write.py $mode $pin";
$command = "python3 gpio_write.py $mode $pin";
//$result = shell_exec($command);
//$command = "/var/www/html/remoteControlPi/web-pins/gpio_write.py $mode $pin";
//$command = escapeshellcmd('./gpio_write.py'); 
//$command = 'python3 test.py 1 17'; 
//$command = 'python3 gpio_write.py 1 17'; 
$result= shell_exec($command); 


echo "pin:$pin mode:$result";


?>
