from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from account.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token

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

# from django.shortcuts import render

# # Create your views here.

# from django.http import HttpResponse, response
# from rest_framework.views import APIView

# from api_Auth.serializer import UserSerializer

# from django.contrib.auth.models import User

# from rest_framework.authtoken.models import Token

# class RegisterUser(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)

#         if not serializer.is_valid():
#             return response({"statusCode": 403, 'errors': serializer.errors, 'message': 'Some'})
        
#         serializer.save()

#         user = User.objects.get(username = serializer.data['username'])

#         token_obj, _ =  Token.objects.get_or_create(user=user)

#         return response({"statusCode": 200, 'payload': serializer.data, 'token': str(token_obj)})