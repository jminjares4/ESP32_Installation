# ESP32_Installation

This repository was develop based on the guidelines of: [Espressif ESP32 installation guide](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html#step-1-install-prerequisites). 

# Dependencies
## Linux Dependencies
```bash
#install all dependencies
sudo apt-get install git wget flex bison gperf python3 python3-pip python3-setuptools cmake ninja-build ccache libffi-dev libssl-dev dfu-util libusb-1.0-0
```
## MacOS Dependencies
```bash
xcode-select --install
```

# Installation
## MacOS or Linux 
### Install through bash script
```bash
chmod +x installation.sh
./installation.sh
```

### Install through python
```bash
python3 esp32_installation.py
```
## Windows
- Use Windows Installer: [ESP32 Windows Installation](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/windows-setup.html)


# ESP-IDF alias
- If you plan to ues esp-idf frequently, you can create an alias for executing export.sh:
Copy and paste the following command to your shell’s profile (.profile, .bashrc, .zprofile, etc.)
    ```bash
    alias get_idf='. $HOME/esp/esp-idf/export.sh'
    ```
* Refresh the configuration by restarting the terminal session or by running source [path to profile], for example, source ~/.bashrc.
  
Now you can run get_idf to set up or refresh the esp-idf environment in any terminal session.

## Author:
[***Jesus Minjares***](https://github.com/jminjares4)
  * **Master of Science in Computer Engineering** <br>
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&style=flat)](https://www.linkedin.com/in/jesusminjares/) [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white&style=flat)](https://github.com/jminjares4)