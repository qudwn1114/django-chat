from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from chat.models import ChatRoom, ChatUser, ChatMessage

import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:    
            self.room_name = self.scope['url_route']['kwargs']['room_name']
            self.room_group_name = f'chat_{self.room_name}'

            # 채팅방을 가져오거나 생성합니다.
            room = await self.get_or_create_room(room_name=self.room_id)

            # send 등 과 같은 동기적인 함수를 비동기적으로 사용하기 위해서는 async_to_sync 로 감싸줘야함
            # 현재 채널을 그룹에 추가합니다. 
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()
        except ValueError as e: # 값 오류가 있을 경우 (예: 방이 존재하지 않음), 오류 메시지를 보내고 연결을 종료합니다.
            await self.send_json({'error': str(e)})
            await self.close()

    async def disconnect(self, close_code):
        try:  
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )
        except Exception as e: # 일반 예외를 처리합니다 (예: 오류 기록).         
            pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        chat_room_id = text_data_json['chat_room_id']
        user_id = text_data_json['user_id']
        message = text_data_json['message']

        await self.save_message(chat_room_id, user_id, message)

        # room group 에게 메세지 send
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # room group 에서 메세지 receive
    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        
        # WebSocket 에게 메세지 전송
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))


@database_sync_to_async
def get_or_create_room(self, room_name):
    room, created = ChatRoom.objects.get_or_create(room_name=room_name)
    return room


@database_sync_to_async
def save_message(self, chat_room_id, user_id, message):
    # 발신자 이메일과 메시지 텍스트가 제공되었는지 확인합니다.
    if not chat_room_id or not user_id or not message:
        raise ValueError("채팅방, 발신자 및 메시지가 필요합니다.")
    # 메시지를 생성하고 데이터베이스에 저장합니다.
    ChatMessage.objects.create(chat_room_id=chat_room_id, user_id=user_id, message=message)