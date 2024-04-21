## 프로젝트명 : Chat⌨️💬 (2024.04)

**총 개발인원 : 1명**

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
서비스 완료 후 사용을 하지않는 ubuntu 가상 서버를 2주 정도 이용할수있는 기회가 있어 실제 서비스까지 제공하기 위해 타임어택으로 개발할 주제를 찾고있었습니다. 웹 개발을 시작한 후 전통적인 Http/Https 프로토콜을 이용한 통신, CRUD api 개발만 하다보니 조금 색다른 개발을 하고 싶었습니다. 학부생 시절 c#으로 채팅 소켓 프로그래밍을 과제로 구현했던 경험을 기반으로 ws(또는 보안 연결에 wss) 프로토콜을 사용하는 웹소켓 채팅 프로그램을 웹서비스화 해봐야겠다는 생각이 들었습니다. 
오늘날 채팅은 웹과 모바일 애플리케이션에서 필수적인 요소가 되었습니다. 웹소켓은 HTTP 기반 통신보다 훨씬 효율적인 방법으로 실시간 양방향 통신을 제공하며, 채팅 애플리케이션의 중요 요구 사항을 만족시킬 수 있습니다.

## 개발 의의
 * Python + Django 사용.
 * Http/Https 외 ws(또는 보안 연결에 wss) 프로토콜을 사용.
 * 웹소켓 서버 구현 및 배포
 * 혼자서 만든 첫번째 사이드 프로젝트

## ERD

<img width="891" alt="스크린샷 2024-04-21 오후 4 14 59" src="https://github.com/qudwn1114/django-chat/assets/39257040/242be141-8e6f-49bf-8aa7-484ace5e4ea0">
