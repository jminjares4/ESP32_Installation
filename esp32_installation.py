'''
Author: Jesus Minjares
        Master of Science in Computer Engineering

Date:   05/13/2022

Objective:  The installation is based on Espressif installation guide. For more
            information go to: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html#installation
'''

import os, sys, stat
from sys import platform

def main():

    # Store parent directory path 
    parent_path = os.getcwd()
    print(parent_path)

    # MacOs and Linux Installation
    if platform == "darwin" or platform == 'linux':

        print("\033[1;32m Running MacOS installation")

        # store home directory
        home = os.path.expanduser('~')
        # change to parent directory
        os.chdir(parent_path)

        # Create esp folder, and go to ~/esp
        print('\033[1;32m Making esp directory...')
        esp_path = f"{home}/esp/"
        os.system(f'mkdir -p {esp_path}')
        os.chdir(esp_path)
        
        # clone git repository
        print('\033[1;32m cloning esp repository \u001b[0m')
        os.system('git clone --recursive https://github.com/espressif/esp-idf.git')
        
        # install esp32
        # if you have a different ESP32:
        #       esp32, esp32s, all 
        # 
        print('\033[1;32m Setting up tools for esp32 \u001b[0m')
        os.chdir('esp-idf')
        os.system('./install.sh esp32') # install the esp32, change if you have a different one

        # Set enviroment variables
        print('\033[1;32m Set up the environment variables \u001b[0m')
        os.system('. ./export.sh')

        # return to parent directory
        print(f'\033[1;32m Returning to {parent_path} \u001b[0m')
        os.chdir(parent_path)

        # Installation complete
        print("\033[1;32m Completed installation \u001b[0m")

    elif platform == "windows":
        # provide guide for Windows users
        window_install_page = 'https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/windows-setup.html'
        print(f"\u001b[31m Please go to: \033[1;36m {window_install_page} \u001b[0m")
    else:
        print("\u001b[31m  The is not MacOS, Linux, or Windows...\u001b[0m")
        return

if __name__=="__main__":
    main()