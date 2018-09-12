pip install websocket-client

sudo apt-get install python-smbus
sudo apt-get install python-serial

cd wiring-pi
chmod 777 build
./build

cd ../bcm2835
./configure
make
sudo make check
sudo make install

cd ../rpi-gpio
sudo python setup.py install

cd ../spidev
sudo python setup.py install