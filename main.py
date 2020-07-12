import dht
import machine
import network
import socket
import time

import credentials as creds


def main():
    # turn off access point
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)

    # connect to wifi
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    while not sta_if.isconnected():
        print("trying to connect to wifi")
        sta_if.connect(creds.wifi_ssid, creds.wifi_pass)
        time.sleep(5)
    print("connected to wifi!")
    print(sta_if.ifconfig())

    # connect to DHT11
    d = dht.DHT11(machine.Pin(5))

    # main communication loop
    s = None
    while True:
        s = ensure_connection(s, creds.listener_ip, creds.listener_port)

        d.measure()
        tempC = d.temperature()
        humidity = d.humidity()

        message = "hello, {:0.1f}C, {:0.1f}%\n".format(tempC, humidity)
        print(message)
        s.send(message)
        time.sleep(5)


def ensure_connection(s, listener_ip, listener_port):
    # TODO: this tries to establish a new connection each time,
    #       should persist previous connection if the connetion is
    #       still alive
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
