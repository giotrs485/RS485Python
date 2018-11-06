#! /bin/sh -e
exec 2> /home/lijian/Code/RS485Python/logs/rc.local.log 
exec 1>&2
set -x

while !(127.0.0.1:6379 ping)
do
   sleep 3
   echo "waiting for redis ..."
done

echo 'config set stop-writes-on-bgsave-error no' | redis-cli
ps aux | grep -ie nohup | awk '{print $2}' | sudo xargs kill -9
sudo nohup /usr/bin/python -u /home/lijian/Code/RS485Python/code/socket_worker.py 1>/home/lijian/Code/RS485Python/logs/socket_worker.log 2>/home/lijian/Code/RS485Python/logs/socket_worker.log &
sudo nohup /usr/bin/python -u /home/lijian/Code/RS485Python/code/serial_worker.py 1>/home/lijian/Code/RS485Python/logs/serial_worker.log 2>/home/lijian/Code/RS485Python/logs/serial_worker.log &

exit 0
