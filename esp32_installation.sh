#install all dependencies
sudo apt-get install git wget flex bison gperf python3 python3-pip python3-setuptools cmake ninja-build ccache libffi-dev libssl-dev dfu-util libusb-1.0-0

#check for python3 
python --version

#make directory and clone repo

mkdir -p ~/esp
cd ~/esp
git clone --recursive https://github.com/espressif/esp-idf.git


#install esp32 and set tools

cd ~/esp/esp-idf
./install.sh esp32

#Set enviroment variables
. $HOME/esp/esp-idf/export.sh