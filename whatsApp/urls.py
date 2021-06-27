from django.urls import path

from . import views
from . import api

urlpatterns = [
    path('', views.all_group, name='all_group'),

    path('api/Groub', api.GroubApi.as_view(), name='GroubApi'),
    path('api/Groub/<int:id>', api.GroubDetailApi.as_view(), name='GroubDetailApi'),
]
