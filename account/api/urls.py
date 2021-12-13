from django.urls import path
from account.api.views import(
	UserFollowUnfollowApiView,
	registration_view,
	ProfileApiView,
	ProfileGroupsAPIView,
)

from .loginToken import login_auth_token

app_name = 'account'

urlpatterns = [
	path('register', registration_view, name="register"),

	
	path('login', login_auth_token, name="login"), # -> see accounts/api/views.py for response and url info

	path('follow-unfollow/<int:pk>',UserFollowUnfollowApiView.as_view(),name="follow-unfollow"),
	path('<int:id>', ProfileApiView.as_view(), name='profile'),
	path('<int:id>/groups', ProfileApiView.as_view(), name='profileGroups'),
]