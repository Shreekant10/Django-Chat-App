from django.contrib import admin
from . models import MyChat


@admin.register(MyChat)
class MyChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'me', 'frnd', 'chats']