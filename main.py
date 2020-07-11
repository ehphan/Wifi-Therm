import time
import network
import socket

import credentials as creds


def main():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)

    while not sta_if.isconnected():
        print("trying to connect to wifi")
        sta_if.connect(creds.wifi_ssid, creds.wifi_pass)
        time.sleep(5)

    print("connected to wifi!")
    s = None
    while True:
        s = ensure_connection(s, creds.listener_ip, creds.listener_port)
        print("hello")
        s.send("hello\n")
        time.sleep(5)


def ensure_connection(s, listener_ip, listener_port):
    if s is None:
        s = socket.socket()

    print("trying to connect to socket")
    while True:
        try:
            s.connect((listener_ip, listener_port))
        except OSError as e:
            print("connection failed to socket")
            s.close()
            s = socket.socket()
            time.sleep(1)
            continue
        break
    return s


if __name__ == "__main__":
    main()
