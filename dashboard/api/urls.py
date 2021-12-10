

from django.urls import path
from .views import GroupsReviewAPIView

urlpatterns=[
    path('', GroupsReviewAPIView.as_view()),
]