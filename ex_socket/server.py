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
    print('���ӵ�ַ:',addr)
    c.send(('��ӭ�㣬����!\n' +'�յ���ش�!').encode())  #encode()ת����str,decode()ת����bety
    #c.send(('�յ���Ӧ��!!!').encode())
    recvdata=c.recv(1024)
    stringrecvdata=recvdata.decode()
    print('client:' + recvdata.decode())
    if (len(recvdata) >  0):
        c.send(('�յ���Ӧ��Ϣ--'+stringrecvdata).encode())
    else :
        c.send((' have not get the message !').encode())   
    
  


