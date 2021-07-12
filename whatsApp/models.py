from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create Group models here.

CATEGORY = [
    ('1', 'واتساب'),
    ('2', 'تليجرام'),
    ('3', 'انستقرام'),
    ('4', 'يوتيوب'),
    ('5', 'تطبيق'),
    ('6', 'غير معروف'),
]

SECTIONS = [
    ('1', 'الكل'),
    ('2', 'إسلامية'),
    ('3', 'أنمي'),
    ('4', 'ترفيه'),
    ('5', 'تعارف'),
    ('6', 'وظائف'),
    ('7', 'سياسة'),
    ('8', 'تعليم'),
    ('9', 'نكت'),
    ('10', 'اعلانات'),
    ('11', 'منوع'),
    ('12', 'دعم'),
]

class Groub(models.Model):
    created_by = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name='user_created_by')
    name = models.CharField(max_length=100, null=True, blank=True)
    link = models.CharField(max_length=255)
    activation = models.BooleanField(default=False, null=True, blank=True)
    created_dt = models.DateTimeField(auto_now_add=True)
    # category = models.CharField(max_length=2, choices=CATEGORY, default='1', null=True, blank=True)
    # sections = models.CharField(max_length=2, choices=SECTIONS, default='1', null=True, blank=True)
    views = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.id)
    



# Create comments models here.

# User = get_user_model()

# class Comment(models.Model):
#     sender = models.ForeignKey(User, null=True, blank=True, related_name='sent_comment', on_delete=models.CASCADE)
#     group = models.ForeignKey(Groub, null=True, blank=True, related_name='post_group', on_delete=models.CASCADE)
#     message = models.TextField()
#     created_dt = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.sender.username
    
    
#     class Meta:
#         ordering = ("created_dt",)