from email import message
from http import client
from socket import *
import threading
from time import sleep

from django.shortcuts import render

def index(request):
    context = {}
    soc = request.GET.get('socket', '')
    if soc != '':
        port = 9999
        try:
            clientSock = socket(AF_INET, SOCK_STREAM)
            clientSock.connect(('127.0.0.1', port))
            clientSock.settimeout(5)
            msg = soc
            clientSock.send(msg.encode('utf-8'))
            data = clientSock.recv(1024)
            print('받은 데이터 : ', data.decode('utf-8'))
            data = clientSock.recv(1024)
            print('받은 데이터 : ', data.decode('utf-8'))
            clientSock.close()
        except timeout:
            print('시간초과 다시시도해주세요.')
        except Exception as e:
            print('접속에러발생..')

    
    return render(request, 'index.html', context)

def send(socket, message): 
    socket.send(message.encode('utf-8'))

def receive(socket): 
    while True: 
        try: 
            message = socket.recv(1024).decode('utf-8')
            print(message)
        except: 
            print("An error occured!") 
            socket.close() 
            break

def room(request, room_name):
    context = {}
    context['room_name'] = room_name

    return render(request, 'room.html', context)