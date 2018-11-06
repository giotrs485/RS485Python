#! /bin/sh 

exec 2> /home/lijian/Code/RS485Python/rc.local.log 
exec 1>&2
set -x

echo 'config set stop-writes-on-bgsave-error no' | redis-cli
ps aux | grep -ie nohup | awk '{print $2}' | sudo xargs kill -9
sudo nohup python -u /home/lijian/Code/RS485Python/code/socket_worker.py > /home/lijian/Code/RS485Python/code/socket_worker.out 2>&1 &
sudo nohup python -u /home/lijian/Code/RS485Python/code/serial_worker.py > /home/lijian/Code/RS485Python/code/serial_worker.out 2>&1 &

exit 0
