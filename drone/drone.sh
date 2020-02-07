#!/bin/sh
FILE="run.py"
CNT="0"

cd /var/www/html/drone/

if [ $CNT = 0 ]; then
  python3 /var/www/html/drone/func1.py
  $CNT="1"
fi
while true ; do

if [ -e $FILE ]; then
  echo "kesud"
  rm $FILE
fi
date +"%H:%M:%S"
wget https://system.kns-iv.com/mirai/drone/drone_config/run.py
echo $?

if [ -e $FILE ]; then
    python3 /var/www/html/drone/error_beep.py
    echo "found!!!"
    wget --post-data="&textbox=get" https://system.kns-iv.com/mirai/drone/post2.php
    python3 /var/www/html/drone/run.py

    curl -X PUT -u kirby:admin "http://kns-iv.com/owncloud/remote.php/webdav/Documents/load.py" --data-binary @/var/www/html/pic/*
else
    echo "notfound"
fi
sleep 10
done
