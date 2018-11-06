echo 'config set stop-writes-on-bgsave-error no' | redis-cli
ps aux | grep -ie nohup | awk '{print $2}' | sudo args kill -9
sudo nohup python -u ./code/socket_worker.py > ./code/socket_worker.out 2>&1 &
sudo nohup python -u ./code/serial_worker.py > ./code/serial_worker.out 2>&1 &
