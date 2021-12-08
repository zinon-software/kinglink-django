from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()
from whatsApp.models import Sections, Category

# Create your models here.

class Group(models.Model):
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='created_by_user')
    titel = models.CharField(max_length=100, null=True, blank=True)
    link = models.CharField(max_length=255)
    activation = models.BooleanField(default=False, null=True, blank=True)
    created_dt = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, default=1, null=True, blank=True, related_name='Category_by', on_delete=models.CASCADE)
    sections = models.ForeignKey(Sections, default=1, null=True, blank=True, related_name='Sections_by', on_delete=models.CASCADE)
    views = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.id)