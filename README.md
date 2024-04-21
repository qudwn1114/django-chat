# Chat⌨️💬 

**총 개발인원 : 1명 (2024.04)**

## 프로젝트 소개

 회원 가입 후 원하는 채팅방에 참여하여 참여인원들과 소통할 수 있는 **실시간 채팅 서비스** 입니다. 
 
 채팅방에 신규 혹은 재 입장시 **이전 채팅 기록** 까지 모두 확인 가능합니다.

## 기술 스택

|Category| - |
| --- | --- |
|Language|Python v3.10.14|
|Web Server|Nginx v1.18.0 (Ubuntu)|
|WSGI Server|Gunicorn v22.0.0|
|ASGI Server|Daphne v4.1.2|
|Web Framework|Django v4.2.11|
|DB|MySQL, Redis|

## 개발 동기
서비스 완료 후 사용을 하지않는 ubuntu 가상 서버를 2주 정도 이용할수있는 기회가 있어 실제 서비스까지 제공하기 위해 타임어택으로 개발할 주제를 찾고있었습니다. 웹 개발을 시작한 후 전통적인 http/https 프로토콜을 이용한 통신, CRUD api 개발만 하다보니 조금 색다른 개발을 하고 싶었습니다. 

학부생 시절 c#으로 채팅 소켓 프로그래밍을 과제로 구현했던 경험을 기반으로 ws(또는 보안 연결에 wss) 프로토콜을 사용하는 웹소켓 채팅 프로그램을 웹서비스화 해보면 어떨까 생각이 들었습니다.

오늘날 채팅은 웹과 모바일 애플리케이션에서 필수적인 요소가 되었습니다. 웹소켓은 HTTP 기반 통신보다 훨씬 효율적인 방법으로 실시간 양방향 통신을 제공하며, 채팅 애플리케이션의 중요 요구 사항을 만족시킬 수 있습니다.

## 개발 의의
 * Python + Django 사용.
 * http/https 와 ws/wss 프로토콜을 모두 사용.
 * 웹소켓 서버 구현 및 배포
 * Channels 라이브러리를 사용하여 Django 애플리케이션에 ASGI 기능 사용. (Django는 기본적으로 ASGI를 지원 X)
 * 타임어택 개발

## ERD
- 회원은 여러 개의 채팅방을 가질 수 있다.
- 채팅방은 여러 명의 회원을 수용할 수 있다.

<img width="891" alt="스크린샷 2024-04-21 오후 4 14 59" src="https://github.com/qudwn1114/django-chat/assets/39257040/242be141-8e6f-49bf-8aa7-484ace5e4ea0">

## 시연

### 나의 계정을 생성하세요! 😀
<img src = "https://github.com/qudwn1114/django-chat/assets/39257040/a288bc6e-9ee2-4479-bd99-7e23ab9f25af" width="800px">

### 로그인 후 채팅방을 생성하세요! 😆
<img src = "https://github.com/qudwn1114/django-chat/assets/39257040/04c4be57-04f6-4db3-9ec3-7e19e7b9bc38" width="800px">

### 채팅방에 참여해 실시간으로 1:1 채팅을 하세요! 🤩
<img src = "https://github.com/qudwn1114/django-chat/assets/39257040/49ab07ae-d989-4726-bf78-42dd57a225ae" width="800px">
<img src = "https://github.com/qudwn1114/django-chat/assets/39257040/e41b8d64-7635-4d5a-87f3-bfb52c5a4ff5" width="800px">

### 채팅방에 여러명이 참여해 실시간으로 다중채팅을 하세요! 😎
<img src = "https://github.com/qudwn1114/django-chat/assets/39257040/4c03397b-9832-44a1-ade1-b0210cbaa603" width="800px">

### 채팅방을 나갔다 와도 이전 채팅내역을 볼 수 있어요! 👀
<img src = "https://github.com/qudwn1114/django-chat/assets/39257040/c02404c4-0cf0-4ca8-87a7-1971a283cf66" width="800px">

### 자리를 비울 때에는 로그아웃을 해주세요! 🚪
<img src = "https://github.com/qudwn1114/django-chat/assets/39257040/902ac9fb-297b-48ac-b0e3-19abafd56461" width="800px">
