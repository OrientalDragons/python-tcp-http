'''请求报文    
GET / HTTP/1.1
Host: 127.0.0.1
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
'''

import socket
import time
cl=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

cl.connect(("192.168.2.130",80))

try:
    out='''GET / HTTP/1.1\t\nHost: 127.0.0.1\t\nConnection: keep-alive\t\nCache-Control: max-age=0\t\nUpgrade-Insecure-Requests: 1\t\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36\t\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\t\nAccept-Encoding: gzip, deflate, br\t\nAccept-Language: zh-CN,zh;q=0.9\t\n\n\nxxx\n'''
    cl.send(out.encode("utf-8"))
    time.sleep(1)
    msg=cl.recv(1024)
    print(msg.decode("utf-8"))
except Exception as e:
    print(e)
cl.close

'''
HTTP/1.0 200 OK
Server: BaseHTTP/0.6 Python/3.7.2
Date: Sun, 30 Jun 2019 07:12:11 GMT

helloword
'''
