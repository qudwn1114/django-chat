from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.http import HttpRequest, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.urls import reverse
from django.db import transaction

from email import message
from http import client
from socket import *
import threading
from time import sleep

class LoginView(View):
    '''
        로그인 기능
    '''
    def get(self, request: HttpRequest, *args, **kwargs):
        context = {}
        if request.user.is_authenticated:
            return redirect('chat:home')
        
        return render(request, 'login.html', context)

    def post(self, request: HttpRequest, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            return JsonResponse({'message':'Incorrect ID or password.'}, status = 400)
        
        if not user.check_password(raw_password=password):
            return JsonResponse({'message':'Incorrect ID or password.'}, status = 400)
        if not user.is_active:
            return JsonResponse({'message':'Deactivated account.'}, status = 400)
    
        login(request, user)
        if 'next' in request.GET:
            url = request.GET.get('next')
            url = url.split('?next=')[-1]
        else:
            url = reverse('chat:home')
        return JsonResponse({'message':'Welcome!', 'url':url}, status = 200)


class SignupView(View):
    '''
        회원가입 기능
    '''
    def get(self, request: HttpRequest, *args, **kwargs):
        context = {}
        if request.user.is_authenticated:
            return redirect('chat:home')
        
        return render(request, 'signup.html', context)

    def post(self, request: HttpRequest, *args, **kwargs):
        membername = request.POST['membername']
        username = request.POST['username']
        password = request.POST['password']
        if not validate_password(password):
            JsonResponse({'message':'The password must be 8 to 16 characters long and contain one letter and one number.'}, status = 400)
        try:
            user = User.objects.get(username=username)
            return JsonResponse({'message':'This account has already signed up.'}, status = 400)
        except:
            pass

        try:
            with transaction.atomic(): 
                user = User.objects.create_user(
                    username=username,
                    password=password
                )
                user.first_name = membername
                user.save()
        except:
            return JsonResponse({'message':'Sign up failed..'}, status = 400)
        
        return JsonResponse({"url":reverse('chat:login'), 'message': 'Sign up has been completed.'}, status=201)


class HomeView(LoginRequiredMixin, View):
    '''
        메인화면
    '''
    def get(self, request: HttpRequest, *args, **kwargs):
        context = {}
        
        return render(request, 'index.html', context)

    def post(self, request: HttpRequest, *args, **kwargs):
        room = request.POST['room']
        url =''
        return JsonResponse({'message':'Chat Room Joined', 'url':url}, status = 200)
    

def room(request, room_name):
    context = {}
    context['room_name'] = room_name

    return render(request, 'room.html', context)


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


def validate_password(password):
    '''
        비밀번호 유효성 체크
    '''
    try:
        # Minimum eight characters Maximum 16 characters, at least one letter and one number
        RegexValidator(regex=r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,16}$')(password)
    except:
        return False

    return True