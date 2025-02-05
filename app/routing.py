from django.urls import path
from app.consumers import MyChatApp

websocket_urlpatterns = [
    path('ws/ajwsc/', MyChatApp.as_asgi()),
]