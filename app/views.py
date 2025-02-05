from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . models import MyChat


def index(request):
    frnd_name = request.GET.get('user', None)
    mychats_data = None
    if frnd_name:
        if User.objects.filter(username= frnd_name).exists() and MyChat.objects.filter(me= request.user, frnd= User.objects.get(username= frnd_name)):
            frnd_ = User.objects.get(username= frnd_name)
            mychats_data = MyChat.objects.get(me= request.user, frnd= frnd_).chats
    frnds = User.objects.exclude(id= request.user.id)
    context = {
        # 'my' : mychats_data,
        'chats' : mychats_data,
        'frnds' : frnds
    }
    return render(request, 'index.html', context)
