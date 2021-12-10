# todo/api/urls.py : API urls.py
from django.urls.conf import path
from .views import NotificationAPIView, NotificationUpdateAPIView


urlpatterns = [
    path("", NotificationAPIView.as_view()),
    path("show", NotificationUpdateAPIView.as_view()),
]