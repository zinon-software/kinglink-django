# todo/urls.py : App urls.py
from django.urls import path, include

urlpatterns = [
    path('', include('group.api.urls')),
]