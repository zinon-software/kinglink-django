from django.urls import path

from . import views
from . import api

urlpatterns = [
    path('', views.all_group, name='all_group'),
    path('update_group', views.update_group, name='update_group'),
    path('Report', views.report, name='Report'),


    path('api/Groub', api.GroubApi.as_view(), name='GroubApi'),
    path('api/Groub/<int:id>', api.GroubDetailApi.as_view(), name='GroubDetailApi'),
    
    path('api/Comment', api.CommentApi.as_view(), name='CommentApi'),
    path('api/Comment/<int:id>', api.CommentDetailApi.as_view(), name='CommentDetailApi'),

    path('api/Report', api.ReportApi.as_view(), name='ReportApi'),
    path('api/Report/<int:id>', api.ReportDetailApi.as_view(), name='ReportDetailApi'),

    path('api/Category', api.CategoryApi.as_view(), name='CategoryApi'),
    path('api/Category/<int:id>', api.CategoryDetailApi.as_view(), name='CategoryDetailApi'),

    path('api/Sections', api.SectionsApi.as_view(), name='SectionsApi'),
    path('api/Sections/<int:id>', api.SectionsDetailApi.as_view(), name='SectionsDetailApi'),
]
