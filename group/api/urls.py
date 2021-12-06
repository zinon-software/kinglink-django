# todo/api/urls.py : API urls.py
from django.urls.conf import path
from .views import MyGroupListApiView, GroupDetailApiView


urlpatterns = [
    path("", MyGroupListApiView.as_view()),
    path('<int:group_id>', GroupDetailApiView.as_view()),
]