from django.urls import path
from account.api.views import(
	UserFollowUnfollowApiView,
	registration_view,
	ProfileApiView,
	ProfileGroupsAPIView,
	AvatarAPIView,
	UsersAPIView,
)

from .loginToken import login_auth_token

app_name = 'account'

urlpatterns = [
	path('register', registration_view, name="register"),

	
	path('login', login_auth_token, name="login"), # -> see accounts/api/views.py for response and url info

	path('follow-unfollow/<int:pk>',UserFollowUnfollowApiView.as_view(),name="follow-unfollow"),
	path('<int:id>', ProfileApiView.as_view(), name='profile'),
	path('<int:id>/groups', ProfileGroupsAPIView.as_view(), name='profileGroups'),


	path('avatar', AvatarAPIView.as_view(), name='avatar'),


	path('users', UsersAPIView.as_view(), name='users'),
]