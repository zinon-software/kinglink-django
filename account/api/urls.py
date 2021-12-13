from django.urls import path
from account.api.views import(
	ObtainAuthToken,
	UserFollowUnfollowApiView,
	registration_view,
	ProfileApiView,
)


app_name = 'account'

urlpatterns = [
	path('register', registration_view, name="register"),

	
	path('login', ObtainAuthToken, name="login"), # -> see accounts/api/views.py for response and url info

	path('follow-unfollow/<int:pk>',UserFollowUnfollowApiView.as_view(),name="follow-unfollow"),
	path('<str:username>', ProfileApiView.as_view(), name='profile'),
]