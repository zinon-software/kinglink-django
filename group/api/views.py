from types import prepare_class
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from whatsApp.models import Groub
from .serializer import MyGroubSerializers, PostGroubSerializers

# Create your views here.

class MyGroupListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        List all the group items for given requested user
        '''
        groups = Groub.objects.filter(created_by = request.user.id)
        serializer = MyGroubSerializers(groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        data = {
            'name': request.data.get('name'), 
            'link': request.data.get('link'), 
            'created_by': request.user.id,
            'category': request.data.get('category'), 
            'sections': request.data.get('sections'), 
        }

        serializer = PostGroubSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GroupDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, group_id, user_id):
        '''
        Helper method to get the object with given group_id, and user_id
        '''
        try:
            return Groub.objects.get(id=group_id, created_by=user_id)
        except Groub.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, group_id, *args, **kwargs):
        '''
        Retrieves the Todo with given group_id
        '''
        group_instance = self.get_object(group_id, request.user.id)
        if not group_instance:
            return Response(
                {"res": "المجموعة غير موجودة"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = MyGroubSerializers(group_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, group_id, *args, **kwargs):
        '''
        Updates the todo item with given group_id if exists
        '''
        group_instance = self.get_object(group_id, request.user.id)
        if not group_instance:
            return Response(
                {"res": "المجموعة غير موجودة"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'), 
            'link': request.data.get('link'), 
            'created_by': request.user.id,
            'category': request.data.get('category'), 
            'sections': request.data.get('sections'), 
        }
        serializer = PostGroubSerializers(instance = group_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, group_id, *args, **kwargs):
        '''
        Deletes the todo item with given group_id if exists
        '''
        group_instance = self.get_object(group_id, request.user.id)
        if not group_instance:
            return Response(
                {"res": "المجموعة غير موجودة"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        group_instance.delete()
        return Response(
            {"res": "تم حذف الكائن!"},
            status=status.HTTP_200_OK
        )