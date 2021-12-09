from django.db import models

from group.models import Group

# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()

# Create comments models here.

class Comment(models.Model):
    sender = models.ForeignKey(User, null=True, blank=True, related_name='sent_comment', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, null=True, blank=True, related_name='post_group', on_delete=models.CASCADE)
    message = models.TextField()
    created_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)