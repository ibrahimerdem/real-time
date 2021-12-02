from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
#from .models import Thread, ChatMessage
import asyncio
import json

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('connected', event)

    async def websocket_receive(self, event):
        print('receive', event)

    async def websocket_disconnect(self, event):
        print('disconnected', event)