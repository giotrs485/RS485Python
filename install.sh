# system requirements
sudo apt-get update
sudo apt-get install vim

# python libs
pip install websocket-client

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