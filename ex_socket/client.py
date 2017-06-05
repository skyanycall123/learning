#! E:notepad/python34/
#coding=utf-8
#filename client.py


import socket

s=socket.socket()
host='192.168.80.137'
port=12345
s.connect((host,port))
#print (s.recv(1024).decode())    #decode()转码
print ('server:' + s.recv(1024).decode())    #decode()转码
s.send(('我已收到信息!').encode())
print('client:ok')
getmessage=s.recv(1024)
print(getmessage.decode())
print('server:' + getmessage.decode())
