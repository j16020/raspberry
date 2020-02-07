<?php
$command="python3 ./drone/beep.py";
exec($command,$output);
print "$output[0]\n";
print "$output[1]\n";
$output = shell_exec("sh ./hoge.sh");
?>
