from django.db import models

from django.contrib.auth import get_user_model

from group.models import Group
User = get_user_model() 

# Create your models here.



class Notification(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User,on_delete=models.CASCADE, related_name='receiver')
    post = models.ForeignKey(Group,on_delete=models.CASCADE,null=True)
    action = models.CharField(max_length=50, blank=True)
    read = models.BooleanField(default=False)    
    created_dt = models.DateTimeField(auto_now_add=True)