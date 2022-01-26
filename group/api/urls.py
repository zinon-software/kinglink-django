# todo/api/urls.py : API urls.py
from django.urls.conf import path
from .views import GroupListApiView, MyGroupListApiView, GroupDetailApiView, PostListApiView, UpdateViewsGroupApiView, LikeApiView


urlpatterns = [
    path("", MyGroupListApiView.as_view()),
    path("groups", GroupListApiView.as_view()),
    path("posts", PostListApiView.as_view()),
    path('<int:group_id>', GroupDetailApiView.as_view()),
    path('views/<int:group_id>', UpdateViewsGroupApiView.as_view()),
    path('like/<int:pk>',LikeApiView.as_view(),name='like'),
]