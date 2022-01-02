

from django.urls import path
from .views import GroupsReviewAPIView, SectionsAIPView, GroupDetailReviewAPIView

urlpatterns=[
    path('', GroupsReviewAPIView.as_view()),
    path('<int:groupID>', GroupDetailReviewAPIView.as_view()),
    path('sections',SectionsAIPView.as_view(),name='sections'),
]