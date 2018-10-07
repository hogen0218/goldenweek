SOCK_DGRAM

import socket
IP = '127.0.0.1'
PORT = 19525
address = (IP,PORT)
cli = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
cli.connect(address)

while 1:
    input_msg = input('type:')
    cli.send(input_msg.encode('utf-8'))
    msg = cli.recv(1024)
    msg = msg.decode('utf8')
    print(msg)
    if not msg:
        cli.close()
        break