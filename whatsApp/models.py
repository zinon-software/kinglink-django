from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Groub(models.Model):
    
    created_by = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name='user_created_by')
    name = models.CharField(max_length=100, null=True, blank=True)
    link = models.CharField(max_length=255)
    activation = models.BooleanField(default=False, null=True, blank=True)
    created_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    