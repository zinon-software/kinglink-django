# todo/api/urls.py : API urls.py
from django.urls.conf import path
from .views import MyGroupListApiView, GroupDetailApiView, UpdateViewsGroupApiView, LikeApiView, SectionsAIPView


urlpatterns = [
    path("", MyGroupListApiView.as_view()),
    path('<int:group_id>', GroupDetailApiView.as_view()),
    path('views/<int:group_id>', UpdateViewsGroupApiView.as_view()),
    path('like',LikeApiView.as_view(),name='like'),
    path('sections',SectionsAIPView.as_view(),name='sections'),
]