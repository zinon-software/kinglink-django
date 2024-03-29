from django.db import models
from django.contrib.auth.models import User

# Create Group models here.



class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name

class Sections(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name


class Groub(models.Model):
    created_by = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name='user_created_by')
    name = models.CharField(max_length=100, null=True, blank=True)
    link = models.CharField(max_length=255)
    activation = models.BooleanField(default=False, null=True, blank=True)
    created_dt = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, default=1, null=True, blank=True, related_name='Category_name', on_delete=models.CASCADE)
    sections = models.ForeignKey(Sections, default=1, null=True, blank=True, related_name='Sections_name', on_delete=models.CASCADE)
    views = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.id)
    



# Create comments models here.

class Comment(models.Model):
    sender = models.ForeignKey(User, null=True, blank=True, related_name='sent_comment', on_delete=models.CASCADE)
    group = models.ForeignKey(Groub, null=True, blank=True, related_name='post_group', on_delete=models.CASCADE)
    message = models.TextField()
    created_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Report(models.Model):
    group = models.ForeignKey(Groub, null=True, blank=True, related_name='report_group', on_delete=models.CASCADE)
    message = models.TextField()
    created_dt = models.DateTimeField(auto_now_add=True)