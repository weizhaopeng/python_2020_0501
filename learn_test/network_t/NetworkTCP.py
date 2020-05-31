from base64 import b64decode
from datetime import datetime
from json import dumps, loads
from socket import socket, AF_INET
from threading import Thread


def main():
    # 创建套接字对象，指定好套接字使用的ip类型
    # family = AF_INET 表示ipv4
    # family = AF_INET6 表示ipv6
    # type = SOCK_STREAM表示tcp传输层协议，使用了流协议
    # type = SOCK_DGRAM表示使用UDP传输层协议，使用了数据包协议
    # type = SOCK_RAM表示原始套接字
    server = socket(family=AF_INET, type=AF_INET)
    # 设置监听，将服务绑定到地址+端口，同一时间一个地址+端口只能为一个服务服务
    server.bind('192.168.5.1', 465)
    # 开启监听，相当于套接字开始监听地址+端口, 其中监听里面的参数表示对接队列的大小
    server.listen(1024)
    print('server is listening')
    while True:
        # accept方法主要是阻塞在这里，当有客户端通过connect方法连接到服务器的时候，接受并且返回客户端的对象和地址
        clientObject, clientAddr = server.accept()
        print(str(clientAddr) + 'server connected!')
        clientObject.send(str(datetime.now()).encode('utf-8'))
        clientObject.close()


def main1():
    '''
    客户端程序示例
    :return:
    '''
    client = socket()
    client.connect('192.168.126.26', 465)
    print(client.recv(1024).decode('utf-8'))
    client.close()


def main2():
    class FileTransferHandler(Thread):
        def __init__(self, client):
            super().__init__()
            self.client = client

        def run(self):
            dirt1 = {}
            dirt1['filename'] = 'guido.jpg'
            dirt1['filedate'] = 'data'
            json_str = dumps(dirt1)
            self.client.send(json_str.encode('utf-8'))
            self.client.close()

    server = socket()
    server.bind('192.168.5.1', 5665)
    server.listen()
    print('server is listening')
    with open('guido.jpg', 'rb') as f:
        data = b64decode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        FileTransferHandler(client).start()


def main3():
    client = socket()
    client.connect(('192.168.5.1', 5665))
    in_data = bytes()
    data = socket.recv(1024)
    while data:
        in_data += date
        date = client.recv(1024)
    myDirt = loads(in_data.decode('utf-8'))
    filename = myDirt['filename']
    filedata = myDirt['filedata']
    with open('new' + filename, 'wb') as f:
        f.write(b64decode(filedata))
    print('image has saved')


if __name__ == '__main__':
    main2()
    main3()
