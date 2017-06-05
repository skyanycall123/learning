#!/usr/bin/python
#-*- coding: gbk -*- 
# file name server.py

import socket

s = socket.socket()
host = '192.168.80.137'
port=12345
s.bind((host,port))


s.listen(5)
while True :
    c,addr= s.accept()
    print('连接地址:',addr)
    c.send(('欢迎你，菜鸟!\n' +'收到请回答!').encode())  #encode()转换成str,decode()转换成bety
    #c.send(('收到请应答!!!').encode())
    recvdata=c.recv(1024)
    stringrecvdata=recvdata.decode()
    print('client:' + recvdata.decode())
    if (len(recvdata) >  0):
        c.send(('收到回应消息--'+stringrecvdata).encode())
    else :
        c.send((' have not get the message !').encode())   
    
  


