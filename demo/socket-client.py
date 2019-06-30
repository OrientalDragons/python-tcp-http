import socket
import time
cl=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

cl.connect(("192.168.2.130",80))
while True:
    try:
        out = input("say somthing:\n")
        if out=="exit":
            break
        cl.send(out.encode("utf-8"))
        time.sleep(1)
        msg=cl.recv(1024)
        print(msg.decode("utf-8"))
    except Exception as e:
        print(e)
        break
cl.close()
