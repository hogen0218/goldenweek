import socket
import threading


def re_msg(conn,addr):
    while True:
        print('message form ',addr)
        msg =conn.recv(1024)
        msg=msg.decode('utf8')
        print(msg)
        if msg =='fin':
            conn.send(b'disconnect ')
            server.close()
            break
        remsg = input('type your msg')
        remg='张泽皓：{}'.format(remsg)
        conn.send(remg.encode('utf8'))

ip = '0.0.0.0'
port = 8812
address = (ip,port)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(address)
server.listen(5)
while True:
    conn, addr = server.accept()
    threading.Thread(target=re_msg,args=(conn,addr)).start()