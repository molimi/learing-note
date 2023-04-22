# -*- encoding: utf-8 -*-
# @Author: CarpeDiem
# @Date: 230419
# @Version: 1.0
# @Description: 一个提供时间日期的服务器


from socket import socket, SOCK_STREAM, AF_INET, gethostname

def main():
    # 1.创建套接字对象默认使用IPv4和TCP协议
    # client = socket()
    client = socket(family=AF_INET, type=SOCK_STREAM)

    # 2.连接到服务器（需要指定IP地址和端口）
    # client.connect(('10.69.164.78', 1030))
    host = gethostname()            # 获取本地主机名
    port = 9999                     # 绑定端口号
    client.connect((host, port))

    # 3.从服务器接受数据, 接收小于 1024 字节的数据
    print(client.recv(1024).decode('utf-8'))
    client.close()

if __name__ == "__main__":
    main()