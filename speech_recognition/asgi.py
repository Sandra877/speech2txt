import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from transcriber.consumers import TranscriptionConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'speech_recognition.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/transcribe/', TranscriptionConsumer.as_asgi()),
        ])
    ),
})
