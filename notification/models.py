from django.db import models

from account.models import Profile

from group.models import Group


# Create your models here.



class Notification(models.Model):
    sender = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name='receiver')
    post = models.ForeignKey(Group,on_delete=models.CASCADE,null=True)
    action = models.CharField(max_length=50, blank=True)
    read = models.BooleanField(default=False)    
    created_dt = models.DateTimeField(auto_now_add=True)