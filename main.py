import network
import json

data = ''
adminCheck = []
flag = False

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('Hakaton_Net', '1qaz2wsx')
while not wlan.isconnected():
    pass
dataStandart = json.dumps(data)


import socket
s = socket.socket()
s.connect(('192.168.1.138', 10000))
s.write('GET /api/test/0 HTTP/1.1\r\nHost: 192.168.1.138\r\n\r\n'.encode())


if flag:
    dataAdminCheck = json.dumps(adminCheck)
    s = socket.socket()
    s.connect(('192.168.1.138', 10000))
    s.write('GET /api/test/0 HTTP/1.1\r\nHost: 192.168.1.138\r\n\r\n'.encode())

while True:
    data = s.recv(256)
    if data:
        print(data)
    else:
        break

s.close()
