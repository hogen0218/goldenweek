import socket
ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.connect(('www.baidu.com',80))

data = "POST {} HTTP/1.1\r\n" \
       "Host:{}\r\n" \
       "Connection:close\r\n" \
       "User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36\r\n\r\n".format(
    '/', 'www.baidu.com').encode('utf8')


ss.send(data)
res =b''
while True:
    msg = ss.recv(1024)
    res+=msg
    if not msg:
        break
print(res.decode('utf8'))

