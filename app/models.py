from django.db import models
from django.contrib.auth.models import User 


class MyChat(models.Model):
    me = models.ForeignKey(to= User, on_delete= models.CASCADE, related_name= "its_me")
    frnd = models.ForeignKey(to= User, on_delete= models.CASCADE, related_name= "my_frnd")
    chats = models.JSONField(default= dict)