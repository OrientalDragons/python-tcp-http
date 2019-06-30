import socket


'''
socket类型                 描述

socket.AF_UNIX            只能够用于单一的Unix系统进程间通信
socket.AF_INET            服务器之间网络通信
socket.AF_INET6           IPv6
socket.SOCK_STREAM        流式socket , for TCP
socket.SOCK_DGRAM         数据报式socket , for UDP
socket.SOCK_RAW           原始套接字，普通的套接字无法处理ICMP、IGMP等网络报文，
                          而SOCK_RAW可以；其次，SOCK_RAW也可以处理特殊的IPv4报文；
                          此外，利用原始套接字，可以通过IP_HDRINCL套接字选项由用户构造IP头。
socket.SOCK_SEQPACKET     可靠的连续数据包服务
创建TCP Socket：          s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
创建UDP Socket：          s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
'''
'''socket服务器编程思路
1 创建套接字，绑定套接字到本地IP与端口  # socket.socket(socket.AF_INET,socket.SOCK_STREAM) , s.bind()
2 开始监听连接                        #s.listen()
3 进入循环，不断接受客户端的连接请求    #s.accept()
4 然后接收传来的数据，并发送给对方数据  #s.recv() , s.sendall()
5 传输完毕后,关闭套接字               #s.close()
'''

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="0.0.0.0"
port=80
server.bind((host,port))
server.listen(5)#连接数
while True:
    cl,addr=server.accept()
    print("地址:{}".format(str(addr)))
    while True:
        try:
            msg=cl.recv(1024)
            if msg.decode("utf-8")=="exit" or not msg:
                print(msg.decode("utf-8"))
                break
            print(msg.decode("utf-8"))
            cl.send("""hello,you had said '{0}'""".format(msg.decode("utf-8")).encode('utf-8'))

            print("send ok")
            # cl.close()
        except Exception as e:
            print(e)
            break
    cl.close()

'''    
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