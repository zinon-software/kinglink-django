from django.db import models

from django.contrib.auth import get_user_model

from account.models import Profile
User = get_user_model()

# Create your models here.




class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name

class Sections(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name



class Group(models.Model):
    created_by = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE, related_name='created_by_user')
    titel = models.CharField(max_length=100, null=True, blank=True)
    link = models.CharField(max_length=170)
    activation = models.BooleanField(default=False, null=True, blank=True)
    created_dt = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, default=1, null=True, blank=True, related_name='Category_by', on_delete=models.CASCADE)
    sections = models.ForeignKey(Sections, default=1, null=True, blank=True, related_name='Sections_by', on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(Profile, related_name='likes',blank=True)

    @property
    def total_likes(self):
        return self.likes.count()
        
    def __str__(self):
        return str(self.id)