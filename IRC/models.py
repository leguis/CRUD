from email import message
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Channel(models.Model):
    name= models.CharField(max_length=200)
    #users: 
    created_at = models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    message= models.TextField()
    channel_id= models.ForeignKey(Channel, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_id) + '.' + str(self.channel_id) + '.' + self.message