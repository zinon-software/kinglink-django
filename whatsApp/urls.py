from django.urls import path

from . import views
from . import api

urlpatterns = [
    path('', views.all_group, name='all_group'),
    path('update_group', views.update_group, name='update_group'),


    path('api/Groub', api.GroubApi.as_view(), name='GroubApi'),
    path('api/Groub/<int:id>', api.GroubDetailApi.as_view(), name='GroubDetailApi'),
    
    path('api/Comment', api.CommentApi.as_view(), name='CommentApi'),
    path('api/Comment/<int:id>', api.CommentDetailApi.as_view(), name='CommentDetailApi'),
]
