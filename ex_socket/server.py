#!/usr/bin/python
#coding= gbk
# file name server.py

import socket

s = socket.socket()
host = '192.168.80.137'
port=12345
s.bind((host,port))


s.listen(5)
while True :
    c,addr= s.accept()
    print('���ӵ�ַ:',addr)
    c.send(('��ӭ�㣬����!\n' +'�յ���ش�!').encode())
    #c.send(('�յ���Ӧ��!!!').encode())
    recvdata=c.recv(1024)
    print(recvdata.decode())
    if (len(recvdata) >  0):
        c.send(recvdata)
    else :
        c.send((' have not get the message !').encode())   
    
  

