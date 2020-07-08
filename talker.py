import network
listener_port = 11111
listener_ip = "192.168.x.y"
ap_if = network.WLAN(network.AP_IF)
s = socket.socket()
s.conect("{}:{}".format(listener_ip, listener_port))
s.connect((listener_ip, listener_port))
