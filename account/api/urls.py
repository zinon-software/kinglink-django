from django.urls import path
from account.api.views import(
	UserFollowUnfollowApiView,
	registration_view,
)

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [
	path('register', registration_view, name="register"),

	
	path('login', obtain_auth_token, name="login"), # -> see accounts/api/views.py for response and url info

	path('follow-unfollow/<int:pk>',UserFollowUnfollowApiView.as_view(),name="follow-unfollow"),
]