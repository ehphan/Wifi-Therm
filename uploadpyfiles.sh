#!/bin/bash

if [ -z "$2" ]; then
    echo "Usage: ./uploadpyfiles.sh <esp_board_ip> <webrepl_pw>"
    exit
fi

./webrepl_cli -p $2 main.py $1:main.py
./webrepl_cli -p $2 credentials.py $1:credentials.py
