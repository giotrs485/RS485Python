# system requirements
sudo apt-get update
sudo apt-get install vim
sudo -H pip install -U pip

# python libs
sudo pip install redis
sudo pip install websocket-client

sudo apt-get install python-smbus
sudo apt-get install python-serial

# dependencies
rm -rf dependency
mkdir dependency
cd dependency

mkdir wiringpi
wget http://206.189.166.192/wiringpi.tar.gz
tar -xzvf wiringpi.tar.gz -C ./wiringpi --strip-components 1
rm -rf wiringpi.tar.gz
cd wiringpi
chmod 777 build
./build
cd ..         

mkdir bcm2835
wget http://206.189.166.192/bcm2835.tar.gz
tar -xzvf bcm2835.tar.gz -C ./bcm2835 --strip-components 1
rm -rf bcm2835.tar.gz
cd bcm2835
./configure
make
sudo make check
sudo make install
cd ..

mkdir rpigpio
wget http://206.189.166.192/rpigpio.tar.gz
tar -xzvf rpigpio.tar.gz -C ./rpigpio --strip-components 1
rm -rf rpigpio.tar.gz
cd rpigpio
sudo python setup.py install
cd ..

mkdir spidev
wget http://206.189.166.192/spidev.tar.gz
tar -xzvf spidev.tar.gz -C ./spidev --strip-components 1
rm -rf spidev.tar.gz
cd spidev
sudo python setup.py install
cd ..

# redis
sudo apt-get install build-essential tcl
wget http://download.redis.io/redis-stable.tar.gz
tar xzvf redis-stable.tar.gz
rm -rf redis-stable.tar.gz
cd redis-stable
make
make test
sudo make install
sudo mkdir /etc/redis

cd ../../
sudo cp configure/redis.conf /etc/redis
sudo cp configure/redis.service /etc/systemd/system/

sudo adduser --system --group --no-create-home redis
sudo mkdir /var/lib/redis
sudo chown redis:redis /var/lib/redis
sudo chmod 770 /var/lib/redis

sudo systemctl enable redis
sudo systemctl start redis
sudo systemctl status redis

echo 'config set stop-writes-on-bgsave-error no' | redis-cli

# system service
sudo cp rs485-python.sh /etc/init.d/rs485-python.sh
sudo chmod +x /etc/init.d/rs485-python.sh
sudo update-rc.d rs485-python.sh defaults 9999