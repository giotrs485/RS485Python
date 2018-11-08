#! /bin/sh -e
exec 2> /home/lijian/Code/RS485Python/logs/rc.local.log 
exec 1>&2
set -x

while ! nc -z 127.0.0.1 6379; do   
  sleep 0.1
  echo "waiting for redis ..."
done

echo 'config set stop-writes-on-bgsave-error no' | redis-cli

ps aux | grep -ie nohup | awk '{print $2}' | xargs kill -9

exec nohup /usr/bin/python2.7 -u /home/lijian/Code/RS485Python/code/socket_worker.py > /home/lijian/Code/RS485Python/logs/socket_worker.log 2>&1 &
exec nohup /usr/bin/python2.7 -u /home/lijian/Code/RS485Python/code/serial_worker.py > /home/lijian/Code/RS485Python/logs/serial_worker.log 2>&1 &

exit 0
