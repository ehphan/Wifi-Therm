Wifi temperature and humidity sensor (DHT11 + ESP8266)

Requirements:

- sudo apt install picocom
- pip3 install esptool

Provisioning an ESP8266 board:

1. Connect via USB cable
2. `./eraseflash.sh`
3. `./flashfirmware.sh <path_to_bin>`
4. `./connectoverusb.sh`
5. In the REPL: `import webrepl_setup`, `E`, enter a `<webrepl_pw>`, `y` to reset the board.
6. Continuing in the reset REPL:

    > import network
    > sta_if = network.WLAN(network.STA_IF)
    > sta_if.active(True)
    > sta_if.connect("<wifi_ssid>", "<wifi_pw>")
    > sta_if.ifconfig() # will print connection info

    If the first number of the tuple is `0.0.0.0`, rerun the `.connect()` line, then run the `.ifconfig()` line again. Repeat this until a valid IP has been assigned.

7. On your router, map the board to `<board_static_ip>`.
8. Reset the board.
9. `./uploadpyfiles.sh <board_static_ip> <webrepl_pw>`
10. Connect the DHT11 to the board.
11. Reset the board and run `./listen.sh` to confirm it is sending TCP packets.
