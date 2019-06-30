import os	#Python的标准库中的os模块包含普遍的操作系统功能
import re	#引入正则表达式对象
# import urllib	#用于对URL进行编解码
from http.server import HTTPServer, BaseHTTPRequestHandler  #导入HTTP处理相关的模块
 
 
#自定义处理程序，用于处理HTTP请求
class TestHTTPHandler(BaseHTTPRequestHandler):
	#处理GET请求
    def do_GET(self):
		#页面输出模板字符串
        print(self.request)
        templateStr = '''helloword'''
        # self.protocal_version = 'HTTP/1.1'	#设置协议版本
        self.send_response(200)	#设置响应状态码
        # self.send_header("Welcome", "Contect")	#设置响应头
        self.end_headers()
        self.wfile.write(templateStr.encode("utf-8"))	#输出响应内容
	
#启动服务函数
def start_server(port):
    http_server = HTTPServer(('0.0.0.0', int(port)), TestHTTPHandler)
    http_server.serve_forever()	#设置一直监听并接收请求
 
# os.chdir('static')	#改变工作目录到 static 目录
start_server(80)	#启动服务，监听8000端口