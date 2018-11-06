#! /bin/sh 

exec 2> /home/lijian/Code/RS485Python/rc.local.log 
exec 1>&2
set -x

sudo bash /home/lijian/Code/RS485Python/start.sh
exit 0
