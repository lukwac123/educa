import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.utils import timezone

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope['user']
        self.id = self.scope['url_route']['kwargs']['course_id']
        self.room_group_name = f'chat_{self.id}'
        # Dołączenie do grupy pokoju
        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)
        
        # Akceptacja połączenia
        self.accept()

    def disconnect(self, close_code):
        # Opuść grupę pokoju rozmów
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name)

    # Odbiór komunikatu z WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        now = timezone.now()
        # Wyślij komunikat do grupy pokoju
        async_to_sync(self.channel_layer.group_send)(self.room_group_name, {
            'type': 'chat_message',
            'message': message,
            'user': self.user.username,
            'datetime': now.isoformat(),
        })

    # Odebranie wiadomości z grupy pokoju rozmów
    def chat_message(self, event):
        # Wysłanie komunikatu do WebSocket
        self.send(text_data=json.dumps(event))