import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="0.0.0.0"
port=80
server.bind((host,port))
server.listen(5)#连接数
while True:
    cl,addr=server.accept()
    print("地址:{}".format(str(addr)))

    try:
        msg=cl.recv(1024)
        print(msg.decode('utf-8'))#打印请求报文
        # 简单模拟http
        out='''HTTP/1.0 200 OK\t\nServer: BaseHTTP/0.6 Python/3.7.2\t\nDate: Sun, 30 Jun 2019 07:12:11 GMT\t\n\nhelloword\n'''
        cl.send(out.encode('utf-8'))
        print("send ok")
    except Exception as e:
        print(e)
        break
    cl.close()

'''响应报文    
HTTP/1.0 200 OK
Server: BaseHTTP/0.6 Python/3.7.2
Date: Sun, 30 Jun 2019 07:12:11 GMT

helloword

'''