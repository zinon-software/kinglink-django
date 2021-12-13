from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from account.api.serializers import RegistrationSerializer, ProfileUpdateSerializers
from rest_framework.authtoken.models import Token

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from account.models import Account, Profile
from group.api.serializer import GroupSerializers
from group.models import Group
from notification.models import Notification

# Register
# Response: https://gist.github.com/mitchtabian/c13c41fa0f51b304d7638b7bac7cb694
# Url: https://<your-domain>/api/account/register

@api_view(['POST', ])
@permission_classes([])
def registration_view(request):

	if request.method == 'POST':
		serializer = RegistrationSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			account = serializer.save()
			data['response'] = 'تم تسجيل المستخدم الجديد بنجاح'
			data['id'] = account.pk
			data['email'] = account.email
			data['username'] = account.username
			token = Token.objects.get(user=account).key
			data['token'] = token
		else:
			data = serializer.error_messages
		return Response(data)



# LOGIN
# Response: https://gist.github.com/mitchtabian/8e1bde81b3be342853ddfcc45ec0df8a
# URL: http://127.0.0.1:8000/api/account/login

# --------------------------------------------------------------------------------------

class UserFollowUnfollowApiView(APIView):
	permission_classes = [permissions.IsAuthenticated]

	def get(self, request, pk, *args, **kwargs):
		print(request.user.username)
		current_user = request.user
		other_user = Account.objects.get(pk=pk)
		print(other_user)

		if other_user not in current_user.profile.follows.all():
			data = "started following you."
			current_user.profile.follows.add(other_user)
			other_user.profile.followers.add(current_user)
			
			notify = Notification.objects.create(sender=current_user,receiver=other_user,action="started following you.")
		else:
			current_user.profile.follows.remove(other_user)
			other_user.profile.followers.remove(current_user)
			data = "not started following you."

		return Response(data)

class ProfileApiView(APIView):
	permission_classes = [permissions.IsAuthenticated]

	def get(self, request, id, *args, **kwargs):
		user =  get_object_or_404(Account,id=id)
		profile = Profile.objects.get(user=user)
		
		group_list = Group.objects.filter(created_by = profile.id)
		# serializer = GroupSerializers(group_list, many=True)
		post_count = group_list.count()

		data = {
			'post_count':post_count,
			"follows":user.profile.follows.all().count(),
			"followers":user.profile.followers.all().count(),
			"name": profile.name,
			"username": user.username,
			"bio": profile.description,
			"avatar": profile.avatar,
			# 'group_list':serializer.data, 
		}
		return Response(data, status=status.HTTP_200_OK)

	def put(self, request, *args, **kwargs):
		
		p_serializers = ProfileUpdateSerializers(instance=request.user.profile, data=request.POST, partial = True)

		if p_serializers.is_valid():
			p_serializers.save()
			return Response(p_serializers.data, status=status.HTTP_200_OK)
		
		return Response(p_serializers.errors, status=status.HTTP_400_BAD_REQUEST)


