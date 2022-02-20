from django.shortcuts import render
from .models import Channel, Message

# Create your views here.
def channels(request):
    channel_list = Channel.objects.all()
    context = {'channels' : channel_list}
    return render(request, 'channels.html', context)

def channel(request, id):
    channel = Channel.objects.get(id=id)
    message_list = channel.message_set.all()
    context= {'messages': message_list, 'channel': channel}
    return render(request, 'channel.html', context)